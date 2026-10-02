# 📊 Future Interns - Task 1: Retail Sales Data Analysis & Executive Dashboard

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.0-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75.svg?logo=plotly&logoColor=white)](https://plotly.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-Modern_UI-38B2AC.svg?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Status](https://img.shields.io/badge/Status-Client--Ready_Production-success.svg)]()

> **Internship Task 1 Deliverable for Future Interns**  
> An end-to-end data analytics, business intelligence, and executive decision-support system analyzing **540k+ retail transactions** ($10.67M gross revenue) to uncover growth opportunities, customer segments, and operational efficiencies.

---

## 🌟 Live Interactive Dashboards

You can explore the interactive dashboards in two ways:

1. **Standalone Executive Web Dashboard (`dashboard.html` / `index.html`)**:
   - Open [dashboard.html](file:///D:/FUTURE_DS_01/dashboard.html) directly in any web browser (Chrome, Edge, Safari, Firefox).
   - Features dynamic KPI metric cards, Plotly.js charts, dark/light theme switching, PDF export, and interactive tabs.
   - Ready for instant deployment on **GitHub Pages**.

2. **Streamlit Interactive Web Application (`app.py`)**:
   - Run locally via terminal:
     ```bash
     streamlit run app.py
     ```
   - Offers real-time date filtering, country multi-select, interactive sliders, data exploration tables, and CSV exports.

---

## 🎯 Executive KPI Highlights

| Metric | Value | Key Business Context |
|---|---|---|
| **Total Gross Revenue** | **$10,666,684.54** | Validated across 530,104 non-cancelled transactions |
| **Total Completed Orders** | **19,960** | Unique invoice orders across 13 months |
| **Active Customer Base** | **4,338** | Repeat purchase rate of 65.4% |
| **Average Order Value (AOV)** | **$534.40** | Median consumer basket: ~$150-$300; B2B wholesale: >$2,500 |
| **Total Product Catalog** | **3,922 SKUs** | Top 19.8% generate 80% of revenue (Pareto Principle) |
| **Global Market Footprint** | **38 Countries** | 84.6% United Kingdom / 15.4% International export markets |

---

## 📈 Visual Analytics & Key Findings

### 1. Monthly Revenue & Holiday Seasonality
![Monthly Revenue Trend](visualizations/01_monthly_revenue_trend.png)
- **Key Finding**: Clear exponential surge during Q4 holiday shopping. Revenue climbed from **$582k in April** to an all-time peak of **$1.51M in November 2011** (+98.2% MoM).
- **Business Action**: Establish supplier inventory buffers and lock packaging contracts by **August** to avoid peak season stockouts.

---

### 2. Top 10 Bestselling Products
![Top 10 Products](visualizations/02_top_10_products_revenue.png)
- **Key Finding**: Top product drivers include *DOTCOM POSTAGE* ($206.2k), *REGENCY CAKESTAND 3 TIER* ($174.5k), and *WHITE HANGING HEART T-LIGHT HOLDER* ($106.3k).
- **Business Action**: High postage revenue indicates an opportunity to launch tiered free-shipping loyalty thresholds (e.g., "Free shipping on orders over $75").

---

### 3. Pareto 80/20 Catalog Concentration
![Pareto Analysis](visualizations/05_pareto_analysis.png)
- **Key Finding**: The top **19.8% of products (776 SKUs)** drive **80.0% of total revenue**. The bottom 80% of the catalog forms a long tail tying up storage costs.
- **Business Action**: Adopt ABC Inventory Classification. Prioritize warehouse placement and just-in-time stock for Class-A items, and run clearance bundles on zero-velocity SKUs.

---

### 4. International Market Expansion
![Revenue by Country](visualizations/03_revenue_by_country.png)
- **Key Finding**: Outside the UK, the Netherlands ($285.4k), EIRE ($283.5k), Germany ($228.9k), and France ($209.7k) are the strongest revenue generators.
- **Business Action**: International orders exhibit **3.2x higher AOV** than domestic orders due to bulk wholesale buying. Launch dedicated localized EU wholesale portals.

---

### 5. Customer RFM Segmentation
![RFM Segments](visualizations/07_rfm_customer_segments.png)
- **Key Finding**: 
  - **Champions & Loyalists (38.2%)**: Drive >60% of total sales.
  - **At Risk / High Value (14.5%)**: 628 high-spending customers have not ordered in >90 days.
- **Business Action**: Implement automated 60-day and 90-day win-back nurture sequences with personalized VIP incentives.

---

### 6. Master 4K Executive Infographic Dashboard
![Master Executive Dashboard](visualizations/08_executive_dashboard_summary.png)

---

## 🗂️ Project Directory Structure

```text
FUTURE_DS_01/
├── app.py                             # Interactive Streamlit analytics application
├── dashboard.html                     # Standalone interactive HTML5/Tailwind/Plotly dashboard
├── index.html                         # GitHub Pages deployable entry point
├── sales_analysis_and_dashboard.ipynb # Complete reproducible Jupyter Notebook
├── analysis_report.md                 # Detailed Executive Business Intelligence Report
├── linkedin_post.txt                  # Formatted LinkedIn showcase post
├── task1.txt                          # Original assignment brief
├── data/
│   └── data.csv                       # Raw sales transaction dataset (541k+ rows)
├── visualization_ready/               # Clean aggregated CSV summaries
│   ├── monthly_sales_summary.csv
│   ├── top_products_summary.csv
│   ├── country_performance_summary.csv
│   └── customer_rfm_segments.csv
├── visualizations/                    # 300 DPI High-Resolution Visual Charts
│   ├── 01_monthly_revenue_trend.png
│   ├── 02_top_10_products_revenue.png
│   ├── 03_revenue_by_country.png
│   ├── 04_sales_heatmap_day_hour.png
│   ├── 05_pareto_analysis.png
│   ├── 06_order_value_distribution.png
│   ├── 07_rfm_customer_segments.png
│   └── 08_executive_dashboard_summary.png
└── scripts/
    ├── generate_analysis_and_charts.py # Automated data pipeline & chart generator
    └── build_notebook.py               # Jupyter Notebook generator
```

---

## 🚀 How to Run & Reproduce

### 1. Clone & Set Up Environment
```bash
# Clone the repository
git clone https://github.com/your-username/FUTURE_DS_01.git
cd FUTURE_DS_01

# Install required dependencies
pip install pandas numpy matplotlib seaborn plotly streamlit openpyxl
```

### 2. Generate All Visuals & Aggregations
```bash
python scripts/generate_analysis_and_charts.py
```

### 3. Launch Interactive Streamlit App
```bash
streamlit run app.py
```

### 4. View Standalone Web Dashboard
Double-click [dashboard.html](file:///D:/FUTURE_DS_01/dashboard.html) or open it in any web browser.

---

## 💡 Strategic Executive Recommendations

1. **Q4 Peak Inventory Readiness**: Lock suppliers and shipping rates by late August for top holiday SKUs.
2. **Pareto Inventory Optimization**: Automate re-order triggers for top 20% revenue-generating items.
3. **Cross-Border Wholesale Expansion**: Expand B2B fulfillment hubs in Netherlands, Germany, and France.
4. **Automated RFM Retention Engine**: Implement automated email win-back workflows for 628 high-value at-risk shoppers.

---

## 👨‍💻 Author & Acknowledgements
- **Program**: Future Interns Data Science Internship Program (Task 1)
- **Tools**: Python, Pandas, Matplotlib, Seaborn, Plotly, Streamlit, HTML5, Tailwind CSS
- **LinkedIn Submission**: [Future Interns](https://www.linkedin.com/company/future-interns/)
