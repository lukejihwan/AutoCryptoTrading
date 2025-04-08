import pybithumb
import datetime

orderbook = pybithumb.get_orderbook('BTC')
print(orderbook)

for k in orderbook:
    print(k)

print(orderbook['payment_currency'])
print(orderbook['order_currency'])
ms = int(orderbook['timestamp'])
dt = datetime.datetime.fromtimestamp(ms/1000)
print(dt)

all = pybithumb.get_current_price('ALL')
for ticker, data in all.items():
    print(ticker, data['closing_price'])
