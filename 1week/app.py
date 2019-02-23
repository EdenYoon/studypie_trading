import pandas as pd
import matplotlib.pyplot as plt

sp_index = pd.read_csv('data/s&p_index.csv')
print(f'평균: {sp_index["S&P 500 COMPOSITE - PRICE INDEX"].mean()}')
print(f'표준편차: {sp_index["S&P 500 COMPOSITE - PRICE INDEX"].std()}')

plt.rcParams["figure.figsize"] = (50, 10)
plt.xticks(rotation='vertical')

plt.plot(sp_index['Date'], sp_index['S&P 500 COMPOSITE - PRICE INDEX'])
plt.savefig('s&p_index.png')
