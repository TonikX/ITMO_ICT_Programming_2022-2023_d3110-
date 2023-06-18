import requests
import lxml
from bs4 import BeautifulSoup
import parsel
import re
for page in range(1,5):
    print("************第{}页正在保存**********".format(page))
    url = 'https://www.guazi.com/gy/dazhong/o{}/#bread'.format(page)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
               'Cookie':'uuid=3bfbeb56-9f3e-4d0d-cbe3-260b14154476; cityDomain=gy; ganji_uuid=2943330065231720816366; lg=1; antipas=z6683504k93003WPO325643r3; clueSourceCode=%2A%2300; user_city_id=36; sessionid=c1cf6d12-f864-40c1-be6a-689466580011; close_finance_popup=2020-07-27; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22seo_baidu%22%2C%22ca_n%22%3A%22default%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22display_finance_flag%22%3A%22-%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%223bfbeb56-9f3e-4d0d-cbe3-260b14154476%22%2C%22ca_city%22%3A%22gy%22%2C%22sessionid%22%3A%22c1cf6d12-f864-40c1-be6a-689466580011%22%7D; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1595389723,1595834426,1595834461; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; preTime=%7B%22last%22%3A1595835397%2C%22this%22%3A1595389721%2C%22pre%22%3A1595389721%7D; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1595835398'}
    response =requests.get(url,headers=headers).content.decode()
    # print(response)


    soup = BeautifulSoup(response,'lxml')
    title_list = soup.find_all('div')
    # title_list = title_list.find_all('p')
    li_list = soup.find('ul',{'class':'carlist clearfix js-top'})
    print(title_list)

    with open(r'python.csv', 'a', encoding='utf-8')as f:
        print(li_list)
        for i in li_list:
            title = i.find('h2',{'class':"t"}).get_text()
            film_title = re.sub(r' ', '', title).split(' ')
            print(film_title)
            data = i.find('div',{'class':'t-i'}).get_text()
            film_data = re.sub(r'|', '', data).split('|')
            # print(film_data)

            year = film_data[0]
            print(year)
            lc = film_data[1]
            print(lc)

            shoujia = i.find('div',{'class':'t-price'}).find('p').get_text()
            print(shoujia)
            try:
                yuanjia = i.find('div',{'class':'t-price'}).find('em').get_text()
                print(yuanjia)
            except AttributeError:
                yuanjia = ''
            f.write('{},{},{},{},{}\n'.format(film_title,year,lc,shoujia,yuanjia))