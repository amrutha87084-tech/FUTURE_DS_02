# FUTURE_DS_02
Customer Churn Analysis using Python and Power BI

# FUTURE_DS_02 – Customer Churn Analysis

## Project Overview

This project analyzes customer churn using the Telco Customer Churn dataset. The analysis was performed using Python for data inspection and analysis, and Power BI for interactive dashboard development.

The objective is to identify customer churn patterns based on contract type, internet service, tenure, monthly charges, payment method, and additional services.

## Tools Used

- Python
- Pandas
- Matplotlib
- Power BI
- Jupyter Notebook / VS Code

## Dataset

Dataset: Telco Customer Churn

The dataset contains customer information, service details, contract information, billing details, and churn status.

## Key Findings

- Total Customers: 7,043
- Churned Customers: 1,869
- Overall Churn Rate: 26.54%
- Average Customer Tenure: 32.37 months

### Important Churn Patterns

- Month-to-month customers have a higher observed churn rate than customers on longer-term contracts.
- Fiber optic customers show higher observed churn than DSL and customers without internet service.
- Customers with shorter tenure show higher churn.
- Electronic check users show relatively higher churn.
- Customers without Tech Support and Online Security show higher observed churn.

## Power BI Dashboard

The Power BI dashboard includes:

- Total Customers KPI
- Churned Customers KPI
- Churn Rate KPI
- Average Tenure KPI
- Churn by Contract Type
- Churn by Internet Service
- Churn by Payment Method
- Churn by Tenure Group
- Churn by Monthly Charges
- Churn by Tech Support
- Churn by Online Security
- Churn Rate by Contract and Internet Service
- Interactive slicers for Contract Type, Internet Service, and Customer Tenure

## Project Structure

```text
FUTURE_DS_02/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── src/
│   └── analysis.py
│
├── results/
│   └── Analysis outputs and report files
│
├── FUTURE_DS_02_Churn_Analysis.pbix
│
└── README.md
