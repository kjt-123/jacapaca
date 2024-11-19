import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

menu_df = conn.read(worksheet="menu_items").to_pandas()
party_df = conn.read(worksheet="orders", usecols=[0,1]).to_pandas()

#title of app
st.title(":taco: Bienvenido a Jacapaca! :beers:")
username = st.text_input("Write your name:")
party_id = st.text_input("Write your party id:")
party = party_df[party_df['party_id'] == party_id]
st.write('Hi ', username, '. Tonight you are dining with:', party, '. If this is correct hit submit, otherwise please talk to your friends and choose a new party id!')
join_party = st.button('Click to submit')

# Display the data.
#for row in df.itertuples():
#    st.write(f"{row.name} has a :{row.pet}:")
st.dataframe(df)
