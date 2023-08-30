import streamlit as st
import pandas as pd
import random
import os
from PIL import Image
from PIL import ImageOps

def load_image(image_path, width=100, height=150):
    img = Image.open(image_path)
    img = ImageOps.fit(img, (width, height), Image.ANTIALIAS)
    return img

# Import the CSV file as a dataframe
df = pd.read_csv('./data/22_data.csv')
df_1 = pd.read_excel('./data/combined_data_2.xlsx')


def app():
    st.title("선호 역할 추천 시스템")
    st.subheader("선호하는 역할이 없을 시 설문 조사를 통해 역할을 추천해줍니다.")

    position = st.selectbox("축구에서 어떤 포지션을 선호하십니까?", ["", "Attacker", "Midfielder", "Defender", "Goalkeeper"])

    if position == "Attacker":
        attacker_type = st.selectbox("어떤 공격 포지션을 선호하십니까?", ["", "Central Attacker", "Wide Attacker"])

        if attacker_type == "Central Attacker":
            goal_preference = st.selectbox("골 넣는것을 좋아하십니까?", ["", "Yes", "골 넣는 것에는 관심이 없습니다."])

            if goal_preference == "Yes":
                spotlight_preference = st.selectbox("주목 받는 것을 좋아 하십니까?", ["", "Yes", "No"])

                if spotlight_preference == "Yes":
                    st.write("당신에게는 Target을 추천드립니다.")

                    # Filter DataFrame based on predicted role
                    filtered_df = df[df["Detailed Role"] == "Target"]

                    # Get top 3 players with the longest '출전시간' and 5 random players
                    top_3_players = filtered_df.nlargest(3, "출전시간")
                    st.write("해당역할의 추천 선수입니다.")
                    # Display the top 3 target players' names and images
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

                    st.write("똑같은 유형의 다른 선수는 어떠세요?")
                    # Display the random 5 target players' names and images
                    cols = st.columns(5)
                    for idx, (index, row) in enumerate(random_players.iterrows()):
                        image_path = f"./data/picture/{index}.png"
                        image = load_image(image_path)
                        cols[idx].image(image, caption=row["선수명"])

                elif spotlight_preference == "No":
                    st.write("당신에게는 Finisher를 추천드립니다.")

                    # Filter DataFrame based on predicted role
                    filtered_df = df[df["Detailed Role"] == "Finisher"]

                    # Get top 3 players with the longest '출전시간' and 5 random players
                    top_3_players = filtered_df.nlargest(3, "출전시간")
                    st.write("해당역할의 추천 선수입니다.")
                    # Display the top 3 target players' names and images
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

                    st.write("똑같은 유형의 다른 선수는 어떠세요?")
                    # Display the random 5 target players' names and images
                    cols = st.columns(5)
                    for idx, (index, row) in enumerate(random_players.iterrows()):
                        image_path = f"./data/picture/{index}.png"
                        image = load_image(image_path)
                        cols[idx].image(image, caption=row["선수명"])

            elif goal_preference == "골 넣는 것에는 관심이 없습니다.":
                st.write("당신에게는 Roamer를 추천드립니다.")

                # Filter DataFrame based on predicted role
                filtered_df = df[df["Detailed Role"] == "Roamer"]

                # Get top 3 players with the longest '출전시간' and 5 random players
                top_3_players = filtered_df.nlargest(3, "출전시간")
                st.write("해당역할의 추천 선수입니다.")
                # Display the top 3 target players' names and images
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

                st.write("똑같은 유형의 다른 선수는 어떠세요?")
                # Display the random 5 target players' names and images
                cols = st.columns(5)
                for idx, (index, row) in enumerate(random_players.iterrows()):
                    image_path = f"./data/picture/{index}.png"
                    image = load_image(image_path)
                    cols[idx].image(image, caption=row["선수명"])

        elif attacker_type == "Wide Attacker":
            individual_ability = st.selectbox("화려한 개인기를 가지고 있다고 생각하십니까?", ["", "Yes", "No"])

            if individual_ability == "Yes":
                assist_preference = st.selectbox("어시스트가 멋있다고 생각하십니까?", ["", "Yes", "No"])

                if assist_preference == "Yes":
                    st.write("당신에게는 Wide Threat을 추천드립니다.")

                    # Filter DataFrame based on predicted role
                    filtered_df = df[df["Detailed Role"] == "Wide Threat"]

                    # Get top 3 players with the longest '출전시간' and 5 random players
                    top_3_players = filtered_df.nlargest(3, "출전시간")
                    st.write("해당역할의 추천 선수입니다.")
                    # Display the top 3 target players' names and images
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

                    st.write("똑같은 유형의 다른 선수는 어떠세요?")
                    # Display the random 5 target players' names and images
                    cols = st.columns(5)
                    for idx, (index, row) in enumerate(random_players.iterrows()):
                        image_path = f"./data/picture/{index}.png"
                        image = load_image(image_path)
                        cols[idx].image(image, caption=row["선수명"])
                
                elif assist_preference == "No":
                    st.write("당신에게는 Outlet을 추천드립니다.")

                    # Filter DataFrame based on predicted role
                    filtered_df = df[df["Detailed Role"] == "Outlet"]

                    # Get top 3 players with the longest '출전시간' and 5 random players
                    top_3_players = filtered_df.nlargest(3, "출전시간")
                    st.write("해당역할의 추천 선수입니다.")
                    # Display the top 3 target players' names and images
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

                    st.write("똑같은 유형의 다른 선수는 어떠세요?")
                    # Display the random 5 target players' names and images
                    cols = st.columns(5)
                    for idx, (index, row) in enumerate(random_players.iterrows()):
                        image_path = f"./data/picture/{index}.png"
                        image = load_image(image_path)
                        cols[idx].image(image, caption=row["선수명"])
            
            elif individual_ability == "No":
                st.write("당신에게는 Unlocker를 추천드립니다.")

                # Filter DataFrame based on predicted role
                filtered_df = df[df["Detailed Role"] == "Unlocker"]

                # Get top 3 players with the longest '출전시간' and 5 random players
                top_3_players = filtered_df.nlargest(3, "출전시간")
                st.write("해당역할의 추천 선수입니다.")
                # Display the top 3 target players' names and images
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

                st.write("똑같은 유형의 다른 선수는 어떠세요?")
                # Display the random 5 target players' names and images
                cols = st.columns(5)
                for idx, (index, row) in enumerate(random_players.iterrows()):
                    image_path = f"./data/picture/{index}.png"
                    image = load_image(image_path)
                    cols[idx].image(image, caption=row["선수명"])
    
    elif position == "Midfielder":
        midfielder_type = st.selectbox("당신은 어떤 미드필더에 관심이 있으십니까?", ["", "Advanced Midfielder", "Deep Midfielder"])

        if midfielder_type == "Advanced Midfielder":
            spotlight_preference = st.selectbox("주목 받는 것을 좋아 하십니까?", ["", "Yes", "No"])

            if spotlight_preference == "Yes":
                st.write("당신에게는 Box crasher를 추천드립니다.")

                # Filter DataFrame based on predicted role
                filtered_df = df[df["Detailed Role"] == "Box crasher"]

                # Get top 3 players with the longest '출전시간' and 5 random players
                top_3_players = filtered_df.nlargest(3, "출전시간")
                st.write("해당역할의 추천 선수입니다.")
                # Display the top 3 target players' names and images
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

                st.write("똑같은 유형의 다른 선수는 어떠세요?")
                # Display the random 5 target players' names and images
                cols = st.columns(5)
                for idx, (index, row) in enumerate(random_players.iterrows()):
                    image_path = f"./data/picture/{index}.png"
                    image = load_image(image_path)
                    cols[idx].image(image, caption=row["선수명"])

            elif spotlight_preference == "No":
                st.write("당신에게는 Creator를 추천드립니다.")

                # Filter DataFrame based on predicted role
                filtered_df = df[df["Detailed Role"] == "Creator"]

                # Get top 3 players with the longest '출전시간' and 5 random players
                top_3_players = filtered_df.nlargest(3, "출전시간")
                st.write("해당역할의 추천 선수입니다.")
                # Display the top 3 target players' names and images
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

                st.write("똑같은 유형의 다른 선수는 어떠세요?")
                # Display the random 5 target players' names and images
                cols = st.columns(5)
                for idx, (index, row) in enumerate(random_players.iterrows()):
                    image_path = f"./data/picture/{index}.png"
                    image = load_image(image_path)
                    cols[idx].image(image, caption=row["선수명"])
        
        elif midfielder_type == "Deep Midfielder":
            good_stamina = st.selectbox("체력이 좋으십니까?", ["", "Yes", "No"]) # Box to Box, Builder

            if good_stamina == "Yes":
                all_round_preference = st.selectbox("수비와 공격 둘다 참여하고 싶으십니까?", ["", "Yes", "No"])

                if all_round_preference == "Yes":
                    st.write("당신에게는 Box to Box를 추천드립니다.")

                        # Filter DataFrame based on predicted role
                    filtered_df = df[df["Detailed Role"] == "Box to Box"]

                    # Get top 3 players with the longest '출전시간' and 5 random players
                    top_3_players = filtered_df.nlargest(3, "출전시간")
                    st.write("해당역할의 추천 선수입니다.")
                    # Display the top 3 target players' names and images
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

                    st.write("똑같은 유형의 다른 선수는 어떠세요?")
                    # Display the random 5 target players' names and images
                    cols = st.columns(5)
                    for idx, (index, row) in enumerate(random_players.iterrows()):
                        image_path = f"./data/picture/{index}.png"
                        image = load_image(image_path)
                        cols[idx].image(image, caption=row["선수명"])

                elif all_round_preference == "No":
                    st.write("당신에게는 Builder를 추천드립니다.")

                        # Filter DataFrame based on predicted role
                    filtered_df = df[df["Detailed Role"] == "Builder"]

                    # Get top 3 players with the longest '출전시간' and 5 random players
                    top_3_players = filtered_df.nlargest(3, "출전시간")
                    st.write("해당역할의 추천 선수입니다.")
                    # Display the top 3 target players' names and images
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

                    st.write("똑같은 유형의 다른 선수는 어떠세요?")
                    # Display the random 5 target players' names and images
                    cols = st.columns(5)
                    for idx, (index, row) in enumerate(random_players.iterrows()):
                        image_path = f"./data/picture/{index}.png"
                        image = load_image(image_path)
                        cols[idx].image(image, caption=row["선수명"])

            elif good_stamina == 'No':
                st.write("당신에게는 Distributor를 추천드립니다.")

                # Filter DataFrame based on predicted role
                filtered_df = df[df["Detailed Role"] == "Distributor"]

                # Get top 3 players with the longest '출전시간' and 5 random players
                top_3_players = filtered_df.nlargest(3, "출전시간")
                st.write("해당역할의 추천 선수입니다.")
                # Display the top 3 target players' names and images
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

                st.write("똑같은 유형의 다른 선수는 어떠세요?")
                # Display the random 5 target players' names and images
                cols = st.columns(5)
                for idx, (index, row) in enumerate(random_players.iterrows()):
                    image_path = f"./data/picture/{index}.png"
                    image = load_image(image_path)
                    cols[idx].image(image, caption=row["선수명"])                                    

    elif position == "Defender":
        defender_type = st.selectbox("당신은 어떤 수비수를 선호하십니까?", ["", "Central Defender", "Wide Defender"])

        if defender_type == "Central Defender": #Spreader Aggressor SCB
            meticulous_degree = st.selectbox("꼼꼼하다고 생각하십니까?", ["", "Yes", "No"])

            if meticulous_degree == "Yes":
                st.write("당신에게는 Aggressor를 추천드립니다.")

                # Filter DataFrame based on predicted role
                filtered_df = df[df["Detailed Role"] == "Aggressor"]

                # Get top 3 players with the longest '출전시간' and 5 random players
                top_3_players = filtered_df.nlargest(3, "출전시간")
                st.write("해당역할의 추천 선수입니다.")
                # Display the top 3 target players' names and images
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

                st.write("똑같은 유형의 다른 선수는 어떠세요?")
                # Display the random 5 target players' names and images
                cols = st.columns(5)
                for idx, (index, row) in enumerate(random_players.iterrows()):
                    image_path = f"./data/picture/{index}.png"
                    image = load_image(image_path)
                    cols[idx].image(image, caption=row["선수명"])                                
    
            elif meticulous_degree == "No":
                fast_judgement = st.selectbox("빠른 판단력을 가지고 있다고 생각하십니까?", ["", "Yes", "No"])

                if fast_judgement == "Yes":
                    st.write("당신에게는 Spreader를 추천드립니다.")

                    # Filter DataFrame based on predicted role
                    filtered_df = df[df["Detailed Role"] == "Spreader"]

                    # Get top 3 players with the longest '출전시간' and 5 random players
                    top_3_players = filtered_df.nlargest(3, "출전시간")
                    st.write("해당역할의 추천 선수입니다.")
                    # Display the top 3 target players' names and images
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

                    st.write("똑같은 유형의 다른 선수는 어떠세요?")
                    # Display the random 5 target players' names and images
                    cols = st.columns(5)
                    for idx, (index, row) in enumerate(random_players.iterrows()):
                        image_path = f"./data/picture/{index}.png"
                        image = load_image(image_path)
                        cols[idx].image(image, caption=row["선수명"])     

                elif fast_judgement == "No":
                    st.write("당신에게는 SCB를 추천드립니다.")

                    # Filter DataFrame based on predicted role
                    filtered_df = df[df["Detailed Role"] == "SCB"]

                    # Get top 3 players with the longest '출전시간' and 5 random players
                    top_3_players = filtered_df.nlargest(3, "출전시간")
                    st.write("해당역할의 추천 선수입니다.")
                    # Display the top 3 target players' names and images
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

                    st.write("똑같은 유형의 다른 선수는 어떠세요?")
                    # Display the random 5 target players' names and images
                    cols = st.columns(5)
                    for idx, (index, row) in enumerate(random_players.iterrows()):
                        image_path = f"./data/picture/{index}.png"
                        image = load_image(image_path)
                        cols[idx].image(image, caption=row["선수명"])     

        elif defender_type == "Wide Defender": #Overlapper Progressor Safety
            meticulous_degree = st.selectbox("꼼꼼하다고 생각하십니까?", ["", "Yes", "No"])

            if meticulous_degree == "Yes":
                st.write("당신에게는 Safety를 추천드립니다.")

                # Filter DataFrame based on predicted role
                filtered_df = df[df["Detailed Role"] == "Safety"]

                # Get top 3 players with the longest '출전시간' and 5 random players
                top_3_players = filtered_df.nlargest(3, "출전시간")
                st.write("해당역할의 추천 선수입니다.")
                # Display the top 3 target players' names and images
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

                st.write("똑같은 유형의 다른 선수는 어떠세요?")
                # Display the random 5 target players' names and images
                cols = st.columns(5)
                for idx, (index, row) in enumerate(random_players.iterrows()):
                    image_path = f"./data/picture/{index}.png"
                    image = load_image(image_path)
                    cols[idx].image(image, caption=row["선수명"]) 

            elif meticulous_degree == "No":
                good_stamina = st.selectbox("체력이 좋다고 생각하십니까?", ["", "Yes", "No"])
       
                if good_stamina == "Yes":
                    st.write("당신에게는 Progressor를 추천드립니다.")

                    # Filter DataFrame based on predicted role
                    filtered_df = df[df["Detailed Role"] == "Progressor"]

                    # Get top 3 players with the longest '출전시간' and 5 random players
                    top_3_players = filtered_df.nlargest(3, "출전시간")
                    st.write("해당역할의 추천 선수입니다.")
                    # Display the top 3 target players' names and images
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

                    st.write("똑같은 유형의 다른 선수는 어떠세요?")
                    # Display the random 5 target players' names and images
                    cols = st.columns(5)
                    for idx, (index, row) in enumerate(random_players.iterrows()):
                        image_path = f"./data/picture/{index}.png"
                        image = load_image(image_path)
                        cols[idx].image(image, caption=row["선수명"]) 

                elif good_stamina == "No":
                    st.write("당신에게는 Overlapper를 추천드립니다.")

                    # Filter DataFrame based on predicted role
                    filtered_df = df_1[df_1["Detailed Role"] == "Overlapper"]

                    # Get top 3 players with the longest '출전시간' and 5 random players
                    top_3_players = filtered_df.nlargest(3, "출전시간")
                    st.write("해당역할의 추천 선수입니다.")
                    # Display the top 3 target players' names and images
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

                    st.write("똑같은 유형의 다른 선수는 어떠세요?")
                    # Display the random 5 target players' names and images
                    cols = st.columns(5)
                    for idx, (index, row) in enumerate(random_players.iterrows()):
                        image_path = f"./data/picture/{index}.png"
                        image = load_image(image_path)
                        cols[idx].image(image, caption=row["선수명"]) 


    elif position == "Goalkeeper":
        activation_degree = st.selectbox("골키퍼 역할 이상으로 경기에 적극적으로 참여하고 싶으십니까?", ["", "Yes", "No"])

        if activation_degree == "Yes":
            st.write("당신에게는 Swiper goalkeeper를 추천드립니다.")

    # Filter DataFrame based on predicted role
            filtered_df = df_1[df_1["Detailed Role"] == "Swiper goalkeeper"]

            # Get top 3 players with the longest '출전시간' and 5 random players
            top_3_players = filtered_df.nlargest(3, "출전시간")
            st.write("해당역할의 추천 선수입니다.")
            # Display the top 3 target players' names and images
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

            st.write("똑같은 유형의 다른 선수는 어떠세요?")
            # Display the random 5 target players' names and images
            cols = st.columns(5)
            for idx, (index, row) in enumerate(random_players.iterrows()):
                image_path = f"./data/picture/{index}.png"
                image = load_image(image_path)
                cols[idx].image(image, caption=row["선수명"])

        elif activation_degree == "No":
            st.write("당신에게는 Goalkeeper를 추천드립니다.")

            filtered_df = df_1[df_1["Detailed Role"] == "Goalkeeper"]

            # Get top 3 players with the longest '출전시간' and 5 random players
            top_3_players = filtered_df.nlargest(3, "출전시간")
            st.write("해당역할의 추천 선수입니다.")
            # Display the top 3 target players' names and images
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

            st.write("똑같은 유형의 다른 선수는 어떠세요?")
            # Display the random 5 target players' names and images
            cols = st.columns(5)
            for idx, (index, row) in enumerate(random_players.iterrows()):
                image_path = f"./data/picture/{index}.png"
                image = load_image(image_path)
                cols[idx].image(image, caption=row["선수명"])


if __name__ == "__main__":
    app()