# Electricity Demand Forecasting for Zurich (EWZ)

HSLU Applied Machine Learning and Predictive Modelling 1, FS26

Paula Barghout, Elena Fuchs, Tamara Marcet

---

## What this project is about

We looked at hourly electricity demand in the city of Zurich and tried to answer three questions:
- What weather and time variables drive demand?
- Can we predict whether a given hour will be a peak demand hour?
- Can we model how many peak hours occur per day?

We used six modelling approaches: a linear model, two GLMs (Poisson and Binomial), a GAM, a Support Vector Machine, and a neural network.

---

## Data

**Electricity demand** -- EWZ Stromabgabe Netzebenen Stadt Zurich
Source: https://data.stadt-zuerich.ch/dataset/ewz_stromabgabe_netzebenen_stadt_zuerich
15-minute readings for grid levels NE5 (medium voltage) and NE7 (low voltage), from 2022 onward.
File: `data/raw/ewz/ewz_stromabgabe_netzebenen_stadt_zuerich.csv`

**Weather data** -- UGZ Meteorological Measurements (hourly)
Source: https://data.stadt-zuerich.ch/dataset/ugz_ogd_meteo_h1
Hourly observations from four monitoring stations in Zurich. We used Zch_Stampfenbachstrasse as it had the fewest missing values.
Files: `data/raw/meteo/ugz_ogd_meteo_h1_20XX.csv` (one per year, 2022-2026)

Both datasets are open data from the City of Zurich and can be downloaded freely from the links above.

---

## Folder structure

```
data/
  raw/
    ewz/        original EWZ electricity file
    meteo/      yearly meteo files from UGZ
  processed/
    hourly_merged.csv   final dataset used by all models

notebooks/
  00_preprocessing.ipynb   merge EWZ + meteo, feature engineering
  01_eda.ipynb             exploratory data analysis
  02_lm.ipynb              linear model (OLS on log demand)
  03_glm_poisson.ipynb     GLM Poisson for peak hours per day
  04_glm_binomial.ipynb    GLM Binomial for binary peak classification
  05_gam.ipynb             generalized additive model (pygam)
  06_svm.ipynb             support vector regression (RBF kernel)
  07_nn.ipynb              neural network (MLPRegressor)
  08_cross_validation.ipynb  TimeSeriesSplit CV comparing SVR kernels
  09_conclusions.ipynb     model comparison tables and summary charts

outputs/
  model_comparison.csv     RMSE/MAE/R2/AUC for all models
  figures/
    01_eda/        EDA plots
    02_lm/         LM diagnostics and predictions
    03_poisson/    Poisson diagnostics and predictions
    04_binomial/   Binomial calibration, ROC, confusion matrix
    05_gam/        GAM partial dependence plots and predictions
    06_svm/        SVM predictions
    07_nn/         NN loss curves and predictions
    08_cv/         cross-validation boxplot
    09_conclusions/ model comparison chart

report.html    main deliverable, self-contained HTML
report.qmd     Quarto source for the report
README.md      this file
```

---

## How to run

The notebooks are in Python 3 and run in order from 00 to 09. The only non-standard dependency beyond numpy/pandas/matplotlib/sklearn is `pygam` (notebook 05), which can be installed with `pip install pygam`.

Running `00_preprocessing.ipynb` first is required as it generates `data/processed/hourly_merged.csv`, which all other notebooks depend on.

---

## Report

`report.html` is the main deliverable. It is self-contained (all images embedded) and can be opened in any browser without additional files. We verified that it does not exceed 30 pages in print preview.
