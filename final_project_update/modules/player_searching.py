import streamlit as st
from PIL import Image
from modules import psm

df = psm.load_df()


def app():
    player = st.text_input('추천 받은 선수 혹은 찾고싶은 선수를 입력해주세요.', '예) 이승우')
    if player in df['선수명'].unique():
        number = psm.player_num(player)
        col1, col2 = st.columns([2, 1])
        with col1:
            image = Image.open('./data/picture/'+ number.astype('str') +'.PNG')
            img_resize = image.resize((900, 1200))
            st.image(img_resize, caption='')
        with col2:
            info = psm.table(number)
            st.write(info)
            st.write(player+" 선수의 2022년 히트맵")
            image = Image.open('./data/heatmap/'+ number.astype('str') +'.PNG')
            img_resize = image.resize((250, 150))
            st.image(img_resize, caption='')

        st.header("")
        st.subheader(player+" 선수의 2022년 상세 스탯")
        col1, col2 = st.columns([1, 1])
        with col1:
            chart = psm.radar_chart(number)
            st.pyplot(chart)
        with col2:
            bar = psm.barh(number)
            st.write(bar)

        st.header("")
        st.subheader(player+" 선수의 하이라이트 영상")

    else:
        st.write("검색한 선수가 없습니다.")