import streamlit as st  # Web app framework
import pdfplumber  # Extract text from PDFs
import re  # Work with text patterns
import pandas as pd  # Handle structured data
import joblib  # Load trained loan prediction model
import numpy as np  # Work with numerical data
import matplotlib.pyplot as plt  # Visualization
import seaborn as sns  # Advanced data visualization

# Load trained loan default prediction model
model = joblib.load("loan_model.pkl")

# Function to extract financial features from M-Pesa statement
def extract_mpesa_features(pdf_path):
    transactions = []  # Store transactions
    total_income = 0  # Sum of credited amounts
    total_expenses = 0  # Sum of debited amounts
    loan_amount = 0  # Total loan disbursed
    loan_repayments = 0  # Total amount repaid
    active_loans = 0  # Number of loans detected
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split('\n')
                for line in lines:
                    match = re.search(r'(\d{2}/\d{2}/\d{4})\s+(.*?)\s+([\d,]+)\s+(CR|DR)', line)
                    if match:
                        date = match.group(1)
                        description = match.group(2).strip().upper()
                        amount = float(match.group(3).replace(',', ''))
                        trans_type = match.group(4)
                        
                        if trans_type == "CR":
                            total_income += amount
                        else:
                            total_expenses += amount
                        
                        if "LOAN DISBURSEMENT" in description:
                            loan_amount += amount
                            active_loans += 1
                        if "LOAN REPAYMENT" in description:
                            loan_repayments += amount
    
    # Compute financial indicators
    income_expense_ratio = total_income / (total_expenses + 1)  # Avoid division by zero
    debt_burden = loan_amount / (total_income + 1)  # Debt burden calculation
    repayment_history = 1 if loan_repayments > 0 else 0  # 1 if repayment exists, else 0
    credit_score_indicator = (repayment_history * 2) - active_loans  # Simple credit score metric
    
    extracted_features = np.array([[total_income, total_expenses, active_loans, loan_amount, 
                                    repayment_history, income_expense_ratio, debt_burden, credit_score_indicator]])
    return extracted_features, {
        "Total Income": total_income,
        "Total Expenses": total_expenses,
        "Active Loans": active_loans,
        "Loan Amount": loan_amount,
        "Repayment History": repayment_history,
        "Income-Expense Ratio": round(income_expense_ratio, 2),
        "Debt Burden": round(debt_burden, 2),
        "Credit Score Indicator": credit_score_indicator
    }

# Streamlit Web App
st.title("M-Pesa Loan Default Predictor")
st.write("Upload your M-Pesa statement (PDF) to analyze your financial data and predict loan default risk.")

uploaded_file = st.file_uploader("Upload M-Pesa Statement (PDF)", type=["pdf"])
if uploaded_file:
    extracted_features, financial_report = extract_mpesa_features(uploaded_file)
    
    # Convert extracted data to DataFrame
    feature_names = ["Income", "Expenses", "Active_Loans", "Loan_Amount", "Repayment_History",
                     "Income_Expense_Ratio", "Debt_Burden", "Credit_Score_Indicator"]
    extracted_features_df = pd.DataFrame(extracted_features, columns=feature_names)
    
    # Make prediction
    prediction = model.predict(extracted_features_df)
    result = "High Risk: Likely to Default" if prediction[0] == 1 else "Low Risk: Likely to Repay"
    
    # Display results
    st.subheader("Prediction Result")
    st.write(result)
    
    # Show financial analysis
    st.subheader("Financial Report")
    st.json(financial_report)
    
    # Plot financial data
    st.subheader("Financial Overview")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x=list(financial_report.keys()), y=list(financial_report.values()), ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    st.pyplot(fig)
