## Import the Libraries
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go


apple=yf.Ticker("AAPL")
apple=apple.history(period="5y")
apple['weekday'] = apple.index.weekday
apple['month_year'] = apple.index.to_period('M')
friday_groupy = apple[apple['weekday'] == 4].groupby(['month_year'])
apple = apple.reset_index()

fig = go.Figure(data=[go.Candlestick(x=apple['Date'],
                open=apple['Open'],
                high=apple['High'],
                low=apple['Low'],
                close=apple['Close'])])
fig.update_layout(xaxis_rangeslider_visible=False)

app = dash.Dash(__name__)

## DIV é um elemento de divisão, um container genérico para contéudo de fluxo, que de certa forma não representa nada. 
## Organizar o conteúdo de forma melhor

app.layout = html.Div([
    html.Label("Dropdown"),
     dcc.Dropdown(
        id='dp-1',
        options=[
            {'label':'Rio Grande do Sul', 'value':'RS'},
            {'label':'São Paulo', 'value':'SP'},
            {'label':'Minas Gerais', 'value':'MG'}],
            value='RS', style={'margin-bottom':'25px'}
    ),
    html.Label("Checklist"),
    dcc.Checklist(
        id='cl-1',
        options=[
            {'label':'Rio Grande do Sul', 'value':'RS'},
            {'label':'São Paulo', 'value':'SP'},
            {'label':'Minas Gerais', 'value':'MG'}],
            value=['RS'], style={'margin-bottom':'25px'}
    ),
    html.Label("Text Input"),
    dcc.Input(value='SP', type='text')
])


if __name__ == '__main__':
    app.run_server(debug=True)