## Import the Libraries
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
external_stylesheets = ['htpps://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df.year.unique()},
        step=None
    )
])

##callback é uma função que é passada como argumento para outra função, espera-se que outra função chame a função callback em sua definição.

@app.callback(
    Output(component_id='graph-with-slider', component_property='figure'),
    [Input(component_id='year-slider', component_property='value')]
)
def update_figure(selected_year):
    filtered_df = df[df.year ==selected_year]
    
    fig = px.scatter(filtered_df, x='gdpPercap', y='lifeExp',
                     size='pop', color='continent', hover_name='country',
                     log_x=True, size_max=55)
    
    fig.update_layout(transition_duration=500)
    
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
