# coding:utf-8
"""
功能：  一致启动，获取最新一期的号码，同步到数据库
作者：  DX3906 993628121@qq.com
"""

import requests
import pymysql
# from bs4 import BeautifulSoup as bs
import json
import datetime

from . import config

mysql_host = config.mysql_host
mysql_user = config.mysql_user
mysql_password = config.mysql_password
mysql_port = config.mysql_port
mysql_db = config.mysql_db


def number_update():
    """
    功能：  获取最新一期号码，存入数据库
    """

    # 连接数据库
    conn = pymysql.connect(host=mysql_host,
                           passwd=mysql_password,
                           port=mysql_port,
                           user=mysql_user,
                           db=mysql_db)
    cursor = conn.cursor()

    page_number = 1
    # page_number = 1000
    url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=100&isVerify=1&pageNo={}'.format(
        page_number)

    page_data = requests.get(url).text
    page_data = json.loads(page_data)
    page_data = page_data['value']['list']
    page_item = page_data[0]
    # number =
    date = page_item['lotteryDrawTime']
    draw_num = page_item['lotteryDrawNum']
    number = page_item['lotteryDrawResult']

    date = date.split('-')
    date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
    number = number.split(' ')
    front_area = ' '.join(number[:5]).strip()
    back_area = ' '.join(number[5:]).strip()
    sql = "insert into lottery_number(Time,number,front_area,back_area) values('{}','{}','{}','{}')".format(
        date, draw_num, front_area, back_area)
    try:
        cursor.execute(sql)
        conn.commit()
        conn.close()
        print("时间：\t", date, "号码：\t", front_area, '\t', back_area)
    except Exception as ex:
        print(ex)
        return


if __name__ == "__main__":
    import time
    while (True):
        time_hour = time.localtime().tm_hour
        # print(time.strftime('%Y-%m-%d %H:%M:%S'))
        if time_hour == 21:
            print('于{}更新最新一期号码。。。'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
            number_update()
            # print(time.asctime)
            time.sleep(86400)
        else:
            time.sleep(60)
