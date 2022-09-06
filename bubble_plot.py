# %%
from turtle import color
import altair as alt
from time import time, sleep

# %%
import pandas as pd
df = pd.read_csv('data/processed.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'])
# %%
def plot_bubble():
    domain = ['view_count', 'comment_count', 'like_count']
    # range_= ['lightskyblue', 'red', 'grey']
    plot = alt.Chart(df).mark_circle().encode(
        alt.Y('value:Q', scale=alt.Scale(type="log")),
        alt.X('yearmonth(publish_time):O'),
        size='duration(s):Q',
        opacity='duration(s):Q',
        color=alt.Color('variable', scale=alt.Scale(domain=domain))
    )
    return plot

plot_bubble()
# %%
import pandas as pd
df = pd.read_csv('data/all_videos_daoyueshe.csv')

df[['minutes']] = df['duration'].str.extract(r'PT(\d+)M', expand=True).astype('int')
df[['seconds']] = df['duration'].str.extract(r'M(\d+)S', expand=True).fillna(0).astype('int')
df['duration(s)'] = 60*df['minutes'] + df['seconds']
df

alt.Chart(df).transform_timeunit(
    Year='year(publish_time)',
    Month = 'month(publish_time)'
).mark_circle().encode(
    alt.X('view_count:Q'),
    alt.Y('like_count:Q'),
    size='duration(s):Q',
    color='duration(s)'
)
# %%
alt.Chart(df).transform_timeunit(
    Year='year(publish_time)',
    Month = 'month(publish_time)'
).mark_circle().encode(
    alt.X('like_count:Q'),
    alt.Y('comment_count:Q'),
    size='duration(s):Q',
    color='duration(s)'
)
# %%
alt.Chart(df).transform_timeunit(
    Year='year(publish_time)',
    Month = 'month(publish_time)'
).mark_circle().encode(
    alt.X('view_count:Q'),
    alt.Y('comment_count:Q'),
    size='duration(s):Q',
    color='duration(s)'
)
# %%
