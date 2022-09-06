# %%
import pandas as pd
import altair as alt
df = pd.read_csv('data/all_videos_daoyueshe.csv')

df[['minutes']] = df['duration'].str.extract(r'PT(\d+)M', expand=True).astype('int')
df[['seconds']] = df['duration'].str.extract(r'M(\d+)S', expand=True).fillna(0).astype('int')
df['duration(s)'] = 60 * df['minutes'] + df['seconds']


df['publish_time'] = pd.to_datetime(df['publish_time'])
df = df.melt(id_vars=['video_id', 'publish_time', 'duration(s)'], value_vars=['view_count', 'like_count', 'comment_count'])
df.to_csv('data/processed.csv')

# %%

# %%
