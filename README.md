# BME research portfolio

[View the research page](https://akanexu.github.io/bme-research/) · [Public source repository](https://github.com/AKanexu/bme-research)

A self-contained research page for **Kane XU** on human-in-the-loop BME measurement from routine clinical MRI. It distinguishes completed pilot work, ongoing cohort annotation and planned formal validation.

## Preview

From this folder:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
```

Open [the local preview](http://127.0.0.1:8765/). Stop with Ctrl+C. You can also open `docs/index.html` directly. No installation, build, model or clinical data is required.

## Publish with GitHub Pages

Use a separate repository containing **only this folder's contents**. Do not publish the enclosing clinical research workspace. The internal audit and publication checklist belong outside this repository.

1. Review the page and the separate `PUBLICATION_CHECKLIST.md` before release.
2. In GitHub Desktop, add this folder as a local repository (or create a repository here), review the file list, commit and publish it under a project name such as `bme-research`. It contains public page source and schematics only.
3. In the new GitHub repository, open **Settings → Pages → Deploy from a branch**, choose **main** and **/docs**, then save.
4. Use the deployed address shown by GitHub Pages. Check it in a signed-out browser before sharing.

These are static files with relative asset paths and `.nojekyll`; project-path hosting works without changing a base URL. [Official publishing instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site). Private-repository Pages availability depends on the GitHub plan; the reviewed public-only repository can be published publicly when ready.

## Edit and check

- `docs/index.html`: copy, statuses, references and contact details.
- `docs/styles.css`: responsive layout, typography and print styling.
- `docs/assets/`: original scientific schematics, including mobile variants.
- `FIGURE_GUIDE.md`: optional figure replacement slots and captions.

After edits, run:

```sh
python3 tools/validate_public.py
```

The check verifies local links, references, allowed assets and known sensitive patterns. It does not certify clinical de-identification or scientific validity. Clinical files and source pipeline code are intentionally not distributed here.
