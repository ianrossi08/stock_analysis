## Import the Libraries
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import datetime
from datetime import time

external_stylesheets = ['htpps://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Análise de Ações com Python"

app.layout = html.Div([
    
    html.Div([
        html.H2("Análise de Ações com Python"),
        html.Label('Insira o ticker de uma ação: '),
        dcc.Input(
            id='input-stock',
            placeholder='Ex: APPL',
            type='text'),
        html.Button(id='submit-button', children='Submit')
    ], style={'width': '48%', 'textAlign': 'left', 'justifyContent':'center'}
    ),
    
    dcc.Graph(id='graphic')
    
])

@app.callback(
    Output('graphic', 'figure'),
    Input('submit-button', 'n_clicks'),
    State('input-stock', 'value')
)
def update_graph(n_clicks, stock):

    ticker = yf.Ticker(stock)
    df = ticker.history(period='10y')
    df = df.reset_index()
    
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
            
    fig.update_layout(transition_duration=500, xaxis_rangeslider_visible=False)
    
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
    



