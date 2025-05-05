import os
import time
import pybithumb
import datetime

from dotenv import load_dotenv

load_dotenv()

def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * 0.5
    return target

def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(window=5).mean()
    return ma[-2]

now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

# 상승장인지 체크
ma5 = get_yesterday_ma5('BTC')
target_price = get_target_price('BTC')

# private API 설정
con_key = os.getenv('con_key')
sec_key = os.getenv('secret_key')

bithumb = pybithumb.Bithumb(con_key, sec_key)

while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.timedelta(seconds=10):
            target_price = get_target_price('BTC')
            mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
            ma5 = get_yesterday_ma5('BTC')

        current_price = pybithumb.get_current_price('BTC')

        if current_price > target_price:
            krw = bithumb.get_balance('BTC')[2]
            orderbook = pybithumb.get_orderbook('BTC')
            sell_price = orderbook['asks'][0]['price']
            unit = krw/float(sell_price)
            bithumb.buy_market_order('BTC', unit)
    except:
        print('에러발생')
    time.sleep(1)

