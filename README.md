# M-Pesa Credit Risk Scoring System
### Loan Default Prediction via Alternative Financial Data

---

## Overview

This project is a machine learning-based credit risk scoring system that predicts the probability of loan default using alternative financial data extracted from M-Pesa mobile money statements.

The system demonstrates how unstructured financial transaction data (PDF statements) can be transformed into structured behavioral features for use in predictive credit modeling. It is designed to simulate real-world underwriting systems used in fintech lending environments.

The solution is deployed as an interactive **Streamlit** application that allows users to upload M-Pesa statements and receive real-time credit risk predictions alongside interpretable financial insights.

---

## Problem Statement

In many emerging markets, traditional credit scoring systems are limited due to a lack of formal banking history. As a result, mobile money transaction data has become a critical alternative source for assessing creditworthiness.

However, raw transaction data is unstructured and not directly usable for machine learning models. This project addresses the challenge of:

- Extracting meaningful financial signals from mobile money statements
- Engineering behavioral credit features from transaction data
- Building a predictive model for loan default risk estimation

---

## Key Objectives

- Extract financial features from M-Pesa PDF statements
- Engineer behavioral indicators of financial health
- Train a supervised machine learning model for default prediction
- Provide interpretable risk insights for lending decisions
- Deploy the model as an interactive web application

---

## Features

###  PDF Data Extraction
Parses M-Pesa statements using `pdfplumber`.

###  Financial Feature Engineering
- Income estimation
- Expense tracking
- Loan disbursement detection
- Repayment behavior analysis
- Cashflow stability indicators

###  Credit Risk Indicators
- Income-to-expense ratio
- Debt burden estimation
- Transaction consistency metrics

###  Machine Learning Model
- Supervised classification (Random Forest)
- Loan default probability prediction

###  Interpretability Layer
- Financial summary dashboard
- Risk indicator visualization

###  Web Interface
- Built using Streamlit for real-time inference

---

## Methodology

### 1. Data Extraction
M-Pesa PDF statements are parsed to extract raw transaction data including deposits, withdrawals, and transfers.

### 2. Feature Engineering
Transactions are transformed into structured financial behavior features such as:
- Monthly income and expenditure patterns
- Loan repayment frequency
- Net cashflow stability
- Transaction volatility

### 3. Model Development
A supervised learning approach is used to train a classification model that predicts loan default risk based on engineered features.

| Parameter | Detail |
|-----------|--------|
| Algorithm | Random Forest Classifier |
| Framework | Scikit-learn |
| Output | Probability of default / non-default |

### 4. Evaluation
Model performance is evaluated using standard classification metrics such as accuracy and feature importance analysis.

### 5. Deployment
The trained model is deployed using Streamlit to allow interactive predictions from uploaded financial documents.

---

## Technologies Used

| Category | Tools |
|----------|-------|
| Language | Python |
| Web App | Streamlit |
| PDF Parsing | pdfplumber |
| Data Processing | pandas, numpy |
| Machine Learning | scikit-learn |
| Visualization | matplotlib, seaborn |

---

## Project Structure

```
├── mpesa_loan_streamlit.py   # Streamlit application
├── loan_model.pkl            # Trained ML model
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

---

## Use Case: Fintech Credit Scoring

This system demonstrates how alternative data sources such as mobile money transactions can be used to:

- Improve credit access for underserved populations
- Support risk-based lending decisions
- Automate loan eligibility assessment
- Reduce reliance on traditional credit bureau data

It is particularly relevant for fintech lenders operating in markets where formal credit histories are limited.

---

## Future Improvements

- [ ] Integration of XGBoost / LightGBM for improved performance
- [ ] Model calibration for probability-of-default scoring
- [ ] Explainability using SHAP values
- [ ] Real-time API deployment for production lending systems
- [ ] Integration with larger financial datasets for improved generalization

---

## Author

**Glenn Kipanga**  
Data Science & AI Enthusiast  
GitHub: [@DARTH-GLENNIUM](https://github.com/DARTH-GLENNIUM)
