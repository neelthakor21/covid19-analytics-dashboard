import streamlit as st
import plotly.express as px
from utils.load_data import load_data
from utils.css import apply_css
import plotly.graph_objects as go

st.set_page_config(page_title="Covid-19 Country Specific Trends", layout="wide")

# Loading the data
df_c, df_d = load_data()

# Country Specific KPIs

# list of all the countries
countries = df_c.columns[1:].to_list()

# Country picker for selecting the country
st.title('Country Specific Trends', width='stretch')
st.markdown("---")
country = st.selectbox("Choose the Country:", countries, index=countries.index('India'))

# Data for the KPI
total_cases = df_c.loc[:, country].iloc[-1].astype(int)
total_deaths = df_d.loc[:, country].iloc[-1].astype(int)

st.subheader(f"Total Cases and Total Deaths of {country}")

# Showing the KPI
apply_css(total_cases, total_deaths)

st.markdown('---')

# Melting the dataframe for the ploty chart

df_melt = load_data(melted=True)

df_melt_c = df_melt[df_melt['Country'] == country]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df_melt_c['Attributes'],
        y=df_melt_c["Cases"],
        name="Cases",
        yaxis="y1",
        line=dict(color="blue", width=3)
    )
)

fig.add_trace(
    go.Scatter(
        x=df_melt_c['Attributes'],
        y=df_melt_c["Deaths"],
        name="Deaths",
        yaxis="y2",
        line=dict(color="red", width=3)
    )
)

fig.update_layout(
    title=f"COVID-19 Cases vs Deaths for {country}",
    xaxis_title="Date",

    yaxis=dict(
        title="Cases"
    ),
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

st.plotly_chart(fig, width='stretch')