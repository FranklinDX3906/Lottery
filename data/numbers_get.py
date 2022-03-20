# coding:utf-8
"""
功能：  获取历史所有大乐透号码，存入数据库
作者：  DX3906 993628121@qq.com
"""

import requests
import pymysql
from bs4 import BeautifulSoup as bs
import json
import datetime

mysql_host = '192.168.213.128'
mysql_user = 'root'
mysql_password = '123456'
mysql_port = 3306
mysql_db = 'lottery'


def numbers_get():
    """
    功能：  获取历史所有大乐透号码，存入数据库
    """

    # 连接数据库
    conn = pymysql.connect(host=mysql_host,
                           passwd=mysql_password,
                           port=mysql_port,
                           user=mysql_user,
                           db=mysql_db)
    cursor = conn.cursor()

    # 页面数
    page_number = 0
    while (True):
        page_number += 1
        # page_number = 1000
        url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=100&isVerify=1&pageNo={}'.format(
            page_number)

        # 记录100个总的
        numbers = []
        page_data = requests.get(url).text
        page_data = json.loads(page_data)
        page_data = page_data['value']['list']
        if not page_data:
            break
        # page_data = str(bs(page_data, 'lxml').p.next).split(',')
        for page_item in page_data:
            date = page_item['lotteryDrawTime']
            draw_num = page_item['lotteryDrawNum']
            number = page_item['lotteryDrawResult']
            # page_item.split(':')
            numbers.append([date, draw_num, number])
            # if page_item[0]

        for date, draw_num, number in numbers:
            date = date.split('-')
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            number = number.split(' ')
            front_area = ' '.join(number[:5]).strip()
            back_area = ' '.join(number[5:]).strip()
            sql = "insert into lottery_number(Time,number,front_area,back_area) values('{}','{}','{}','{}')".format(
                date, draw_num, front_area, back_area)
            try:
                cursor.execute(sql)
            except:
                continue
            print("时间：\t", date, "号码：\t", front_area, '\t', back_area)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    numbers_get()
