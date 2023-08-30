import pandas as pd
import matplotlib.pyplot as plt

total_GCRB = pd.read_csv('C:/Users/eleun/Downloads/total_gamerank.csv')
total_GCRB.drop(['Unnamed: 0', '연번'], axis=1, inplace=True)

def Info():
    total_GCRB.info()
    total_GCRB.describe()

#밸류의 수를 카운트하는 함수
def value_count(data, col):
    dummy_dict = {}
    dummy_dict = dict(data[col].value_counts())
    return dummy_dict

#등급분류 기관
ARC = value_count(total_GCRB, '등급분류기관')

#특정 단어 찾아서 지정한 키 값으로 해당 단어가 포함된 항목의 값을 밸류로하는 딕셔너리 제작 함수
sample_dict = {}
def word_search(data, col, word):
    newdata = data[data[col].str.contains(word, na=False)].index
    sample_dict[word] = len(newdata)
    data = data.drop(newdata, inplace=True)
    return sample_dict

GCRB_cp = total_GCRB.copy()

#나이 등급
word_search(GCRB_cp, '결정등급', '15세')
word_search(GCRB_cp, '결정등급', '12세')
word_search(GCRB_cp, '결정등급', '등급')
GCRB_dt = dict(GCRB_cp.value_counts())
GCRB_dt.update(sample_dict)

#딕셔너리 키 이름 변경하는 소스코드
keyname = {'청소년이용불가':'age18+', '전체이용가':'All-age', 
            '15세':'age15', '12세':'age12', '등급':'Another'}
GCRB_new = dict((keyname[key], value) for (key, value) in GCRB_dt.items())

#파이차트 옵션
wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 5, 'clip_on': False}
title1 = 'Game Content Rating Board'
title2 = 'Age Rating Coalition'
color1 = ['red', 'green', 'yellow', 'blue', 'silver']

#파이차트 제작 함수
def circle_chart_making(title, label, data, color, explode=None):
    '''
    matplotlib pie 원형 그래프 출력 함수 / 한글 출력 안 됨.
    title: 원형 그래프 이름
    label: 각 항목의 이름
    data: 원형 그래프로 나타낼 데이터 값
    color: 그래프의 각 항의 색을 지정
    explode: 그래프 각 항을 원점에서 어느정도 나오게 설정할 지 정할 수 있음
    '''

    #한글폰트 경로
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
    plt.pie(data, labels=label , autopct='%.1f%%', startangle=10, colors=color, 
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
title3 = 'Production '
color2 = ['red', 'blue', 'yellow', 'green', 'silver', 'orange', 
        'purple', 'brown', 'pink', 'gold', 'mint', 'cream']

circle_chart_making(title1, GCRB_new.keys(), GCRB_new.values(), color1)
circle_chart_making(title2, ARC.keys(), ARC.values(), color=('Orange', 'Green'))
circle_chart_making(title3, GPRD.keys(), GPRD.values(), color2)

