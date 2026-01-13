import streamlit as st
import plotly.express as px
from utils.load_data import load_data
import plotly.graph_objects as go

st.set_page_config(page_title="Worst affected countries", layout="wide")

# Loading the data
df_c, df_d = load_data()

# Loading the melted data
df_melted = load_data(melted=True)

# finding the 10 most affected countries by death
countries_series = df_d.iloc[-1, 1:].sort_values(ascending=False).iloc[:10]

df_con = df_melted[
    (df_melted['Country'].isin(countries_series.index)) 
    & 
    (df_melted['Attributes'] == '09-03-2023')
    ].sort_values(ascending=False, by='Deaths')


fig = go.Figure()

# Bars: Cases
fig.add_trace(
    go.Bar(
        x=df_con['Country'],
        y=df_con["Cases"],
        name="Cases",
        marker_color="#a57feb",
        yaxis="y1"
    )
)

# Line: Deaths
fig.add_trace(
    go.Scatter(
        x=df_con['Country'],
        y=df_con["Deaths"],
        name="Deaths",
        mode="lines",
        line=dict(color="#d62728", width=5, dash='dot'),
        yaxis="y2"
    )
)

fig.update_layout(
    title="COVID-19 Cases (Bars) vs Deaths (Line)",
    xaxis_title="Most affected Countries",

    yaxis=dict(title="Cases"),
    yaxis2=dict(
        title="Deaths",
        overlaying="y",
        side="right"
    ),

    template="plotly_white",
    hovermode="x unified",
    legend=dict(
        x=1.05,
        y=1,
        xanchor="left",
        yanchor="top"
    ),
    margin=dict(r=120)
)

st.header('Most Affected Countries in the World by Death')
st.plotly_chart(fig, width='stretch')

st.markdown("---")

# Plotting correlation chart

fig = px.scatter(
    df_melted,
    x="Cases",
    y="Deaths",
    trendline="ols",
    title="Cases vs Deaths Correlation"
)
st.plotly_chart(fig, width='stretch')