import streamlit as st
from PIL import Image

img1 = Image.open('C:/Users/eleun/Downloads/Multipage.png')
img2 = Image.open('C:/Users/eleun/Downloads/EDA1.png')
img3 = Image.open('C:/Users/eleun/Downloads/EDA2.png')

def show_image():
    name = ['스트림릿 다이어그램', 'EDA 1: 다이어그램', 'EDA 2: 다이어그램']

    choice = st.radio('화면에 나타낼 다이어그램을 고르세요', name)
    if choice == name[0]:
        st.subheader('스트림릿 멀티페이지 구축 다이어그램입니다.')
        st.image(img1)
    elif choice == name[1]:
        st.subheader('기상관측자료 품질 검사 및 표출 페이지 다이어 그램입니다.')
        st.image(img2)
    elif choice == name[2]:
        st.subheader('Open Critic 관련 데이터 분석 페이지 다이어 그램입니다.')
        st.image(img3)