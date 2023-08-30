import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image

#포지션 분류 딕셔너리
def position_classification(data):
    pos = {}
    item = data.flatten()
    pos['DF'] = item[0]
    pos['FW'] = item[1]
    pos['GK'] = item[2]
    pos['MF'] = item[3]
    max_key = max(pos, key=pos.get)
    return max_key

#이미지 분류 시스템 함수
def heatmap_image_classification():
    #모델 파일 경로
    model_path = './data/image_cc_model.h5'
    
    #모델 로드
    model = load_model(model_path)

    #파일 업로드 버튼
    file = st.file_uploader("이미지 파일 확장자를 소문자로 변경해 주세요", type=['png', 'jpg', 'jpeg'])

    #시스템에 입력
    if file is not None:
        file_extension = file.name.split(".")[-1].lower()
        if file_extension in ["png", "jpg", "jpeg"]:
            img = image.load_img(file, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            data = model.predict(x)
            position = position_classification(data)
            st.write(f"히트맵 분석 결과 당신의 포지션은 {position} 입니다.")

        else:
            st.write("형식에 맞는 이미지를 업로드 해주세요")

        return position


#랜덤 이미지 선택
import random
import glob
def random_image():
    image_dir = './data/heatmap'
    image_files = glob.glob(image_dir + "/*.png")
    random_image_file = random.choice(image_files)
    return random_image_file