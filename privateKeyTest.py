import pybithumb
import time

# Set API parameters
con_key = ''
sec_key = ''

bithumb = pybithumb.Bithumb(con_key, sec_key)

for ticker in pybithumb.get_tickers():
    balance = bithumb.get_balance(ticker)
    print(ticker, ":", balance)
    time.sleep(0.1)
    print(format(balance[0], 'f'))

# 지정가 매수하는 법
order = bithumb.buy_limit_order('BTC', 130000000, 0.001)
print(order)

