import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_folium import folium_static
import folium

total_GCRB = pd.read_csv('C:/Users/eleun/Documents/project_seven/data/total_gamerank.csv')

total_GCRB.drop(['Unnamed: 0', '연번'], axis=1, inplace=True)
GCRB_cp = total_GCRB.copy()


#데이터 프레임 columns value의 종류와 수를 세는 함수
def value_count(data, col):
    dummy_dict = {}
    dummy_dict = dict(data[col].value_counts())
    return dummy_dict

ARC = value_count(total_GCRB, '등급분류기관')

sample_dict = {}
#단어가 포함되어 있는 columns의 value를 추출하여 수를 딕셔너리 value로 검색 단어를 key로 저장하는 함수
def word_search(data, col, word):    
        newdata = data[data[col].str.contains(word, na=False)].index
        sample_dict[word] = len(newdata)
        data = data.drop(newdata, inplace=True)
        return sample_dict

word = '15세', '12세', '등급'
for i in word:
    word_search(GCRB_cp, '결정등급', i)
GCRB_dt = dict(GCRB_cp['결정등급'].value_counts())
GCRB_dt.update(sample_dict)

#딕셔너리 키 이름을 변경하는 소스코드
keyname = {'청소년이용불가':'age18+', '전체이용가':'All-age', 
            '15세':'age15', '12세':'age12', '등급':'Another'}
GCRB_new = dict((keyname[key], value) for (key, value) in GCRB_dt.items())

#matplotlib pie chart 옵션 코드
wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5, 'clip_on': False}
title1 = 'Game Content Rating Board'
title2 = 'Age Rating Coalition'
title3 = 'Production '
color1 = ['red', 'green', 'yellow', 'blue', 'silver']
color2 = ['red', 'blue', 'yellow', 'green', 'silver', 'orange', 
        'purple', 'brown', 'pink', 'gold', 'gray', 'cyan']

#pie chart 제작 함수
def circle_chart_making(title, label, data, color, explode=None):
    '''
    matplotlib pie : 원형 그래프 출력 함수 / 한글 출력 안 됨.
    title : 원형 그래프 이름
    label : 차트의 각 항목 이름
    data : 원형 그래프로 나타낼 데이터 값
    color : 그래프의 각 항의 색을 지정
    explode : 그래프 각 항을 원점에서 어느정도 나오게 설정할 지 정할 수 있음
    '''

    #한글폰트 경로 pie chart에서 인식 안 됨.
    '''
    font_path = '한글폰트 경로 입력'
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    plt.rc("font", family=font_name)
    '''
    #차트 옵션
    '''
    autopct: 각 항의 비율 표시(소숫점 설정 가능)
    startangle: 차트 시작 각도 설정
    shadow: 차트의 그림자 설정
    textprops: 차트 내 글자 설정
    '''
    plt.title(title, size=20)
    plt.axis('equal')
    plt.pie(data, labels=label , autopct='%.1f%%', startangle=15, colors=color, 
            textprops={'size':15}, explode=explode, wedgeprops=wedgeprops)
    plt.legend()
    plt.show()

GCRB_cp2 = total_GCRB.copy()
sample_dict = {}
name = {'스마일게이트':'Smilegate', '네오위즈':'Neowiz', '세가':'Sega', '에이치투':'H2',
        '반다이남코':'BandaiNamco', '마이크로소프트':'MS', '일렉트로닉아츠':'EA', '소니':'Sony',
        '닌텐도':'Nintendo', '테이크투':'Take-Two', '유비소프트':'Ubisoft', '크래프톤':'Krafton'}

for i in name:
    word_search(GCRB_cp2, '신청사', i)
GCRB_dt2 = {}
GCRB_dt2.update(sample_dict)
GPRD = dict((name[key], value) for (key, value) in GCRB_dt2.items())

pc_room = pd.read_csv('C:/Users/eleun/Documents/project_seven/data/daegu_pcr.csv')
pc_room.drop('Unnamed: 0', axis=1, inplace=True)

def maping():
    map = folium.Map(location=[35.92, 128.56], zoom_start=12, tiles='Stamen Terrain')
    for name, lat, lng in zip(pc_room.상호, pc_room.Latitude, pc_room.Longitude):
        folium.Marker([lat, lng], popup=name).add_to(map)
    st.write('대구 북구 게임 제공업소 지도')
    folium_static(map)

#데이터 정보 확인 함수
def Info():
    name = ['게임물등급관리', '결정등급', '결정기관', '신청사', '제공업소']
    choice = st.selectbox('데이터룰 볼 항목을 선택: ', name)
    if choice == name[0]:
        st.write("게임물등급관리 데이터 일부")
        st.table(total_GCRB.head(10))
    elif choice == name[1]:
        st.write('결정등급 데이터')
        st.table(pd.DataFrame(GCRB_new.items(), columns=['결정등급', '포함 수']))
    elif choice == name[2]:
        st.write('결정기관 데이터')
        st.table(pd.DataFrame(ARC.items(), columns=['결정기관', '처리 수']))
    elif choice == name[3]:
        st.write('신청사 데이터 일부')
        st.table(pd.DataFrame(GCRB_dt2.items(), columns=['신청사', '신청 수']))
    elif choice == name[4]:
        st.write('대구 북구 게임 제공업소 데이터 일부')
        st.table(pc_room.head(10))
    
def de_info():
    st.write("total_GCRB, pc_room 요약 정보")
    if st.checkbox('내용 보기'):
        st.write(total_GCRB.describe())
        st.write(pc_room.describe())
    else:
        st.text('체크박스를 누르면 내용을 확인할 수 있습니다.')

def choice():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    name = ['결정등급', '결정기관', '신청사']
    select = st.selectbox('차트로 볼 항목을 선택하세요', name)
    
    if select == name[0]:
        st.write('결정등급 차트를 선택했습니다.')
        st.pyplot(circle_chart_making(title1, GCRB_new.keys(), GCRB_new.values(), color1))
    elif select == name[1]:
        st.write('결정기관 차트를 선택했습니다.')
        st.pyplot(circle_chart_making(title2, ARC.keys(), ARC.values(), color=('Orange', 'Green')))
    elif select == name[2]:
        st.write('신청사 차트를 선택했습니다.')
        st.pyplot(circle_chart_making(title3, GPRD.keys(), GPRD.values(), color2))