import streamlit as st

# Custom imports 
from multipage import MultiPage
from modules import mainmain, role_desc, chatbot_desc, clustering_desc, image_clf_desc, role_clf_desc, searching_desc

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("축구 역할 분류 시스템")

# Add all your applications (pages) here
app.add_page('Main', mainmain.app)
app.add_page('Role Description', role_desc.app)
app.add_page('Chatbot Description', chatbot_desc.app)
app.add_page('Clustering Description', clustering_desc.app)
app.add_page('Image Classification Description', image_clf_desc.app)
app.add_page('Role Classification Description', role_clf_desc.app)
app.add_page('Player Searching Description', searching_desc.app)

# The main app
app.run()