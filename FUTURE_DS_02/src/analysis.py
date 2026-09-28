import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/Telco-Customer-Churn.csv")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

# Fill missing TotalCharges
df["TotalCharges"] = df["TotalCharges"].fillna(0)

# -----------------------------
# BASIC KPIs
# -----------------------------

total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
retained_customers = (df["Churn"] == "No").sum()
churn_rate = churned_customers / total_customers * 100

print("\n========== KEY KPIs ==========")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)
print("Churn Rate:", round(churn_rate, 2), "%")

# -----------------------------
# CHURN BY CUSTOMER ATTRIBUTES
# -----------------------------

def churn_rate_by(column):
    result = pd.crosstab(
        df[column],
        df["Churn"],
        normalize="index"
    ) * 100

    result = result.round(2)

    print(f"\n--- CHURN BY {column.upper()} ---")
    print(result)

    return result


contract_churn = churn_rate_by("Contract")
internet_churn = churn_rate_by("InternetService")
payment_churn = churn_rate_by("PaymentMethod")
senior_churn = churn_rate_by("SeniorCitizen")
partner_churn = churn_rate_by("Partner")
dependents_churn = churn_rate_by("Dependents")
paperless_churn = churn_rate_by("PaperlessBilling")
techsupport_churn = churn_rate_by("TechSupport")
security_churn = churn_rate_by("OnlineSecurity")

# -----------------------------
# TENURE ANALYSIS
# -----------------------------

print("\n========== TENURE ANALYSIS ==========")
print(df.groupby("Churn")["tenure"].mean())

# Create tenure groups
df["TenureGroup"] = pd.cut(
    df["tenure"],
    bins=[-1, 6, 12, 24, 48, 72],
    labels=[
        "0-6 months",
        "7-12 months",
        "13-24 months",
        "25-48 months",
        "49-72 months"
    ]
)

tenure_churn = pd.crosstab(
    df["TenureGroup"],
    df["Churn"],
    normalize="index"
) * 100

print("\n--- CHURN BY TENURE GROUP ---")
print(tenure_churn.round(2))

# -----------------------------
# MONTHLY CHARGES ANALYSIS
# -----------------------------

df["MonthlyChargeGroup"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0, 40, 70, 100, float("inf")],
    labels=[
        "Low (<$40)",
        "Medium ($40-$70)",
        "High ($70-$100)",
        "Very High (>$100)"
    ]
)

charge_churn = pd.crosstab(
    df["MonthlyChargeGroup"],
    df["Churn"],
    normalize="index"
) * 100

print("\n--- CHURN BY MONTHLY CHARGE GROUP ---")
print(charge_churn.round(2))

# -----------------------------
# VISUALIZATIONS
# -----------------------------

sns.set_theme(style="whitegrid")

# 1. Overall churn
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("results/churn_distribution.png")
plt.close()

# 2. Contract
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Contract", hue="Churn")
plt.title("Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("results/churn_by_contract.png")
plt.close()

# 3. Internet service
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="InternetService", hue="Churn")
plt.title("Churn by Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("results/churn_by_internet.png")
plt.close()

# 4. Payment method
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x="PaymentMethod", hue="Churn")
plt.title("Churn by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Customers")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("results/churn_by_payment.png")
plt.close()

# 5. Tenure
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="TenureGroup", hue="Churn")
plt.title("Churn by Tenure Group")
plt.xlabel("Tenure")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("results/churn_by_tenure.png")
plt.close()

# 6. Monthly charges
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="MonthlyChargeGroup", hue="Churn")
plt.title("Churn by Monthly Charges")
plt.xlabel("Monthly Charge Group")
plt.ylabel("Number of Customers")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("results/churn_by_monthly_charge.png")
plt.close()

# 7. Tech support
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="TechSupport", hue="Churn")
plt.title("Churn by Tech Support")
plt.xlabel("Tech Support")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("results/churn_by_tech_support.png")
plt.close()

# 8. Online security
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="OnlineSecurity", hue="Churn")
plt.title("Churn by Online Security")
plt.xlabel("Online Security")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("results/churn_by_security.png")
plt.close()

# -----------------------------
# SAVE CLEANED DATA
# -----------------------------

df.to_csv("results/cleaned_telco_churn.csv", index=False)

print("\n================================")
print("CHURN ANALYSIS COMPLETED")
print("================================")
print("Charts saved inside the results folder.")
print("Cleaned dataset saved successfully.")
# -----------------------------
# COMBINATION ANALYSIS
# -----------------------------

