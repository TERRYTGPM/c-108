import random
import plotly.express as px
import plotly.figure_factory as ff

e = []
count = []

for i in range(0, 100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    e.append(dice1+dice2)
    count.append(i)

fog = ff.create_distplot([e], ["L"], show_hist=False)
fog.show()