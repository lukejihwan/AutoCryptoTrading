import pybithumb
import time

# 파이썬에서 예외처리하는 법
while True:
    price = pybithumb.get_current_price('BTC')
    try:
        print(price/10)
    except:
        print('에러발생', price)
    time.sleep(0.2)

