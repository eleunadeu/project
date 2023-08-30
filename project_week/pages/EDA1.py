import streamlit as st
from utils import EDA1_util as E1u

def app():

    st.title('EDA 1: 기상관측자료 품질검사 및 표출')

    E1u.data_info()

    E1u.graph_list()