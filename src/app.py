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
import io

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

                    html.Iframe(
                        id='time_series', 
                        style = {
                            'height': '400px',
                            'width': '850px'
                            },
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
                    html.Iframe(
                        id='ranking', 
                        style = {
                            'height': '200px',
                            'width': '545px'
                            },
                    ),
                    
                    html.Iframe(
                        id='location_or_not', 
                        style = {
                            'height': '200px',
                            'width': '545px'
                            },
                    ),

                    html.Iframe(
                        id='duration', 
                        style = {
                            'height': '400px',
                            'width': '545px'
                            },
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






df = pd.read_csv('data/processed.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'])

@app.callback(
    [
        Output(component_id='time_series', component_property='srcDoc')
     ],
    [
        Input(component_id='year_dropdown', component_property='value'),
        Input(component_id='type_selection', component_property='value'),
    ]
)
def plot_bubble(year, types):

    if types == 'views':
        types = 'view_count'

    if types == 'likes':
        types = 'like_count'
    
    if types == 'comments':
        types = 'comment_count'


    plot_df = df[(df['year']==year)]

    # domain = ['view_count', 'comment_count', 'like_count']
    # range_= ['lightskyblue', 'red', 'grey']
    domain_pd = pd.to_datetime(['2019-01-01', '2022-12-31']).astype(int) / 10 ** 6

    plot = alt.Chart(plot_df).mark_circle().encode(
        alt.Y(types, scale=alt.Scale(type="log")),
        alt.X('yearmonth(publish_time):T', scale=alt.Scale(domain=list(domain_pd))),
        size=types,
        # opacity=types,
        color = types,
        # color=alt.Color('variable', scale=alt.Scale(domain=domain))
    ).properties(
        height = 320,
        width = 650
    )


    return [plot.to_html()]



@app.callback(
    [
        Output(component_id='ranking', component_property='srcDoc')
     ],
    [
        Input(component_id='year_dropdown', component_property='value'),
        Input(component_id='type_selection', component_property='value'),
    ]
)
def plot_ranking(year, types):

    if types == 'views':
        types = 'view_count'

    if types == 'likes':
        types = 'like_count'
    
    if types == 'comments':
        types = 'comment_count'
    
    plot_df = df[df['year']==year].sort_values(by = types).iloc[0:8, ]
    plot = alt.Chart(plot_df).mark_bar().encode(
        x= types,
        y= alt.Y('video_id', sort='-x'),
        tooltip=['video_title', 'description']
    ).properties(
        height = 160,
        width = 390
    )
    return [plot.to_html()]



@app.callback(
    [
        Output(component_id='location_or_not', component_property='srcDoc')
     ],
    [
        Input(component_id='year_dropdown', component_property='value'),
        Input(component_id='type_selection', component_property='value'),
    ]
)
def plot_violin(year, types):
    if types == 'views':
        types = 'view_count'

    if types == 'likes':
        types = 'like_count'
    
    if types == 'comments':
        types = 'comment_count'

    plot_df = df[df['year']==year]

    plot = alt.Chart(plot_df).transform_density(
        types,
        as_=[types, 'density'],
        extent=[5, 300000],
        groupby=['location_or_not']
    ).mark_area(orient='horizontal').encode(
        y=types,
        color='location_or_not:N',
        x=alt.X(
            'density:Q',
            stack='center',
            impute=None,
            title=None,
            axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),
        ),
        column=alt.Column(
            'location_or_not:N',
            header=alt.Header(
                titleOrient='bottom',
                labelOrient='bottom',
                labelPadding=0,
            ),
        )
    ).properties(
        width=160,
        height=160

    ).configure_facet(
        spacing=0
    ).configure_view(
        stroke=None
    )

    return [plot.to_html()]




@app.callback(
    [
        Output(component_id='duration', component_property='srcDoc')
     ],
    [
        Input(component_id='year_dropdown', component_property='value'),
        Input(component_id='type_selection', component_property='value'),
    ]
)
def plot_duration(year, types):

    if types == 'views':
        types = 'view_count'

    if types == 'likes':
        types = 'like_count'
    
    if types == 'comments':
        types = 'comment_count'


    plot_df = df[df['year']==year]

    plot = alt.Chart(plot_df).mark_circle(size=60).encode(
        x='duration(s)',
        y='view_count',
        color='location_or_not',
        size = 'view_count',
        tooltip=['video_id', 'duration(s)']
    ).properties(
        height = 320,
        width = 300
    ).interactive()

    return [plot.to_html()]



if __name__ == '__main__':
    app.run_server(debug=True)