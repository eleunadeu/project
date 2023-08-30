import streamlit as st
from PIL import Image

def app():
    
    st.header("이미지 분류 시스템(Image Classification System) 설명")
    st.subheader("기본 개념")
    st.write("주어진 이미지를 사전 정의된 클래스 또는 카테고리로 분류하는 작업")
    st.write("이미지는 0~255 정수 범위의 값을 가지는 'width x height x 3' 크기의 3차원 배열")

    st.subheader("축구에서 히트맵이란?")
    st.markdown("특정 선수가 경기장 내에서 움직인 위치를 누적시켜 그 분포와 정도를 시각화해서 나타낸 것으로 히트맵을 통해 선수 특징이나 역할(포지션)을 알 수 있음")

    st.subheader("이미지 분류 모델(CNN Model) 제작 과정")
    st.write("목표 : 선수의 포지션을 히트맵 이미지를 통해 분류할 수 있는 모델 제작")
    st.write("데이터 : 총 1701개의 히트맵 이미지에 클래스(라벨: 포지션 이름) 부여 후 1361개를 학습 및 검증 데이터 셋으로 나머지를 테스트 데이터 셋으로 분류")
    st.write("모델 제작 : CNN 모델 구성(Convolution layer, Pooling layer, Dense layer)")
    st.write("모델 학습 : 전처리 된 학습 및 검증 데이터를 사용하여 예측 및 실제 레이블 간의 오차 최소화 위해 모델 조정(구성 및 하이퍼 파라미터 최적화 작업)")
    st.write("모델 평가 : 테스트(평가) 데이터로 학습된 모델의 정확도를 평가 후 최적화 된 모델을 저장")

    st.subheader("포지션 분류 과정")
    st.write("1. 업로드 된 히트맵 이미지를 224 x 224 크기로 변경 후 행렬 데이터(np.array)로 변환")
    st.write("2. 변환된 데이터를 이미지 분류 모델에 입력 후 포지션 예측(predict) 실시")
    st.write("3. 예측 결과 값에 해당하는 클래스(포지션) 이름을 화면에 출력")
    st.write("사용한 모델의 이미지 분류 정확도 : 90%")

    st.subheader("이미지 분류 시스템 Diagram")
    img = Image.open('./data/cnn_diagram.png')
    st.image(img, caption='diagram')
