from parser import parser
from pandas.io.json import json_normalize
import os
from dotenv import load_dotenv
import requests
import pandas as pd
import matplotlib.pyplot as plt
from func import golfista



if __name__ == "__main__":
    year, first_name, last_name = parser()
    print(f"Year: {year}\nName: {last_name},{first_name}")
    res=golfista(year, last_name, first_name)
    if Year & last_name & first_name:
        print(str(res)[::-1]
        