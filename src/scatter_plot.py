# %%
import altair as alt

import pandas as pd

df = pd.read_csv('data/processed.csv')
df
# %%
alt.Chart(df).mark_circle(size=60).encode(
    x='duration(s)',
    y='view_count',
    color='location_or_not',
    size = 'view_count',
    tooltip=['video_id', 'duration(s)']
).interactive()
# %%
