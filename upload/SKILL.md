---
name: upload
description: Upload a learning plan JSON to the LP2 agentapi endpoint, with preflight and a database read-back. Use when the user wants to upload, publish, push or activate a learning plan or a chapter (any grade, any subject, one file or a whole folder) - "upload sci6 ch8", "publish class 9 maths", "push these plans to staging".
---

# Upload a learning plan

One endpoint publishes a plan and, for a chapter's first version, registers the
chapter and activates it in the same call:

```
POST {base}/agentapi/api/lp2/learning-plans/upload?activate=true
  -F "file=@<plan>.json;type=application/json"
  -F "chapter_master_id=<N>"
  -F "phase=<N>"
```

`base` is `https://staging.singularity-learn.com` unless the user names another.
**Never substitute a production host on your own initiative** - ask.

Use this instead of `pipeline/db_push/push_chapter.py` for a first version:
push_chapter supersedes an active version and cannot create the `lp2_chapters`
row, so it refuses a chapter that has never been published. This endpoint does
both.

## The one thing that fails silently

**`chapter_master_id` and `phase` are form fields. The endpoint does not read
them from the JSON.** A wrong `chapter_master_id` attaches good content to the
wrong chapter, returns `success: true`, and looks like a clean upload.

So take the id from the plan's own `chapter_master_id`, which is what
`upload_lp.py` does. If the user gives an id, pass it as `--chapter-master-id`
and the script asserts it matches the plan rather than trusting either. On a
mismatch, or a plan with no id at all, stop and ask - do not pick one.

## Run it

Two bundled scripts, stdlib only, no third-party imports, both live beside this
file. Quote paths with spaces. `python` on Windows, `python3` elsewhere.

**HARD RULE in this pipeline: `upload_lp.py` refuses to upload (even with
`--skip-preflight`) unless `validation/validate_local.py` has already run and
left a fresh, matching `<plan>.stamp.json` next to the file.** Run that first;
see `validation/STAMP_FORMAT.md`. This also only ever uploads phase 2 - there is
no `_V3`/Phase 3 build in this pipeline, so `--phase` can only confirm 2, never
override it to something else.

```bash
UP="<this pipeline>/upload/upload_lp.py"

# 0. local gate + stamp - required before step 2 can do anything
python "<this pipeline>/validation/validate_local.py" "<plan>.json"

# 1. see what would go where; sends nothing
python "$UP" "<plan>.json" --dry-run

# 2. upload (activate=true is the default)
python "$UP" "<plan>.json"

# a whole grade, one call, each plan carrying its own id
python "$UP" "Class 9"/maths9_ch*/maths9_ch*.json

# an id the user gave you: asserted against the plan, never trusted over it
python "$UP" "<plan>.json" --chapter-master-id 226
```

`--dry-run` first is the habit worth keeping: it prints each plan's
`chapter_id`, `chapter_master_id`, phase and shape, so the user can see the id
mapping before anything is sent. Show them that table when they have not named
the ids themselves. There is no separate server-side "validate without
uploading" endpoint - `--dry-run` (stamp check + preflight + print, nothing
sent) is the closest thing and is the right step to run before the real one.

