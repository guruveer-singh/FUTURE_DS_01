import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, LineChart, DoughnutChart, Reference
import pandas as pd
import win32com.client
import os

monthly_df = pd.read_csv('visualization_ready/monthly_sales_summary.csv')
top_prod_df = pd.read_csv('visualization_ready/top_products_summary.csv')
country_df = pd.read_csv('visualization_ready/country_performance_summary.csv')

wb = openpyxl.Workbook()

# Data sheets
ws_m = wb.active
ws_m.title = 'Data_Monthly'
ws_m.append(['Month', 'Revenue ($k)', 'Orders'])
for _, r in monthly_df.iterrows():
    ws_m.append([r['YearMonth'], round(r['Revenue']/1000, 1), int(r['Orders'])])

ws_p = wb.create_sheet(title='Data_TopProducts')
ws_p.append(['Product', 'Revenue ($k)'])
for _, r in top_prod_df.head(10).iterrows():
    desc = str(r['Description'])
    if len(desc) > 20: desc = desc[:18] + '..'
    ws_p.append([desc, round(r['Revenue']/1000, 1)])

ws_g = wb.create_sheet(title='Data_Geo')
ws_g.append(['Region', 'Revenue ($M)'])
uk_rev = country_df[country_df['Country'] == 'United Kingdom']['Revenue'].sum()
top_eu = country_df.iloc[1:10]['Revenue'].sum()
rest = country_df.iloc[10:]['Revenue'].sum()
ws_g.append(['UK', round(uk_rev/1e6, 2)])
ws_g.append(['Top EU', round(top_eu/1e6, 2)])
ws_g.append(['Rest', round(rest/1e6, 2)])

ws_t = wb.create_sheet(title='Data_Tiers')
ws_t.append(['Tier', 'Revenue ($k)'])
tiers = [('<$50', 184), ('$50-150', 812), ('$150-300', 1420), ('$300-500', 1680), ('$500-1k', 2190), ('$1k-5k', 3140), ('>$5k', 1240)]
for t, rev in tiers:
    ws_t.append([t, rev])

# Dashboard Sheet
ws = wb.create_sheet(title='Dashboard', index=0)
ws.views.sheetView[0].showGridLines = True

# Column sizing
ws.column_dimensions['A'].width = 3
for col in ['B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R']:
    ws.column_dimensions[col].width = 13.5
ws.column_dimensions['J'].width = 7 # Wide gap between left & right panels

# Set specific row heights to guarantee plenty of breathing space
ws.row_dimensions[1].height = 15
ws.row_dimensions[2].height = 28
ws.row_dimensions[3].height = 18
ws.row_dimensions[4].height = 12

for r in range(5, 8):
    ws.row_dimensions[r].height = 22

ws.row_dimensions[8].height = 15
ws.row_dimensions[9].height = 22
ws.row_dimensions[10].height = 10

# Chart rows 11 to 30: 20 rows of height 18 = 360 pt
for r in range(11, 31):
    ws.row_dimensions[r].height = 18

ws.row_dimensions[31].height = 20 # Generous vertical gap
ws.row_dimensions[32].height = 22 # Section header 2
ws.row_dimensions[33].height = 10

for r in range(34, 54):
    ws.row_dimensions[r].height = 18

# Charts: width=14 cm, height=8 cm
c1 = LineChart()
c1.title = 'Monthly Revenue ($k)'
c1.width = 14.5
c1.height = 8.5
c1.add_data(Reference(ws_m, min_col=2, min_row=1, max_row=14), titles_from_data=True)
c1.set_categories(Reference(ws_m, min_col=1, min_row=2, max_row=14))
c1.legend = None
ws.add_chart(c1, 'B11')

c2 = BarChart()
c2.type = 'bar'
c2.title = 'Top 10 Products ($k)'
c2.width = 14.5
c2.height = 8.5
c2.add_data(Reference(ws_p, min_col=2, min_row=1, max_row=11), titles_from_data=True)
c2.set_categories(Reference(ws_p, min_col=1, min_row=2, max_row=11))
c2.legend = None
ws.add_chart(c2, 'K11')

c3 = DoughnutChart()
c3.title = 'Market Share ($M)'
c3.width = 14.5
c3.height = 8.5
c3.add_data(Reference(ws_g, min_col=2, min_row=1, max_row=4), titles_from_data=True)
c3.set_categories(Reference(ws_g, min_col=1, min_row=2, max_row=4))
ws.add_chart(c3, 'B34')

c4 = BarChart()
c4.type = 'col'
c4.title = 'Order Basket Sizes ($k)'
c4.width = 14.5
c4.height = 8.5
c4.add_data(Reference(ws_t, min_col=2, min_row=1, max_row=8), titles_from_data=True)
c4.set_categories(Reference(ws_t, min_col=1, min_row=2, max_row=8))
c4.legend = None
ws.add_chart(c4, 'K34')

test_path = os.path.abspath('test_layout.xlsx')
wb.save(test_path)

# Verify with COM!
excel = win32com.client.Dispatch('Excel.Application')
excel.Visible = False
excel.DisplayAlerts = False
wb_com = excel.Workbooks.Open(test_path)
sheet_com = wb_com.Sheets('Dashboard')

shapes = []
for sh in sheet_com.Shapes:
    shapes.append({
        'name': sh.Name,
        'left': round(sh.Left, 1),
        'top': round(sh.Top, 1),
        'width': round(sh.Width, 1),
        'height': round(sh.Height, 1),
        'right': round(sh.Left + sh.Width, 1),
        'bottom': round(sh.Top + sh.Height, 1)
    })

print(f"Total visual shapes found: {len(shapes)}")
overlaps = []
for i in range(len(shapes)):
    for j in range(i+1, len(shapes)):
        s1 = shapes[i]
        s2 = shapes[j]
        # Check intersection
        x_overlap = not (s1['right'] <= s2['left'] or s2['right'] <= s1['left'])
        y_overlap = not (s1['bottom'] <= s2['top'] or s2['bottom'] <= s1['top'])
        if x_overlap and y_overlap:
            overlaps.append((s1['name'], s2['name']))

print("Overlapping chart pairs:", len(overlaps))
for s in shapes:
    print(f"{s['name']}: Top={s['top']}, Left={s['left']}, Width={s['width']}, Height={s['height']} -> Bottom={s['bottom']}, Right={s['right']}")

wb_com.Close(False)
excel.Quit()
if os.path.exists(test_path): os.remove(test_path)
