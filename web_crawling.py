# 아래 모듈은 외장 라이이브러리 이므로, 별도 설치 필요
# 설치를 할때 pip라는 패키지 tool을 이용(python설치시 동시에 pip설치)
# pip install requests
# 만약에 pip --version 때 버전정보가 잘 안나오다면, path가 문제인데
# path를 다시 잡기보다는 python 삭제후 재설치시 add path옵션 추가
import requests
from bs4 import BeautifulStoneSoup

# url = 'https://ko.wikipedia.org/wiki/%EC%95%84%EB%B0%94%ED%83%80:_%EB%AC%BC%EC%9D%98_%EA%B8%B8'

# # 웹으로 주고받는 통신프로토콜 을 http 통신이라 한다.
# # http 통신을 하기 위해서는 http 통신규격에 맞에 request를 서버로 전달해야 한다.
# # request는 header 와 body 로 이루어져있따
# # 마찬가지로 응답 도 header 와 body로 이루어져있다
# header = {'user-Agent' : 'Mozilla/5.0'}
# response = requests.get(url, header=header)
# html_response = BeautifulStoneSoup(response.text, 'html.parser')
# for sup in html_response.find_all('sup'):
#     sup.decompose()
# print(html_response)

# # 감독정보, 제작비 정보
# # tag정보를 가지rh html_response에서 원하는정보 추출
# director_info = html_response.select_one('table.infobox>tbody>tr:nth-oftype(3)>td').get_text()
# budget_info = html_response.select_one('table.infobox>tbody>tr:nth-oftype(16)>td').get_text()
# # print(f"아바타의 감독은 {director_info}이고 제작비는 {budget_info}이다")

# import requests
# from bs4 import BeautifulStoneSoup
# # 코인 시세정보 API url
# import json
# url = "https://api.binance.com/api/v3/ticker/24hr"
# response = requests.get(url)
# data_json = json.loads(response.text)


# # 출력결과
# # "symbol" : "BTCUSDT","lastPrice" : XXXX(가격)
# for a in data_json:
#     if a['symbol'] == "BTCUSDT":
#         print(f"{a['symbol']}코인의 price는 {a['lastPrice']}입니다")



# csv 파일 parsing 
import seaborn
from matplotlib import pyplot
import pandas

file_path = r'C:\Users\User\Desktop\김명남\tips.csv'
csv_data = pandas.read_csv(file_path)

# 성별에 따라 tip 어떻게 달라지는지
# day에 따라 tip 이 어떻게 달라지는지
# agg : 집계함수, mean: 평균, std : 표준편차
tip_by_gender = csv_data.groupby('gender')['tip'].agg(['mean','std']).reset_index()
# tip_by_gender = csv_data.groupby('day')['tip'].agg(['mean','std']).reset_index()

seaborn.barplot(x='gender',y='mean', data= tip_by_gender, yerr=tip_by_gender['mean'], capsize= 0.1)
seaborn.despine() # 테두리 없애주는 함수
pyplot.title('average tip per gender')
pyplot.xlabel('gender')
pyplot.ylabel('average tip')
pyplot.show()