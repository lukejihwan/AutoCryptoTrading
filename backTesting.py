import numpy as np
import pybithumb

df = pybithumb.get_ohlcv('DOGE')
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)
df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'], 1)
ror = df['ror'].cumprod()[-2]
print(ror)

df.to_excel('trade.xlsx')
