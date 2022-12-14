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
        html.Button(id='submit-button', n_clicks=0, children='Submit')
    ], style={'width': '48%', 'textAlign': 'left', 'justifyContent':'center'}
    ),
    html.Hr(),
    dcc.Graph(id='graphic-candlestick'),
    dcc.Graph(id='graphic-dividends')
    
])

@app.callback(
    [Output('graphic-candlestick', 'figure'),
    Output('graphic-dividends', 'figure')],
    Input('submit-button', 'n_clicks'),
    State('input-stock', 'value')
)

def update_graph(n_clicks, stock):

    ticker = yf.Ticker(str(stock.upper()))
    df = ticker.history(period='max')
    df = df.reset_index()
    
    df_dividends = ticker.dividends.to_frame().reset_index()
    df_dividends['Date'] = df_dividends['Date'].dt.date
    df_dividends['Date'] = pd.to_datetime(df_dividends['Date'])
    df_dividends['year'] = df_dividends['Date'].dt.year
    
    fig_candlestick = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
            
    fig_candlestick.update_layout(transition_duration=500, xaxis_rangeslider_visible=False)
    
    fig_dividends = px.bar(df_dividends, x='year', y='Dividends')
    
    return fig_candlestick, fig_dividends


if __name__ == '__main__':
    app.run_server(debug=True)
    



