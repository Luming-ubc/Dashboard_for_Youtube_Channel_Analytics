from click import style
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import altair as alt
from dash import Dash, dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
from datetime import date

# df = pd.read_csv('data/processed.csv')


app = Dash(__name__)

tab_style = {'padding': '6px', 'fontWeight': 'bold', 'background': 'rgb(31, 5, 43)', 'color': 'white', 'border': 'none'}
tab_selected_style = {'border': 'none', 'borderBottom': '3px solid #EE334E',  'padding': '7px', 'fontWeight': 'bold', 'color': 'black', 'background': '#FCB131'}


app.layout = html.Div(id = 'main_container', children = [
        
        # header container
        html.Div(id = 'header', children = [

            # title of the dashboard
            html.H1("Youtube Channel Analytics",
                    style = {
                        'color': '#61c2f2', 
                        'text-align': 'left', 
                        'padding': '0px 0px 0px 20px', 
                        'margin-bottom': '-20px',
                        'fontSize': 40,
                    }),

            # description of the dashboard
            html.H4("Insights for your youtube channel performance", 
                    style = {
                        'color': '#b1b9bd', 
                        'text-align': 'left', 
                        'padding': '0px 0px 10px 20px'
                    }),            
            ], 
            # header container style
            style = {
                'margin': '10px',
                'background-color': '#345b6e', 
                'border-radius': '10px',
                'display': 'flex', 
                'justify-content': 'space-around', 
                'flex-direction': 'column'
        }),


        # body container
        html.Div(id = 'body', children = [

            # menu container
            html.Div(id = 'menu', children = [

                # 1. channel id textarea
                html.Div([
                    # subtitle
                    html.H2("Youtube Channel ID", 
                            style = {
                                'flex-grow': '1', 
                                'margin': '0px',
                                'border-bottom': '2px solid #b1b9bd', 
                                'line-height': '1',
                                'textAlign': 'center',
                                'color': '#b1b9bd',
                            }),
                    html.Br(),
                    # text area
                    dcc.Textarea(id='textarea-example',
                                value='Please enter channel ID: ',
                                style={'width': '100%', 
                                        'height': 30,
                                        'background-color': '#345b6e',
                                        'color': '#b1b9bd', 
                                        # 'flex-grow': '1',
                                        },
                                ),
                    # echo
                    html.Div(id='textarea-example-output', children = [
                            'You entered: UvXX123sdgG'
                            ],
                            style={
                                'whiteSpace': 'pre-line',
                                'color': '#b1b9bd',
                                # 'flex-grow': '1',
                            }),
                ],
                style = {
                    'flex-grow' : '1'
                }),




                html.Br(),
                # 2. Year slider
                html.Div([
                    # subtitle
                    html.H2("Year:", 
                            style = {
                                'flex-grow': '1', 
                                'margin': '0px',
                                # 'border-bottom': '2px solid #b1b9bd', 
                                'line-height': '1',
                                'textAlign': 'left',
                                'color': '#b1b9bd',
                            }),
                    html.Br(),
                    # dcc.RangeSlider(
                    #     id = 'year_slider',
                    #     min = 2015, max = 2022,
                    #     marks = {i: {'label': f'{i}', 'style': {'color': '#f5f5f5'}} for i in range(2015, 2022, 1)},
                    #     value = [2015, 2022],
                    #     tooltip={"placement": "right", "always_visible": True}
                    # ),

                    dcc.Dropdown(
                        options=[
                            {"label": "2022", "value": 2022},
                            {"label": "2019", "value": 2019},
                            {"label": "2020", "value": 2020},
                            {"label": "2021", "value": 2021}],
                        value = '2019', 
                        id='year_dropdown'
                        ),

                    html.Div(id='slider-output-container'),

                ],
                style = {
                    'flex-grow' : '1'
                }),





                html.Br(),
                html.Br(),
                # 3. Count Type 
                html.Div([

                    # subtitle
                    html.H2("Analytics Type: ", 
                            style = {
                                'flex-grow': '1', 
                                'margin': '0px',
                                # 'border-bottom': '2px solid #b1b9bd', 
                                'line-height': '1',
                                'textAlign': 'left',
                                'color': '#b1b9bd',
                            }),
                    # which view RadioItems
                    dcc.RadioItems(
                        id='type_selection',
                        options=['views', 'likes', 'comments'],
                        value='views',
                        inline=False,
                    )
                ], 
                style = {
                    'width': '100%', 
                    'flex-grow': '1', 
                    'color': '#f5f5f5',
                    }),






                # 4. helpers
                dbc.Tooltip(
                    "Need help to find the ID, go to www.youtube.com",
                    target="channel_id_help",
                    placement = 'right',
                    className = 'tooltip'
                ),



            ], 
            style = {
                'width': '19%', 
                'margin-top': '0px', 
                'padding': '25px', 
                'background-color': '#305d73', 
                'border-radius': '10px',
                'display': 'flex', 
                'justify-content': 'space-around', 
                'flex-direction': 'column'
            }), 

            # Graph Container Div         
            html.Div(id = 'graphs', children = [
                html.Div(children=[


                    dcc.Graph(
                        id='world_map', 
                        figure={},
                        style = {
                            'height': '50%',
                            
                            },
                    ),

                    dcc.Graph(
                        id='time_series', 
                        style = {'height': '50%'},
                    ),
                    

                    
                ], 
                style={
                    'flex': 3,
                    'justify-content': 'space-around', 
                    'border-radius': '10px',
                    'margin-top': '0px', 
                    'padding': '2px',
                    # 'background-color' : '#6d7778',
                }),



                html.Div(children = [
                    dcc.Graph(
                        id='ranking', 
                        style = {'height': '33%'},
                    ),
                    
                    dcc.Graph(
                        id='location_or_not', 
                        style = {'height': '33%'},
                    ),

                    dcc.Graph(
                        id='duration', 
                        style = {'height': '33%'},
                    ),
                ],
                style={
                    'flex': 2,
                    'justify-content': 'space-around', 
                    'border-radius': '10px',
                    'margin-top': '0px', 
                    'padding': '2px',
                }),





            ], 
            style = {
                'width': '74%', 
                'overflow': 'hidden', 
                'height': '780px', 
                'background-color': '#305d73', 
                'border-radius': '10px', 
                'padding': '1%',
                'display': 'flex', 
                'flex-direction': 'row'
            })


        ], 
        style = {
            'display': 'flex', 
            'justify-content': 'space-around'
        })
], 
style = {
    'display': 'fixed', 
    'height': '100%', 
    'padding': '0px',
})




df = pd.read_csv('data/processed.csv')

# Connect the Plotly graphs with Dash Components
@app.callback(
    [
        Output(component_id='world_map', component_property='figure')
     ],
    [
        Input(component_id='year_dropdown', component_property='value'),
        Input(component_id='type_selection', component_property='value'),
    ]
)
def plot_map(year, types):

    label = types

    if types == 'views':
        types = 'view_count'

    if types == 'likes':
        types = 'like_count'
    
    if types == 'comments':
        types = 'comment_count'


    plot_df = df.copy()
    plot_df = df[(df['year']==year)].dropna()

    fig = px.scatter_mapbox(plot_df, lat="latitude", lon="longitude", color=types, size=types,
                            color_continuous_scale="agsunset",
                            center={"lat": 44.9, "lon": -93.246}, zoom=2.2,
                            mapbox_style="carto-darkmatter", hover_name="video_title")
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        legend_title_text= label
    )

    return [go.Figure(data=fig)]





if __name__ == '__main__':
    app.run_server(debug=True)