from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import seaborn as sns

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


df = sns.load_dataset('tips')

fig = px.bar(df, x="day", y="tip", color="time", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)