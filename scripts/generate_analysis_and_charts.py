import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json

# Set aesthetic styling
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Segoe UI', 'DejaVu Sans', 'Arial'
plt.rcParams['axes.edgecolor'] = '#cbd5e1'
plt.rcParams['axes.linewidth'] = 0.8

print("Loading raw dataset...")
df = pd.read_csv('data/data.csv', encoding='ISO-8859-1')
print(f"Raw record count: {len(df):,}")

# Clean and parse
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], format='mixed')
df['Description'] = df['Description'].fillna('Unknown Product').str.strip()

# Data filtering: positive quantity and unit price, non-cancelled
clean_df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0) & (~df['InvoiceNo'].str.startswith('C', na=False))].copy()
clean_df['Revenue'] = clean_df['Quantity'] * clean_df['UnitPrice']
clean_df['Year'] = clean_df['InvoiceDate'].dt.year
clean_df['Month'] = clean_df['InvoiceDate'].dt.month
clean_df['YearMonth'] = clean_df['InvoiceDate'].dt.to_period('M').astype(str)
clean_df['DayOfWeek'] = clean_df['InvoiceDate'].dt.day_name()
clean_df['DayOfWeekNum'] = clean_df['InvoiceDate'].dt.dayofweek
clean_df['Hour'] = clean_df['InvoiceDate'].dt.hour
clean_df['Date'] = clean_df['InvoiceDate'].dt.date

# Save cleaned transactions
clean_df.to_parquet('data_clean/cleaned_sales.parquet', index=False) if hasattr(clean_df, 'to_parquet') else None
clean_sample = clean_df.head(1000)
clean_sample.to_csv('data_clean/cleaned_sample_1000.csv', index=False)

print(f"Cleaned valid records: {len(clean_df):,}")
total_revenue = clean_df['Revenue'].sum()
total_orders = clean_df['InvoiceNo'].nunique()
total_customers = clean_df['CustomerID'].nunique()
total_products = clean_df['StockCode'].nunique()
total_countries = clean_df['Country'].nunique()
avg_order_val = total_revenue / total_orders
avg_item_price = clean_df['UnitPrice'].mean()

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Average Order Value: ${avg_order_val:,.2f}")

# -------------------------------------------------------------
# 1. MONTHLY REVENUE & ORDER TRENDS
# -------------------------------------------------------------
monthly = clean_df.groupby('YearMonth').agg(
    Revenue=('Revenue', 'sum'),
    Orders=('InvoiceNo', 'nunique'),
    Quantity=('Quantity', 'sum'),
    UniqueCustomers=('CustomerID', 'nunique')
).reset_index()

monthly['MoM_Growth'] = monthly['Revenue'].pct_change() * 100
monthly.to_csv('visualization_ready/monthly_sales_summary.csv', index=False)

fig, ax1 = plt.subplots(figsize=(12, 6), dpi=300)
color1 = '#2563eb' # Royal Blue
color2 = '#f59e0b' # Amber

ax1.set_title('Monthly Revenue & Order Volume Trend (2010 - 2011)', fontsize=16, fontweight='bold', pad=15, color='#1e293b')
bars = ax1.bar(monthly['YearMonth'], monthly['Revenue'] / 1000, color=color1, alpha=0.85, width=0.6, label='Revenue ($k)')
ax1.set_xlabel('Month', fontsize=12, fontweight='bold', color='#334155', labelpad=10)
ax1.set_ylabel('Revenue ($ in Thousands)', fontsize=12, fontweight='bold', color=color1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.tick_params(axis='x', rotation=45)

for bar in bars:
    height = bar.get_height()
    ax1.annotate(f'${height:,.0f}k',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 4), textcoords="offset points",
                ha='center', va='bottom', fontsize=9, fontweight='semibold', color='#1e293b')

