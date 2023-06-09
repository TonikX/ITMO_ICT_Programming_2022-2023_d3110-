
import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/subject/1300374/'

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36' }
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 电影名称
movie_title = soup.select_one('h1 > span').text
# 电影简介
movie_summary2 = soup.select_one('div.indent span[property="v:summary"]').text

print('电影名称：', movie_title)
print('电影简介：', movie_summary2)
with open('thegreenmile.txt', 'w',encoding='utf-8') as f:
    f.write('电影名称：'+movie_title+'\n')
    f.write('电影简介：'+movie_summary2)
