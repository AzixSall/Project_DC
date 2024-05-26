import streamlit as st
import streamlit.components.v1 as components

def iframe_component(url):
    components.iframe(url, height=600, scrolling=True)

def reviewPage():
    st.title("Notez notre application")
    iframe_component('https://ee.kobotoolbox.org/i/ZUfuy8R1')

st.set_page_config(page_title="Noter notre application", page_icon="📈")
st.markdown("# Note application")
st.sidebar.header("Note Application")

st.write(
    """Cette page montre un formulaire fait avec Kobotool, qui permet de laisser une appreciation"""
)
reviewPage()