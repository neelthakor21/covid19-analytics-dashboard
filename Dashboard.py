import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date
from utils.Country import country_to_iso3
from utils.load_data import load_data
from utils.css import apply_css

st.set_page_config(page_title="Covid-19 Data Dashboard.", layout="wide")

# Loading the cached data
df_c, df_d = load_data()

st.title('Global Covid-19 Cases and Deaths Overview.')
st.markdown('---')

# Making dataframe suitable for choropleth, because choropleth works best with the column values

columns_d = df_d.columns[1:].to_list()
iso_codes_d = [country_to_iso3(c) for c in columns_d]
iso_codes_d.insert(0, 'Attributes')
                       
df_map = df_d
df_map.columns = iso_codes_d

# 1. Melt the dataframe
df_map = df_map.iloc[2:, :].melt(
    id_vars=['Attributes'],
    var_name='Country',
    value_name='Deaths'
)

# Min and Max date for the date input
min_date = date(2020, 1, 22)
max_date = date(2023, 3, 9)

# Date inpute with available range for showing data for each date. 
date = st.date_input(
    'Enter the Date: ',
    value=max_date,
    max_value=max_date,
    min_value=min_date
)

idx_c= df_c.index[df_c['Attributes'] == date.strftime('%d-%m-%Y')]
idx_d= df_d.index[df_d['Attributes'] == date.strftime('%d-%m-%Y')]

# Total Cases and Total Deaths for KPI.

total_cases = df_c.iloc[idx_c, 1:].sum(axis=1).astype("Int64").iloc[0]
total_deaths = df_d.iloc[idx_d, 1:].sum(axis=1).astype("Int64").iloc[0]

# importing the style for KPI box.
apply_css(total_cases, total_deaths)
st.markdown('---')

st.subheader(f'Covid-19 Deaths data on {date.strftime('%d-%m-%Y')}')

# Plotting the Choropleth for total Deaths per country on perticular date.
fig = px.choropleth(
    df_map[df_map['Attributes'] == date.strftime('%d-%m-%Y')],
    locations='Country',
    locationmode='ISO-3',
    color='Deaths',
    color_continuous_scale='OrRd'
)

fig.update_geos(
    showcountries=True,
    showcoastlines=False,
    showframe=False
)

fig.update_traces(
    hovertemplate="<b>%{location}</b><br>" +
    "Deaths: <b>%{z}</b>"
)

fig.update_layout(
    height=650,
    width=1000
)

st.plotly_chart(fig, width='stretch')

## -------------------------------------------------------------------------------

st.markdown('''---''')

st.subheader(f'Covid-19 Active Cases data on {date.strftime('%d-%m-%Y')}')

# df_map = df_c.reset_index().rename(columns={'index':'Date'})
columns_c = df_c.columns[1:].to_list()
iso_codes_c = [country_to_iso3(c) for c in columns_c]
iso_codes_c.insert(0, 'Attributes')

df_map = df_c
df_map.columns = iso_codes_c

df_map = df_c.iloc[2:, :].melt(
    id_vars=['Attributes'],
    var_name='Country',
    value_name='Cases'
)

fig = px.choropleth(
    df_map[df_map['Attributes'] == date.strftime('%d-%m-%Y')],
    locations='Country',
    locationmode='ISO-3',
    color='Cases',
    color_continuous_scale='OrRd'
)

fig.update_geos(
    showcountries=True,
    showcoastlines=False,
    showframe=False
)

fig.update_traces(
    hovertemplate="<b>%{location}</b><br>" +
    "Cases: <b>%{z}</b>"
)

fig.update_layout(
    height=650,
    width=1000
)

st.plotly_chart(fig, width='stretch')