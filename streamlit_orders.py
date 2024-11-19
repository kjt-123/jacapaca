import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(worksheet="menu_items")

#title of app
st.title(":taco: :green salad: Welcome to Jacapaca! :clinking beer mugs:")

# Display the data.
#for row in df.itertuples():
#    st.write(f"{row.name} has a :{row.pet}:")
st.dataframe(df)
