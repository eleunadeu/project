import streamlit as st
from multipage import MultiPage
from modules import position, role

app = MultiPage()

st.title("역할 분류")

app.add_page("Position Confirmation", position.app)
app.add_page("Role confirmation", role.app)

app.run()