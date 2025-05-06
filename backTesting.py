import numpy as np
import pybithumb

# k값 조정
def get_ror(k=0.5):
    df = pybithumb.get_ohlcv('BTC')
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032

    df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)
    ror = df['ror'].cumprod()[-2]
    return ror

for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))


# df = pybithumb.get_ohlcv('BTC')
# df['range'] = (df['high'] - df['low']) * 0.5
# df['target'] = df['open'] + df['range'].shift(1)
#
# fee = 0.0032
# df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'] - fee, 1)
# ror = df['ror'].cumprod()[-2]
# print(ror)
# # 수수료 및 슬리피지 계산하기
#
# df.to_excel('trade.xlsx')
