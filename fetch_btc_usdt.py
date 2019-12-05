import requests
import pandas as pd
from datetime import datetime,timedelta

base_url = "https://public.coindcx.com/market_data/candles?pair={}&interval={}&startTime={}&endTime={}&limit={}"

pair='B-BTC_USDT'
interval='5m'

ts='2019-09-01 00:00:00'


startTime=datetime.strptime(ts,'%Y-%m-%d %H:%M:%S')
df=pd.DataFrame()
for i in range(30):
    endTime=startTime+timedelta(seconds=24*60*60*3-1)
    Ts=int(startTime.timestamp()*1000)
    Te=int(endTime.timestamp()*1000)
    url = base_url.format(pair, interval, Ts, Te,1000)
    df=df.append(pd.DataFrame(requests.get(url).json()))

    print(startTime,endTime)
    startTime=startTime+timedelta(seconds=24*60*60*3)

