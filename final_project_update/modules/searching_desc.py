import streamlit as st
from PIL import Image

def app():
    st.header('선수 검색 설명')
    st.write("K리그 데이터 포털의 선수 검색 페이지에서 영감을 얻어 비슷하게 적용했다.")
    st.write("선수 검색을 하면, 선수의 이미지와 포지션, 역할, 상세역할과 2022년의 히트맵을 먼저 상단에 띄워놓았다.")
    st.write("그 밑은 Radar Chart를 이용해 슈팅 능력, 드리블 능력, 롱패스 능력, 숏패스 능력, 태클 능력, 몸싸움 능력을 시각화 하였고,")
    st.write("오른쪽은 선수의 세부적인 2022년 기록을 수평막대그래프로 시각화하였다.")