Other options: `--phase N` (must equal the plan's own phase, which must be 2),
`--no-activate`, `--base-url URL`, `--skip-preflight`, `--timeout SECONDS`.

`upload_lp.py` resolves and preflights **every** plan before sending **any**, so
a bad file in a batch means nothing at all was uploaded.

## Uploading a 2d_tool: the .tsx and the .json, and nothing else

A tool's files go to the GCS bucket, not to the plan endpoint. `upload_tool.py`
lives beside this file.

```bash
UT="<this pipeline>/upload/upload_tool.py"
python "$UT" "<chapter>/Tools/<MEDIA_ID>" "<chapter>/<plan>.json" --dry-run
python "$UT" "<chapter>/Tools/<MEDIA_ID>" "<chapter>/<plan>.json"
```

**Only `<MEDIA_ID>.tsx` and `<MEDIA_ID>.json` are ever uploaded.** No
`.preview.html`, no `preview.v2`, no dev previews, nothing else in the folder.
The user set this rule on 11 Sep 2026 and the bucket already obeys it: every one
of the thirty-six tool folders in `learning_plan_assets` holds exactly those two
files. The preview is a local reference implementation; the host never fetches
it. The script skips anything that is not one of those two extensions, and
anything not named by the media id, and prints what it skipped.

**The subject folder is `mathematics` for every asset type.** User rule, 12 Sep
2026:

```
tools   V2/.../class_3/mathematics/ch_3/2dtool/<MEDIA_ID>/<MEDIA_ID>.tsx|.json
images  V2/.../class_3/mathematics/ch_3/image/<MEDIA_ID>.png
```

The bucket used to split one chapter across two subject folders by asset type -
tools under `maths/`, images under `mathematics/`. **Class 3 and 4 were migrated
to `mathematics/` on 12 Sep 2026 (their old `maths/` copies were left in place as
fallback); classes 6-10 still carry the split**, so a live path there may still
read `maths/`.

**The folder is read off the plan's own `2d_tool_url`, never assembled.** That is
also what makes a migration work: rewrite the url in the plan, and this script
follows it. Assembling the path from the grade and subject puts the file one
directory from where the host looks, the upload answers `success: true`, and the
url 404s.

Form fields are `folder_name` (the key prefix, starting at `V2/`, with
`learning_plan_assets/` **stripped**) and `bucket_name=learning_plan_assets`.
Passing the full `learning_plan_assets/V2/...` as `folder_name` lands the file in
the *other* bucket behind the load balancer, where its url 404s.

Verify against `https://storage.googleapis.com/learning_plan_assets/<key>`, which
bypasses the load balancer. **Do not probe the `media.singularity-learn.com` url
before uploading**: the LB caches the 404 for an hour, so a pre-upload check makes
the file look missing long after it is live.

**Verifying a RE-upload needs a cache-buster.** `storage.googleapis.com` serves
these objects with `Cache-Control: public, max-age=3600`, so after replacing a
file a plain re-check reports the **old** size and looks like the upload failed.
Add a throwaway query param and read `x-goog-stored-content-length`.

## Before re-uploading a plan: what the rebuild silently dropped

Run `verify_uploaded.py` first and read the diff by **direction**, not by count.
The question that matters is *which leaves does the live blob have content in
where the local file is empty* - those are what the upload destroys.

On 11 Sep 2026 Class 3 chapter 3 rebuilt with all **39 `image_url`s empty**,
because the builder hardcodes `"image_url": ""` and the urls are attached after
publication by the image upload step. Uploading it would have taken every picture
in the chapter off the page and answered `success: true`. The fix was to pin the
published urls in the builder keyed by **media id**, so a rebuild cannot blank
them again. Check any chapter whose images were uploaded separately for the same
hole before publishing a rebuild.

### Preflight

`gates/media_content.py` (imported by both `upload_lp.py` and
`validation/validate_local.py`, so there is one source of truth): media enum,
no `tool_2d`, no em or en dashes, contiguous segment/topic/concept ids, every
topic offering an `available_content_types`, every tool carrying a filled
`2d_tool_url`, a `tool_config` and its `tool_questions`, asset urls under the
plan's own `class_<grade>`, and no textbook branding outside the internal
`description`/`context` fields. These are delivery breaks the API accepts
happily: a plan can import clean and still show a blank topic or 404 every
tool - this preflight alone is not the local-validation hard rule; the full
gate run (`gates/gate_runner.py`, which also checks arithmetic truth) is, and
that is what `validation/validate_local.py` runs to produce the stamp.

Before uploading, also confirm the id against the live database, never a
remembered table:

```bash
python core/check_master_id.py "<plan>.json"    # keys vs the live database
```

## Read the reply, not just `success`

```json
{"success":true,"action":"imported","plan_id":"cbse_eng_maths9_ch1_v1","version":1,
 "is_active":true,"is_draft":false,"phase":2,
 "counts":{"modules":4,"segments":10,"topics":10,"concepts":50,"objectives":48,"media":37},
 "diff":{"added":[...],"removed":[],"retained_count":0,"is_replace":false},
 "validation_errors":[]}
```

- `counts` must match the plan's real shape - `upload_lp.py` prints both.
- `validation_errors` must be empty. It is not the same field as `success`.
- **`diff.removed` on a re-upload means those media ids are orphaned**: the
  chapter will 404 those tools and images until the assets are re-uploaded at the
  new ids. Report it; it is a reason to check with whoever owns the assets, not a
  reason the upload failed.

## Then prove it from the database

The API's own reply is not the verdict. Read it back - one active version, and
the blob equal to the file leaf for leaf, `_activate` excepted, which
`?activate=true` sets:

```bash
python "<this pipeline>/upload/verify_uploaded.py" "<plan>.json"
```

It reads this pipeline's own `core/config.py`, which needs this pipeline's own
`.env` (see `.env.example` at the pipeline root) for `DATABASE_URL`, and
connects with `readonly=True`. If that `.env` is not filled in, say so and
report the upload's `counts` instead of implying a verification that did not
happen.

## Report

Per chapter: `plan_id`, version, active, phase, counts, validation errors, and
the read-back verdict. Name anything skipped. If a plan was refused, say which
and why, and leave it to the user to fix rather than guessing an id.
