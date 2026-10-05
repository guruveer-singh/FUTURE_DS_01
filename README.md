# 💼 Future Interns - Data Science & Analytics Portfolio

[![Excel](https://img.shields.io/badge/Excel-Dashboard_Ready-217346.svg?logo=microsoft-excel&logoColor=white)](Customer_Retention_Dashboard.xlsx)
[![PowerBI](https://img.shields.io/badge/Power_BI-PBIX_Model-F2C811.svg?logo=power-bi&logoColor=black)](FUTURE_DS_01.pbix)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg?logo=python&logoColor=white)](customer_retention_and_churn_analysis.ipynb)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626.svg?logo=jupyter&logoColor=white)](customer_retention_and_churn_analysis.ipynb)
[![Status](https://img.shields.io/badge/Status-Client--Ready_Production-success.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

> **Future Interns Data Science & Analytics Program (2026)**  
> Production-grade data analytics, executive dashboard engineering, cohort retention modeling, and strategic business intelligence portfolio.

---

## 📌 Portfolio Project Quick Navigation

| Project | Domain | Core Tools | Primary Deliverable | Status |
|---|---|---|---|---|
| **[Task 2: Customer Retention & Churn Analysis](#-task-2-customer-retention--churn-analysis)** | Subscription & SaaS Analytics | Excel, Python, Pandas, Matplotlib | [Excel Dashboard](Customer_Retention_Dashboard.xlsx) \| [Report](retention_analysis_report.md) \| [Notebook](customer_retention_and_churn_analysis.ipynb) | ✅ **Complete** |
| **[Task 1: Retail Sales Analysis & Executive Dashboard](#-task-1-retail-sales-data-analysis--executive-dashboard)** | E-Commerce & Retail BI | Excel, Power BI, Python, RFM | [Excel Dashboard](Retail_Sales_Dashboard.xlsx) \| [PBIX Model](FUTURE_DS_01.pbix) \| [Report](analysis_report.md) | ✅ **Complete** |

---

# 🚀 Task 2: Customer Retention & Churn Analysis

> **Executive Business Objective:**  
> In subscription and recurring revenue models, acquiring a replacement customer costs **5x to 7x more** than retaining an existing one. This task analyzes **7,043 subscriber accounts** ($456.1K baseline MRR) to understand why customers churn, identify high-risk segments, model customer cohort survival over 72 months, and formulate high-ROI retention interventions.

### 📑 Task 2 Core Deliverables
- **[Customer_Retention_Dashboard.xlsx](Customer_Retention_Dashboard.xlsx)**: 4-tab client-ready Excel dashboard featuring symmetrical KPI cards, native Excel charts, cohort retention tables, customer churn risk scoring, and 7,043 cleaned records with autofilters.
- **[retention_analysis_report.md](retention_analysis_report.md)**: In-depth executive advisory report detailing cohort decay, root-cause drivers, LTV economics, and a 30-60-90 day retention roadmap.
- **[customer_retention_and_churn_analysis.ipynb](customer_retention_and_churn_analysis.ipynb)**: Reproducible Python notebook covering data cleaning, EDA, cohort survival curves, risk modeling, and financial simulations.
- **[TASK2_README.md](TASK2_README.md)**: Dedicated stand-alone documentation for Task 2.
- **[task2_linkedin_post.txt](task2_linkedin_post.txt)**: Pre-formatted professional LinkedIn showcase post.
- **[visualizations/retention/](visualizations/retention/)**: 7 high-resolution (300 DPI) publication-ready charts.

### 🎯 Task 2 Executive KPI Scorecard
- **Total Subscriber Base:** 7,043 accounts (5,174 Retained | 1,869 Churned)
- **Portfolio Churn Rate:** **26.54%** (SaaS target benchmark: < 5–8%)
- **Monthly Revenue Lost (MRR):** **$139,130.85 / mo** (30.5% of total portfolio MRR)
- **Annualized Run-Rate Loss:** **$1,669,570.20 / year**
- **Year-1 Retention Rate:** **52.56%** (**47.4% churn in months 0–12** - The Onboarding Cliff)
- **Observed Mean Account Tenure:** **32.4 Months** (Snapshot base; right-censored active accounts)
- **Mature Cumulative Spend (TotalCharges):** **$5,180.67** (18.8x higher than Year-1 charges of $275)

> **📌 Methodological Note:** This analysis evaluates a **cross-sectional snapshot** of 7,043 customer accounts observed at a single point in time. Grouping accounts into 12-month tenure lifecycle brackets provides a cross-sectional proxy for attrition propensity. Active accounts are right-censored; 32.4 months represents observed mean tenure rather than completed actuarial customer lifetimes.

### 📈 Task 2 Visual Analytics & Strategic Findings

#### 1. Portfolio Churn Overview & Revenue Exposure
![Churn Overview & Revenue Exposure](visualizations/retention/01_churn_overview_and_revenue.png)
- **Key Finding:** Churned accounts account for **30.5% of total portfolio revenue** ($139.1K/mo), indicating that churn disproportionately affects higher-priced tiers ($74.44/mo churned vs. $61.26/mo retained).

#### 2. The Onboarding Cliff (Tenure Bracket Retention & Churn Decay)
![Cohort Tenure Retention Survival](visualizations/retention/02_cohort_tenure_survival.png)
- **Key Finding:** **55.5% of all churn occurs in months 0–12** (47.4% first-year churn). Accounts active past Month 24 experience attrition rates dropping to 21.6% and down to 6.6% for Month 61–72. Proactive onboarding in Days 1–90 is the highest leverage retention initiative.

#### 3. Contract Commitment as the Strongest Retention Anchor
![Contract Risk Breakdown](visualizations/retention/03_contract_risk_breakdown.png)
- **Key Finding:** Month-to-month contracts have a **42.7% churn rate** and drive **86.9% ($120.8K/mo) of lost MRR**. In contrast, 1-Year plans churn at 11.3% and 2-Year plans at only 2.8% (a **15x risk reduction**).

#### 4. The Fiber Optic Support Paradox
![Fiber Optic Support Paradox](visualizations/retention/04_fiber_optic_service_paradox.png)
- **Key Finding:** Premium Fiber Optic users ($91.50/mo) churn at **41.9%** vs. 19.0% for DSL. However, bundling Tech Support and Online Security cuts churn by **54% (down to 22.6%)**. Unbundled technical support damages customer satisfaction.

#### 5. Payment Channel Friction & Involuntary Churn
![Payment Method Friction](visualizations/retention/05_payment_method_friction.png)
- **Key Finding:** Electronic Check users churn at **45.3%**, while automated Credit Card and Bank Transfer churn at 15.2% and 16.7%. Auto-pay eliminates monthly invoice friction and involuntary billing lapses.

#### 6. Customer Lifetime Value (CLV) Progression
![Customer Lifetime Value Progression](visualizations/retention/06_clv_and_tenure_progression.png)
- **Key Finding:** Cumulative customer value expands by **18.8x** from Year 1 ($275) to Year 6 ($5,180). Month 61–72 subscribers contribute **$7.29M (45.4%) of all historical revenue**.

#### 7. Executive Retention Dashboard Summary
![Executive Retention Dashboard](visualizations/retention/07_executive_retention_dashboard_summary.png)

### 💡 Task 2 Strategic Retention Playbook
1. **Contract Migration Campaign:** Offer a 15% annual discount or 2 months free to migrate Month-to-Month accounts. Converting 20% saves **~$24,000/mo ($288K ARR)**.
2. **Day 1–90 Structured Onboarding:** Deploy automated telemetry alerts and proactive customer success check-ins to defeat the 47.4% Year-1 churn cliff.
3. **Mandatory Fiber Support Bundling:** Bundle 24/7 Priority Tech Support directly into base Fiber Optic plans, capturing an immediate 54% churn reduction.
4. **Auto-Pay Conversion Incentive:** Offer a $5/month statement credit for enrolling in Auto-Pay, slashing manual billing drop-offs.

---

# 📊 Task 1: Retail Sales Data Analysis & Executive Dashboard

> **Executive Business Objective:**  
> An end-to-end data analytics and business intelligence project analyzing **540,000+ retail sales transactions** ($10.67M gross revenue) to answer core business questions on revenue trends, top-selling products, regional profitability, and strategic growth opportunities.

### 📑 Task 1 Core Deliverables
- **[Retail_Sales_Dashboard.xlsx](Retail_Sales_Dashboard.xlsx)**: Client-ready visual Excel dashboard with formatted KPI cards, native Excel charts (Monthly Trend, Top Products, Geo Share, Order Tiers), and strategic takeaways.
- **[FUTURE_DS_01.pbix](FUTURE_DS_01.pbix)**: Power BI project file pre-loaded with the complete retail transaction data model.
- **[analysis_report.md](analysis_report.md)**: Comprehensive markdown business report detailing findings, Pareto concentration, and growth recommendations.
- **[sales_analysis_and_dashboard.ipynb](sales_analysis_and_dashboard.ipynb)**: End-to-end reproducible Python notebook covering data cleaning, EDA, KPI engineering, and statistical analysis.
- **[linkedin_post.txt](linkedin_post.txt)**: Submission text ready to share on LinkedIn, tagging Future Interns.

### 🎯 Task 1 Executive KPI Highlights
- **Total Gross Revenue:** **$10,666,684.54** (530,104 cleaned transactions)
- **Total Completed Orders:** **19,960** unique invoice orders
- **Active Customer Base:** **4,338** customers (Repeat purchase rate of 65.4%)
- **Average Order Value (AOV):** **$534.40** (Wholesale B2B orders: >$2,500)
- **Product Catalog:** **3,922 SKUs** (Top 19.8% generate 80% of revenue - Pareto Principle)
- **Global Footprint:** **38 Countries** (84.6% UK / 15.4% International export markets)

### 📈 Task 1 Visual Analytics & Key Findings
- **Q4 Holiday Seasonality:** Revenue peaked at **$1.51M in November 2011** (+98.2% MoM) driven by holiday shopping.
- **Pareto Catalog Concentration:** Top 19.8% of products drive 80% of revenue; top items include *DOTCOM POSTAGE* ($206.2k) and *REGENCY CAKESTAND* ($174.5k).
- **International Market Expansion:** International orders have a **3.2x higher AOV** than domestic UK retail orders.
- **Customer RFM Segments:** Identified 628 high-value customers ($1.45M revenue) at risk (>90 days inactive).

---

## 🗂️ Complete Repository Directory Structure

```text
FUTURE_DS_01/
├── Customer_Retention_Dashboard.xlsx        # [Task 2] Visual Excel retention dashboard with native charts
├── customer_retention_and_churn_analysis.ipynb # [Task 2] Reproducible Python cohort & churn notebook
├── retention_analysis_report.md             # [Task 2] Comprehensive executive advisory report
├── TASK2_README.md                          # [Task 2] Dedicated Task 2 documentation
├── task2_linkedin_post.txt                  # [Task 2] LinkedIn showcase post
├── task2.txt                                # [Task 2] Assignment brief
├── Retail_Sales_Dashboard.xlsx              # [Task 1] Visual Excel sales dashboard
├── FUTURE_DS_01.pbix                        # [Task 1] Power BI data model
├── sales_analysis_and_dashboard.ipynb       # [Task 1] Jupyter sales analysis notebook
├── analysis_report.md                       # [Task 1] Task 1 Executive BI report
├── linkedin_post.txt                        # [Task 1] LinkedIn post
├── PROJECT_SUMMARY_CONTEXT.md               # Portfolio context summary
├── README.md                                # Master Portfolio Documentation
├── data/
│   ├── data.csv                             # [Task 1] 540k+ retail transaction dataset
│   ├── telco_customer_churn.csv             # [Task 2] Raw customer churn dataset
│   └── telco_customer_churn_cleaned.csv     # [Task 2] Cleaned dataset with risk scoring
├── scripts/                                 # Build automation scripts
│   ├── build_excel_dashboard.py
│   ├── build_jupyter_notebook.py
│   └── create_charts.py
└── visualizations/                          # 300 DPI High-Resolution Visualizations
    ├── 01_monthly_revenue_trend.png         # [Task 1]
    ├── 02_top_10_products_revenue.png       # [Task 1]
    ├── 03_revenue_by_country.png            # [Task 1]
    ├── 04_sales_heatmap_day_hour.png        # [Task 1]
    ├── 05_pareto_analysis.png               # [Task 1]
    ├── 06_order_value_distribution.png      # [Task 1]
    ├── 07_rfm_customer_segments.png         # [Task 1]
    ├── 08_executive_dashboard_summary.png   # [Task 1]
    └── retention/                           # [Task 2] Customer Retention Visualizations
        ├── 01_churn_overview_and_revenue.png
        ├── 02_cohort_tenure_survival.png
        ├── 03_contract_risk_breakdown.png
        ├── 04_fiber_optic_service_paradox.png
        ├── 05_payment_method_friction.png
        ├── 06_clv_and_tenure_progression.png
        └── 07_executive_retention_dashboard_summary.png
```

---

## 👨‍💻 Author & Acknowledgements
- **Program:** Future Interns Data Science & Analytics Internship (2026)
- **Intern:** Guruveer Singh
- **GitHub Repository:** [guruveer-singh/FUTURE_DS_01](https://github.com/guruveer-singh/FUTURE_DS_01)
- **LinkedIn Submission:** [Future Interns](https://www.linkedin.com/company/future-interns/)
