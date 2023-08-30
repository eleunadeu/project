import streamlit as st
from utils import project2_desc as p2d


def app():
	st.write('''
		### 주간 프로 젝트
		'''
		)
	p2d.desc()
