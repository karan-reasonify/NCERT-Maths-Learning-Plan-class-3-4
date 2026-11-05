# The stamp file

`validation/validate_local.py <plan.json> <chapter.config.json>` writes a stamp next to the
plan, at `<plan>.stamp.json`, only when `gates.gate_runner.run()` returns zero errors. This is
the mechanical half of the hard rule "no upload without a passing local validation" - a human
cannot skip this step under time pressure, because `upload/upload_lp.py` refuses to run
without a fresh, matching stamp.

## Fields

```json
{
  "sha256": "<hex digest of the exact plan.json bytes on disk at stamp time>",
  "config_path": "<absolute path to the chapter.config.json this was validated against>",
  "config_sha256": "<hex digest of that config file's bytes at stamp time>",
  "chapter_id": "<plan's chapter_id>",
  "chapter_master_id": <plan's chapter_master_id>,
  "phase": <plan's phase>,
  "version": <plan's version>,
  "plan_id": "<plan's plan_id>",
  "timestamp": "<UTC ISO-8601 when the stamp was written>",
  "gate_summary": {"errors": 0, "counts": {...}}
}
```

`config_path`/`config_sha256` bind the stamp to the exact config it was checked against -
`chapter.config.json` picks the `eqcheck` variant (plain/signed/powers) and can carry an
`eqcheck_errata` list of exact chain strings to exempt from the arithmetic-truth gate (e.g.
`maths7_ch10`'s own `K.ERRATA`, for a known, deliberately-kept printed-book error, never a way
to silence a real failure - `gate_runner` itself fails if an exempted entry is never matched,
so a stale exemption can't linger). Swap in a looser config after stamping and the sha256
mismatch invalidates the stamp exactly like an edited plan would.

`sha256` is hashed from the file's bytes, not a re-serialization of the dict - the same bytes
`upload_lp.py` POSTs via `io.open(path, "rb")`. If the plan file changes by even one byte after
the stamp is written (a re-run of `core/set_version.py`, a manual edit, line-ending drift), the
hash no longer matches and the stamp is dead.

## Order this forces

1. `core/set_version.py` (sets the final `version`/`plan_id` bytes)
2. `core/published_media.py pin-videos ...` (if rebuilding over live assets - also changes bytes)
3. `validation/validate_local.py` (hashes the now-final bytes, writes the stamp)
4. `upload/upload_lp.py --dry-run` (independent second look - preflight + stamp check + prints
   what would be sent, sends nothing; there is no separate server-side "validate without
   uploading" endpoint, so this is the closest thing to one)
5. `upload/upload_lp.py` (checks the stamp, then POSTs those exact bytes)

Running `validate_local.py` before step 1 or 2 produces a stamp that can never match what gets
uploaded, and the upload is refused forever until validation re-runs on the final file - this
is deliberate, not a bug to route around.

## Staleness

A stamp older than 24 hours, or one whose `sha256` does not match the plan file's current
bytes, is treated as absent. `upload/upload_lp.py` deletes a stale stamp it refuses on, so a
leftover stamp from an earlier, abandoned attempt can never be mistaken for a fresh pass.
