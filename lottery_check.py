# coding:utf-8
"""
功能：  大乐透查询
作者：  DX3906 993628121@qq.com
"""

from source import number_get, number_analyze

front_area = ['07', '10', '17', '19', '30']
back_area = ['09', '11']

numbers_list = number_get.number_get(100)

number = {'front_area': front_area, 'back_area': back_area}

res = number_analyze.number_analyze_money(numbers_list, number)

for item in res:
    print(item)
