# Electricity Demand Forecasting for Zurich (EWZ)

## Overview

This project investigates short-term electricity demand forecasting for the city of Zurich using high-frequency (15-minute resolution) consumption data provided by EWZ.

The dataset contains electricity demand separated by voltage level:

- **NE7** – Low voltage (households and SMEs)
- **NE5** – Medium voltage (large commercial and industrial consumers)

The goal is to compare statistical and machine learning models for short-term forecasting and evaluate their predictive performance.

---

## Objectives

- Model and forecast short-term electricity demand
- Compare classical statistical models with machine learning approaches
- Evaluate forecasting accuracy using time-series cross-validation
- Compare predictability between NE5 and NE7 demand segments

---

## Dataset

- Frequency: 15-minute intervals
- Time span: Since 2015
- Variables:
  - `time`
  - `NE5`
  - `NE7`
  - `id`

Optional extensions include weather data (temperature, humidity, radiation, etc.).

---

## Methodology

### 1. Exploratory Data Analysis
- Daily, weekly, and yearly seasonality
- Comparison between NE5 and NE7
- Peak demand analysis

### 2. Feature Engineering
- Temporal features (hour, weekday, month, holidays)
- Lag features (15 min, 1 hour, 1 day, 1 week)
- Rolling averages
- Optional weather variables

### 3. Models

- Baseline (seasonal naive)
- Linear Regression
- Generalized Linear Models (Poisson, Binomial)
- Generalized Additive Model (GAM)
- Support Vector Regression (SVM)
- Random Forest / XGBoost
- Neural Network

### 4. Evaluation

- Time-series cross-validation
- RMSE / MAE for regression
- AUC for peak classification
- Comparison across consumer segments

---

## Project Structure
- data/
- notebooks/
- src/
- outputs/
- README.md


---

## Reproducibility

1. Clone the repository
2. Install dependencies (see `requirements.txt` or `pyproject.toml`)
3. Run notebooks in order:
   - EDA
   - Feature Engineering
   - Model Training
   - Model Comparison

---

## Authors

- Elena Fuchs
- Paula Gili
- Tamara Marcet

---

## Research Questions
TBD 

---

## License

This project is developed for academic purposes (Machine Learning 1).
