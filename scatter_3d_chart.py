import plotly.express as px
import pandas as pd
import plotly.io as pio

dtypes={'Grams': float, 'Calories': float, 'Protein': float, 'Fat': float,'Sat.Fat': float, 'Fiber': float, 'Carbs': float}

df = pd.read_csv("kaggle_niharika41298_nutritional_facts_for_most_common_foods.csv")

def str_to_num(input):
    
    if not isinstance(input, str):
        return input
    
    input_clean = input.replace(',', '').replace('t', '').replace('a', '').replace("'", "")
    
    if len(input_clean) == 0:
        return None
    
    return eval(input_clean)

for attr in dtypes:
    df[attr] = df[attr].apply(str_to_num)

fig = px.scatter_3d(df, x="Carbs", y="Protein", z="Calories", color="Category",
                               width=800, height=600)
fig.update_traces(marker=dict(size=3))
# fig.update_layout(legend=dict(x=1, y=1, xanchor='right', yanchor='top'))

fig.show()

graphJSON = pio.to_json(fig)

out_folder_path = "plotly_charts_json/"
out_file_name = "scatter_3d_chart_food_cal.json"

with open(out_folder_path+out_file_name, "w") as fp:
    fp.write(graphJSON)
