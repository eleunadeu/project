import streamlit as st
from multipage import MultiPage
from pages import Diagram, EDA1, EDA2

app = MultiPage()

st.title('주간 프로젝트')
st.header('EDA 분석결과 표출')

app.add_page("Project Diagram", Diagram.app)
app.add_page("기상관측자료 품질검사 및 표출", EDA1.app)
app.add_page("Open Critic 관련 데이터 분석", EDA2.app)

app.run()