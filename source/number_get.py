# coding:utf-8
"""
功能：获取最近100期的所有号码
作者：DX3906 993628121@qq.com
"""

import requests
from bs4 import BeautifulSoup as bs
import os

import config


def number_get(num=100):
    """
    功能：
        获取最新一百期的号码
    输入：
        num：获取最新的期数，默认100
    输出：
        numbers：最近一百期的号码
    """
    numbers = [[[], []] for _ in range(100)]
    '''
    test_text = requests.get(config.LOTTERY_URL)
    soup = BeautifulSoup(test_text.text, 'lxml')
    data = soup.select(config.LOTTERY_SELECTOR)

    print(data)
    '''

    data_1 = []
    for i in range(1, 91):
        url = 'http://www.lottery.gov.cn/historykj/history_' + str(
            i) + '.jspx?_ltype=dlt'
        data = requests.get(url).text
        data = bs(data, 'lxml')
        data = data.find('tbody').find_all('tr')
        for content in data:
            number = content.get_text().strip().replace('\r', '').replace(
                '\t', '').replace('\n', ' ')
            with open('data_recent', 'a') as f:
                f.write(number + '\n')
    f.close()

    return numbers


if __name__ == "__main__":
    number_get()