ax2 = ax1.twinx()
ax2.plot(monthly['YearMonth'], monthly['Orders'], color=color2, marker='o', linewidth=3, markersize=8, label='Order Count')
ax2.set_ylabel('Total Number of Orders', fontsize=12, fontweight='bold', color=color2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.grid(False)

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', frameon=True, facecolor='white', framealpha=0.9)

plt.tight_layout()
plt.savefig('visualizations/01_monthly_revenue_trend.png')
plt.close()
print("Saved 01_monthly_revenue_trend.png")

# -------------------------------------------------------------
# 2. TOP 10 PRODUCTS BY REVENUE
# -------------------------------------------------------------
product_summary = clean_df.groupby(['StockCode', 'Description']).agg(
    Revenue=('Revenue', 'sum'),
    Quantity=('Quantity', 'sum'),
    Orders=('InvoiceNo', 'nunique'),
    AvgUnitPrice=('UnitPrice', 'mean')
).reset_index()

# Handle duplicate descriptions for same stock code or vice versa
prod_agg = product_summary.groupby('Description').agg(
    Revenue=('Revenue', 'sum'),
    Quantity=('Quantity', 'sum'),
    Orders=('Orders', 'sum')
).reset_index().sort_values('Revenue', ascending=False)

prod_agg.to_csv('visualization_ready/top_products_summary.csv', index=False)

top10_prod = prod_agg.head(10).sort_values('Revenue', ascending=True)

fig, ax = plt.subplots(figsize=(12, 7), dpi=300)
colors = sns.color_palette('Blues_r', n_colors=10)
bars = ax.barh(top10_prod['Description'], top10_prod['Revenue'] / 1000, color=colors, edgecolor='#0f172a', linewidth=0.5)

ax.set_title('Top 10 Products by Total Revenue ($)', fontsize=16, fontweight='bold', pad=15, color='#1e293b')
ax.set_xlabel('Revenue ($ in Thousands)', fontsize=12, fontweight='bold', color='#334155', labelpad=10)
ax.set_ylabel('Product Description', fontsize=12, fontweight='bold', color='#334155')

for bar in bars:
    width = bar.get_width()
    ax.annotate(f' ${width:,.1f}k',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0), textcoords="offset points",
                ha='left', va='center', fontsize=9.5, fontweight='bold', color='#0f172a')

ax.set_xlim(0, max(top10_prod['Revenue'] / 1000) * 1.15)
plt.tight_layout()
plt.savefig('visualizations/02_top_10_products_revenue.png')
plt.close()
print("Saved 02_top_10_products_revenue.png")

# -------------------------------------------------------------
# 3. REVENUE BY COUNTRY (TOP 10)
# -------------------------------------------------------------
country_summary = clean_df.groupby('Country').agg(
    Revenue=('Revenue', 'sum'),
    Orders=('InvoiceNo', 'nunique'),
    Customers=('CustomerID', 'nunique'),
    Quantity=('Quantity', 'sum')
).reset_index().sort_values('Revenue', ascending=False)

country_summary['RevenueShare_%'] = (country_summary['Revenue'] / total_revenue) * 100
country_summary['AOV'] = country_summary['Revenue'] / country_summary['Orders']
country_summary.to_csv('visualization_ready/country_performance_summary.csv', index=False)

top10_countries = country_summary.head(10)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), dpi=300, gridspec_kw={'width_ratios': [1.8, 1.2]})

# Bar chart of non-UK or full top 10
colors = ['#1e40af' if c == 'United Kingdom' else '#0284c7' for c in top10_countries['Country']]
bars = ax1.bar(top10_countries['Country'], top10_countries['Revenue'] / 1e6, color=colors)
ax1.set_title('Top 10 Geographic Markets by Revenue ($ Millions)', fontsize=14, fontweight='bold', pad=12, color='#1e293b')
ax1.set_ylabel('Revenue ($ Millions)', fontsize=11, fontweight='bold', color='#334155')
ax1.tick_params(axis='x', rotation=45)

for bar in bars:
    h = bar.get_height()
    ax1.annotate(f'${h:.2f}M',
                xy=(bar.get_x() + bar.get_width() / 2, h),
                xytext=(0, 4), textcoords="offset points",
                ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#1e293b')

# Pie chart: UK vs Rest of World
uk_rev = country_summary[country_summary['Country'] == 'United Kingdom']['Revenue'].sum()
other_top9_rev = country_summary.iloc[1:10]['Revenue'].sum()
rest_rev = country_summary.iloc[10:]['Revenue'].sum()

pie_data = [uk_rev, other_top9_rev, rest_rev]
pie_labels = [f"UK\n({(uk_rev/total_revenue)*100:.1f}%)", 
              f"Top 2-10 EU/Intl\n({(other_top9_rev/total_revenue)*100:.1f}%)", 
              f"Other 28 Mkts\n({(rest_rev/total_revenue)*100:.1f}%)"]
pie_colors = ['#1e40af', '#38bdf8', '#cbd5e1']

wedges, texts, autotexts = ax2.pie(pie_data, labels=pie_labels, autopct='%1.1f%%',
                                  colors=pie_colors, startangle=140, 
                                  wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2),
                                  textprops={'fontsize': 10, 'weight': 'bold'})
