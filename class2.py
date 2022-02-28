import csv

with open("class2.csv", newline = '')as f:
    r = csv.reader(f)
    file_data = list(r)
    
file_data.pop(0)

totalMarks = 0
totalEntries = len(file_data)
for i in file_data:
    totalMarks += float(i[1])
    
mean = totalMarks / totalEntries
print(mean)

import plotly_express as px
import pandas as pd


df = pd.read_csv("class2.csv" )
fig = px.scatter( df , x="Student Number" , y = "Marks")

fig.update_layout( shapes = [
     dict(
          type = 'line',
          y0 = mean , y1 = mean,
          x0 = 0 , x1 = totalEntries
     )
])

fig.update_yaxes(rangemode = "tozero")

fig.show()