import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")

AvgRating_list = df["Avg Rating"].tolist()

fig = ff.create_distplot([AvgRating_list], ["Avg Rating"])
fig.show()