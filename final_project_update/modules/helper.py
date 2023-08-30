import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import streamlit as st
import numpy as np

def load_models():
    models = {}
    with open("./data/random_forest_classifier_model_FW_2.pkl", "rb") as f:
        models["FW"] = pickle.load(f)
    with open("./data/gradient_boosting_classifier_model_MF_2.pkl", "rb") as f:
        models["MF"] = pickle.load(f)
    with open("./data/gradient_boosting_classifier_model_DF_2.pkl", "rb") as f:
        models["DF"] = pickle.load(f)
    with open("./data/random_forest_classifier_model_GK_1.pkl", "rb") as f:
        models["GK"] = pickle.load(f)
    return models

def predict_player_role(position, player_stats, models):
    if position != "GK":
        model = models[position]
        player_role = model.predict([player_stats])[0]
        return f"선수의 예측된 역할: {player_role}", player_role
    else:
        model = models[position]
        player_role = model.predict([player_stats])[0]
        return f"선수의 예측된 역할: {player_role}", player_role

def input_player_stats(stats, position):
    player_stats_raw = [st.number_input(label, value=0, step=1, format="%d") for _, label in stats]

    player_stats = []
    if position == "GK":
        stats_to_square = ['forward_pass', 'defensive_pass_trial', 'long_pass']
        for stat_name, stat in zip([x[0] for x in stats], player_stats_raw):
            if stat_name in stats_to_square:
                player_stats.append(stat ** 2)
            else:
                player_stats.append(np.sqrt(stat))
    else:
        for stat in player_stats_raw:
            player_stats.append(np.sqrt(stat))

    return player_stats