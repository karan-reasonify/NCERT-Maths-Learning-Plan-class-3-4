# -*- coding: utf-8 -*-
"""The one place credentials, service settings and the publish destination live.

Two files at the repo root feed this module, and both are gitignored:

    .env          DATABASE_URL, bare KEY=value lines
    config.json   the Google service account, plus an `app_config` block of
                  batch sizes and worker counts for the image jobs

Nothing else in the pipeline reads either file. A script that needs the database
calls `config.connect()`; a script that needs the image credentials calls
`config.google_credentials()`. That is the whole interface, and it means a
rotated key or a moved file is one edit here rather than a search.

The real environment always wins over `.env`, so a one off run can still say
`DATABASE_URL=... python pipeline/db_push/push_chapter.py ...` and be obeyed.

    python pipeline/config.py        print what resolved, secrets masked

THE DESTINATION
---------------
A learning plan is published into the **lpv2** tables (`lp2_plans`,
`lp2_plan_blobs`, keyed against `lp2_chapters`). That is the default and it is
what every push, verify and key check now targets without being told.

The older `plans` / `plan_blobs` pair is registered as `lpv1` so it is named
rather than stumbled into. It is read only here: it carries no `status`,
`plan_meta` or `phase` column, so the v2 publish transaction cannot run against
it, and `push_chapter.py` refuses it rather than half writing a row.
"""
from __future__ import annotations

import io
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

ENV_FILE = os.path.join(ROOT, ".env")
CONFIG_FILE = os.path.join(ROOT, "config.json")

IDENT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


# ----------------------------------------------------------------- .env

_env_loaded = False


def _unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def load_env(path=None, override=False):
    """Read the root `.env` into os.environ. Idempotent, and safe to call twice.

    Values already present in the environment are left alone unless `override`,
    because a value passed on the command line is a deliberate act and a file is
    a default. Returns the keys it actually set.
    """
    global _env_loaded
    path = path or ENV_FILE
    if _env_loaded and path == ENV_FILE and not override:
        return []
    applied = []
    if os.path.exists(path):
        for raw in io.open(path, encoding="utf-8"):
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            if line.startswith("export "):
                line = line[len("export "):]
            key, value = line.split("=", 1)
            key = key.strip()
            if not key:
                continue
            if override or key not in os.environ:
                os.environ[key] = _unquote(value)
                applied.append(key)
    if path == ENV_FILE:
        _env_loaded = True
    return applied


# -------------------------------------------------------------- config.json

_config_cache = None


def load_config(path=None):
    """The parsed config.json. Cached, because it holds a private key."""
    global _config_cache
    path = path or CONFIG_FILE
    if _config_cache is None or path != CONFIG_FILE:
        if not os.path.exists(path):
            raise SystemExit(
                "config.json is missing at %s.\n"
                "It carries the Google service account and the app_config block; "
                "it is gitignored, so copy it in from wherever it is kept." % path)
        data = json.load(io.open(path, encoding="utf-8"))
        if path != CONFIG_FILE:
            return data
        _config_cache = data
    return _config_cache


def google_credentials(export=True):
    """Path to the service account json, and by default put it where the Google
    libraries look for it. They read GOOGLE_APPLICATION_CREDENTIALS from the
    environment, so this is the whole of "set up the service account"."""
    load_config()                     # fail here if it is missing or malformed
    if export:
        os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS", CONFIG_FILE)
    return CONFIG_FILE


def service_account():
    """The service account fields, without the app_config block."""
    return {k: v for k, v in load_config().items() if k != "app_config"}


def gcp_project():
    return load_config().get("project_id")


def app_setting(name, override=None):
    """One value from config.json's `app_config`, resolved and clamped.

        explicit argument  >  environment variable of the same name  >  default

    and never above the `max` the file records, because those ceilings are the
    remote service's, not a preference.
    """
    block = (load_config().get("app_config") or {}).get(name)
    if block is None:
        raise KeyError("no app_config entry named %r in config.json" % name)

    value = override
    if value is None:
        raw = os.environ.get(name.upper())
        if raw is not None:
            value = _coerce(raw, block.get("default"))
    if value is None:
        value = block.get("default")

    ceiling = block.get("max")
    if ceiling is not None and isinstance(value, (int, float)) and value > ceiling:
        value = ceiling
    return value


def _coerce(raw, like):
    if isinstance(like, bool):
        return raw.strip().lower() in ("1", "true", "yes", "on")
    if isinstance(like, int):
        return int(raw)
    if isinstance(like, float):
        return float(raw)
    return raw


def app_config():
    """Every app_config name resolved through `app_setting`."""
    return {name: app_setting(name)
            for name in (load_config().get("app_config") or {})}


# ------------------------------------------------------------------ secrets

def database_url(required=True):
    load_env()
    url = os.environ.get("DATABASE_URL")
    if not url and required:
        raise SystemExit(
            "DATABASE_URL is not set. Put it in %s as a bare KEY=value line, or "
            "pass it in the environment for one run." % ENV_FILE)
    return url


# -------------------------------------------------------------- destination

