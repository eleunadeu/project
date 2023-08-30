import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import random
import plotly.express as px 

def load_df():
    df = pd.read_csv('./data/visualize_3.csv', encoding='cp949')

    return df

def player_num(player):
    df = load_df()
    df = df[['Unnamed: 0', '선수명']]
    df.columns = ['index', '선수명']
    player_num = df[df['선수명'] == player].iloc[0, 0]
    return player_num

def table(player_num):
    df = load_df()
    df = df[['선수명', '클럽명', 'Position', 'Role', 'Detailed Role']]
    df.columns = ['선수 이름', '2022년 소속 클럽', '포지션', '역할', '상세역할']
    df1 = df.T
    table = df1.iloc[:, player_num]
    return table



def radar_chart(player_num):
    df = load_df()
    a1 = df.iloc[:, 16:-4]

    cmaps = ['lightcoral', 'orangered', 'olive', 'dodgerblue', 'midnightblue', 'darkviolet', 'deeppink']
    random_cmaps = random.choice(cmaps)

    # 라벨 리스트
    labels = ['SHO', 'DRI', 'LOP', 'SHP', 'TAK', 'PHY', 'SHO']

    # 각 label에 해당하는 값 리스트
    values = a1.iloc[player_num, :]

    # 데이터 개수
    num_labels = len(labels)-1

    # 각 라벨이 놓일 각도를 계산
    angles = np.linspace(0, 2*np.pi, num_labels, endpoint=False)

    # 라벨의 위치 설정
    angles = np.concatenate((angles, [angles[0]]))

    # 데이터의 첫번째 값과 마지막 값이 이어지도록 설정
    values = np.concatenate((values, [values[0]]))

    # 레이더 차트 그리기
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, values, color=random_cmaps, linewidth=1, linestyle='solid')
    ax.fill(angles, values, color=random_cmaps, alpha=0.1)

    # 라벨 텍스트 설정
    ax.set_thetagrids(angles * 180/np.pi, labels, fontsize=20)

    # 각 라벨 위치에 컬럼 이름 표시
    for label, angle in zip(ax.get_xticklabels(), angles):
        if angle == 0:
            label.set_horizontalalignment('center')
        elif 0 < angle < np.pi:
            label.set_horizontalalignment('left')
        else:
            label.set_horizontalalignment('right')
        label.set_rotation(angle * 180/np.pi - 90)

    # 반경 눈금 설정
    ax.set_rlabel_position(0)
    plt.xticks(rotation=90)
    plt.yticks([0, 20, 40, 60, 80, 100], ["0", "20", "40", "60", "80", "100"], color="grey", size=8)

    ax.set_title("Player Stats", fontsize=20)
    ax.grid(True)

    return fig

def barh(player_num):
    df = load_df()
    a2 = df.iloc[:, 4:-10]
    fig=px.bar(a2.iloc[player_num, :], orientation='h')
    
    return fig