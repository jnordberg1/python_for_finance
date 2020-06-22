# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:26:37 2020

@author: JacobNordberg
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2002, 1,1)
end = dt.datetime(2020, 12,31)
#
df = web.DataReader('DKNG', 'yahoo', start, end)

df.to_csv('DKNG.csv')

df = pd.read_csv('DKNG.csv', parse_dates= True, index_col = 0)

#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods= 0).mean()

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

#converting dates to mdates
df_ohlc.reset_index(inplace = True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
#print(df_ohlc.head())

ax1 = plt.subplot2grid((6, 1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6, 1), (5,0), rowspan = 1, colspan = 1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup = 'g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()

#df['Adj Close'].plot()
#plt.show()