# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:14:27 2020

@author: JacobNordberg
"""
import os
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import bs4 as bs
import pickle
import requests
import time
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')


stock_dfs = r'C:\Users\\Documents\GitHub\python_for_finance\Stock Analysis\interested_dfs'

print ("Start time:")
starttime = (dt.datetime.now())

print (starttime)
"""
This function scrapes S&P 500 tickers from wikipedia and pickles them for use later.
"""

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'id':'constituents'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.find('td').text.strip()
        tickers.append(ticker)
    with open("sp500ticker.pickle", "wb") as f:
        pickle.dump(tickers, f)
    print(tickers)
    return tickers



        