contract_internet = pd.crosstab(
    df["Contract"],
    df["InternetService"],
    values=(df["Churn"] == "Yes"),
    aggfunc="mean"
) * 100

print("\n--- CHURN RATE: CONTRACT × INTERNET SERVICE ---")
print(contract_internet.round(2))

plt.figure(figsize=(8, 5))
sns.heatmap(
    contract_internet,
    annot=True,
    fmt=".1f",
    cmap="Blues"
)
plt.title("Churn Rate by Contract and Internet Service")
plt.xlabel("Internet Service")
plt.ylabel("Contract Type")
plt.tight_layout()
plt.savefig("results/churn_contract_internet_heatmap.png")
plt.close()
# -----------------------------
# CUSTOMER LIFETIME ANALYSIS
# -----------------------------

lifetime_analysis = df.groupby("Churn").agg(
    Customer_Count=("customerID", "count"),
    Average_Tenure_Months=("tenure", "mean"),
    Median_Tenure_Months=("tenure", "median"),
    Average_Monthly_Charges=("MonthlyCharges", "mean"),
    Average_Total_Charges=("TotalCharges", "mean"),
    Median_Total_Charges=("TotalCharges", "median")
).round(2)

print("\n========== CUSTOMER LIFETIME ANALYSIS ==========")
print(lifetime_analysis)

# Save lifetime analysis
lifetime_analysis.to_csv("results/customer_lifetime_analysis.csv")
# -----------------------------
# KEY CHURN DRIVERS SUMMARY
# -----------------------------

driver_summary = pd.DataFrame({
    "Factor": [
        "Contract Type",
        "Internet Service",
        "Payment Method",
        "Tech Support",
        "Online Security",
        "Tenure",
        "Monthly Charges"
    ],
    "Key Observation": [
        "Month-to-month customers have 42.71% churn",
        "Fiber optic customers have 41.89% churn",
        "Electronic check users have 45.29% churn",
        "Customers without tech support have 41.64% churn",
        "Customers without online security have 41.77% churn",
        "0-6 month customers have 52.94% churn",
        "High ($70-$100) group has 37.82% churn"
    ]
})

print("\n========== KEY CHURN DRIVERS ==========")
print(driver_summary.to_string(index=False))

driver_summary.to_csv(
    "results/key_churn_drivers.csv",
    index=False
)
# -----------------------------
# BUSINESS INSIGHTS
# -----------------------------

insights = pd.DataFrame({
    "Insight": [
        "Month-to-month customers show a high observed churn rate.",
        "Customers in the first 6 months show the highest churn rate.",
        "Electronic check users show a high observed churn rate.",
        "Fiber optic customers show a high observed churn rate.",
        "Customers without technical support show higher observed churn.",
        "Customers without online security show higher observed churn.",
        "Higher monthly charges are associated with higher churn in the analyzed charge groups.",
        "Churned customers have substantially shorter average tenure than retained customers."
    ],
    "Evidence": [
        "42.71% churn",
        "52.94% churn",
        "45.29% churn",
        "41.89% churn",
        "41.64% churn",
        "41.77% churn",
        "37.82% churn for $70-$100 group",
        "17.98 vs 37.57 months"
    ]
})

print("\n========== BUSINESS INSIGHTS ==========")
print(insights.to_string(index=False))

insights.to_csv(
    "results/business_insights.csv",
    index=False
)
# -----------------------------
# RETENTION RECOMMENDATIONS
# -----------------------------

recommendations = pd.DataFrame({
    "Observed Finding": [
        "0-6 month customers have 52.94% churn",
        "Month-to-month customers have 42.71% churn",
        "Electronic check users have 45.29% churn",
        "Fiber optic customers have 41.89% churn",
        "Customers without Tech Support have 41.64% churn",
        "Customers without Online Security have 41.77% churn",
        "$70-$100 monthly charge group has 37.82% churn"
    ],
    "Recommended Action": [
        "Create a first-6-month onboarding and customer check-in program.",
        "Provide suitable incentives and plan options for longer-term contracts.",
        "Review the electronic payment experience and promote convenient alternatives.",
        "Investigate service quality and customer support experience for fiber customers.",
        "Increase awareness or availability of technical support services.",
        "Promote relevant security features and explain their customer benefits.",
        "Review pricing, perceived value, and service bundles in this charge range."
    ]
})

print("\n========== RETENTION RECOMMENDATIONS ==========")
print(recommendations.to_string(index=False))

recommendations.to_csv(
    "results/retention_recommendations.csv",
    index=False
)