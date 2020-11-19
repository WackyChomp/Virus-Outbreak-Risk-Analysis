

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



def get_data(ticker):        #function 1
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