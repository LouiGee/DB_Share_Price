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

def GSshareprice(inputStart, inputEnd): 
    
    style.use('ggplot')
    
    #Format Input dates
    start = datetime.strptime(inputStart, '%d/%m/%Y')
    end = datetime.strptime(inputEnd, '%d/%m/%Y')
   
    #Access Yahoo API
    df = web.DataReader("GS", 'yahoo', start, end)
    df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
    
    #Intialise plots
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1,)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
    
    #Plot the data
    ax1.plot(df.index, df['Adj Close'])
    ax1.plot(df.index, df['100ma'])
    ax2.bar(df.index, df['Volume'])
    
    #Show the data
    plt.show()
    
    
GSshareprice('01/01/2001', '01/01/2017')



