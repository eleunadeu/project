import streamlit as st
import pandas as pd
from modules import helper
import random
from PIL import Image
from PIL import ImageOps

def load_image(image_path, width=100, height=150):
    img = Image.open(image_path)
    img = ImageOps.fit(img, (width, height), Image.ANTIALIAS)
    return img

def load_dataframe():
    df = pd.read_csv("./data/22_data.csv")
    return df

def app():
    models = helper.load_models()
    df = load_dataframe()

    # Streamlit app
    st.title("선수 역할 예측")

    position = st.sidebar.selectbox("포지션", ["FW", "MF", "DF", "GK"])
    stats = [
        ("goal", "골"),
        ("assist", "도움"),
        ("shot", "슈팅"),
        ("throw_in", "스로인"),
        ("dribble_attempt", "드리블 시도"),
        ("key_pass", "키패스"),
        ("forward_pass", "전방 패스 시도"),
        ("sideways_pass", "횡패스 시도"),
        ("attacking_pass_trial", "공격지역패스 시도"),
        ("defensive_pass_trial", "수비지역패스 시도"),
        ("central_pass_trial", "중앙지역패스 시도"),
        ("long_pass", "롱패스"),
        
        ("short_pass", "숏패스 시도"),
        ("cross", "크로스 시도"),
        ("ground_duels_attempted", "경합 지상 시도"),
        ("aerial_duels_attempted", "경합 공중 시도"),
        ("tackles_attempted", "태클 시도"),
        ("clearing", "클리어링"),
        ("interceptions", "인터셉트"),
        ("blocking", "차단"),
        ("blocks", "블락"),
        ("fouls_committed", "파울"),
        ("fouls_suffered", "피파울"),
    ]

    with st.sidebar:
        player_stats = helper.input_player_stats(stats, position)
        check_button = st.button("확인")
    if check_button:
        # Predict player role
        player_role_prediction, player_role = helper.predict_player_role(position, player_stats, models)
        st.write(player_role_prediction)

        # Filter DataFrame based on predicted role
        filtered_df = df[df["Detailed Role"] == player_role]

        # Get top 3 players with the longest '출전시간' and 5 random players
        top_3_players = filtered_df.nlargest(3, "출전시간")

        # Display images and names of top 3 players with the longest '출전시간'
        st.write("해당역할의 추천 선수입니다.")
        cols = st.columns(3)
        for idx, (index, row) in enumerate(top_3_players.iterrows()):
            image_path = f"./data/picture/{index}.png"
            image = load_image(image_path)
            cols[idx].image(image, caption=row["선수명"])

        # Remove top 3 players with the longest '출전시간' from the filtered DataFrame
        filtered_df = filtered_df.drop(top_3_players.index)

        # Check if there are enough players to sample from
        num_random_players = min(5, len(filtered_df))

        # Sample random players from the filtered DataFrame
        random_players = filtered_df.sample(num_random_players)

        # Display images and names of random players
        st.write("똑같은 유형의 다른 선수는 어떠세요?")
        cols = st.columns(5)
        for idx, (index, row) in enumerate(random_players.iterrows()):
            image_path = f"./data/picture/{index}.png"
            image = load_image(image_path)
            cols[idx].image(image, caption=row["선수명"])
