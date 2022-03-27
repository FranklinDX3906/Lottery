# coding:utf-8
"""
功能：  预测结果读写
作者：  DX3906 993628121@qq.com
"""

from . import config

import pymysql

mysql_host = config.mysql_host
mysql_user = config.mysql_user
mysql_password = config.mysql_password
mysql_port = config.mysql_port
mysql_db = config.mysql_db


def number_res_write(res1, res2):
    """
    功能：
        写入两种预测结果
    输入：
        res1：  最小中奖次数原则
        res2：  最小中奖金额原则
    """
    # 连接数据库
    conn = pymysql.connect(host=mysql_host,
                           passwd=mysql_password,
                           port=mysql_port,
                           user=mysql_user,
                           db=mysql_db)
    cursor = conn.cursor()

    # 清空数据库
    sql = "delete from lottery_predict"
    cursor.execute(sql)
    conn.commit()

    # 存入第一种
    numbers, base_num = res1['numbers'], res1['base_num']
    for number in numbers:
        front_area = number['front_area']
        front_area = ' '.join(front_area).strip(' ')
        back_area = number['back_area']
        back_area = ' '.join(back_area).strip(' ')
        sql = "insert into lottery_predict(type,front_area,back_area,award_num,base_num,money_sum) values('最小中奖次数原则','{}','{}',0,{},0)".format(
            front_area, back_area, base_num)
        cursor.execute(sql)
    conn.commit()

    # 第二种
    number, base_num, award_num, money_sum = res2['number'], res2[
        'base_num'], res2['award_num'], res2['money_sum']
    front_area = number['front_area']
    front_area = ' '.join(front_area).strip(' ')
    back_area = number['back_area']
    back_area = ' '.join(back_area).strip(' ')
    sql = "insert into lottery_predict(type,front_area,back_area,award_num,base_num,money_sum) values('最小中奖金额原则','{}','{}',{},{},{})".format(
        front_area, back_area, award_num, base_num, money_sum)
    cursor.execute(sql)

    conn.commit()

    cursor.close()
    conn.close()
