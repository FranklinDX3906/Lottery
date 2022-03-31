# coding:utf-8
"""
功能：  大乐透查询
作者：  DX3906 993628121@qq.com
"""

from source import number_get, number_analyze

front_area = ['08', '15', '16', '19', '33']
back_area = ['03', '04']

numbers_list = number_get.number_get(100)

number = {'front_area': front_area, 'back_area': back_area}

res = number_analyze.number_analyze_money(numbers_list, number)

for item in res:
    print(item)
