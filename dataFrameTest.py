from pandas import DataFrame, Series
import pandas as pd
import requests

data = {'open':[100,200], 'high':[110,210]}
df = DataFrame(data)
print(df)

# DataFrame으로 엑셀 만들기
dataList = {'open': [737, 750], 'high': [755, 780], 'low': [700, 710], 'close': [750, 770]}
dataFrame = DataFrame(dataList, index=['2018-01-01', '2018-01-02'])
print(dataFrame)

## DataFrame에 컬럼 추가하기
s = Series([300,400])
df['volume'] = s
print(df)

# 네이버 금융데이터 불러와서 DataFrame으로 만들기
url = 'https://finance.naver.com/item/sise_day.nhn?code=066570'
data = pd.read_html(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text)
print(data[0])

