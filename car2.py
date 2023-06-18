import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_vehicle_info():
    # 使用requests库发送HTTP请求到Guazi网站
    response = requests.get('https://www.guazi.com/buy#bread')

    # 解析响应并获取HTML代码
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取所有标题和段落
    title_list = soup.find_all('h1')
    body_list = soup.find_all('p')

    # 将标题和段落写入txt文件
    with open('vehicle_info.txt', 'w') as f:
        for title in title_list:
            f.write(title.text + '\n')

        for body in body_list:
            f.write(body.text + '\n')

            # 关闭响应
    response.close()

if __name__ == '__main__':
    get_vehicle_info()
