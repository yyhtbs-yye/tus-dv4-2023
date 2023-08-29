import plotly.express as px
import plotly.io as pio

out_folder_path = "plotly_charts_json/"
out_file_name = "line_chart_simple.json.json"

fig = px.line(x=["a","b","c"], y=[1,3,2], title="y=f(x)")

graphJSON = pio.to_json(fig)

with open(out_folder_path+out_file_name, "w") as fp:
    fp.write(graphJSON)