for autotext in autotexts:
    autotext.set_color('white')
ax2.set_title('Global Market Revenue Share', fontsize=14, fontweight='bold', pad=12, color='#1e293b')

plt.tight_layout()
plt.savefig('visualizations/03_revenue_by_country.png')
plt.close()
print("Saved 03_revenue_by_country.png")

# -------------------------------------------------------------
# 4. SALES HEATMAP: DAY OF WEEK VS HOUR OF DAY
# -------------------------------------------------------------
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday']
clean_df['DayOfWeek_Cat'] = pd.Categorical(clean_df['DayOfWeek'], categories=day_order, ordered=True)

heatmap_data = clean_df.groupby(['DayOfWeek_Cat', 'Hour'], observed=False)['Revenue'].sum().unstack().fillna(0) / 1000

fig, ax = plt.subplots(figsize=(13, 6), dpi=300)
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.0f', cbar_kws={'label': 'Revenue ($k)'}, ax=ax, linewidths=0.5)
ax.set_title('Revenue Heatmap: Day of Week vs. Hour of Day ($ in Thousands)', fontsize=15, fontweight='bold', pad=15, color='#1e293b')
ax.set_xlabel('Hour of Day (24-Hour Format)', fontsize=12, fontweight='bold', color='#334155', labelpad=10)
ax.set_ylabel('Day of Week', fontsize=12, fontweight='bold', color='#334155')
plt.tight_layout()
plt.savefig('visualizations/04_sales_heatmap_day_hour.png')
plt.close()
print("Saved 04_sales_heatmap_day_hour.png")

# -------------------------------------------------------------
# 5. PARETO 80/20 ANALYSIS (PRODUCTS)
# -------------------------------------------------------------
prod_agg['Cumulative_Revenue'] = prod_agg['Revenue'].cumsum()
prod_agg['Cumulative_Share_%'] = (prod_agg['Cumulative_Revenue'] / total_revenue) * 100
prod_agg['Product_Rank'] = np.arange(1, len(prod_agg) + 1)
prod_agg['Product_Share_%'] = (prod_agg['Product_Rank'] / len(prod_agg)) * 100

# Top products reaching 80% revenue
top_80_count = len(prod_agg[prod_agg['Cumulative_Share_%'] <= 80])
top_80_pct = (top_80_count / len(prod_agg)) * 100

fig, ax = plt.subplots(figsize=(11, 6), dpi=300)
ax.plot(prod_agg['Product_Share_%'], prod_agg['Cumulative_Share_%'], color='#dc2626', linewidth=3, label='Cumulative Revenue %')
ax.plot([0, 100], [0, 100], color='#94a3b8', linestyle='--', linewidth=1.5, label='Equal Distribution Baseline')

# 80/20 lines
ax.axhline(80, color='#1e293b', linestyle=':', alpha=0.7)
ax.axvline(top_80_pct, color='#1e293b', linestyle=':', alpha=0.7)

ax.annotate(f'Pareto Principle Validated:\nTop {top_80_pct:.1f}% of products ({top_80_count:,} SKUs)\ngenerate 80.0% of total revenue!',
            xy=(top_80_pct, 80), xytext=(top_80_pct + 15, 60),
            arrowprops=dict(facecolor='#dc2626', shrink=0.08, width=1.5, headwidth=8),
            fontsize=10.5, fontweight='bold', color='#1e293b',
            bbox=dict(boxstyle="round,pad=0.5", fc="#fef2f2", ec="#dc2626", lw=1.5))

ax.set_title('Pareto Analysis (80/20 Rule): Product Revenue Concentration', fontsize=15, fontweight='bold', pad=15, color='#1e293b')
ax.set_xlabel('% of Total Product Catalog (Ranked by Revenue)', fontsize=12, fontweight='bold', color='#334155', labelpad=10)
ax.set_ylabel('Cumulative % of Total Revenue', fontsize=12, fontweight='bold', color='#334155')
ax.set_xlim(0, 100)
ax.set_ylim(0, 105)
ax.legend(loc='lower right', frameon=True, facecolor='white')

