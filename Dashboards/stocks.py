## Import the Libraries
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State

input = input('Insira um ticker de uma ação:')

def get_stock_price(ticker, ini_date, final_date):
    ticker=ticker
    df = yf.download(ticker, ini_date, final_date)
    df = df.reset_index()
    return df

df = df = get_stock_price('AMZN', '2000-01-01', '2022-12-31')
external_stylesheets = ['htpps://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    
    html.Div([
        dcc.Dropdown(
            id='axis-column',
            options=[{'label': i, 'value': i} for i in df.drop(columns='Date').columns],
            value='Close'
        )
    ]),
    
    dcc.Graph(id='graphic')
    
])

@app.callback(
    Output('graphic', 'figure'),
    [Input('axis-column', 'value')]
)
def update_graph(axis_column):

    fig = px.line(df, x='Date', y=axis_column)
    
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
    



