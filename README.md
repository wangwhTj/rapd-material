# RaPD presentation materials

Slides and poster for **RaPD: Resolution-Agnostic Pixel Diffusion via Semantics-Enriched Implicit Representations** (NeurIPS 2026).

- [Project page](https://wangwhtj.github.io/rapd-page/)
- [Code](https://github.com/wangwhTj/rapd)

## Files

| Material | Source | Existing PDF |
| --- | --- | --- |
| Camera-ready slides | [LaTeX](slide/slides_camera_ready.tex) | [PDF](slide/slides_camera_ready.pdf) |
| First-submission slides | [LaTeX](slide/slides_first_submit.tex) | [PDF](slide/slides_first_submit.pdf) |
| Editable poster | See restoration command below | [PDF](poster/poster_camera_ready_editable.pdf) |
| LaTeX poster | [LaTeX](poster/poster_camera_ready.tex) | [PDF](poster/poster_camera_ready.pdf) |

`figures/` contains the shared LaTeX dependencies. `project page/assets/` contains the single image referenced by the slide title page. `poster/assets/` and `poster/logo/` preserve the editable poster resources. Compilation caches, editor lock files, and intermediate backup versions are excluded.

## Restore the poster PowerPoint file

The original poster PPTX exceeds 100 MiB and is stored in two lossless parts. From the repository root, run:

```bash
python3 restore_poster.py
```

This creates `poster/poster_camera_ready_editable.pptx` and verifies its SHA-256 against the original. The reconstructed file is ignored by Git; the parts remain tracked.

Both the original poster PPTX and `poster/logo/logo.pptx` have a `%TSD-Header-###%` file header rather than a standard Office ZIP header. They are preserved byte-for-byte; opening them may require the originating software/environment. This repository does not convert or remove that wrapper. The PDF exports are available separately.

## Compile LaTeX

Use a TeX Live installation with Beamer, TikZ, tcolorbox, textpos, and the packages listed in each source. Run each command twice from its indicated directory:

```bash
cd slide
pdflatex -interaction=nonstopmode -halt-on-error slides_camera_ready.tex
pdflatex -interaction=nonstopmode -halt-on-error slides_camera_ready.tex
# Optional earlier version:
pdflatex -interaction=nonstopmode -halt-on-error slides_first_submit.tex
pdflatex -interaction=nonstopmode -halt-on-error slides_first_submit.tex
cd ../poster
pdflatex -interaction=nonstopmode -halt-on-error poster_camera_ready.tex
pdflatex -interaction=nonstopmode -halt-on-error poster_camera_ready.tex
```

The LaTeX poster and editable PowerPoint poster are separate versions. Existing PDFs are archived as supplied; rebuilding LaTeX may produce different output. `checksums.json` records the sizes and SHA-256 hashes of all original files and the poster parts. No visual inspection was performed during packaging.

Packaging validation: all 36 original files matched their source SHA-256 hashes; reconstruction from the two poster parts passed; both slide sources and the poster source each compiled successfully in two pdflatex passes with output written to temporary directories. The archived PDFs were not overwritten.
