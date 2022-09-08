# %%
from click import style
import pandas as pd
import plotly.express as px
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


app = Dash(__name__)


# define KPIs
total_view_count = str(15)
total_like_count = str(20)
total_comment_count = str(30)

# App layout
app.layout = html.Div([
    html.Div(children=[
        html.H1('Youtube Channel Analytics'),
        dcc.Checklist(
            ['New York City', 'Montréal', 'San Francisco'],
            ['New York City', 'Montréal'],
            inline = False,
        ),

    ]),

    html.Div(children=[
        html.Div(children=[
            html.Div(children=[

                html.Br(),
                html.Label('Total view count:'),
                html.Div(children=[total_view_count]),
                dcc.Textarea(
                    id='text1',
                    value=total_view_count,
                    style={'width': '50%', 'height': 100},
                ),

                html.Br(),
                html.Br(),
                html.Br(),

                # help(dcc.Textarea),

                dcc.Textarea(
                    id='text2',
                    value='Total view count:',
                    style={'width': '50%', 'height': 100},
                ),

                html.Br(),
                dcc.Textarea(
                    id='text3',
                    value='Total view count:',
                    style={'width': '50%', 'height': 100},
                ),

                html.Br(),
                dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown'),

            ], style={'padding': 20, 'flex': 1}),
            
            html.Div(children=[dcc.Graph()], style={'flex': 3}),
            html.Div(children=[dcc.Graph()], style={'flex': 2}),
            ], style={'display': 'flex', 'flex-direction': 'row'}),
    ]),

])

@app.callback(
    [Output(component_id='text1', component_property='value'),
     Output(component_id='text2', component_property='value')],
    # [Input(component_id='slct_year', component_property='value')]
)
def kpi(text1=10, text2=15):
    return text1, text2


if __name__ == '__main__':
    app.run_server(debug=True)
    
