# coding:utf-8
"""
功能：  分析一个号码在一组号码中的中奖情况
作者：  DX3906 993628121@qq.com
"""

from typing import List


def number_analyze(number_list, number):
    """
    功能：  分析一个号码在一组号码中的中奖情况
    """
    res = []

    for number_his in number_list:
        front_area_his = number_his['front_area']
        back_area_his = number_his['back_area']

        front_area = number['front_area']
        back_area = number['back_area']

        front_num = 0
        back_num = 0

        for num in front_area:
            if num in front_area_his:
                front_num += 1
        for num in back_area:
            if num in back_area_his:
                back_num += 1
        if (front_num > 1 and back_num > 0) or front_num > 2 or back_num > 1:
            res.append(number_his)

    return res
