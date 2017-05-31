# -*- coding: utf-8 -*-
"""
Created on Tue May 30 16:26:35 2017

@author: Fitec
"""

import pandas as pd
#from pandas_datareader import data, wb   # Package and modules for importing data; this code may change depending on pandas version
import datetime
import pandas_datareader.data as web
# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
end = datetime.date.today()
#dir(wb) 
# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
#Data1=pd.read_csv('C://Users//Fitec//Desktop//prices//S&Psymbols.csv')
Data1=pd.read_csv('C://Users//Fitec//Desktop//prices//nasdaq//companylist.csv')
symbollist=Data1['Symbol']

start = datetime.datetime(2016,1,1)
end = datetime.date.today()
for i in  symbollist:
    try:
        temp = web.DataReader(i,"google", start, end)
        temp.to_csv(i+'.csv')
    except:
        pass