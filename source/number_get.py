# coding:utf-8
"""
功能：  获取大乐透能够获得的所有代码
作者：  DX3906 993628121@qq.com
"""

import pymysql

from . import config

mysql_host = config.mysql_host
mysql_user = config.mysql_user
mysql_password = config.mysql_password
mysql_port = config.mysql_port
mysql_db = config.mysql_db


def number_get(num=-1):
    """
    功能：
        获取最新一百期的号码
    输入：
        num：获取最新的期数，默认全部
    输出：
        numbers：最近一百期的号码
    """

    # 连接数据库
    conn = pymysql.connect(host=mysql_host,
                           passwd=mysql_password,
                           port=mysql_port,
                           user=mysql_user,
                           db=mysql_db)
    cursor = conn.cursor()

    # 获取对应数量的
    if num == -1:
        sql = "select * from lottery_number"
    else:
        sql = "select * from lottery_number order by Time desc limit {}".format(
            num)
    cursor.execute(sql)

    res = cursor.fetchall()

    number_list = []

    for time, number, front_area, back_area in res:
        front_area = front_area.split(' ')
        back_area = back_area.split(' ')
        number = {
            'time': time,
            'number': number,
            'front_area': front_area,
            'back_area': back_area
        }
        number_list.append(number)

    cursor.close()
    conn.close()

    return number_list


if __name__ == "__main__":
    number_get()
