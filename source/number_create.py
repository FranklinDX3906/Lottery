# coding:utf-8
"""
功能：随机生成一组大乐透号码
作者：DX3906 993628121@qq.com
"""

import random


def number_create():
    """
    功能：
        随机生成大乐透号码
    输入：
        无
    输出：
        front_real：生成的前区号码
        back_real： 生成的后区号码
    """
    front_zone = [i for i in range(1, 36)]  # 前区所有号码
    # print(front_zone)
    back_zone = [i for i in range(1, 13)]  # 后区所有号码

    # 生成前区
    front_real = []
    for i in range(5):
        val = random.choice(front_zone)
        front_real.append(val)
        # front_real.append(random.choice(front_zone))
        front_zone.remove(val)
    # print(front_real)
    front_real.sort()

    # 生成后区
    back_real = []
    # front_real = []
    for i in range(2):
        val = random.choice(back_zone)
        back_real.append(val)
        # front_real.append(random.choice(front_zone))
        back_zone.remove(val)
    back_real.sort()

    return front_real, back_real
