import streamlit as st
st.header('Case Study V: Glass Classification')

import viz
import about
import modelling

PAGES = {
    "About": about,
    "Prediction": modelling,
    "Visualization": viz
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()


