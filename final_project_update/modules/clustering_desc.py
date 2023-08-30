import streamlit as st
from PIL import Image

def app():
    st.header('군집화 설명')
    st.subheader("기본 아이디어")
    st.write("(1701,26)모양의 데이터를 19개로 한번에 군집하는 것은 굉장히 비효율적이다.")
    st.write("따라서, 히트맵 이미지를 보고 Position Classification을 먼저 수행한뒤")
    st.write("GK, DF, MF, FW로 나누고 4개 중에서 GK, DF(CB, FB), MF(CDM, CAM), FW(WF, CF)로 군집하기위해 필요한 속성을 가져와 군집화 실행.")
    st.write("GK : GK, SGK")
    st.write("FB : Overlapper, Progressor, Safety")
    st.write("CB : Aggressor, SCB, Spreader")
    st.write("CDM : Box to Box, Builder, Distributor")
    st.write("CAM : Creator, Box Crasher")
    st.write("WF : Wide Threat, Outlet, Unlocker")
    st.write("CF : Finisher, Target, Roamer")
    st.write("총 10번의 군집화 실행 및 각 군집화 결과는 실루엣 계수 0.3이상으로 채택.")

    img = Image.open('./data/clustering.png')
    st.image(img, caption='Clustering')