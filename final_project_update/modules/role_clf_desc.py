import streamlit as st
from PIL import Image

def app():
    
    st.header("세부 역할 분류 시스템 (Detailed Role Classification System) 설명")
    st.subheader("기본 개념")
    st.write("주어진 데이터를 바탕으로 사전 정의된 클래스 또는 세부 역할로 분류하는 작업")
    st.write("주어진 데이터는 포지션 + 23개의 60분 단위로 측정된 스텟 데이터")

    st.subheader("축구에서 세부 역할이란?")
    st.markdown("특정 선수의 포지션과 23개의 스텟 데이터를 바탕으로 분류되는 역할로 총 19개의 세부역할이 존재한다.")

    st.subheader("세부 역할 분류 시스템 (Random forest classifier, Gradient Boosting classifier) 제작 과정")
    st.write("목표 : 선수의 세부 역할을 선수의 포지션과 23개의 스텟 데이터를 바탕으로 분류할 수 있는 모델 제작")
    st.write("데이터 : 총 1701개의 선수 데이터에 클래스(라벨: 세부 역할 이름) 부여 후 1191개를 학습 데이터 셋으로 나머지를 테스트 데이터 셋으로 분류")
    st.write("모델 제작 : 머신러닝 모델 구성(Random forest classifier, Gradient Boosting classifier)")
    st.write("모델 학습 : 전처리 된 학습 데이터를 사용하여 예측 및 실제 레이블 간의 오차 최소화 위해 모델 조정(구성 및 하이퍼 파라미터 최적화 작업)")
    st.write("모델 평가 : 테스트(평가) 데이터로 학습된 모델의 정확도를 평가 후 Random forest classifier와 Gradient Boosting classifier 중 최적화 된 모델을 저장")

    st.subheader("세부 역할 분류 과정")
    
    st.write("1. 포지션과 60분간 측정된 스텟 데이터를 바탕으로 세부 역할 예측(predict) 실시")
    st.write("2. 예측 결과 값에 해당하는 세부 역할 이름을 화면에 출력")
    st.write("사용한 모델의 세부 역할 분류 정확도 : FW(84%), MF(88%), DF(93%), GK(100%)")

    st.subheader("세부 역할 분류 시스템 Diagram")
    img = Image.open('./data/DRCS_diagram_3.png')
    st.image(img, caption='diagram')
