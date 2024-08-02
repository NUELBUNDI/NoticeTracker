import streamlit as st
import pandas as pd
from supabase import create_client
import json

api_key = st.secrets['supabase']['API_KEY']
api_url = st.secrets['supabase']['API_URL']

@st.cache_data
def load_data():
    supabase = create_client(api_url,api_key)
    data = supabase.table('notice').select('*').execute().data
    df = pd.DataFrame(data)
    return df