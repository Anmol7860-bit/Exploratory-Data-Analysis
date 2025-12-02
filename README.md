# Exploratory Data Analysis — Guide

> A practical, step-by-step guide to Exploratory Data Analysis (EDA) with example scripts and datasets.

---

## Repository overview

This repository contains a hands-on guide to performing EDA in Python. It includes ready-to-run scripts, example datasets, and utility modules for visualization, outlier detection, skewness checks, and feature engineering.

**Main files & folders**

* `EDA.py` — Core walkthrough and examples for performing EDA (data loading, summary stats, missing values, correlation, etc.).
* `Data_viz.py` — Visualization utilities and example plots (histograms, boxplots, scatterplots, pairplots, etc.).
* `Feature_engineering.py` — Examples of transforming variables, encoding, scaling, and creating features.
* `Outlier.py` — Outlier detection and treatment examples (IQR, z-score methods, trimming/imputation).
* `Skewed.py` — Tests and transformations for skewed distributions (log, Box–Cox, Yeo–Johnson).
* `diabetes.csv`, `kc_house_data.csv`, `penguins_lter.csv`, `gapminder_data_graphs.csv` — Example datasets used in the scripts.
* `venv/` — (Optional) virtual environment (ignore in source control if reusing this repo locally).
* `README.md` — This file.
* `LICENSE` — MIT License.

---

## Goals of this guide

1. Teach a practical, repeatable EDA workflow you can apply to most tabular datasets.
2. Provide clear scripts you can run or adapt for your projects.
3. Demonstrate visualization, missing-value handling, outlier treatment, skewness correction, correlation analysis, and basic feature engineering.

---

## Quick start

1. **Clone the repo**

```bash
git clone https://github.com/Anmol7860-bit/Exploratory-Data-Analysis.git
cd Exploratory-Data-Analysis
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate
# On Windows (PowerShell)
venv\Scripts\Activate.ps1
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not present, install common packages used in the scripts:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy statsmodels
```

4. **Run the main EDA script**

```bash
python EDA.py
```

> Or open and run the example notebooks (if present) in Jupyter.

---

## Suggested EDA workflow (step-by-step)

1. **Understand the problem & dataset**

   * Read the data dictionary (if available) and inspect the target variable.
   * Load data with `pd.read_csv()` and view `df.head()`.

2. **Quick data snapshot**

   * `df.info()`, `df.describe(include='all')`, `df.shape`, `df.dtypes`.

3. **Missing values & duplicates**

   * `df.isna().sum()` to identify missing values.
   * Decide: drop, impute (mean/median/mode), or model-based imputation.

4. **Univariate analysis**

   * Continuous vars: histograms, KDEs, boxplots; compute skewness/kurtosis.
   * Categorical vars: bar charts, frequency tables.

5. **Bivariate analysis**

   * Numerical vs numerical: scatterplots, correlation matrix, pairplots.
   * Numerical vs categorical: boxplots, violin plots, group statistics.
   * Categorical vs categorical: contingency tables, stacked bar charts.

6. **Outliers**

   * Visual: boxplots; Statistical: IQR rule, z-score.
   * Handle: keep, cap (winsorize), remove, or impute depending on context.

7. **Skewness & transformations**

   * Apply log/Box–Cox/Yeo–Johnson to reduce skew for modeling.

8. **Feature engineering & selection**

   * Create interaction terms, bin continuous variables, encode categoricals.
   * Use correlation, mutual information, or model-based importance for selection.

9. **Document findings**

   * Save cleaned datasets and a short report/notebook summarizing key insights and pitfalls.

---

## Code examples

### Load and inspect data (from `EDA.py`)

```python
import pandas as pd

df = pd.read_csv('diabetes.csv')
print(df.shape)
print(df.info())
print(df.describe())
```

### Visual check (from `Data_viz.py`)

```python
from Data_viz import quick_plot

quick_plot(df, column='age')
```

### Outlier detection (from `Outlier.py`)

```python
from Outlier import iqr_outliers

outlier_indices = iqr_outliers(df['bmi'])
print(len(outlier_indices))
```

---

## Best practices & tips

* Always start by asking: what is the target and what business or scientific question are you answering?
* Visualizations are your friend — plot early and plot often.
* Keep a reproducible pipeline: scripts, notebooks, and saved artifacts (cleaned data, plots, models).
* Avoid leaking information from the future when building features for modeling.
* Prefer simple transformations and document why you applied them.
* Use cross-validation when testing models built on features from EDA.

---

## Suggestions for improvements (how you can contribute)

* Add Jupyter notebooks demonstrating the EDA step-by-step for each dataset.
* Add automated tests or smoke checks for scripts.
* Add a `requirements.txt` and `Makefile` or `setup.py` for easier setup.
* Provide more datasets and project-style walkthroughs (challenge datasets).

---

## License

This project is released under the MIT License. See `LICENSE` for details.

---

## Contact

If you want feedback on the code or help improving the guide, open an issue or submit a pull request on the repository.

Happy exploring! ☁️
