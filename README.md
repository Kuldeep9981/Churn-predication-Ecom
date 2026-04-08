# 🔮 ChurnIQ — Customer Churn Intelligence Dashboard

> **Predict risk. Understand behavior. Retain customers.**

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://churn-predication-ecom.streamlit.app)
[![Model](https://img.shields.io/badge/Model-Random%20Forest-4CAF50?style=for-the-badge)](https://scikit-learn.org/)
[![Accuracy](https://img.shields.io/badge/Accuracy-91.0%25-blue?style=for-the-badge)]()
[![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge&logo=python)](https://python.org)

---

## 📌 Project Overview

ChurnIQ is an end-to-end **customer churn prediction system** built on 50,000 e-commerce customer records. It identifies which customers are at risk of churning and surfaces the behavioral signals behind that risk — enabling data-driven retention strategies.

The project covers the full data analyst workflow:

- Data cleaning & feature engineering
- Exploratory data analysis (EDA)
- Model training, comparison & evaluation
- Business interpretation & recommendations
- Interactive Streamlit dashboard for real-time prediction

---

## 🚀 Live Demo

👉 **[churn-predication-ecom.streamlit.app](https://churn-predication-ecom.streamlit.app)**

The dashboard has three tabs:

| Tab | Description |
|---|---|
| 🎯 Churn Prediction | Enter a customer profile and get a real-time churn risk score |
| 📊 EDA Insights | Visualize patterns across the dataset |
| ⚡ Feature Importance | See which features drive churn the most |

---

## 📸 Screenshots

### Churn Prediction Tab
<img src="ChurnIQ Dashboard.png" width="900">

### Prediction Result
<img src="Prediction Result.png" width="900">

### Feature Importance
<img src="Feature Importance.png" width="900">


---

## 📂 Project Structure
---

## 📊 Dataset Overview

| Property | Details |
|---|---|
| Records | 50,000 customers |
| Features | 25 columns (demographic, behavioral, transactional, support) |
| Target | `Churned` (0 = retained, 1 = churned) |
| Churn Rate | ~29% (14,450 churned / 35,550 retained) |

### Data Cleaning Steps

- **Missing values** — Numerical columns imputed with median
- **Outliers** — Age values above 75 removed; high-purchase records kept as valid
- **Encoding** — One-hot encoding applied to `Gender`, `Country`, `City`, `Signup_Quarter`, `Customer_Segment`
- **Dropped columns** — `Wishlist_Items`, `Product_Reviews_Written`, `Payment_Method_Diversity` (low predictive value)

---

## 🔍 Key EDA Insights

### Churn vs Retention Patterns

| Signal | Retained Customers | Churned Customers |
|---|---|---|
| Avg. Total Purchases | 13.83 | 11.35 |
| Avg. Days Since Last Purchase | 26.54 days | 35.97 days |
| Login Frequency | Higher | Lower |
| Session Duration | Longer | Shorter |

- **Inactivity is a leading churn indicator** — churned customers had ~35% longer gaps since their last purchase.
- **Engagement metrics** (login frequency, session duration) were consistently lower among churners.
- **Cart abandonment & support calls** emerged as the strongest friction-based signals.
- **Demographics** (gender, country, city) showed smaller churn-rate differences compared to behavioral features.

---

## 🤖 Models & Performance

Two models were trained and compared:

| Model | Accuracy | Churn Precision | Churn Recall |
|---|---|---|---|
| Logistic Regression (baseline) | 70.7% | 0.49 | 0.73 |
| **Random Forest (final)** | **91.0%** | **0.92** | **0.76** |

The **Random Forest** model was selected as the final model. It strikes the right balance for a retention use case — catching most churners (recall = 0.76) while keeping false alarms low (precision = 0.92).

---

## ⚡ Top 10 Churn Drivers (Feature Importance)

| Rank | Feature | Importance Score |
|---|---|---|
| 1 | Customer Service Calls | 0.1239 |
| 2 | Lifetime Value | 0.1081 |
| 3 | Cart Abandonment Rate | 0.0907 |
| 4 | Age | 0.0715 |
| 5 | Discount Usage Rate | 0.0540 |
| 6 | Average Order Value | 0.0501 |
| 7 | Total Purchases | 0.0491 |
| 8 | Email Open Rate | 0.0466 |
| 9 | Session Duration Avg | 0.0458 |
| 10 | Days Since Last Purchase | 0.0441 |

> 💡 **Key Insight:** Churn is driven more by **customer experience and engagement** than by demographics. Frequent support calls and cart abandonment are strong friction indicators.

---

## 💼 Business Recommendations

Based on the model's findings, the most impactful retention actions are:

1. **Improve support quality** — `Customer_Service_Calls` is the #1 churn driver. Reducing the need for support calls and improving resolution quality directly reduces churn risk.
2. **Reduce checkout friction** — High `Cart_Abandonment_Rate` signals friction in the buying journey. Simplify checkout flows and use abandonment re-targeting.
3. **Re-engage inactive customers** — Customers with high `Days_Since_Last_Purchase` are at elevated risk. Trigger re-engagement campaigns for customers inactive for 30+ days.
4. **Protect high-value customers** — `Lifetime_Value` is the #2 driver. High-LTV customers who show early warning signals should receive proactive outreach.
5. **Personalize email campaigns** — Low `Email_Open_Rate` correlates with churn. Improve email relevance and targeting.

---