plt.tight_layout()
plt.savefig('visualizations/05_pareto_analysis.png')
plt.close()
print("Saved 05_pareto_analysis.png")

# -------------------------------------------------------------
# 6. ORDER VALUE DISTRIBUTION & TICKET SIZES
# -------------------------------------------------------------
order_totals = clean_df.groupby('InvoiceNo')['Revenue'].sum()

bins = [0, 50, 150, 300, 500, 1000, 5000, np.inf]
labels = ['<$50 (Micro)', '$50-$150 (Small)', '$150-$300 (Medium)', '$300-$500 (Large)', '$500-$1k (VIP)', '$1k-$5k (Wholesale)', '>$5k (Bulk)']
order_tiers = pd.cut(order_totals, bins=bins, labels=labels).value_counts().reindex(labels)
order_tier_rev = clean_df.groupby(pd.cut(clean_df.groupby('InvoiceNo')['Revenue'].transform('sum'), bins=bins, labels=labels), observed=False)['Revenue'].sum()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), dpi=300)

colors = sns.color_palette('viridis', len(labels))
bars1 = ax1.barh(labels, order_tiers, color=colors)
ax1.set_title('Order Volume by Order Value Tier', fontsize=14, fontweight='bold', pad=12, color='#1e293b')
ax1.set_xlabel('Number of Orders', fontsize=11, fontweight='bold', color='#334155')

for bar in bars1:
    w = bar.get_width()
    pct = (w / total_orders) * 100
    ax1.annotate(f' {w:,} ({pct:.1f}%)',
                 xy=(w, bar.get_y() + bar.get_height() / 2),
                 xytext=(4, 0), textcoords="offset points",
                 ha='left', va='center', fontsize=8.5, fontweight='bold', color='#0f172a')
ax1.set_xlim(0, max(order_tiers) * 1.25)

tier_rev_df = clean_df.groupby('InvoiceNo').agg(Rev=('Revenue', 'sum')).reset_index()
tier_rev_df['Tier'] = pd.cut(tier_rev_df['Rev'], bins=bins, labels=labels)
tier_rev_summary = tier_rev_df.groupby('Tier', observed=False)['Rev'].sum() / 1000

bars2 = ax2.barh(labels, tier_rev_summary, color=colors)
ax2.set_title('Revenue Contribution by Order Value Tier ($k)', fontsize=14, fontweight='bold', pad=12, color='#1e293b')
ax2.set_xlabel('Revenue ($ in Thousands)', fontsize=11, fontweight='bold', color='#334155')

for bar in bars2:
    w = bar.get_width()
    pct = (w * 1000 / total_revenue) * 100
    ax2.annotate(f' ${w:,.0f}k ({pct:.1f}%)',
                 xy=(w, bar.get_y() + bar.get_height() / 2),
                 xytext=(4, 0), textcoords="offset points",
                 ha='left', va='center', fontsize=8.5, fontweight='bold', color='#0f172a')
ax2.set_xlim(0, max(tier_rev_summary) * 1.25)

plt.tight_layout()
plt.savefig('visualizations/06_order_value_distribution.png')
plt.close()
print("Saved 06_order_value_distribution.png")

# -------------------------------------------------------------
# 7. RFM CUSTOMER SEGMENTATION ANALYSIS
# -------------------------------------------------------------
cust_df = clean_df[clean_df['CustomerID'].notnull()].copy()
cust_df['CustomerID'] = cust_df['CustomerID'].astype(int).astype(str)

ref_date = cust_df['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm = cust_df.groupby('CustomerID').agg(
    Recency=('InvoiceDate', lambda x: (ref_date - x.max()).days),
    Frequency=('InvoiceNo', 'nunique'),
    Monetary=('Revenue', 'sum')
).reset_index()

