import streamlit as st
import plotly.express as px
import pandas as pd
from utils.load_data import load_data
import plotly.graph_objects as go

# Daily Growth Features
# cases_growth_rate = new_cases / total_cases
# deaths_growth_rate = new_deaths / total_deaths

st.set_page_config(page_title="Covid-19 Globle Trends", layout="wide")

# Loading the cached data
df_c, df_d = load_data()

# Plotting the chart of some selected countries with cases and deaths
# countries = ['India', 'Australia', 'China', 'Japan', 'Canada', 'US', 'United Kingdom', 'United Arab Emirates', 'Germany', 'France', 'Russia', 'Singapore', 'New Zealand']

# Making new dataframe for the plotting
df_bc = df_c[['Attributes', 'India', 'Australia', 'China', 'Japan', 'Canada', 'US', 'United Kingdom', 'United Arab Emirates', 'Germany', 'France', 'Russia', 'Singapore', 'New Zealand']]
df_dc = df_d[['Attributes', 'India', 'Australia', 'China', 'Japan', 'Canada', 'US', 'United Kingdom', 'United Arab Emirates', 'Germany', 'France', 'Russia', 'Singapore', 'New Zealand']]

# Deleting latitude and longitude from df_bc and df_dc.
df_bc = df_bc.iloc[2:, :]
df_dc = df_dc.iloc[2:, :]

# Melting to get proper dataframe for plotly
df_bc = df_bc.melt(
    id_vars=['Attributes'],
    var_name='Countries',
    value_name='Cases'
)

sr_d = df_dc.melt(
    id_vars=['Attributes'],
    var_name='Countries',
    value_name='Deaths'
).iloc[:, -1]

df_bc['Deaths'] = sr_d
df_bc_d = df_bc[df_bc['Attributes'] == '09-03-2023']

fig = go.Figure()

# Bars: Cases
fig.add_trace(
    go.Bar(
        x=df_bc_d['Countries'],
        y=df_bc_d["Cases"],
        name="Cases",
        marker_color="#a57feb",
        yaxis="y1"
    )
)

# Line: Deaths
fig.add_trace(
    go.Scatter(
        x=df_bc_d['Countries'],
        y=df_bc_d["Deaths"],
        name="Deaths",
        mode="lines",
        line=dict(color="#d62728", width=5, dash='dot'),
        yaxis="y2"
    )
)

fig.update_layout(
    title="COVID-19 Cases (Bars) vs Deaths (Line)",
    xaxis_title="Date",

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

st.subheader("Analysis of some countrie's cases and deaths count.")
st.plotly_chart(fig, width='stretch')

# Plotting golobal covid-19 deaths treand
st.subheader('Golobal covid-19 deaths treand')

# list of total deaths
total_deaths = []

# looping through the dataframe.
for i in df_d.index[2:]:
    deaths = df_d.iloc[i, 1:].sum().astype(int)
    total_deaths.append(deaths)

# plottig with plotly
fig = px.line(
    x=df_d.iloc[2:, 0],
    y=total_deaths,
    labels={'x': 'Date', 'y': 'Deaths'},
    title='Covid-19 global death trend.'
)

# Displaying via streamlit
st.plotly_chart(fig, width='stretch')

# Calculating the growth rate per date line chart
# Growth rate per date list
cases_growth_rate = []
# total_cases = df_c.iloc[-1, 1:].sum().astype(int)

# Looping through all the dates to find the cases growth rate
for i in df_c.index[3:]:
    curr_cases = df_c.iloc[i, 1:].sum().astype(int)
    last_cases = df_c.iloc[i-1, 1:].sum().astype(int)
    new_cases = curr_cases - last_cases
    case_rate = new_cases/last_cases
    cases_growth_rate.append(case_rate)

# Plotting the global growth rate per date
st.subheader("Global Covid-19 cases growth rate.")

fig = px.line(
    x=df_c.iloc[3:, 0],
    y=cases_growth_rate,
    labels={'x': 'Date', 'y': 'Cases Growth Rate'},
    title='Covid-19 globel cases growth rate daily'
)

fig.update_yaxes(
    tick0=0,
    dtick=0.05
)

st.plotly_chart(fig, width='stretch')
