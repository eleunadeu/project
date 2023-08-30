import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from datetime import datetime
import platform

st.set_option('deprecation.showPyplotGlobalUse', False)

#그래프 한글 지정
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

#데이터 입력 및 데이터 프레임화
critic = pd.read_csv('C:/Users/eleun/Documents/project_week/data/critic_data.csv')
critic.drop('Unnamed: 0', axis=1, inplace=True)
critic.columns = ['critic_score', 'game_title', 'platform', 'release_date']

#영어로 된 날짜 숫자로 변경하는 함수
res_date = []
def date_change():
    for n in critic.release_date:
        date = ' '.join(n.replace(',','').split())
        res = datetime.strptime(date, '%b %d %Y').strftime('%Y-%m-%d')
        res_date.append(res)
date_change()
critic['release_date'] = res_date

#결측값 확인 및 결측 값 대체
#critic.isnull().value_counts()
#critic = critic['critic_score'].fillna(method='bfill')

#히스토 그램 그래프 그리는 함수
def critic_hist():
    plt.figure(figsize=(14,10))
    plt.title('Critic 점수 분포', size=25)
    plt.hist(critic.critic_score)
    plt.xlabel('Critic 점수', size=20)
    plt.ylabel('게임 수', size=20)
    plt.grid()
    plt.show()

#빈 데이터 프레임
over90 = pd.DataFrame()
over80 = pd.DataFrame()
over70 = pd.DataFrame()
over60 = pd.DataFrame()
over50 = pd.DataFrame()
under50 = pd.DataFrame()

#100~50까지 10단위로 끊어서 저장 및 50이하 값은 하나로 저장
def score_rate():
    for n, p in enumerate(critic.critic_score):
        if p >= 90:
            over90[n] = critic.loc[n]
        elif p >= 80:
            over80[n] = critic.loc[n]
        elif p >= 70:
            over70[n] = critic.loc[n]
        elif p >= 60:
            over60[n] = critic.loc[n]
        elif p >= 50:
            over50[n] = critic.loc[n]
        else:
            under50[n] = critic.loc[n]

score_rate()

#데이터 프레임 행렬 변경
over90 = over90.T
over80 = over80.T
over70 = over70.T
over60 = over60.T
over50 = over50.T
under50 = under50.T

#Pie Chart 그리는 함수(점수별 비율 그래프)
def score_rate_piechart():
    critic_ratio =  [len(over90), len(over80), len(over70), len(over60), len(over50), len(under50)]
    color_1 = ['red', 'orange', 'blue', 'cyan', 'green', 'silver']
    label_1 = ['90점 이상', '80점 이상', '70점 이상', '60점 이상', ' 50점 이상', '50점 이하']
    wedgeprops = {'width': 1, 'edgecolor': 'w', 'linewidth': 2, 'clip_on': False}
    plt.figure(figsize=(14,10))
    plt.axis('equal')
    plt.title('Critic 점수 별 비율', size=25)
    plt.pie(critic_ratio, autopct='%.1f%%', labels=label_1, startangle=15, colors=color_1, 
            textprops={'size':20}, wedgeprops=wedgeprops, shadow=True)
    plt.legend(loc='best')
    plt.show()

#백분위 수 구하기
score = critic.critic_score
np.percentile(score, 90)
np.percentile(score, 60)
np.percentile(score, 30)

#Open Critic 설명
open_critic = '''open critic
"Mighty Man" is OpenCritic's way of tagging games based on the scores awarded to them by top critics. 
The color scheme comes from video games, where "orange" loot is often best, with purple, blue, and green tiered loot following.
Mighty
The top 10% of game ratings. Best in their genre. Universal critical acclaim.
Strong
The next 30% of all games scored on OpenCritic. Great execution with a few flaws.
Fair
Games scored in the 30th - 60th percentiles. Some issues hold these games.
Weak
The bottom 30% of game ratings. Games that missed on some key elements.
'''

#빈 데이터 프레임
Mighty = pd.DataFrame()
Strong = pd.DataFrame()
Fair = pd.DataFrame()
Weak = pd.DataFrame()

#Open Critic 기준으로 데이터 나눠서 저장
def mighty_man():
    for n, p in enumerate(critic.critic_score):
        if p >= 84:
            Mighty[n] = critic.loc[n]
        elif p >= 75:
            Strong[n] = critic.loc[n]
        elif p >= 66:
            Fair[n] = critic.loc[n]
        else:
            Weak[n] = critic.loc[n]

