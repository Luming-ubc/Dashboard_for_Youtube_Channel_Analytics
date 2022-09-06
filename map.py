# %%
from tkinter import Scale
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

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", color="view_count", size="view_count",
                        color_continuous_scale="agsunset",
                        center={"lat": 52.261, "lon": -123.246}, zoom=3.5,
                        mapbox_style="carto-positron", hover_name="video_title")
fig.update_layout(margin=dict(l=0, r=0, t=30, b=10))
# fig.show()
# %%
