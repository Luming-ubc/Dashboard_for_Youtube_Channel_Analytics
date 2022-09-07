# %%
from click import style
import pandas as pd
import plotly.express as px
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children=[dcc.Graph()]),

    html.Div(children=[
        html.Div(children=[
            html.Div(children=[dcc.Graph()], style={'flex': 1}),
            html.Div(children=[dcc.Graph()], style={'flex': 1}),
            html.Div(children=[dcc.Graph()], style={'flex': 1}),
            ], style={'display': 'flex', 'flex-direction': 'row'}),
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)
    
