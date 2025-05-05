import pybithumb
import time

while True:
    price = pybithumb.get_current_price('BTC')
    df = pybithumb.get_ohlcv('BTC')
    print(price)
    print(df.tail())
    time.sleep(0.2)