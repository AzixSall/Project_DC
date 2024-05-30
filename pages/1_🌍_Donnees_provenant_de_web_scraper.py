import base64
import streamlit as st
import pandas as pd

def webScraperData():
    st.title("Données scrappées avec Web Scraper")

    data_voitures = pd.read_csv('Expat_voitures.csv')
    data_motos = pd.read_csv('Expat_moto.csv')
    data_equipements = pd.read_csv('Expat_equipements_pieces.csv')

    tabVoiture, tabMoto, tabEquipements = st.tabs(["Voitures Expat Dakar", "Motos Expat Dakar", "Equipements Expat Dakar"])
    tabVoiture.write("Voitures Expat Dakar")
    tabMoto.write("Motos Expat Dakar")
    tabEquipements.write("Equipements Expat Dakar")

    with tabVoiture :
        st.dataframe(data_voitures, use_container_width=True)
        if st.button('Telecharger les donnees voitures'):
            # Convert DataFrame to CSV
            csv = data_voitures.to_csv(index=False)

            # Create a text file
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}" download="Expat_voiture.csv">Telecharger en format CSV</a>'

            # Display the link
            st.markdown(href, unsafe_allow_html=True)
    with tabMoto:
        st.dataframe(data_motos)

        if st.button('Telecharger les donnees motos'):
            # Convert DataFrame to CSV
            csv = data_motos.to_csv(index=False)

            # Create a text file
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}" download="Expat_motos.csv">Telecharger en format CSV</a>'

            # Display the link
            st.markdown(href, unsafe_allow_html=True)

    with tabEquipements:
        st.dataframe(data_equipements)

        if st.button('Telecharger les donnees equipements'):
            # Convert DataFrame to CSV
            csv = data_equipements.to_csv(index=False)

            # Create a text file
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            href = f'<a href="data:file/csv;base64,{b64}" download="Expat_equipements.csv">Telecharger en format CSV</a>'

            # Display the link
            st.markdown(href, unsafe_allow_html=True)

st.set_page_config(page_title="Donnees venant de Web Scraper", page_icon="🌍")
st.markdown("# Web Scraper")
st.sidebar.header("Web Scraper")

st.write(
    """Cette page montre differentes donnees non nettoyer scraper avec Web Scraper"""
)

webScraperData()