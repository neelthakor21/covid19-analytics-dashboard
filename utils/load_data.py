import streamlit as st
import pandas as pd

@st.cache_resource(show_spinner='Loading Data.....')
def load_data():

    # Loading data into Dataframe
    df_c = pd.read_csv("Data/Covid_19_Cases_Cleaned.csv")
    df_d = pd.read_csv("Data/Covid_19_Deaths_Cleaned.csv")

    # Preprocessing based on the data
    df_c.drop('Unnamed: 0', axis=1, inplace=True)
    df_d.drop('Unnamed: 0', axis=1, inplace=True)

    return df_c, df_d

