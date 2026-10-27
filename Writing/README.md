# Contents

`Data Analysis.qmd` exports figures to `Figures/` and LaTeX table bodies to `Tables/`.

The combined manuscript and online appendix source is `Moral_Balancing_Combined.tex`. Its bibliography is `sample.bib`, and the static appendix screenshots are in `Figures/`.

## Compiling the manuscript

First render the analysis from the repository root so that the generated figures and tables exist:

```sh
quarto render "Data Analysis.qmd"
```

Then compile the manuscript from this folder:

```sh
latexmk -pdf Moral_Balancing_Combined.tex
```

This produces `Moral_Balancing_Combined.pdf` (main text plus appendix). It requires a full LaTeX installation with `latexmk` and `biber`, together with the packages used in the preamble (including `tabularray`, `siunitx`, `biblatex-apa`, `pgfplots`, and `fancyhdr`).
