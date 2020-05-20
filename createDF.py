import sys
import os
import pandas as pd
import numpy as np

fileName=sys.argv[1]
path='data/'
fileFullPath=path+fileName

data=pd.read_csv(fileFullPath)
data=data[data['symbol']=="XBTUSD"]
data=data.set_index('timestamp')
data.index=pd.to_datetime(data.index,format="%Y-%m-%dD%H:%M:%S.%f")

save=np.array(['size','price'])
remove=np.setdiff1d(data.columns.values,save)
data=data.drop(remove,axis=1)

data['open']=data['price'].copy()
data['high']=data['price'].copy()
data['low']=data['price'].copy()
data['close']=data['price'].copy()
data['volume']=data['size'].copy()
data.drop(['size','price'],axis=1)

aggStrategy={'open':'first','high':'max','low':'min','close':'last','volume':'sum'}
data_1min=data.resample('1Min').agg(aggStrategy)
data_1h=data.resample('1h').agg(aggStrategy)

save_path="candles/1h/"+fileName
data_1h.to_csv(save_path)

save_path="candles/1min/"+fileName
data_1min.to_csv(save_path)