import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(worksheet="menu_items")

#title of app
st.title(":taco: Bienvenido a Jacapaca! :beers:")
username = st.text_input("Write your name:")
party_id = st.text_input("Hi " + username + "! Write your party id:")
check_party = st.button('Check party details')

# Display the data.
#for row in df.itertuples():
#    st.write(f"{row.name} has a :{row.pet}:")
st.dataframe(df)
