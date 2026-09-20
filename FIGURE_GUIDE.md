# Public figures

The site uses two complementary figures, without a repeated segmentation diagram.

| Asset | Placement and purpose | Public status |
|---|---|---|
| `docs/assets/bme_workflow_public.png` | Figure 1, after the research question and before My Contributions. The master framework combines clinical inputs, prompting, expert review, geometry and planned evaluation. Clicking opens the original image without a lightbox. | Supplied by the author; de-identification and public-display permission explicitly confirmed on 20 September 2026. Copied without modification, including provenance metadata. The caption distinguishes the intended endpoint from completed results. |
| `docs/assets/physical_space_quantification.svg` and `physical_space_mobile.svg` | Figure 2, in Physical-space quantification. Actual slice positions define integration intervals; thickness alone does not. | Scientific schematics without patient-derived measurements. |

The master workflow depicts the intended study as a whole. Its verified-mask and reliability-characterised outputs must not be interpreted as completed cohort validation. Keep the adjacent status caption when reusing it. The figure labels Centre A as 3T / approximately 3–4 mm and Centre B as 1.5T / approximately 4 mm.

## Optional genuine annotation screenshot

Reserved asset: `docs/assets/annotation_tool_public.png`. Reserved location: after the annotation-tool description in the human–AI workflow section. No broken image or fabricated screenshot is rendered.

Suggested caption: “The radiologist annotation interface showing multiple lesion boxes, progress and QC states. [Specify a synthetic example or separately cleared de-identified imaging.]”

Capture the actual interface using synthetic labels or separately cleared examples. Check identifying text, filenames, window titles, paths, image metadata and overlays. The clearance for the current master figure does not cover other research images. Review a new PNG before adding its digest to `tools/validate_public.py`; the validator deliberately accepts only the exact approved raster asset.
