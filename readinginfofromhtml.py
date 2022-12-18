import pandas as pd
import numpy as np

scrapedData = pd.read_csv("https://football-data.co.uk/mmz4281/2223/E0.csv")

scrapedData.rename(columns={"FTHG":"Home_Goals", "FTAG": "Away_Goals"}, inplace=True)

num = 5
num = np.binary_repr(5,12)
print(num)
num = int(num, 2)
print(num)