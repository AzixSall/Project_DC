import streamlit as st
import pandas as pd
from requests import get
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scraping(selected_value, selected_category):
    data_list = []

    for p in range(1, selected_value + 1):
        url = f'https://www.expat-dakar.com/{selected_category}?page={p}'
        driver = webdriver.Firefox()
        driver.get(url)

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "listings"))
            )
        except Exception as e:
            print(f"An error occurred: {e}")

        soup = bs(driver.page_source, 'html.parser')
        driver.quit()

        containers = soup.find_all('div', class_ = 'listings-cards__list-item')
        if selected_category == 'voitures':
            for container in containers:
                try:
                    infoGen = container.find('div', class_ = 'listing-card__header__tags').findAll('span')
                    carState = infoGen[0].text
                    marque = infoGen[1].text
                    anne = infoGen[2].text
                    boitVit = infoGen[3].text
                    adresseVente = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                    prix = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                    image_link = container.find('img', 'listing-card__image__resource vh-img')['src']

                    obj = {
                        'etat_car' : carState,
                        'marque': marque,
                        'annee' : int(anne),
                        'boite_vit' : boitVit,
                        'adresse_vente' : adresseVente,
                        'prix' : int(prix),
                        'image_link' : image_link
                    }

                    data_list.append(obj)
                except:
                    pass
        elif selected_category == 'motos-scooters':
            for container in containers:
                try:
                    infoGen = container.find('div', class_ = 'listing-card__header__tags').findAll('span')
                    etat = infoGen[0].text
                    marque = infoGen[1].text
                    annee = infoGen[2].text
                    adresseVente = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                    prix = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                    image_link = container.find('img', 'listing-card__image__resource vh-img')['src']

                    obj = {
                        'etat_moto' : etat,
                        'marque': marque,
                        'annee' : int(annee),
                        'adresse_vente' : adresseVente,
                        'prix' : int(prix),
                        'image_link' : image_link
                    }

                    data_list.append(obj)
                except:
                    pass
                       
        else:
            for container in containers:
                try:
                    details = container.find('div', class_ = 'listing-card__header__title').text.strip('[\n')
                    etat = container.find('div', class_ = 'listing-card__header__tags').find('span').text
                    adresseVente = container.find('div', class_ = 'listing-card__header__location').text.replace('\n', '')
                    prix = container.find('span', class_ = 'listing-card__price__value 1').text.replace('\n', '').replace('\u202f', '').replace(' F Cfa', '')
                    image_link = container.find('img', 'listing-card__image__resource vh-img')['src']

                    obj = {
                        'details': details,
                        'etat' : etat,
                        'adresse_vente' : adresseVente,
                        'prix' : int(prix),
                        'image_link' : image_link
                    }

                    data_list.append(obj)
                except:
                    pass

    df = pd.DataFrame(data_list)
    st.dataframe(df)

st.set_page_config(page_title="Scrapper a partir de Expat Dakar", page_icon="🌍")
st.markdown("# Scrapper des donnees a partir de Expat")
st.sidebar.header("Scrapper des donnees a partir de Expat")

st.write(
    """Cette page nous permet de selectionner un nombre de page et de scrapper des donnees sur Expat Dakar avec le nombre de page et la categorie choisie"""
)

selected_value = st.selectbox("Selectionner le nombre de page a scraper sur Expat", list(range(1, 11)))
selected_category = st.radio('Choississez une categorie:', ['voitures','motos-scooters','equipements-pieces'])
scraping(selected_value, selected_category)