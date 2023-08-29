import pandas as pd
import plotly.express as px
import plotly.io as pio

# Read the CSV data into a DataFrame
df = pd.read_csv("sales_data_sample.csv", encoding='ISO-8859-1')

# Group by 'MONTH_ID' and sum the sales for each month
monthly_sales = df.groupby(['YEAR_ID', 'MONTH_ID'])['SALES'].sum().reset_index()

monthly_sales['YEAR_MONTH_ID'] = monthly_sales['YEAR_ID'].astype('str') + "-"+ monthly_sales['MONTH_ID'].astype('str')

# Plotting the monthly sales data
fig = px.line(monthly_sales, x='YEAR_MONTH_ID', y='SALES', 
              title="Monthly Sales Data From Jan 2003 To May 2005", 
              width=600, height=300)

graphJSON = pio.to_json(fig)

out_folder_path = "plotly_charts_json/"
out_file_name = "line_chart_monthly_sales.json"

with open(out_folder_path+out_file_name, "w") as fp:
    fp.write(graphJSON)
