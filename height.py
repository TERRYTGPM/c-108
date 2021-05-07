import csv
import plotly.express
import plotly.figure_factory as ff
import pandas

df = pandas.read_csv("l.csv")

height = df["Height"]

fig = ff.create_distplot([height], ["People"])
fig.show()