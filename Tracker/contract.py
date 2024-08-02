import streamlit as st 
from utils.data import *

st.set_page_config(layout='wide')

# Load css from assets directory

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()},</style>',unsafe_allow_html=True)

# Load css
load_css('assests/style.css')
# Get Data
df = load_data()

st.markdown('<div class="custom-title"> Contract Tracker Dashboard </div>',unsafe_allow_html=True)

st.markdown('Coming soon..................................')