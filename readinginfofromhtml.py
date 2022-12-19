import pandas as pd
import numpy as np

scrapedData = pd.read_csv("https://football-data.co.uk/mmz4281/2223/E0.csv")

scrapedData.rename(columns={"FTHG":"Home_Goals", "FTAG": "Away_Goals"}, inplace=True)


print(int("010101111000" ,2))