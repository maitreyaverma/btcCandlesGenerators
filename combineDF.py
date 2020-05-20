import os
import pandas as pd
path='candles/1h/'
days=os.listdir(path)
days.sort()
days=[path+x for x in days]
combined=pd.concat([pd.read_csv(x) for x in days])
combined=combined.set_index('timestamp')
combined.to_csv('1hCombined.csv')