class Destination(object):
    """Which set of tables a plan is published into."""

    def __init__(self, name, plans, blobs, chapters, writable, note):
        for table in (plans, blobs, chapters):
            if not IDENT.match(table):
                raise ValueError("not a plain table name: %r" % table)
        self.name = name
        self.plans = plans
        self.blobs = blobs
        self.chapters = chapters
        self.writable = writable
        self.note = note

    def __repr__(self):
        return "<Destination %s: %s / %s / %s>" % (
            self.name, self.plans, self.blobs, self.chapters)


DESTINATIONS = {
    "lpv2": Destination(
        "lpv2", "lp2_plans", "lp2_plan_blobs", "lp2_chapters", True,
        "the live learning plan store: one row per version, "
        "uq_lp2_plan_active keeps exactly one active per (chapter_id, level)"),
    "lpv1": Destination(
        "lpv1", "plans", "plan_blobs", "lp_chapters", False,
        "the superseded store. Read only from here: it has no status, "
        "plan_meta or phase column, so the v2 publish transaction cannot run "
        "against it"),
}

DEFAULT_DESTINATION = "lpv2"


def destination(name=None):
    """The publish destination: argument, else $LP_DESTINATION, else lpv2."""
    load_env()
    name = (name or os.environ.get("LP_DESTINATION")
            or DEFAULT_DESTINATION).strip().lower()
    if name not in DESTINATIONS:
        raise SystemExit("unknown destination %r; known: %s"
                         % (name, ", ".join(sorted(DESTINATIONS))))
    return DESTINATIONS[name]


def add_destination_arg(parser):
    """Give a script the same --destination flag as every other script."""
    parser.add_argument(
        "--destination", default=None, metavar="NAME",
        choices=sorted(DESTINATIONS),
        help="which plan tables to use (default %s)" % DEFAULT_DESTINATION)
    return parser


# ------------------------------------------------------------------ connect

def connect(readonly=False, autocommit=None):
    """A psycopg2 connection to DATABASE_URL, with .env already loaded.

    psycopg2 is imported here rather than at module scope so that the build
    pipeline, which never touches the database, keeps its one dependency.
    """
    try:
        import psycopg2
    except ImportError:
        raise SystemExit(
            "psycopg2 is not installed. Install it with:\n"
            "    python -m pip install psycopg2-binary")
    conn = psycopg2.connect(database_url(), connect_timeout=int(
        os.environ.get("DB_CONNECT_TIMEOUT", "15")))
    if readonly:
        conn.set_session(readonly=True,
                         autocommit=True if autocommit is None else autocommit)
    elif autocommit is not None:
        conn.autocommit = autocommit
    else:
        conn.autocommit = False
    return conn


def cursor(conn):
    """A dict cursor, which is what every caller here wants."""
    import psycopg2.extras
    return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


# ------------------------------------------------------------------- doctor

def _mask(value, keep=4):
    if not value:
        return "(unset)"
    if len(value) <= keep * 2:
        return "*" * len(value)
    return "%s...%s (%d chars)" % (value[:keep], value[-keep:], len(value))


def _mask_dsn(url):
    if not url:
        return "(unset)"
    return re.sub(r"://([^:/@]+):([^@]+)@", r"://\1:****@", url)


def main():
    print("root            %s" % ROOT)
    print(".env            %s" % (ENV_FILE if os.path.exists(ENV_FILE)
                                  else "MISSING at %s" % ENV_FILE))
    print("config.json     %s" % (CONFIG_FILE if os.path.exists(CONFIG_FILE)
                                  else "MISSING at %s" % CONFIG_FILE))
    print()
    print("DATABASE_URL    %s" % _mask_dsn(database_url(required=False)))

    if os.path.exists(CONFIG_FILE):
        account = service_account()
        print("service account %s" % account.get("client_email"))
        print("gcp project     %s" % account.get("project_id"))
        print("credentials at  %s" % google_credentials())
        print()
        print("app_config")
        for name, value in sorted(app_config().items()):
            print("  %-22s %s" % (name, value))

    print()
    dest = destination()
    print("destination     %s%s" % (dest.name,
                                    "" if dest.name == DEFAULT_DESTINATION
                                    else "  (default is %s)" % DEFAULT_DESTINATION))
    print("  plans         %s" % dest.plans)
    print("  blobs         %s" % dest.blobs)
    print("  chapters      %s" % dest.chapters)
    print("  writable      %s" % ("yes" if dest.writable else "no, read only"))

    url = database_url(required=False)
    if not url:
        print("\nno DATABASE_URL, so the connection was not tested")
        return 1
    try:
        conn = connect(readonly=True)
        cur = cursor(conn)
        cur.execute("select current_database() as db, current_user as who")
        row = cur.fetchone()
        cur.execute("select count(*) as n from %s" % dest.plans)
        plans = cur.fetchone()["n"]
        cur.execute("select count(*) as n from %s" % dest.chapters)
        chapters = cur.fetchone()["n"]
        conn.close()
    except SystemExit:
        raise
    except Exception as exc:                       # noqa: BLE001 - reported, not raised
        print("\nCONNECTION FAILED: %s" % exc)
        return 1
    print("\nconnected to %s as %s: %d plan rows, %d chapter rows"
          % (row["db"], row["who"], plans, chapters))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
