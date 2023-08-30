import streamlit as st
from PIL import Image

def app():
    
    st.header("세부 역할 선호도, 추천 시스템 설명")
    st.subheader("기본 개념")
    st.write("주어진 설문을 바탕으로 사전 정의된 클래스 또는 세부 역할을 추천해 주는 작업")
    st.write("주어진 설문은 사람들의 성향, 선호하는 포지션 등을 기반으로 작성")

    st.subheader("축구에서 세부 역할이란?")
    st.markdown("특정 선수의 포지션과 스텟 데이터를 바탕으로 분류되는 역할로 총 19개의 세부역할이 존재한다.")

    st.subheader("세부 역할 선호도, 추천 시스템 제작 과정")
    st.write("목표 : 주어진 설문을 바탕으로 세부 역할을 추천할 수 있는 모델 제작")
    st.write("모델 제작 : 설문을 통해서 특정 세부 역할을 추천해 주는 시스템 (if, elif 문 사용) 제작")
    st.write("모델 평가: 설문을 통한 세부 역할 추천이 제대로 작동하는지 확인")
    
    

    #st.subheader("세부 역할 선호도, 추천 시스템 Diagram")
    #img = Image.open('DRCS_diagram_1.png')
    #st.image(img, caption='diagram')

if __name__ == "__main__":
    app()