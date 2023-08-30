import streamlit as st
from utils import project1_desc as p1d

def app():
	st.write('''
		### 세미 프로젝트
		'''
		)
	
	p1d.Info()
	
	p1d.de_info()
	
	p1d.choice()
	
	p1d.maping()