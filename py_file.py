import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

r_data=pd.read_table('dailydata.txt')


L=['MMM','AXP', 'BA', 'CAT', 'KO', 'XOM', 'GE', 'IBM', 'JPM', 'MCD', 'MRK', 'PG', 'UTX', 'DIS']

IBM = r_data.loc[r_data['tic'] == "IBM"]
dts = IBM['datadate'].apply(lambda x: dt.datetime.strptime(str(x), '%Y%m%d'))


myTotalReturnIndex_IBM=IBM['prccd']*IBM['trfd']/IBM['ajexdi'] #just IBM
