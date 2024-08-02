import streamlit as st 
from utils.data import *

st.set_page_config(layout='wide')

# Load css from assets directory
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()},</style>',unsafe_allow_html=True)
        
# Load css
load_css('assests/style.css')

# Title
st.markdown('<div class="custom-title"> Group Compliance Dashboard </div>',unsafe_allow_html=True)
st.markdown("##### The summary report details the Notices issued by various Revenue Authorities across various Africa Countries. To generate the report for a specific country,\
    kindly select the country of interest from the dropdown menu on the sidebar slider")

# Get Data
df = load_data()

df['date'] = pd.to_datetime(df['date']).dt.date
# st.data_editor(df)

# Sidebar
with st.sidebar:
    country         = st.sidebar.multiselect("Select a country", options=df['country'].unique().tolist(),default=df['country'].unique().tolist())
    no_of_notices  = st.slider('No of Notices', 0,10,2)
    view_options    = st.sidebar.selectbox("View Options", options=['Container','Expander'],index=1)
    
    
# Select Choosen data

s_data = df[df['country'].isin(country)]
# display_data  = selected_data.head(no_of_notices)

for country_ in sorted(s_data['country'].unique()):
    selected_data = s_data[s_data['country']==country_]
    selected_data.sort_values(by='date',ascending=False)
    
    display_data  = selected_data.head(no_of_notices)
    
    st.markdown(f'<h4 class="country-title"> {country_.capitalize()} Notices </h4>', unsafe_allow_html=True)

    for index , row in display_data.iterrows():
        if view_options == 'Container': 
                    
            with st.container(border=True):
                st.markdown(f'<h1 class="notice-title"> {row["title"].strip().upper()}</h1>', unsafe_allow_html=True)
                st.markdown(f'<p class="notice-date"> Date: {row["date"]}</p>', unsafe_allow_html=True)
                st.markdown(f"<p class= 'summary'> Summary </p>", unsafe_allow_html=True)
                st.markdown(f'<p class="notice-summary">{row["subject"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<a class="notice-url"  href="{row["website_url"]}" target="_blank"> Click here to read full article: </a>', unsafe_allow_html=True)
                
        if view_options == 'Expander':
            with st.expander(f'{row["date"]} : {row["title"].strip().upper()} ',):
                st.markdown(f'<h1 class="notice-title"> {row["title"].strip().upper()}</h1>', unsafe_allow_html=True)
                st.markdown(f'<p class="notice-date"> Date: {row["date"]}</p>', unsafe_allow_html=True)
                st.markdown(f"<p class= 'summary'> Summary </p>", unsafe_allow_html=True)
                st.markdown(f'<p class="notice-summary">{row["subject"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<a class="notice-url"  href="{row["url"]}" target="_blank"> Click here to read the full article: </a>', unsafe_allow_html=True)



# st.dataframe(df)



footer ="""
<div class="footer"><p>Lee Bundi &copy; 2024 . All rights reserved.</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)