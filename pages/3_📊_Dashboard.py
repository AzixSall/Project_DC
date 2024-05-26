import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def dashboard():
    st.title("Dashboard")

    data_voitures = pd.read_csv('Expat_voitures_clean.csv')
    data_motos = pd.read_csv('Expat_moto_clean.csv')
    data_equipements = pd.read_csv('Expat_equipments_clean.csv')

    tabVoiture, tabMoto, tabEquipements = st.tabs(["Dashboard Voitures Expat", "Dashboard Motos Expat", "Dashboard Equipements Expat"])

    with tabVoiture :
        fig, ax = plt.subplots()
        sns.barplot(x='année', y='prix(FCFA)', data=data_voitures, ax=ax)
        st.pyplot(fig)
    
    with tabMoto:
        st.dataframe(data_motos)

    with tabEquipements:
        st.dataframe(data_equipements)

st.set_page_config(page_title="Dashboard", page_icon="📊")
st.markdown("# Dashboard")
st.sidebar.header("Dashboard")

st.write(
    """Cette page montre different diagrammes basees sur les donnees scrapees et nettoyees avec Web Scraper"""
)

dashboard()