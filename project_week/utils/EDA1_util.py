import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from datetime import datetime
from scipy import interpolate

st.set_option('deprecation.showPyplotGlobalUse', False)

def concat_file(data, co_data):
    file_name = data
    tot_data = pd.DataFrame()
    for fname in file_name:
        temp = pd.read_csv(fname, encoding=co_data)
        tot_data = pd.concat([tot_data, temp])
    tot_data.to_csv('C:/Users/eleun/Documents/project_week/data/weather_data.csv')
data_ = glob('C:/Users/eleun/Downloads/weather/*.csv')
concat_file(data_, 'cp949')

w_data = pd.read_csv('C:/Users/eleun/Documents/project_week/data/weather_data.csv')
w_data.drop(['Unnamed: 0', '지점', '지점명'], axis=1, inplace=True)
w_data.rename(columns={'기온(°C)':'기온'}, inplace=True)
w_data = w_data.sort_values(by='일시')
w_data.일시 = pd.to_datetime(w_data.일시)
w_data.set_index('일시', inplace=True)
w_data_c = w_data.copy()
w_data_c2 = w_data.copy()

null_test = w_data.기온.isnull()
error_test = (w_data['기온'] == 9999|99999)
null_result = []
error_result = []

def QC_test1(data, result):
    '''결측값 검사 함수: isnull()로 True와 False로 바꾼 데이터를
    함수를 통해 True(NaN값)만 추출하여 dataframe에서 찾아낼 수 있게
    하는 함수
    '''
    for i, j in enumerate(data):
        if j == True:
            result.append(w_data.iloc[i])

QC_test1(null_test, null_result)
QC_test1(error_test, error_result)

limit_result = []
def QC_test2(data):
    '''한계검사 함수: QC 검사의 한계 값 영상 40도와 영하 33도 값에 해당하는
    온도 값을 검사하기 위한 함수.
    '''
    for n in range(len(data)):
        if (data['기온'].iloc[n] >= 40)|(data['기온'].iloc[n] <= -33):
            limit_result.append(data.iloc[n])

QC_test2(w_data)

step_result = []
def QC_test3(data):
    '''단계검사 함수: QC 검사의 단계 검사를 위해 1분 전의 온도와 현재의 온도를
    비교해 두 온도의 차이가 3도 이상 날 경우 해당되는 row를 저장하는 함수.
    '''
    data['단계검사'] = data['기온'] - data['기온'].shift()
    for n in range(len(data)):
        if (data['단계검사'].iloc[n] >= 3.0)|(data['단계검사'].iloc[n] <= -3.0):
            step_result.append(data.iloc[n])

QC_test3(w_data)

persis_result = []
persis_index = []
def QC_test4(data):
    '''지속성검사 함수 1: resample 기능을 사용해
    1시간 단위의 합계 값을 구하고 결과 리스트에 저장하는 함수.
    '''
    pr_data = abs(data['단계검사']).resample('1H', closed='right').sum()
    for n, num in enumerate(pr_data):
        if num <= 0.1:
            persis_result.append(pr_data.iloc[n])
            persis_index.append(pr_data.index[n])

QC_test4(w_data)

pv_result = []
def persis_valid(data, index):
    '''python이 실수를 정확히 표현할 수 없어서 발생하는 근사값이
    지속성 검사의 조건인 0.1과 같은지 비교하기 위해 isclose()를
    사용해 검사하는 함수.
    data: QC 지속성검사 결과 리스트
    index: QC 지속성검사 인덱스 리스트
    '''
    import math
    for i in range(len(data)):
        num = data[i]
        if math.isclose(num, 0.1) == True:
            pass
        else:
            pv_result.append(index[i])

persis_valid(persis_result, persis_index)

del_data1 = w_data['2020-02-05 23:01:00':'2020-02-06 00:00:00']
del_data2 = w_data['2020-02-08 01:01:00':'2020-02-08 02:00:00']

def data_remove(data, remover):
    ''' data : 데이터 수정하려는 데이터 프레임(카피본으로 준비, 원본 살리기) 예)df2 = df.copy()
        remover : 제거하려는 항목이 있는 리스트
        QC검사에서 결측값으로 결정 된 값들을 데이터 프레임에서
        drop 시키는 함수.
    '''
    #for n in range(len(remover)):
    #    key = str(remover[n])
    #    data.drop(key, inplace=True)
    for n in remover.index:
        data.drop(n, axis=0, inplace=True)

data_remove(w_data_c, del_data1)
data_remove(w_data_c, del_data2)

hours_mean_data = w_data_c.resample('1H', closed='right').agg(['mean', 'min', 'max', 'size'])

three_hours_mean_data = w_data_c.resample('3H', closed='right').agg(['mean', 'min', 'max', 'size'])

days_mean_data = w_data_c.resample('D', closed='right').agg(['mean', 'min', 'max', 'size'])

size_check_list = []
def size_check(data):
    '''dataframe을 1시간 기준으로 resample 시 크기가 60의 80%인 48일 시
    해당 row를 제외하기 위해 48이하인 항목을 저장하기 위해 사용.
    '''
    for i, j in enumerate(data[('기온','size')]):
        if j < 48:
            size_check_list.append(data.iloc[i])

size_check(hours_mean_data)

def gap_filling(data):
    '''갭 필링을 위한 함수'''
    data = data.interpolate(method='linear')
    return data

gf_data = gap_filling(hours_mean_data)

