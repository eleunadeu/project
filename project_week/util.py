import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse

file_name = glob('C:Users/eleun/Documents/project_week/data/*.csv')
total_data = pd.DataFrame()
for file_name in file_name:
    temp = pd.read_csv(file_name, encoding='cp949')
    total_data = pd.concat([total_data, temp])
total_data.to_csv('C:Users/eleun/Documents/project_week/data/total_data.csv')

tdata = pd.read_csv('C:Users/eleun/Documents/project_week/data/total_data.csv')
tdata.drop('Unameed: 0', axis=1, inplace=True)