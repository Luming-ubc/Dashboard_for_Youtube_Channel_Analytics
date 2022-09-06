# %%
from turtle import color
import altair as alt
from vega_datasets import data

source = data.gapminder_health_income.url

alt.Chart(source).mark_circle().encode(
    alt.X('income:Q', scale=alt.Scale(type='log')),
    alt.Y('health:Q', scale=alt.Scale(zero=False)),
    size='population:Q'
)
# %%
import pandas as pd
df = pd.read_csv('data/all_videos_daoyueshe.csv')

df[['minutes']] = df['duration'].str.extract(r'PT(\d+)M', expand=True).astype('int')
df[['seconds']] = df['duration'].str.extract(r'M(\d+)S', expand=True).fillna(0).astype('int')
df['total_seconds'] = 60*df['minutes'] + df['seconds']
df

# %%
alt.Chart(df).transform_timeunit(
    Year='year(publish_time)',
    Month = 'month(publish_time)'
).mark_circle().encode(
    alt.X('like_count:Q'),
    alt.Y('view_count:Q'),
    size='total_seconds:Q',
    color='total_seconds:Q'
)
# ).facet(
#     row=alt.Column(
#         'Year:T',
#         title=None,
#         header=alt.Header(labelAngle=0, labelAlign='left', format='%Y')
#     )
# )

# %%
