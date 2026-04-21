# Electricity Demand Forecasting for Zurich (EWZ)

HSLU Applied Machine Learning and Predictive Modelling 1, FS26

Paula Barghout, Elena Fuchs, Tamara Marcet

---

## Project description

We analyse hourly electricity demand in Zurich using open data from the City of Zurich (EWZ grid, 2022–2025). We address three research questions: what drives demand, whether peak hours can be predicted, and whether daily peak counts can be modelled. Six methods are applied: Linear Model, GLM Poisson, GLM Binomial, GAM, SVM, and Neural Network.

---

## Research questions

- **RQ1:** What weather and time variables drive hourly electricity demand, and how accurately can we predict it?
- **RQ2:** Can we predict whether a given hour will be a peak demand hour (top 10% of all demand)?
- **RQ3:** Can we model how many peak hours a day is likely to have?

---

## Data sources

- **Electricity demand:** [EWZ Stromabgabe Netzebenen](https://data.stadt-zuerich.ch/dataset/ewz_stromabgabe_netzebenen_stadt_zuerich)
- **Weather data:** [UGZ Meteorological Measurements](https://data.stadt-zuerich.ch/dataset/ugz_ogd_meteo_h1)

Both datasets are open data from the City of Zurich.

---

## Team contributions

| Member | Lead responsibilities |
|---|---|
| Tamara Marcet | Linear Model (02), GLM Poisson (03), Conclusions (09), report | final check & submission
| Paula Barghout | Preprocessing (00), EDA (01), GLM Binomial (04), GAM (05), Cross-validation (08), Conclusions (09), report |
| Elena Fuchs | SVM (06), Neural Network (07), Conclusions (09), report |

---

## Folder structure

```
data/
  raw/
    ewz/                              original EWZ electricity file
    meteo/                            yearly meteo files from UGZ
  processed/
    hourly_merged.csv                 final dataset used by all models

notebooks/
  00_preprocessing.ipynb             merge EWZ + meteo, feature engineering (Paula)
  01_eda.ipynb                       exploratory data analysis (Paula)
  02_lm.ipynb                        linear model OLS on log demand (Tamara)
  03_glm_poisson.ipynb               GLM Poisson for peak hours per day (Tamara)
  04_glm_binomial.ipynb              GLM Binomial for binary peak classification (Paula)
  05_gam.ipynb                       generalized additive model pygam (Paula)
  06_svm.ipynb                       support vector regression with hyperparameter tuning (Elena)
  07_nn.ipynb                        neural network with lagged features and hyperparameter tuning (Elena)
  08_cross_validation.ipynb          TimeSeriesSplit CV comparing SVR kernels (Paula)
  09_conclusions.ipynb               model comparison, research questions, limitations (Elena)

outputs/
  model_comparison.csv               RMSE/MAE/R2/AUC for all models
  figures/
    01_eda/                          EDA plots
    02_lm/                           LM diagnostics and predictions
    03_poisson/                      Poisson diagnostics and predictions
    04_binomial/                     Binomial calibration, ROC, confusion matrix
    05_gam/                          GAM partial dependence plots and predictions
    06_svm/                          SVM predictions and performance visualisations
    07_nn/                           NN predictions and performance visualisations
    08_cv/                           cross-validation boxplot
    09_conclusions/                  model comparison charts

report.html                          main deliverable, self-contained HTML
report.qmd                           Quarto source for the report
README.md                            this file
```
---

## How to run

Notebooks run in order from 00 to 09 in Python 3. Run `00_preprocessing.ipynb` first as it generates `hourly_merged.csv` which all model notebooks depend on.

Non-standard dependencies: `pygam` (notebook 05) — install with `pip install pygam`.

---

## Report

`report.html` is the main deliverable and can be opened in any browser. It does not exceed 30 pages in print preview.