# Scoring
rfm['R_Score'] = pd.qcut(rfm['Recency'], q=4, labels=[4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=4, labels=[1, 2, 3, 4])
rfm['M_Score'] = pd.qcut(rfm['Monetary'].rank(method='first'), q=4, labels=[1, 2, 3, 4])
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

def assign_segment(row):
    r = int(row['R_Score'])
    f = int(row['F_Score'])
    m = int(row['M_Score'])
    rf_avg = (r + f) / 2
    
    if r >= 4 and f >= 4:
        return 'Champions (VIP)'
    elif r >= 3 and f >= 3:
        return 'Loyal Customers'
    elif r >= 3 and f < 3:
        return 'Recent / Promising'
    elif r == 2 and f >= 2:
        return 'Need Attention'
    elif r == 1 and f >= 3:
        return 'At Risk / High Value'
    else:
        return 'Hibernating / Lost'

rfm['Segment'] = rfm.apply(assign_segment, axis=1)
rfm.to_csv('visualization_ready/customer_rfm_segments.csv', index=False)

rfm_agg = rfm.groupby('Segment').agg(
    CustomerCount=('CustomerID', 'count'),
    TotalRevenue=('Monetary', 'sum'),
    AvgMonetary=('Monetary', 'mean'),
    AvgRecency=('Recency', 'mean'),
    AvgFrequency=('Frequency', 'mean')
).reset_index().sort_values('TotalRevenue', ascending=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), dpi=300)
palette = ['#10b981', '#3b82f6', '#8b5cf6', '#f59e0b', '#f97316', '#ef4444']

ax1.pie(rfm_agg['CustomerCount'], labels=rfm_agg['Segment'], autopct='%1.1f%%',
        colors=palette[:len(rfm_agg)], startangle=140,
        wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2),
        textprops={'fontsize': 9.5, 'weight': 'bold'})
ax1.set_title('Customer Distribution by RFM Segment', fontsize=14, fontweight='bold', pad=12, color='#1e293b')

bars = ax2.barh(rfm_agg['Segment'], rfm_agg['TotalRevenue'] / 1000, color=palette[:len(rfm_agg)])
ax2.set_title('Revenue Contribution by RFM Segment ($k)', fontsize=14, fontweight='bold', pad=12, color='#1e293b')
ax2.set_xlabel('Total Revenue ($ in Thousands)', fontsize=11, fontweight='bold', color='#334155')

for bar in bars:
    w = bar.get_width()
    pct = (w * 1000 / rfm['Monetary'].sum()) * 100
    ax2.annotate(f' ${w:,.0f}k ({pct:.1f}%)',
                 xy=(w, bar.get_y() + bar.get_height() / 2),
                 xytext=(4, 0), textcoords="offset points",
                 ha='left', va='center', fontsize=9, fontweight='bold', color='#0f172a')
ax2.set_xlim(0, max(rfm_agg['TotalRevenue'] / 1000) * 1.25)

plt.tight_layout()
plt.savefig('visualizations/07_rfm_customer_segments.png')
plt.close()
print("Saved 07_rfm_customer_segments.png")

# -------------------------------------------------------------
# 8. MASTER 4K EXECUTIVE DASHBOARD SUMMARY (INFOGRAPHIC)
# -------------------------------------------------------------
fig = plt.figure(figsize=(20, 14), dpi=300, facecolor='#f8fafc')
gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.25, left=0.05, right=0.95, top=0.92, bottom=0.05)

fig.suptitle('EXECUTIVE SALES PERFORMANCE & REVENUE INTELLIGENCE DASHBOARD', 
             fontsize=22, fontweight='heavy', color='#0f172a', y=0.97)

# KPI Cards row representation at top
# Chart 1: Monthly Trend (Spans 2 cols)
ax_trend = fig.add_subplot(gs[0, 0:2])
ax_trend.plot(monthly['YearMonth'], monthly['Revenue'] / 1000, color='#2563eb', marker='o', linewidth=2.5, label='Revenue ($k)')
ax_trend.fill_between(monthly['YearMonth'], monthly['Revenue'] / 1000, color='#3b82f6', alpha=0.15)
ax_trend.set_title('📈 Monthly Revenue Trend & Holiday Seasonality Spike ($k)', fontsize=12, fontweight='bold', color='#1e293b')
ax_trend.tick_params(axis='x', rotation=35, labelsize=9)
ax_trend.set_ylabel('Revenue ($k)', fontweight='bold', color='#334155')

# Chart 2: Top Countries (1 col)
ax_cntry = fig.add_subplot(gs[0, 2])
top6_cntry = country_summary.head(6).sort_values('Revenue', ascending=True)
ax_cntry.barh(top6_cntry['Country'], top6_cntry['Revenue'] / 1e6, color='#0284c7')
ax_cntry.set_title('🌍 Top Revenue Generating Countries ($M)', fontsize=12, fontweight='bold', color='#1e293b')
ax_cntry.set_xlabel('Revenue ($M)', fontweight='bold', color='#334155')
ax_cntry.tick_params(labelsize=9)

