# %%
from turtle import color
import altair as alt
from time import time, sleep

# %%
import pandas as pd
df = pd.read_csv('data/processed.csv')

# %%
alt.Chart(df).mark_circle().encode(
    alt.Y('value:Q', scale=alt.Scale(type="log")),
    alt.X('yearmonth(publish_time):O'),
    size='duration(s):Q',
    opacity='duration(s):Q',
    color='variable'
)


