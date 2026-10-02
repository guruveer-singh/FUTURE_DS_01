# Visualization Guide for Future DS 01 Sales Analysis

This directory contains cleaned, analysis-ready data files for creating visualizations in Excel, Power BI, Tableau, or other BI tools.

## Files Included

1. **product_revenue.csv** - Top products by revenue
   - Columns: Product, Revenue, Quantity, Transaction_Count
   - Sorted by revenue descending (highest first)
   - Top 20 products included

2. **daily_sales.csv** - Daily sales trends
   - Columns: Date, Revenue, Transaction_Count
   - Date format: MM/DD/YYYY
   - Sorted chronologically
   - Ready for time series line charts

3. **country_revenue.csv** - Revenue by country
   - Columns: Country, Revenue, Quantity, Transaction_Count
   - Sorted by revenue descending
   - Shows geographic performance

## Recommended Visualizations

### 1. Revenue Over Time (Line Chart)
- **Data Source**: daily_sales.csv
- **X-Axis**: Date
- **Y-Axis**: Revenue
- **Purpose**: Show sales trends, seasonal patterns, growth/decline
- **Insights**: Holiday spikes, monthly trends, overall direction

### 2. Top Products by Revenue (Horizontal Bar Chart)
- **Data Source**: product_revenue.csv (Top 10-15)
- **X-Axis**: Revenue
- **Y-Axis**: Product Description
- **Purpose**: Identify best-selling products
- **Insights**: Revenue concentration, product performance

### 3. Revenue by Country (Geographic Map or Pie Chart)
- **Data Source**: country_revenue.csv
- **Options**:
  - **Geographic Map**: Color intensity by revenue (if tool supports)
  - **Pie Chart**: Revenue distribution by country
  - **Bar Chart**: Top 10 countries by revenue
- **Purpose**: Understand geographic performance
- **Insights**: Market concentration, expansion opportunities

### 4. Price vs Quantity Analysis (Scatter Plot)
- **Data Source**: Create from original data.csv
- **X-Axis**: UnitPrice
- **Y-Axis**: Quantity
- **Color/Size**: Revenue (Quantity × UnitPrice)
- **Purpose**: Identify pricing strategies
- **Insights**: High-volume low-price vs low-volume high-price products

### 5. Revenue Concentration (Pareto Chart)
- **Data Source**: product_revenue.csv
- **X-Axis**: Products (sorted by revenue desc)
- **Left Y-Axis**: Revenue (bars)
- **Right Y-Axis**: Cumulative % (line)
- **Purpose**: Apply 80/20 rule analysis
- **Insights**: How few products drive most revenue

### 6. Order Value Distribution (Histogram)
- **Data Source**: Calculate from original data
- **X-Axis**: Order Value (Quantity × UnitPrice per InvoiceNo)
- **Y-Axis**: Frequency
- **Purpose**: Understand customer spending patterns
- **Insights**: Typical order size, outliers, customer segments

## How to Create These Visualizations

### In Excel:
1. Import CSV files via Data → Get Data → From Text/CSV
2. Use Insert → Charts to create visualizations
3. Use PivotTables for summaries
4. Format charts for professional appearance

### In Power BI:
1. Get Data → Text/CSV
2. Import the three CSV files
3. Create relationships if needed (Date tables for time intelligence)
4. Use built-in visualizations:
   - Line chart for trends
   - Bar chart for rankings
   - Map visual for geographic
   - Scatter plot for price/quantity
5. Add filters, slicers, and drill-through capabilities

### In Tableau:
1. Connect to Text File for each CSV
2. Drag dimensions/measures to create:
   - Time series: Date (continuous) vs Revenue
   - Bar hierarchy: Product vs Revenue
   - Geographic: Country (geographic role) vs Revenue
   - Scatter: UnitPrice vs Quantity with Revenue size

## Sample Insights to Extract

From these visualizations, you should be able to answer:

### Business Questions:
1. **Which products generate the most revenue?** → Product bar chart
2. **How do sales change over time?** → Daily sales line chart
3. **Which regions are most profitable?** → Country map/bar chart
4. **Where should the business focus to grow faster?** → Combine all insights

### Specific Analyses:
- **Seasonality**: Look for annual patterns in daily sales
- **Product Performance**: Identify winners/losers in product chart
- **Market Concentration**: See if revenue is focused in few countries
- **Price Sensitivity**: Analyze scatter plot for patterns
- **Revenue Distribution**: Pareto chart shows concentration

## Next Steps for Professional Dashboard

1. **Import all three CSV files** into your preferred BI tool
2. **Create the 6 recommended visualizations**
3. **Add filters** (date range, product category, country)
4. **Create key metrics cards** (Total Revenue, Total Orders, AOV)
5. **Add insights** as text boxes or captions
6. **Export as PDF/PNG** or publish to web/share
7. **Document methodology** in your final report

## Data Notes

- **Date Format**: MM/DD/YYYY (US format) - ensure correct parsing
- **Revenue**: Calculated as Quantity × UnitPrice
- **Data Cleaning**: These files assume basic validity (positive quantities/prices)
- **Sample Size**: Product data shows top 20; date and country data are complete

## File Locations
- Ready-to-use files: `/d/FUTURE_DS_01/visualization_ready/`
- Original data: `/d/FUTURE_DS_01/data/data.csv`
- Analysis reports: `/d/FUTURE_DS_01/analysis_report.md`
- Executive summary: `/d/FUTURE_DS_01/analysis/dashboard.txt`

Happy visualizing! 📊
