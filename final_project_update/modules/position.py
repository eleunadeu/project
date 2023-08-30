import streamlit as st
from modules import Image_cc as icc
from PIL import Image

def app():

    st.header("히트맵에 따른 포지션 분류")

    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write(' ')
    with col2:
        img = icc.random_image()
        image = Image.open(img)
        img_resize = image.resize((300, 180))
        st.image(image, caption='heatmap')
    with col3:
        st.write(' ')

    st.markdown('히트맵(이미지)을 업로드하면 분석 후 포지션을 분류합니다.', unsafe_allow_html=True)

    icc.heatmap_image_classification()