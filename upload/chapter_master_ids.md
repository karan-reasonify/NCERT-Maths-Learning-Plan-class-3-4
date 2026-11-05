# Known chapter_master_id values (Class 3 and 4)

The Class 3 and Class 4 ids are in **`upload/chapter_ids.local.json`**, which is git-ignored on purpose: it holds the issued
upload ids, so it is never committed and none are written in this file. In it, `chapterId` is `chapter_master_id` and
`subjectId` is `subject_ref_id` (the product's `chapterMaster` table: `ChapterId`, `SubjectId`). It has one subject id per
class and 14 chapters per class, each with its id and the platform's chapter name.

Note for whoever reads it: within a class the ids fall as the chapter number rises. That is how they were issued; do not
"smooth" them into an ascending run.

`core/lp_start.py` reads the JSON and fills `chapter_master_id`, `subject_ref_id` and a book-title vs platform-name check into
each chapter's `chapter.config.json`. `upload_lp.py` always reads the id from the plan itself, never from a file like this.

**Always confirm live before an upload:** `python -I -X utf8 core/check_master_id.py <plan.json>` compares the plan's
`chapter_master_id` and `subject_ref_id` with the `chapterMaster` row (needs `DATABASE_URL` in `.env`). A wrong id attaches
good content to the wrong chapter, returns `success: true`, and looks like a clean upload.

If the JSON is lost, re-create it from the content team's table (a chapterId and a name per chapter, one subjectId per class)
in the same shape: `{"3": {"subject_ref_id": N, "chapters": {"1": {"chapter_master_id": N, "name": "..."}}}, "4": {...}}`.
For an id that is not in the file, pass `--master-id N --subject-ref-id M` to `core/lp_start.py`.
