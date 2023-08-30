import streamlit as st
from PIL import Image

def app():
    image = Image.open('./data/athletic.png')
    st.image(image, caption='출처 : The Athletic')
    st.write("위 사진은 The Athletic에서 2017-18시즌 유럽 5대 리그 선수들의 데이터를 분석해 18가지의 역할을 나눈사진이다.")

    st.subheader("")
    st.write("이번 프로젝트는 2020년, 2021년, 2022년 K리그 선수들의 데이터를 분석해 위와 같이 역할군을 나누었다.")
    st.write("이렇게 나누어진 역할군들을 분류 학습을 통해 축구 역할 분류 모델을 만들었다.")
    st.write("이 모델은 아마추어 선수들이 축구 경기를할 때 자신이 어떤 역할인지 정확하게 알 수 있고,\
             다양한 역할을 수행하면서 자신에게 맞는 역할이 무엇인지 알 수 있다.")
    st.write("또한, 이용자가 축구를 처음 접하게 될때를 대비해 선호 역할 추천 시스템으로 자신이 선호하는 스타일의 축구 역할을 추천받을 수 있다.")
    st.write("마지막으로 역할을 추천받았을 때 그 역할을 수행하는 2022년 기준 K리그 선수들도 추천하고 추천 선수의 세부 스탯도 확인할 수 있다.")