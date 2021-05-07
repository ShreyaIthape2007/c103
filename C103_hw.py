import pandas as pd
import plotly_express as px
import csv

file=pd.read_csv('coviddata.csv')

graph = px.scatter(file,x='date',y='cases',color='country')

graph.show()