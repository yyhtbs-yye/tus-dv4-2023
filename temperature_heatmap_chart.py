import pandas as pd
import plotly.express as px
import plotly.io as pio

import os

folder_path = './data_temperature'  # Replace with the path to your folder
all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Initialize an empty list to hold dataframes
dfs = []

# Loop through each file, read it into a dataframe, and append to the list
for filename in all_files:
    file_path = os.path.join(folder_path, filename)
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate all dataframes in the list into a single dataframe
final_df = pd.concat(dfs, ignore_index=True)

# Create a pivot table
pivot_df = final_df.pivot_table(index="Country", columns="Year", values="AvgTemperature", aggfunc="mean")

# Plotting the heatmap using Plotly
fig = px.imshow(pivot_df,
                labels=dict(x="Year", y="Country", color="Avg Temperature"),
                title="Average Temperature Heatmap by Country and Year",
                width=700, height=500)
fig.show()

graphJSON = pio.to_json(fig)

out_folder_path = "plotly_charts_json/"
out_file_name = "heatmap_chart_country_temperature.json"

with open(out_folder_path+out_file_name, "w") as fp:
    fp.write(graphJSON)

