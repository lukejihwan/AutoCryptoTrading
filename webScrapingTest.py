import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text
soup = BeautifulSoup(html, "html5lib")
# 어떤 값을 어떻게 가져와야 할지 모르겠다면 css 셀렉터를 사용해서 아래와 같이 사용해보자
tags = soup.select("#tab_con1 > div:nth-child(4) > table > tbody > tr:nth-child(2) > td > em:nth-child(1)")

for tag in tags:
    print(tag.text)