from pandas_datareader import data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import fix_yahoo_finance as yf
yf.pdr_override() 

symbol = 'AMZN'
data_source='google'
start_date = '2015-01-01'
end_date = '2016-01-01'

BAC = data.get_data_yahoo('BAC', start_date, end_date)
C = data.get_data_yahoo('C', start_date, end_date)
GS = data.get_data_yahoo('GS', start_date, end_date)
JPM = data.get_data_yahoo('JPM', start_date, end_date)
MS = data.get_data_yahoo('MS', start_date, end_date)
WFC = data.get_data_yahoo('WFC', start_date, end_date)
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],axis=1,keys=tickers)

bank_stocks.columns.names = ['Bank Ticker','Stock Info']

print(bank_stocks.head(3))

pd1=bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()
print(pd1)



returns = pd.DataFrame()


for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()
    
print(returns.head(3))


sns.pairplot(returns[1:])

plt.show()




