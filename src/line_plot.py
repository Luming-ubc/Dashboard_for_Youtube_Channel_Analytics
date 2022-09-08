# %%
import altair as alt
from vega_datasets import data

# %%
import pandas as pd

df = pd.read_csv('data/all_videos_map.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'])
df = df.melt(id_vars=['video_id', 'publish_time'], value_vars=['view_count', 'like_count', 'comment_count'])
df
# %%
alt.Chart(df).mark_line().encode(
    x= alt.X('yearmonth(publish_time)'),
    y= alt.Y('value', scale=alt.Scale(type="log")),
    color='variable',
    strokeDash='variable',
)

# %%
df

#%%
source.info()
# %%

# %%
# %%

