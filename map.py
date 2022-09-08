# %%
# from tkinter import Scale
import altair as alt
import pandas as pd

df = pd.read_csv('data/all_videos_map.csv').dropna()
df

# %%
from vega_datasets import data
states = alt.topo_feature(data.us_10m.url, 'states')
world_map = alt.topo_feature(data.world_110m.url, 'countries')


background = alt.Chart(world_map).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project(type='albersUsa')
# project(type='naturalEarth1', scale=500, translate=[140, 610])
# .properties(
#     width=500,
#     height=300
# )

points = alt.Chart(df).mark_circle().encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    size= 'view_count', # alt.value(10),
    tooltip='video_title'
)

background + points


# %%
import plotly.express as px

def plot_map(year, type):

    plot_df = df[(df['year']==year)].dropna()

    fig = px.scatter_mapbox(plot_df, lat="latitude", lon="longitude", color=type, size=type,
                            color_continuous_scale="agsunset",
                            center={"lat": 43.6, "lon": -100.246}, zoom=1.7,
                            mapbox_style="carto-positron", hover_name="video_title")
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=10))

    return fig
# fig.show()
# %%
year = 2019
type = 'view_count'
df = pd.read_csv('data/processed.csv')
df = df[(df['year']==year)].dropna()
df

plot_map(year, type)
# %%
