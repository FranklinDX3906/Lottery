# coding:utf-8
"""
功能：  分析一个号码在一组号码中的中奖情况
作者：  DX3906 993628121@qq.com
"""

# from typing import List


def number_analyze(number_list, number):
    """
    功能：
        分析一个号码在一组号码中的中奖情况
    输入：
        number_list：历史号码组
        number：随机号码
    输出：
        res：中奖情况
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


def number_analyze_money(number_list, number):
    """
    功能：
        分析一个号码在一组号码中的中奖情况，区分金额
    输入：
        number_list：历史号码组
        number：随机号码
    输出：
        res：中奖情况
    """
    res = []

    for number_his in number_list:
        front_area_his = number_his['front_area']
        back_area_his = number_his['back_area']

        front_area = number['front_area']
        back_area = number['back_area']

        front_num = 0
        back_num = 0

        # 计算前区和后区分别的符合号码
        for num in front_area:
            if num in front_area_his:
                front_num += 1
        for num in back_area:
            if num in back_area_his:
                back_num += 1

        # 进行金额判定
        if front_num == 5 and back_num == 2:
            res.append({'号码与时间': number_his, '奖项': '一等奖', '金额': 10000000})
        elif front_num == 5 and back_num == 1:
            res.append({'号码与时间': number_his, '奖项': '二等奖', '金额': 150000})
        elif front_num == 5 and back_num == 0:
            res.append({'号码与时间': number_his, '奖项': '三等奖', '金额': 10000})
        elif front_num == 4 and back_num == 1:
            res.append({'号码与时间': number_his, '奖项': '四等奖', '金额': 200})
        elif front_num == 3 and back_num == 2:
            res.append({'号码与时间': number_his, '奖项': '四等奖', '金额': 200})
        elif front_num == 4 and back_num == 0:
            res.append({'号码与时间': number_his, '奖项': '五等奖', '金额': 10})
        elif front_num == 3 and back_num == 1:
            res.append({'号码与时间': number_his, '奖项': '五等奖', '金额': 10})
        elif front_num == 2 and back_num == 2:
            res.append({'号码与时间': number_his, '奖项': '五等奖', '金额': 10})
        elif front_num == 3 and back_num == 0:
            res.append({'号码与时间': number_his, '奖项': '六等奖', '金额': 5})
        elif front_num == 1 and back_num == 2:
            res.append({'号码与时间': number_his, '奖项': '六等奖', '金额': 5})
        elif front_num == 2 and back_num == 1:
            res.append({'号码与时间': number_his, '奖项': '六等奖', '金额': 5})
        elif front_num == 0 and back_num == 2:
            res.append({'号码与时间': number_his, '奖项': '六等奖', '金额': 5})
        else:
            continue

    return res
