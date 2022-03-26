# coding:utf-8
"""
功能：超级大乐透主函数
作者：DX3906 993628121@qq.com
"""

# from itertools import count
# from turtle import back
from source import number_create
from source import number_get
from source import config
from source import number_analyze

max_try = config.MAX_TRY
allow_num = config.allow_rate
start_numbers = 150  # 最初在start_numbers期中寻找
visited = set()  # 遍历过的期数

while (start_numbers >= 100):
    if start_numbers in visited:
        break
    else:
        visited.add(start_numbers)
    print('\n正在从{}期中计算。。。'.format(start_numbers))
    count = 1
    have_res = 0  # 是否存在预测结果
    # 获取对应数量的号码
    number_list = number_get.number_get(start_numbers)
    for _ in range(max_try):
        count += 1
        if count % (max_try // 10) == 0:
            print('已随机生成{}个号码。。。'.format(count))
        # 先随机产生一组数
        front_area, back_area = number_create.number_create()
        number = {'front_area': front_area, 'back_area': back_area}

        # 进行分析
        number_res = number_analyze.number_analyze(number_list, number)

        if len(number_res) == 0:
            have_res = 1
            print('\n历史 {} 期内预测号码：\t前区：\t{}，\t后区：\t{}\n原因：中奖期数：\t{}'.format(
                start_numbers, number['front_area'], number['back_area'],
                len(number_res)))
            if number_res:
                print('分别为：', number_res, '\n')
            # start_numbers += 10
            # break
        # else:
        #     have_res = 0
        # print('号码为：\t', number, '历史中奖期数：\t', len(number_res))
    if have_res:
        # have_res = 00
        start_numbers += 10
    else:
        start_numbers -= 1
