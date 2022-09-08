# %%
import altair as alt
from vega_datasets import data
import pandas as pd
df = pd.read_csv('data/processed.csv')

# %%

def plot_violin():
    plot = alt.Chart(df).transform_density(
        'view_count',
        as_=['view_count', 'density'],
        extent=[5, 300000],
        groupby=['location_or_not']
    ).mark_area(orient='horizontal').encode(
        y='view_count:Q',
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
        width=100
    ).configure_facet(
        spacing=0
    ).configure_view(
        stroke=None
    )

    return plot

plot_violin()

# %%
