import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

start = dt.datetime(2020, 1, 1)
end = dt.datetime.now()

tickers = ['AAPL', 'NVDA', 'GS', 'TSLA', 'T', 'BAC', 'CCL']
colnames = []

for ticker in tickers:
    data = web.DataReader(ticker, 'yahoo', start, end)
    if len(colnames) == 0:
        combined = data[['Adj Close']].copy()
    else:
        combined = combined.join(data['Adj Close'])
    colnames.append(ticker)
    combined.columns = colnames

corr_data = combined.pct_change().corr(method='pearson')
sns.heatmap(corr_data, annot=True, cmap='winter')
plt.title('Stock Correlation Map')
plt.show()