import time

import pybithumb

# ticker목록 뽑기
tickers = pybithumb.get_tickers()
print(len(tickers))

# 특정 가상화폐 가격 출력
price = pybithumb.get_current_price('BTC')
print(price)

# 매초마다 가격 불러오기
while True:
    price = pybithumb.get_current_price('BTC')
    print(price)
    time.sleep(1)

# 모든 가상화폐 가격 불러오기
for ticker in tickers:
    price = pybithumb.get_current_price(ticker)
    print(ticker, price)
    time.sleep(1)