hours_mean_data2 = hours_mean_data.drop('2020-02-05 23:00:00')
hours_mean_data2 = hours_mean_data.drop('2020-02-08 01:00:00')

def data_info():
    st.header("기상관측 데이터 통계 정보")
    choice = ['기상관측 데이터 통계: 초기', '기상관측 데이터 통계: QC', '기상관측 데이터 통계: 1시간',
    '기상관측 데이터 통계: 3시간', '기상관측 데이터 통계: 1일']
    status = st.radio('확인할 통계 정보 선택', choice)
    if status == choice[0]:
        st.write(w_data_c2.describe())
    elif status == choice[1]:
        st.write(w_data_c.describe())
    elif status == choice[2]:
        st.write(hours_mean_data.describe())
    elif status == choice[3]:
        st.write(three_hours_mean_data.describe())
    elif status == choice[4]:
        st.write(days_mean_data.describe())

'''그래프 11개'''

import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    font_path = 'lropkeBatangM.woff'
    fontprop = font_manager.FontProperties(fname=font_path, size=10)
    font_name = fontprop.get_name()
    rc('font', family=font_name)

def graph_show(data, title):
    plt.figure(figsize=(14,10))
    plt.title(title, size=25)
    x = data.index
    y = data.기온
    plt.plot(x, y)
    plt.xlabel('날짜', size=20)
    plt.ylabel('기온', size=20)
    plt.grid()
    plt.show()

def graph_show2(data, title, name):
    plt.figure(figsize=(14,10))
    plt.title(title, size=25)
    x = data.index
    y1 = data[('기온', 'mean')]
    #y2 = data[('기온', 'min')]
    #y3 = data[('기온', 'max')]
    plt.plot(x, y1, label=name[0], color='g')
    #plt.plot(x, y2, label=name[1], color='b')
    #plt.plot(x, y3, label=name[2], color='r')
    plt.xlabel('날짜', size=20)
    plt.ylabel('기온', size=20)
    plt.grid()
    plt.legend()
    
name = ['mean', 'min', 'max']

def graph_list():
    st.header('기온관측 자료 그래프 목록')
    graph = ['기온관측자료', '기온관측자료 - 결측검사 결과', '기온관측자료 - 한계검사 전',
             '기온관측자료 - 한계검사 결과', '기온관측자료 - 단계검사 전', 
             '기온관측자료 - 단계검사 결과', '기온관측자료 - 지속성검사 전',
             '기온관측자료 - 지속성검사 결과', '기온관측 1시간 평균자료',
             '기온관측 3시간 평균자료', '기온관측 1일 평균자료',
             '기온관측 1시간 평균자료 -gapfilling']
    select = st.selectbox('확인할 그래프를 선택하세요', graph)
    if select == graph[0]:
        st.write(f'{graph[0]} 그래프를 선택했습니다')
        st.pyplot(graph_show(w_data, '기온관측자료')) # 1.최초 데이터 그래프
    elif select == graph[1]:
        st.write(f'{graph[1]} 그래프를 선택했습니다')
        st.pyplot(graph_show(w_data, '기온관측자료 - 결측검사 결과')) # 2.QC 1단계 후 그래프
    elif select == graph[2]:
        st.write(f'{graph[2]} 그래프를 선택했습니다')
        st.pyplot(graph_show(w_data, '기온관측자료 - 한계검사 전')) # 3.QC 2단계 전 그래프
    elif select == graph[3]:
        st.write(f'{graph[3]} 그래프를 선택했습니다')
        st.pyplot(graph_show(w_data, '기온관측자료 - 한계검사 결과')) # 4.QC 2단계 후 그래프
    elif select == graph[4]:
        st.write(f'{graph[4]} 그래프를 선택했습니다')
        st.pyplot(graph_show(w_data, '기온관측자료 - 단계검사 전')) # 5.QC 3단계 전 그래프
    elif select == graph[5]:
        st.write(f'{graph[5]} 그래프를 선택했습니다') 
        st.pyplot(graph_show(w_data, '기온관측자료 - 단계검사 결과')) # 6.QC 3단계 후 그래프
    elif select == graph[6]:
        st.write(f'{graph[6]} 그래프를 선택했습니다')
        st.pyplot(graph_show(w_data, '기온관측자료 - 지속성검사 전')) # 7.QC 4단계 전 그래프
    elif select == graph[7]:
        st.write(f'{graph[7]} 그래프를 선택했습니다')
        st.pyplot(graph_show(w_data_c, '기온관측자료 - 지속성검사 결과')) # 8.QC 4단계 후 그래프
    elif select == graph[8]:
        st.write(f'{graph[8]} 그래프를 선택했습니다')
        st.pyplot(graph_show2(hours_mean_data, '기온관측 1시간 평균자료', name)) # 9.1시간 평균 자료 그래프
    elif select == graph[9]:
        st.write(f'{graph[9]} 그래프를 선택했습니다')
        st.pyplot(graph_show2(three_hours_mean_data, '기온관측 3시간 평균자료', name)) # 10.3시간 평균 자료 그래프
    elif select == graph[10]:
        st.write(f'{graph[10]} 그래프를 선택했습니다')
        st.pyplot(graph_show2(days_mean_data, '기온관측 1일 평균자료', name)) # 11.1일 평균 자료 그래프
    elif select == graph[11]:
        st.write(f'{graph[11]} 그래프를 선택했습니다')
        st.pyplot(graph_show2(gf_data, '기온관측 1시간 평균자료 -gapfilling', name)) # 12.GapFilling 후 그래프