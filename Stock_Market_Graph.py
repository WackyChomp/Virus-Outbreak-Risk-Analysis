

#!/usr/bin/python
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd                            #pd, np are both alias = easier to reference
import numpy as np
from datetime import datetime				#previously not working

START_DATE = '2007-10-01'      #around the time of the Great Depression

END_DATE = str(datetime.now().strftime('%Y-%m-%d'))        
#currently using '2020-05-15'     			alternative: str(datetime.now().strftime('%Y-%m-%d))


#four functions 
#1) gets data
#2) cleans data
#3) creates plot/ graph
#4) basic stats about the stock


#function 1: collect data
def get_data(ticker):
	try:
		stock_data = data.DataReader(ticker,
						'yahoo',
						START_DATE,
						END_DATE)
		adj_close = clean_data(stock_data, 'Adj Close')           #adjusted close
		create_plot(adj_close, ticker)

	except RemoteDataError:
		print("No data available for {t}".format(t = ticker))

#-------------------------------------------------#

#function 2: cleaning data
#collect weekday data and ignores weekend data
def clean_data(stock_data, col):
	weekdays = pd.date_range(start = START_DATE , end = END_DATE)
	clean_data = stock_data[col].reindex(weekdays)
	return clean_data.fillna(method = 'ffill')        
    
    #ffill is used to fill missing value with the next/foward data


#-------------------------------------------------#


