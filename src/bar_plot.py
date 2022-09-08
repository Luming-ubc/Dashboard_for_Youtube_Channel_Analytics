# %%
import pandas as pd
import altair as alt

df = pd.read_csv('data/processed.csv')
df

# %%

def plot_ranking(year, types):

    plot_df = df[df['year']==year].sort_values(by = types).iloc[0:10, ]
    plot = alt.Chart(plot_df).mark_bar().encode(
        x= types,
        y= alt.Y('video_id', sort='-x'),
        tooltip=['video_title', 'description']
    )
    return plot

plot_ranking(2019, 'view_count')
# %%
df.sort_values(by = 'view_count').iloc[0:10, ]
# %%
