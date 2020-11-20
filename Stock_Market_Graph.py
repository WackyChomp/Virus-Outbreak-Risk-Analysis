

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
#3) basic stats about the stock
#4) creates plot/ graph


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

#function 3: collect basic statistics
#stats are used for the graph visual
def get_stats(stock_data):
	return {
		'last': np.mean(stock_data.tail(1)),
		'short_mean': np.mean(stock_data.tail(30)),           #last 30 days
		'long_mean': np.mean(stock_data.tail(200)),         #last 200 days
		'short_rolling': stock_data.rolling(window = 30).mean(),
		'long_rolling': stock_data.rolling(window = 200).mean(),
	}

#-------------------------------------------------#

#function 4: creating the graph visual
def create_plot(stock_data, ticker):
	stats = get_stats(stock_data)
	plt.style.use('dark_background')        #change color of background
	plt.subplots(figsize = (12,8)),
	plt.plot(stock_data, label = ticker)
	plt.plot(stats['short_rolling'], label = '30 day rolling mean')
	plt.plot(stats['long_rolling'], label = '200 day rolling mean')
	plt.xlabel('Date')
	plt.ylabel('Adj Close (p)')             #keeps price constant 
	plt.legend()      #box shows what the lines represent (similar to a map)
	plt.title('Stock Prices over Time')
	plt.show()

USA_STOCK = 'AMZN'
get_data(USA_STOCK)