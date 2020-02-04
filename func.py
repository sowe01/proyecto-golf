from pandas.io.json import json_normalize
import os
from dotenv import load_dotenv
import requests
import pandas as pd
import matplotlib.pyplot as plt

import math
import datetime
load_dotenv()



def golfista (year,last_name,first_name):  
    df = pd.read_csv('./rank.csv')
    if df[(df["Season"].float.contains(year))]  & df[(df["last_name"].str.contains(name))] & df[(df["first_name"].str.contains(name))]:
        return df.loc[:, 'Top_10','Events','media_Top10', 'Money']