mighty_man()
#데이터 프레임 행렬 변경
Mighty = Mighty.T
Strong = Strong.T
Fair = Fair.T
Weak = Weak.T

#pie chart 그리는 함수 2(open critic 기준 별 비율 그래프)
def mighty_piechart():
    mighty_ratio = [len(Mighty), len(Strong), len(Fair), len(Weak)]
    color_2 = ['orange', 'purple', 'blue', 'green']
    label_2 = ['Mighty', 'Strong', 'Fair', 'Weak']
    wedgeprops = {'width': 1, 'edgecolor': 'w', 'linewidth': 2, 'clip_on': False}
    plt.figure(figsize=(14,10))
    plt.title('Open Critic 등급 별 비율', size=25)
    plt.pie(mighty_ratio, autopct='%.1f%%', labels=label_2, colors=color_2, wedgeprops=wedgeprops, 
            textprops={'size':17}, shadow=True, counterclock=False, startangle=90)
    plt.legend(loc='best')
    plt.show()

#기종 별 데이터 나눠서 저장하는 코드
switch = critic[critic.platform.str.contains('Switch')]
wiiu = critic[critic.platform.str.contains('Wii-U')]
n3ds = critic[critic.platform.str.contains('3DS')]
ps4 = critic[critic.platform.str.contains('PS4')]
ps5 = critic[critic.platform.str.contains('PS5')]
vita = critic[critic.platform.str.contains('Vita')]
xbxs = critic[critic.platform.str.contains('XBXS')]
xb1 = critic[critic.platform.str.contains('XB1')]
pc = critic[critic.platform.str.contains('PC')]
stadia = critic[critic.platform.str.contains('Stadia')]

#VR 기종 데이터 프레임 만드는 함수
vive = pd.DataFrame()
oculus = pd.DataFrame()
psvr = pd.DataFrame()
def platform_vr():
    for n, pf in enumerate(critic.platform):
        if 'Vive' in pf:
            vive[n] = critic.loc[n]
        elif 'Oculus' in pf:
            oculus[n] = critic.loc[n]
        elif 'PSVR' in pf:
            psvr[n] = critic.loc[n]

platform_vr()
#데이터 프레임 병합
vive = vive.T
oculus = oculus.T
psvr = psvr.T
vr = pd.concat([vive, oculus, psvr])
vr.columns = ['critic_score', 'game_title', 'platform', 'release_date']
vr = vr.sort_values(by=['critic_score'], ascending=False)

#기종 별 mean, max, min 값 데이터 프레임
nintendo = pd.concat([switch, wiiu, n3ds])
playstation = pd.concat([ps4, ps5, vita, psvr])
xbox = pd.concat([xbxs, xb1])
pc_total = pd.concat([pc, stadia, oculus, vive])
game_merchine = [switch, wiiu, n3ds, ps4, ps5, vita, xbxs, xb1, pc, stadia,
                 vr]
game_platform = [nintendo, playstation, xbox, pc_total]
platform_name = ['Nintendo', 'PlayStation', 'XBOX', 'PC']

platform_df = pd.DataFrame()
platform_dict = {}
platform_list = []
def data_frame_create(lists, dicts, df, data, name):
    for n in data:
        result = n.critic_score.agg(['mean', 'max', 'min'])
        lists.append(result)
    for i in range(len(name)):
        dicts[name[i]] = [lists[i][0], lists[i][1], lists[i][2]]
    df = pd.DataFrame(dicts.values(), index=dicts.keys(), columns=['mean', 'max', 'min'])
    return df

