import csv
import plotly.express
import plotly.figure_factory as ff
import pandas

df = pandas.read_csv("l.csv")

weight = df["Weight"]

fig = ff.create_distplot([weight], ["People"])
fig.show()