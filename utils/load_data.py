import streamlit as st
import pandas as pd

@st.cache_data(show_spinner='Loading Data.....')
def load_data(melted=False):

    # Loading data into Dataframe
    df_c = pd.read_csv("Data/Cleaned Data/Covid_19_Cases_Cleaned.csv")
    df_d = pd.read_csv("Data/Cleaned Data/Covid_19_Deaths_Cleaned.csv")

    # Preprocessing based on the data
    df_c.drop('Unnamed: 0', axis=1, inplace=True)
    df_d.drop('Unnamed: 0', axis=1, inplace=True)

    if melted:
        # Melting the dataframe for the ploty chart

        df_melt = df_c.iloc[2:, :]

        df_melt = df_melt.melt(
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

        return df_melt

    return df_c, df_d