#기종 별 비율 Pie Chart 그리는 함수(2중 pie 그래프)
def platform_piechart():
    p_ratio = [len(switch), len(n3ds), len(ps4), len(wiiu), len(ps5), len(xbxs), 
            len(stadia), len(xb1), len(vita), len(pc), len(vr)]
    p_ratio2 = [len(switch + n3ds + wiiu), len(ps4 + ps5 + vita), len(xbxs + xb1), len(pc + stadia),
                len(vr)]
    color_3 = ['red', 'coral', 'blue', 'orange', 'deepskyblue', 'green', 'lime', 
            'purple', 'darkviolet', 'magenta', 'darkgray']
    color_4 = ['red', 'blue', 'green', 'magenta', 'silver']
    label3 = ['Switch', '3DS', 'PS4', 'Wii-U', 'PS5', 'XBXS', 'Stadia', 'XB1', 'Vita', 'PC', 'VR']
    label4 = ['Nintendo', 'PlayStation', 'XBOX', 'PC', 'VR']
    fig, ax = plt.subplots()
    plt.title('platform', size=30, pad=250)
    plt.figure(figsize=(15,10))
    ax.pie(p_ratio, radius=3, colors=color_3, labels=label3, 
            rotatelabels=False, startangle=90, counterclock=False, 
            pctdistance=0.8, labeldistance=1.1, wedgeprops={'width':1, 'edgecolor':'w'}, 
            textprops={'size':20}, autopct='%.1f%%')
    ax.pie(p_ratio2, radius=2, colors=color_4, labels=label4, 
            rotatelabels=False, startangle=90, counterclock=False, 
            pctdistance=0.8, labeldistance=0.4, wedgeprops={'width':1.5, 'edgecolor':'w'}, 
            textprops={'size':20}, autopct='%.1f%%')
    ax.set(aspect='equal')
    plt.show()
    st.pyplot(fig)
    
#년도 별 출시 게임끼리 나눠서 저장하는 코드
rd_2023 = critic[critic.release_date.str.contains('2023')]
rd_2022 = critic[critic.release_date.str.contains('2022')]
rd_2021 = critic[critic.release_date.str.contains('2021')]
rd_2020 = critic[critic.release_date.str.contains('2020')]
rd_2019 = critic[critic.release_date.str.contains('2019')]
rd_2018 = critic[critic.release_date.str.contains('2018')]
rd_2017 = critic[critic.release_date.str.contains('2017')]
rd_2016 = critic[critic.release_date.str.contains('2016')]
rd_2015 = critic[critic.release_date.str.contains('2015')]
rd_2014 = critic[critic.release_date.str.contains('2014')]
rd_2013 = critic[critic.release_date.str.contains('2013')]
rd_2012 = critic[critic.release_date.str.contains('2012')]
rd_2011 = critic[critic.release_date.str.contains('2011')]
rd_2010 = critic[critic.release_date.str.contains('2010')]
rd_2009 = critic[critic.release_date.str.contains('2009')]
rd_2006 = critic[critic.release_date.str.contains('2006')]
rd_2005 = critic[critic.release_date.str.contains('2005')]
rd_2004 = critic[critic.release_date.str.contains('2004')]
rd_2003 = critic[critic.release_date.str.contains('2003')]
rd_2002 = critic[critic.release_date.str.contains('2002')]
rd_1999 = critic[critic.release_date.str.contains('1999')]

#출시 년도 별 게임 비율(어느 년도에 가장 많이 게임이 출시 했는지)
def release_date_piechart():
    ratio = [len(rd_2023), len(rd_2022), len(rd_2021), len(rd_2020), len(rd_2019), 
             len(rd_2018), len(rd_2017), len(rd_2016), len(rd_2015), len(rd_2014),  
             (len(rd_2012)+ len(rd_2011) + len(rd_2010) + len(rd_2009) + len(rd_2006) + 
              len(rd_2005) + len(rd_2004) + len(rd_2003) + len(rd_2002) + len(rd_1999) + 
              len(rd_2013))]
    color = ['red', 'blue', 'green', 'yellow', 'orange', 'aqua', 'slategray', 'blueviolet',
             'pink', 'deepskyblue', 'magenta']
    label = ['2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', 
             'another']
    wedgeprops = {'width': 0.7, 'edgecolor': 'w', 'linewidth': 2, 'clip_on': False}
    plt.figure(figsize=(14,10))
    plt.title("출시 년도별 게임 비율 그래프")
    plt.pie(ratio, labels=label, autopct='%.1f%%', startangle=15, colors=color, textprops={'size':15}, 
            wedgeprops=wedgeprops, shadow=True, pctdistance=0.8, counterclock=False)
    plt.show()