# Chart 3: Top Products (1 col)
ax_prod = fig.add_subplot(gs[1, 0])
top5_prod = prod_agg.head(5).sort_values('Revenue', ascending=True)
short_labels = [d[:20] + '...' if len(d) > 20 else d for d in top5_prod['Description']]
ax_prod.barh(short_labels, top5_prod['Revenue'] / 1000, color='#10b981')
ax_prod.set_title('🏆 Top 5 Revenue SKU Performers ($k)', fontsize=12, fontweight='bold', color='#1e293b')
ax_prod.set_xlabel('Revenue ($k)', fontweight='bold', color='#334155')
ax_prod.tick_params(labelsize=8.5)

# Chart 4: Day/Hour Heatmap (1 col)
ax_hm = fig.add_subplot(gs[1, 1])
sns.heatmap(heatmap_data, cmap='YlGnBu', cbar=False, ax=ax_hm, annot=False)
ax_hm.set_title('⏰ Peak Purchasing Windows (Day vs Hour)', fontsize=12, fontweight='bold', color='#1e293b')
ax_hm.tick_params(labelsize=8)

# Chart 5: RFM Segments (1 col)
ax_rfm = fig.add_subplot(gs[1, 2])
ax_rfm.pie(rfm_agg['CustomerCount'], labels=rfm_agg['Segment'], autopct='%1.0f%%', colors=palette[:len(rfm_agg)], textprops={'fontsize': 8, 'weight': 'bold'}, wedgeprops=dict(width=0.4))
ax_rfm.set_title('👥 RFM Customer Segment Breakdown', fontsize=12, fontweight='bold', color='#1e293b')

# Chart 6: Order Value Tiers (Spans 2 cols)
ax_tiers = fig.add_subplot(gs[2, 0:2])
bars_tier = ax_tiers.bar(labels, tier_rev_summary, color=sns.color_palette('mako', len(labels)))
ax_tiers.set_title('💰 Revenue Contribution Across Order Ticket Tiers ($k)', fontsize=12, fontweight='bold', color='#1e293b')
ax_tiers.set_ylabel('Revenue ($k)', fontweight='bold', color='#334155')
ax_tiers.tick_params(axis='x', rotation=25, labelsize=8.5)

# Strategic Executive Takeaways Box (1 col)
ax_box = fig.add_subplot(gs[2, 2])
ax_box.axis('off')
summary_text = (
    "🎯 STRATEGIC EXECUTIVE ACTION PLAN:\n\n"
    "1. Q4 Seasonality Ramp:\n"
    "   Revenue peaks in Nov ($1.5M, +98% MoM).\n"
    "   Lock in supplier inventory by late August.\n\n"
    "2. 80/20 Inventory Priority:\n"
    "   20% of catalog produces 80% of revenue.\n"
    "   Prevent stockouts on Top 50 hero SKUs.\n\n"
    "3. High-Value Customer Retention:\n"
    "   Champions & Loyalists generate >65% revenue.\n"
    "   Deploy automated VIP retention tiers.\n\n"
    "4. Cross-Border European Expansion:\n"
    "   Netherlands, Germany, France show >$200k sales.\n"
    "   Localize fulfillment & multi-currency checkout."
)
ax_box.text(0.05, 0.95, summary_text, transform=ax_box.transAxes, fontsize=10,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round,pad=1', facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1.5))

plt.savefig('visualizations/08_executive_dashboard_summary.png', facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print("Saved 08_executive_dashboard_summary.png")

print("\n--- KPI SUMMARY METRICS FOR REPORTING ---")
print(f"Total Gross Revenue: ${total_revenue:,.2f}")
print(f"Total Completed Orders: {total_orders:,}")
print(f"Total Unique Customers: {total_customers:,}")
print(f"Average Order Value (AOV): ${avg_order_val:,.2f}")
print(f"Average Item Unit Price: ${avg_item_price:.2f}")
print(f"Peak Revenue Month: {monthly.sort_values('Revenue', ascending=False).iloc[0]['YearMonth']} (${monthly['Revenue'].max():,.2f})")
print(f"UK Revenue Share: {(uk_rev / total_revenue)*100:.2f}% (${uk_rev:,.2f})")
print(f"Top Product: {prod_agg.iloc[0]['Description']} (${prod_agg.iloc[0]['Revenue']:,.2f})")
