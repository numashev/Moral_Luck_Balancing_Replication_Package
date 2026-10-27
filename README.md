# Moral_Luck_Balancing_Replication_Package

Replication package for *Moral and Luck Balancing* (Grossman, Karakostas, and Umashev).

## Contents

- `Data/` — the experimental data, one workbook per session (`Session1.xlsx` to `Session26.xlsx`).
- `Data Analysis.qmd` — the complete analysis: data preparation, descriptive statistics, figures, hypothesis tests, robustness checks, and the tables quoted in the paper.
- `Codebook.md` — definitions and coding for all 133 variables in the cleaned analysis dataset.
- `oTree/` — the oTree experiment code used to run the study.
- `Ethics/` — the ESSCA and Monash IRB ethics approval letters.
- `Writing/` — output folder and manuscript source. Figures are exported to `Writing/Figures/` and LaTeX table fragments to `Writing/Tables/`. Both subfolders are created automatically when the document is rendered. `Writing/Moral_Balancing_Combined.tex` is the combined manuscript and online appendix source; `Writing/sample.bib` and the static appendix screenshots are included so it can be compiled directly.

## Requirements

- **R** (tested with R 4.4.2)
- **Quarto** (tested with Quarto 1.10.18) — <https://quarto.org/docs/get-started/>
- The R packages `tidyverse`, `readxl`, `haven`, `janitor`, `modelsummary`, `broom`, `ggplot2`, `patchwork`, `knitr`, `tinytable`, and `tibble`.

The first code chunk installs any missing packages, but installing them up front is faster and avoids network issues during the render:

```r
install.packages(c(
  "tidyverse", "readxl", "haven", "janitor", "modelsummary",
  "broom", "ggplot2", "patchwork", "knitr", "tinytable", "tibble"
))
```

A LaTeX installation with `latexmk` and `biber` (for example a full TeX Live installation) is needed to render the analysis document to PDF or to compile the manuscript.

## Reproducing the results

1. Clone or download this repository, so that the `Data`, `Writing`, and `Data Analysis.qmd` files sit in the same folder.
2. Render the document from the repository root:

   ```sh
   quarto render "Data Analysis.qmd"
   ```

   Alternatively, open `Data Analysis.qmd` in RStudio and click **Render**.

   The root directory is set with `root_dir <- normalizePath(".")` in the *Directories* chunk. Quarto and RStudio both execute the document with the working directory set to the folder containing the `.qmd`, so no path editing is needed. If you run individual chunks interactively, first set the working directory to this package folder (or point `root_dir` at its absolute path).

3. The render takes roughly 30 seconds once the packages are installed. It produces:

   - `Data Analysis.html` (HTML render) or `Data-Analysis.pdf` (PDF render) — the full analysis document.
   - `Writing/Figures/*.pdf` — all figures (for example `MoralBalancing_Graph.pdf`, `LuckBalancing_Graph.pdf`, `dicefreq.pdf`, `poweranal.pdf`).
   - `Writing/Tables/*.tex` — LaTeX table bodies for the regression tables, the Fisher randomization tests, and the multiple-testing correction.
   - `Data/AppendedData-DataFinale.rds` — the cleaned analysis dataset created by the *Dataset Generation* section.

## Compiling the manuscript

After rendering `Data Analysis.qmd`, compile the combined manuscript and appendix from the `Writing` folder:

```sh
cd Writing
latexmk -pdf Moral_Balancing_Combined.tex
```

This produces `Writing/Moral_Balancing_Combined.pdf`. The source uses the generated tables in `Writing/Tables/`, the generated figures plus static screenshots in `Writing/Figures/`, and the bibliography in `Writing/sample.bib`.

## Notes

- Run the document top to bottom. The *Data Analysis* section loads `Data/AppendedData-DataFinale.rds`, which is written by the preceding *Dataset Generation* section, so the chunks cannot be run out of order.
- Re-rendering overwrites the generated figures, tables, `.rds` file, and output document.

## Pre-registration

The pre-registration can be found via the following link:

<https://doi.org/10.17605/OSF.IO/TAF4C>
