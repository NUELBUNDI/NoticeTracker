
import streamlit as st 

compliance = st.Page('Tracker/compliance.py', title='Compliance ',icon='🏛️')
contract   = st.Page('Tracker/contract.py',   title='Contract '  ,icon='📝')


pg = st.navigation(
                    {"Tracker" :[compliance,contract],}
    )

pg.run()