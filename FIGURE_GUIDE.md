# Optional figure replacements

The page already uses original, responsive scientific schematics. There are no empty or broken image slots. These optional filenames reserve clear replacements for later figure generation. Do not add a clinical image until its de-identification and permission to share have been verified.

| Optional asset | Placement and caption | Requirements |
|---|---|---|
| `docs/assets/project_overview.png` | Hero: “The developing measurement framework, from native slice masks to physical area and acquisition-aware volumetry.” | Schematic only; distinguish technical pilot work from planned validation. Suggested 1280 × 1140 px. Keep a mobile version or retain the existing mobile SVG. |
| `docs/assets/human_ai_workflow.png` | Workflow: “Radiologist prompting, MedSAM initial mask, expert review and correction before quantitative measurement.” | Label any example as synthetic or explicitly approved/de-identified. Do not imply cohort completion. Suggested 2000 × 540 px; keep the mobile HTML workflow. |
| `docs/assets/physical_space_quantification.png` | Measurement: “Actual patient-coordinate slice positions determine integration intervals; nominal thickness is not a substitute for centre-to-centre distance.” | Label as a proposed-method schematic. Distinguish gaps, missing coverage and thickness. Suggested 1800 × 540 px; retain the mobile SVG. |
| `docs/assets/annotation_tool_synthetic.png` | Annotation tool: “The annotation interface using a synthetic example; no patient data are shown.” | Capture the actual interface only after loading a synthetic image and synthetic labels. Remove centre names, real identifiers, filesystem paths and window titles that disclose private context. Do not label an invented UI as a real screenshot. |

Update the corresponding image/picture source and its alt text in `docs/index.html` only after a replacement exists. Remove the obsolete asset if it is no longer used. The public-file validator initially accepts SVG/HTML/CSS only; deliberately add PNG support after reviewing each new asset rather than dropping arbitrary exports into the site.

No source clinical MRI, pilot overlay, radiology report or hospital viewer screenshot is cleared for publication by this guide. The existing SVGs are a complete publishable visual solution without clinical examples.
