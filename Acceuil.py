import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Acceuil",
        page_icon="👋",
    )

    st.write("# Bienvenue sur notre démo! 👋")

    st.sidebar.success("Selectionnez une page sur le menu.")

    st.markdown(
        """
        Ceci est notre soumission pour le projet de Data Collecion.
        **👈 Selectionnez une page sur le menu** pour pouvoir interagir!
        ### Participants?
        - Abdou Aziz Sall
        - Papa Ndongo Ndong
        - Castelnau Godefroy Ondongo
    """
    )


if __name__ == "__main__":
    run()