#시리즈 게임 20개 추출하는 코드
super_mario = critic[critic.game_title.str.contains('Mario')]
legend_of_zelda = critic[critic.game_title.str.contains('Zelda')]
kirby = critic[critic.game_title.str.contains('Kirby')]
pokémon = critic[critic.game_title.str.contains('Pokémon')] 
pokemon = critic[critic.game_title.str.contains('Pokemon')]
assassins_creed = critic[critic.game_title.str.contains("Assassin's Creed")]
far_cry = critic[critic.game_title.str.contains('Far Cry')]
final_fantasy = critic[critic.game_title.str.contains('Final Fantasy')]
resident_evil = critic[critic.game_title.str.contains('Resident Evil')]
call_of_duty = critic[critic.game_title.str.contains('Call of Duty')]
battlefield = critic[critic.game_title.str.contains('Battlefield')]
sonic = critic[critic.game_title.str.contains('Sonic')]
need_for_speed = critic[critic.game_title.str.contains('Need for Speed')]
fifa = critic[critic.game_title.str.contains('FIFA')]
forza = critic[critic.game_title.str.contains('Forza')]
fire_emblem = critic[critic.game_title.str.contains('Fire Emblem')]
mega_man = critic[critic.game_title.str.contains('Mega Man')]
tetris = critic[critic.game_title.str.contains('Tetris')]
tom_clancys = critic[critic.game_title.str.contains("Tom Clancy's")]
spider_man = critic[critic.game_title.str.contains('Spider-Man')]
monster_hunter = critic[critic.game_title.str.contains('Monster Hunter')]
#pokemon, pokémon 데이터 프레임 결합 코드
pokemon = pd.concat([pokémon, pokemon])

#시리즈 게임 mean, max, min 값 데이터 프레임
game_series = [super_mario, legend_of_zelda, kirby, pokemon, assassins_creed,
               far_cry, final_fantasy, resident_evil, call_of_duty, battlefield,
               sonic, need_for_speed, fifa, forza, fire_emblem, mega_man,
               tetris, tom_clancys, spider_man, monster_hunter]

