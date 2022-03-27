# coding:utf-8
"""
功能：  大乐透预测
作者：  DX3906 993628121@qq.com
"""

from cmath import inf
# from re import M
from . import config, number_get, number_create, number_analyze

max_try = config.MAX_TRY


def number_predict():
    """
    功能：  号码预测，最小中奖次数原则
    """

    res = []

    # 从200期开始算
    start_numbers = 200
    while (start_numbers):
        have_res = 0  # 是否存在预测结果
        number_list = number_get.number_get(start_numbers)
        # print(start_numbers)
        for _ in range(max_try):
            # 先随机产生一组数
            front_area, back_area = number_create.number_create()
            number = {'front_area': front_area, 'back_area': back_area}

            # 进行分析
            number_res = number_analyze.number_analyze(number_list, number)

            if len(number_res) == 0:
                # print(number)
                res.append(number)
                have_res = 1
        if have_res:
            break
        else:
            start_numbers -= 1

    return {'numbers': res, 'base_num': start_numbers}


def number_predict_money():
    """
    功能：  号码预测，最小中奖金额原则
    """

    min_award = inf
    min_number = {}

    # 获取所有号码
    number_list = number_get.number_get()
    for _ in range(max_try):
        # 先随机产生一组数
        front_area, back_area = number_create.number_create()
        number = {'front_area': front_area, 'back_area': back_area}

        # 进行分析
        number_res_list = number_analyze.number_analyze_money(
            number_list, number)

        # 计算奖金
        money = 0
        for nummber_res in number_res_list:
            money += nummber_res['金额']

        if money < min_award:
            min_award = money
            min_number = number

    return {
        'number': min_number,
        'base_num': len(number_list),
        'award_num': len(number_res_list),
        'money_sum': min_award
    }


if __name__ == "__main__":
    print(number_predict())
