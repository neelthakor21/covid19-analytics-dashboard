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

df_melt = df_c.iloc[2:, :]

df_melt = df_c.melt(
    id_vars=['Attributes'],
    var_name='Country',
    value_name='Cases'
)

sr_d = df_d.iloc[2:, :].melt(
    id_vars=['Attributes'],
    var_name='Country',
    value_name='Deaths'
).iloc[:, -1]

df_melt['Deaths'] = sr_d

# df_plot = df_melt[df_melt['Country'] == country]

# Plotting the line chart

fig = px.line(
    df_melt[df_melt['Country'] == country],
    x='Attributes',
    y=['Cases', 'Deaths'],
    title=f"COVID-19 Trend in {country}",
    labels={
        "Attributes": "Date",
        "value": "Count",
        "variable": "Metric"
    }
)

st.plotly_chart(fig, width='stretch')