# M-Pesa Loan Default Predictor

## Overview
This project is a web application built with Streamlit that allows users to upload their M-Pesa statements (PDFs) and receive a loan default prediction based on their financial transactions. The app extracts relevant financial features from the statement, analyzes them, and predicts whether the individual is likely to repay or default on a loan.

## Background
In Kenya, mobile money lenders play a significant role in providing short-term loans to individuals who may not have access to traditional banking services. Many lenders use transaction history from M-Pesa to assess creditworthiness. This project aims to automate and improve that process using machine learning, helping lenders make informed lending decisions based on financial behavior.

## Features
- Extracts income, expenses, loan disbursements, and repayments from M-Pesa statements.
- Provides an interactive web interface where users can upload statements and view results.
- Uses a trained machine learning model to assess loan repayment risk.
- Displays key financial indicators, including income-expense ratio, debt burden, and credit score indicators.
- Generates financial reports and visualizations to help users understand their financial standing.

## Technologies Used
- Python
- Streamlit (for the web interface)
- pdfplumber (for extracting text from M-Pesa PDFs)
- pandas & numpy (for data manipulation)
- scikit-learn (for machine learning model)
- matplotlib & seaborn (for visualizations)

## Project Structure
```
├── mpesa_loan_streamlit.py    # Main Streamlit app
├── loan_model.pkl             # Trained Random Forest model
├── requirements.txt           # Dependencies
├── README.md                  # Project documentation
```

## Installation & Running the App
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/mpesa-loan-default-predictor.git
cd mpesa-loan-default-predictor
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Streamlit App
```bash
streamlit run mpesa_loan_streamlit.py
```
This will open the app in your web browser.

## How It Works
1. Upload an M-Pesa Statement (PDF).
2. The app extracts financial data such as income, expenses, active loans, and loan repayments.
3. It predicts whether the individual is likely to default on a loan.
4. Displays a financial report and visualizations based on extracted data.

## Use Case for Mobile Money Lenders in Kenya
With the rise of mobile lending platforms in Kenya, financial institutions and fintech startups rely heavily on transaction data to assess borrowers. This project helps lenders automate credit risk assessment, reduce manual analysis, and improve decision-making based on real transaction behavior.

## Contributing
If you would like to contribute to this project, feel free to fork the repository, create a branch, and submit a pull request.

## License
This project is open-source and available under the MIT License.

We welcome feedback and suggestions for improvement.


