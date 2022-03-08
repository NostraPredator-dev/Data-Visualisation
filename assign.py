import pandas as pd
import plotly.express as px

#For PC/VSCode use complete file address for browser use onlt the file name
df = pd.read_csv("E:\Py Projects\C-103\Assignment\Data.csv")
fig = px.scatter(df, x = "date", y = "cases", color = "country", title = "Cases on a day in a Country")

fig.show()