#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:42:54 2019

@author: LuisGoate
"""

 import datetime as dt
 import matplotlib.pyplot as plt
 from matplotlib import style
 import pandas as pd
 import pandas_datareader.data as web

def DBshareprice(y1,m1,d1,y2,m2,d2):    
    style.use('ggplot')
    
    start = dt.datetime(y1, m1, d1)
    end = dt.datetime(y2, m2, d2)
    
    df = web.DataReader("DBK.DE", 'yahoo', start, end)
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
    
    ax1.plot(df.index, df['Adj Close'])
    ax1.plot(df.index, df['100ma'])
    ax2.bar(df.index, df['Volume'])
    
    plt.show()
    
    
DBshareprice(2001,1,1,2017,1,1)



