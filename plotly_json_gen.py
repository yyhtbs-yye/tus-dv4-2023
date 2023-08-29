import plotly.express as px
import plotly.io as pio

out_folder_path = "plotly_charts_json/"
out_file_name = "line_chart_simple_400_400.json"

fig = px.line(x=[1, 2, 3], y=[2, 4, 6], title="y=x", width=400, height=400)

graphJSON = pio.to_json(fig)

with open(out_folder_path+out_file_name, "w") as fp:
    fp.write(graphJSON)
