# Moral_Luck_Balancing_Replication_Package

Replication package for *Moral and Luck Balancing* (Grossman, Karakostas, and Umashev).

## Contents

- `Data/` — the experimental data, one workbook per session (`Session1.xlsx` to `Session26.xlsx`).
- `Data Analysis.qmd` — the complete analysis: data preparation, descriptive statistics, figures, hypothesis tests, robustness checks, and the tables quoted in the paper.
- `Writing/` — output folder. Figures are exported to `Writing/Figures/` and LaTeX table fragments to `Writing/Tables/`. Both subfolders are created automatically when the document is rendered.

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

A LaTeX installation (for example TinyTeX) is only needed if you also want to render the document to PDF.

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

## Notes

- Run the document top to bottom. The *Data Analysis* section loads `Data/AppendedData-DataFinale.rds`, which is written by the preceding *Dataset Generation* section, so the chunks cannot be run out of order.
- Re-rendering overwrites the generated figures, tables, `.rds` file, and output document.
- The permutation-based Fisher randomization tests are seeded (`set.seed(42)`). Point estimates and test statistics are deterministic; permutation p-values can differ in the last digits across R versions.
- The exported LaTeX table fragments use plain numeric cells (for example `0.046`), matching the manuscript. Rendering to PDF adds `\num{...}` (siunitx) wrappers internally, but the export step strips them, so HTML and PDF renders produce the same table bodies. Render to PDF only if you also need the PDF version of the analysis document.
- If HTML rendering fails with a LaTeX-related message, make sure you are rendering `--to html`; LaTeX is only required for `--to pdf`.

## Pre-registration

The pre-registration can be found via the following link:

<https://doi.org/10.17605/OSF.IO/TAF4C>
