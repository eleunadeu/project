import streamlit as st
from utils import EDA2_util as E2u

def app():
    st.title("EDA 2: Open Critic 관련 데이터 분석")

    #st.header("Open Critic 게임 타이틀 검색 기능")
    #E2u.search_game_title()

    st.header("Open Critic 통계 자료")
    E2u.show_data_frame()

    st.header("Open Critic 그래프")
    E2u.chart_graph()