#데이터 프레임 선택 박스
def show_data_frame():
    choice = ['Open Critic Ranking 10', '점수 별 게임 목록', '기종 별 게임 목록', 'Open Critic 기준 게임 분류', 
              '년도별 게임 분류', '시리즈 게임 20개 분류']
    select = st.selectbox('확인할 데이터 종류를 선택하세요', choice)
    if select == choice[0]:
        order = ['상위 10개 게임', '하위 10개 게임']
        sr = st.radio('보고 싶은 표를 선택하세요', order)
        if sr == order[0]:
            st.subheader('Top 10 Games')
            st.table(critic.head(10))
        elif sr == order[1]:
            st.subheader('Bottom 10 Games')
            st.table(critic.sort_values(by='critic_score', ascending=True).head(10))
    elif select == choice[1]:
        order = ['90점 이상 게임', '80점 이상 게임', '70점 이상 게임', '60점 이상 게임',
                 '50점 이상 게임', '50점 이하 게임']
        sr = st.radio('보고 싶은 점수 대를 고르세요', order, horizontal=True)
        if sr == order[0]:
            st.subheader('90점 대 게임 목록')
            st.dataframe(over90)
        elif sr == order[1]:
            st.subheader('80점 대 게임 목록')
            st.dataframe(over80)
        elif sr == order[2]:
            st.subheader('70점 대 게임 목록')
            st.dataframe(over70)
        elif sr == order[3]:
            st.subheader('60점 대 게임 목록')
            st.dataframe(over60)
        elif sr == order[4]:
            st.subheader('50점 대 게임 목록')
            st.dataframe(over50)
        elif sr == order[5]:
            st.subheader('50점 이하 게임 목록')
            st.dataframe(under50)
    elif select == choice[2]:
        order = ['닌텐도 스위치', '닌텐도 위유', '닌텐도 3DS', '플레이스테이션 4',
                 '플레이스테이션 5', '플레이스테이션 비타', '엑스박스 시리즈 엑스',
                 '엑스박스 원', '컴퓨터', '구글 스테디아', 'VR', '기기 및 기종 통계']
        sr = st.radio('보고 싶은 기종 별 게임 목록을 선택하세요', order, horizontal=True)
        if sr == order[0]:
            st.subheader('닌텐도 스위치 게임 목록')
            st.dataframe(switch)
            st.write("Best 5 Game")
            st.table(switch.head(5))
            st.write("Worst 5 Game")
            st.table(switch.sort_values(by='critic_score', ascending=True).head(5))
        elif sr == order[1]:
            st.subheader('닌텐도 위유 게임 목록')
            st.dataframe(wiiu)
            st.write("Best 5 Game")
            st.table(wiiu.head(5))
            st.write("Worst 5 Game")
            st.table(wiiu.sort_values(by='critic_score', ascending=True).head(5))
        elif sr == order[2]:
            st.subheader('닌텐도 3DS 게임 목록')
            st.dataframe(n3ds)
            st.write("Best 5 Game")
            st.table(n3ds.head(5))
            st.write("Worst 5 Game")
            st.table(n3ds.sort_values(by='critic_score', ascending=True).head(5))
        elif sr == order[3]:
            st.subheader('플레이스테이션 4 게임 목록')
            st.dataframe(ps4)
            st.write("Best 5 Game")
            st.table(ps4.head(5))
            st.write("Worst 5 Game")
            st.table(ps4.sort_values(by='critic_score', ascending=True).head(5))
        elif sr == order[4]:
            st.subheader('플레이스테이션 5 게임 목록')
            st.dataframe(ps5)
            st.write("Best 5 Game")
            st.table(ps5.head(5))
            st.write("Worst 5 Game")
            st.table(ps5.sort_values(by='critic_score', ascending=True).head(5))
        elif sr == order[5]:
            st.subheader('플레이스테이션 비타 게임 목록')
            st.dataframe(vita)
            st.write("Best 5 Game")
            st.table(vita.head(5))
            st.write("Worst 5 Game")
            st.table(vita.sort_values(by='critic_score', ascending=True).head(5))
        elif sr == order[6]:
            st.subheader('엑스박스 시리즈 엑스 게임 목록')
            st.dataframe(xbxs)
            st.write("Best 5 Game")
            st.table(xbxs.head(5))
            st.write("Worst 5 Game")
            st.table(xbxs.sort_values(by='critic_score', ascending=True).head(5))
        elif sr == order[7]:
            st.subheader('엑스박스 원 게임 목록')
            st.dataframe(xb1)
            st.write("Best 5 Game")
            st.table(xb1.head(5))
            st.write("Worst 5 Game")
            st.table(xb1.sort_values(by='critic_score', ascending=True).head(5))
        elif sr == order[8]:
            st.subheader('컴퓨터 게임 목록')
            st.dataframe(pc)
            st.write("Best 5 Game")
            st.table(pc.head(5))
            st.write("Worst 5 Game")
            st.table(pc.sort_values(by='critic_score', ascending=True).head(5))
        elif sr == order[9]:
            st.subheader('구글 스테디아 게임 목록')
            st.dataframe(stadia)
            st.write("Best 5 Game")
            st.table(stadia.head())
            st.write("Worst 5 Game")
            st.table(stadia.sort_values(by='critic_score', ascending=True).head())
        elif sr == order[10]:
            st.subheader('VR 게임 목록')
            st.dataframe(vr)
            st.write("Best 5 Game")
            st.table(vr.head(5))
            st.write("Worst 5 Game")
            st.table(vr.sort_values(by='critic_score', ascending=True).head(5))
        elif sr == order[11]:
            st.subheader('기기 및 기종 통계')
            merchine_total = data_frame_create(platform_list, platform_dict, platform_df, game_merchine, order[0:-1])
            pl_list = []
            pl_dict = {}
            pl_df = pd.DataFrame()
            platform_total = data_frame_create(pl_list, pl_dict, pl_df, game_platform, platform_name)
            order = ['평균 내림차순 정렬 : 기기', '평균 내림차순 정렬 : 기종',
                     '최대값 기준 정렬 : 기기', '최대값 기준 정렬 : 기종',
                     '최소값 기준 정렬 : 기기', '최소값 기준 정렬 : 기종']
            sr = st.radio('정렬 방법을 선택하세요', order, horizontal=True)
            if sr == order[0]:
                st.write('기기 별 평균 점수')
                st.table(merchine_total.sort_values(by='mean', ascending=False))
            elif sr == order[1]:
                st.write('기종 별 평균 점수')
                st.table(platform_total.sort_values(by='mean', ascending=False))
            elif sr == order[2]:
                st.write('기기 별 최고 점수')
                st.table(merchine_total.sort_values(by='max', ascending=False))
            elif sr == order[3]:
                st.write('기종 별 최고 점수')
                st.table(platform_total.sort_values(by='max', ascending=False))
            elif sr == order[4]:
                st.write('기기 별 최저 점수')
                st.table(merchine_total.sort_values(by='min', ascending=True))
            elif sr == order[5]:
                st.write('기종 별 최저 점수')
                st.table(platform_total.sort_values(by='min', ascending=True))
    elif select == choice[3]:
        st.write("'Mighty Man'is OpenCritic's way of tagging games based on the scores awarded to them by top critics.\n The color scheme comes from video games, where 'orange' loot is often best, with purple, blue, and green tiered loot following.")
        order = ['Mighty 등급', 'Strong 등급', 'Fair 등급', 'Weak 등급']
        sr = st.radio('Open Critic 등급을 선택하세요', order, horizontal=True)
        if sr == order[0]:
            st.subheader('Mighty 등급 게임 목록')
            st.write("Mighty\n The top 10% of game ratings. Best in their genre. Universal critical acclaim.")
            st.dataframe(Mighty)
        elif sr == order[1]:
            st.subheader('Strong 등급 게임 목록')
            st.write("Strong\n The next 30% of all games scored on OpenCritic. Great execution with a few flaws")
            st.dataframe(Strong)
        elif sr == order[2]:
            st.subheader('Fair 등급 게임 목록')
            st.write("Fair\n Games scored in the 30th - 60th percentiles. Some issues hold these games.")
            st.dataframe(Fair)
        elif sr == order[3]:
            st.subheader('Weak 등급 게임 목록')
            st.write("Weak\n The bottom 30% of game ratings. Games that missed on some key elements.")
            st.dataframe(Weak)
    elif select == choice[4]:
        order = ['2023년도 게임', '2022년도 게임', '2021년도 게임', '2020년도 게임', '2019년도 게임',
                 '2018년도 게임', '2017년도 게임', '2016년도 게임', '2015년도 게임', '2014년도 게임',
                 '2013년도 게임', '2012년도 게임', '2011년도 게임', '2010년도 게임']
        sr = st.radio('확인하녀는 출시년도를 선택하세요', order, horizontal=True)
        if sr == order[0]:
            st.subheader('23년도 출시 게임 목록')
            st.dataframe(rd_2023)
            st.write("Best 3 Game")
            st.table(rd_2023.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2023.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[1]:
            st.subheader('22년도 출시 게임 목록')
            st.dataframe(rd_2022)
            st.write("Best 3 Game")
            st.table(rd_2022.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2022.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[2]:
            st.subheader('21년도 출시 게임 목록')
            st.dataframe(rd_2021)
            st.write("Best 3 Game")
            st.table(rd_2021.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2021.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[3]:
            st.subheader('20년도 출시 게임 목록')
            st.dataframe(rd_2020)
            st.write("Best 3 Game")
            st.table(rd_2020.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2020.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[4]:
            st.subheader('19년도 출시 게임 목록')
            st.dataframe(rd_2019)
            st.write("Best 3 Game")
            st.table(rd_2019.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2019.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[5]:
            st.subheader('18년도 출시 게임 목록')
            st.dataframe(rd_2018)
            st.write("Best 3 Game")
            st.table(rd_2018.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2018.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[6]:
            st.subheader('17년도 출시 게임 목록')
            st.dataframe(rd_2017)
            st.write("Best 3 Game")
            st.table(rd_2017.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2017.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[7]:
            st.subheader('16년도 출시 게임 목록')
            st.dataframe(rd_2016)
            st.write("Best 3 Game")
            st.table(rd_2016.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2016.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[8]:
            st.subheader('15년도 출시 게임 목록')
            st.dataframe(rd_2015)
            st.write("Best 3 Game")
            st.table(rd_2015.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2015.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[9]:
            st.subheader('14년도 출시 게임 목록')
            st.dataframe(rd_2014)
            st.write("Best 3 Game")
            st.table(rd_2014.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2014.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[10]:
            st.subheader('13년도 출시 게임 목록')
            st.dataframe(rd_2013)
            st.write("Best 3 Game")
            st.table(rd_2013.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2013.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[11]:
            st.subheader('12년도 출시 게임 목록')
            st.dataframe(rd_2012)
            st.write("Best 3 Game")
            st.table(rd_2012.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2012.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[12]:
            st.subheader('11년도 출시 게임 목록')
            st.dataframe(rd_2011)
            st.write("Best 3 Game")
            st.table(rd_2011.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2011.sort_values(by='critic_score', ascending=True).head(3))
        elif sr == order[13]:
            st.subheader('19년도 출시 게임 목록')
            st.dataframe(rd_2010)
            st.write("Best 3 Game")
            st.table(rd_2010.head(3))
            st.write("Worst 3 Game")
            st.table(rd_2010.sort_values(by='critic_score', ascending=True).head(3))
    elif select == choice[5]:
        order = ['슈퍼 마리오', '젤다의 전설', '별의 커비', '포켓몬스터', '어쌔신크리드', '파크라이',
                 '파이널 판타지', '바이오하자드', '콜 오브 듀티', '배틀필드', '소닉', '니드 포 스피드',
                 '피파', '포르자', '파이어 엠블럼', '메가맨', '테트리스', '톰 클랜시 시리즈', '스파이더맨',
                 '몬스터 헌터', '시리즈 게임 통계: 20개 목록']
        sr = st.radio('게임 시리즈를 선택하세요', order, horizontal=True)
        if sr == order[0]:
            st.subheader('게임 시리즈 : 슈퍼 마리오')
            st.dataframe(super_mario)
            st.write("Best Game")
            st.table(super_mario.head(1))
            st.write("Worst Game")
            st.table(super_mario.tail(1))
        elif sr == order[1]:
            st.subheader('게임 시리즈 : 젤다의 전설')
            st.dataframe(legend_of_zelda)
            st.write("Best Game")
            st.table(legend_of_zelda.head(1))
            st.write("Worst Game")
            st.table(legend_of_zelda.tail(1))
        elif sr == order[2]:
            st.subheader('게임 시리즈 : 별의 커비')
            st.dataframe(kirby)
            st.write("Best Game")
            st.table(kirby.head(1))
            st.write("Worst Game")
            st.table(kirby.tail(1))
        elif sr == order[3]:
            st.subheader('게임 시리즈 : 포켓몬스터')
            st.dataframe(pokemon)
            st.write("Best Game")
            st.table(pokemon.head(1))
            st.write("Worst Game")
            st.table(pokemon.tail(1))
        elif sr == order[4]:
            st.subheader('게임 시리즈 : 어쌔신크리드')
            st.dataframe(assassins_creed)
            st.write("Best Game")
            st.table(assassins_creed.head(1))
            st.write("Worst Game")
            st.table(assassins_creed.tail(1))
        elif sr == order[5]:
            st.subheader('게임 시리즈 : 파크라이')
            st.dataframe(far_cry)
            st.write("Best Game")
            st.table(far_cry.head(1))
            st.write("Worst Game")
            st.table(far_cry.tail(1))
        elif sr == order[6]:
            st.subheader('게임 시리즈 : 파이널 판타지')
            st.dataframe(final_fantasy)
            st.write("Best Game")
            st.table(final_fantasy.head(1))
            st.write("Worst Game")
            st.table(final_fantasy.tail(1))
        elif sr == order[7]:
            st.subheader('게임 시리즈 : 바이오하자드')
            st.dataframe(resident_evil)
            st.write("Best Game")
            st.table(resident_evil.head(1))
            st.write("Worst Game")
            st.table(resident_evil.tail(1))
        elif sr == order[8]:
            st.subheader('게임 시리즈 : 콜 오브 듀티')
            st.dataframe(call_of_duty)
            st.write("Best Game")
            st.table(call_of_duty.head(1))
            st.write("Worst Game")
            st.table(call_of_duty.tail(1))
        elif sr == order[9]:
            st.subheader('게임 시리즈 : 배틀필드')
            st.dataframe(battlefield)
            st.write("Best Game")
            st.table(battlefield.head(1))
            st.write("Worst Game")
            st.table(battlefield.tail(1))
        elif sr == order[10]:
            st.subheader('게임 시리즈 : 소닉')
            st.dataframe(sonic)
            st.write("Best Game")
            st.table(sonic.head(1))
            st.write("Worst Game")
            st.table(sonic.tail(1))
        elif sr == order[11]:
            st.subheader('게임 시리즈 : 니드 포 스피드')
            st.dataframe(need_for_speed)
            st.write("Best Game")
            st.table(need_for_speed.head(1))
            st.write("Worst Game")
            st.table(need_for_speed.tail(1))
        elif sr == order[12]:
            st.subheader('게임 시리즈 : 피파')
            st.dataframe(fifa)
            st.write("Best Game")
            st.table(fifa.head(1))
            st.write("Worst Game")
            st.table(fifa.tail(1))
        elif sr == order[13]:
            st.subheader('게임 시리즈 : 포르자')
            st.dataframe(forza)
            st.write("Best Game")
            st.table(forza.head(1))
            st.write("Worst Game")
            st.table(forza.tail(1))
        elif sr == order[14]:
            st.subheader('게임 시리즈 : 파이어 엠블럼')
            st.dataframe(fire_emblem)
            st.write("Best Game")
            st.table(fire_emblem.head(1))
            st.write("Worst Game")
            st.table(fire_emblem.tail(1))
        elif sr == order[15]:
            st.subheader('게임 시리즈 : 메가 맨')
            st.dataframe(mega_man)
            st.write("Best Game")
            st.table(mega_man.head(1))
            st.write("Worst Game")
            st.table(mega_man.tail(1))
        elif sr == order[16]:
            st.subheader('게임 시리즈 : 테트리스')
            st.dataframe(tetris)
            st.write("Best Game")
            st.table(tetris.head(1))
            st.write("Worst Game")
            st.table(tetris.tail(1))
        elif sr == order[17]:
            st.subheader('게임 시리즈 : 톰클랜시')
            st.dataframe(tom_clancys)
            st.write("Best Game")
            st.table(tom_clancys.head(1))
            st.write("Worst Game")
            st.table(tom_clancys.tail(1))
        elif sr == order[18]:
            st.subheader('게임 시리즈 : 스파이더맨')
            st.dataframe(spider_man)
            st.write("Best Game")
            st.table(spider_man.head(1))
            st.write("Worst Game")
            st.table(spider_man.tail(1))
        elif sr == order[19]:
            st.subheader('게임 시리즈 : 몬스터 헌터')
            st.dataframe(monster_hunter)
            st.write("Best Game")
            st.table(monster_hunter.head(1))
            st.write("Worst Game")
            st.table(monster_hunter.tail(1))
        elif sr == order[20]:
            st.subheader('시리즈 게임 통계: 20개 목록')
            order2 = ['평균 점수 기준 정렬', '최고 점수 기준 정렬', '최저 점수 기준 정렬']
            sr2 = st.radio('정렬 기준을 선택', order2, horizontal=True)
            s_list = []
            s_dict = {}
            s_df = pd.DataFrame()
            series_total = data_frame_create(s_list, s_dict, s_df, game_series, order[0:-1])
            if sr2 == order2[0]:
                st.write('시리즈 평균 점수 정렬')
                st.table(series_total.sort_values(by='mean', ascending=False))
            elif sr2 == order2[1]:
                st.write('시리즈 최고 점수 정렬')
                st.table(series_total.sort_values(by='max', ascending=False))
            elif sr2 == order2[2]:
                st.write('시리즈 최저 점수 정렬')
                st.table(series_total.sort_values(by='min', ascending=True))
            

def chart_graph():
    order = ['Critic Score 분포', '점수 별 비율(10점 단위)', '점수 별 비율(by.Mighty Man)',
             '게임 기기 별 비율(진영 별, 기기 별)', '게임 출시 년도 별 비율']
    sr = st.radio('그래프를 선택하세요', order, horizontal=True)
    if sr == order[0]:
        st.subheader('Critic Socre 분포 그래프')
        st.pyplot(critic_hist())
    elif sr == order[1]:
        st.subheader('점수 별 비율 그래프 : 10점 단위')
        st.pyplot(score_rate_piechart())
    elif sr == order[2]:
        st.subheader('점수 별 비율 그래프 : Mighty Man 기준')
        st.pyplot(mighty_piechart())
    elif sr == order[3]:
        st.subheader('기기 별 비율 그래프 : 게임기 진영, 기기 별')
        st.pyplot(platform_piechart())
    elif sr == order[4]:
        st.subheader('게임 출시 년도 별 비율 그래프')
        st.pyplot(release_date_piechart())

'''def search_game_title():
    st.subheader('찾고 싶은 게임 타이틀을 입력하세요')
    stop = 'z'
    title = ''
    while title != stop:
        title = st.text_input('타이틀을 영문으로 입력, 검색 종료는 z')
        if title == 'z':
            break
        else:
            title = str(title)   
            result = critic.game_title.str.contains(title)
            if result.all() == False:
                st.write('일치하는 결과가 없습니다.')
                st.write('다시 검색하세요.')
            else:
                for n in result:
                    if n == True:
                        st.table(show = critic[critic.game_title.str.contains])
                 
    st.write('검색을 종료했습니다.')  '''