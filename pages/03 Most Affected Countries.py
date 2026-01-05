import streamlit as st
import plotly.express as px
from utils.load_data import load_data

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

# Plotting the data of 10 worst affected countries
fig = px.bar(
    df_con,
    x='Country',
    y=['Cases', 'Deaths'],
    barmode='group',
    labels={
        'Attributes': 'Country',
        'value': 'Count',
        'variable': 'Matric'
        },
    title='Most affected countries: Date vs Cases and Deaths'
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