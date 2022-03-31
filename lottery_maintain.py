# coding:utf-8
"""
功能：  大乐透维护，更新数据库，并把分析结果存入数据库
作者：  DX3906 993628121@qq.com
"""

import time

from source import number_predict, number_update, number_res

# print(number_predict.number_predict_money())
# 预测两种

res1 = number_predict.number_predict()
res2 = number_predict.number_predict_money()

# res1 = {'numbers': [{...}], 'base_num': 170}
# 写入库中
print('于{}预测最新一期号码。。。'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
number_res.number_res_write(res1, res2)

while (True):
    time_hour = time.localtime().tm_hour
    # time_minute = time.localtime().tm_min
    # print(time.strftime('%Y-%m-%d %H:%M:%S'))
    if time_hour == 21:
        # 计算此时的时间，以便于预测之后准确休眠
        time_start = time.clock()

        # 更新库
        print('于{}更新最新一期号码。。。'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
        number_update.number_update()

        # 预测两种
        res1 = number_predict.number_predict()
        res2 = number_predict.number_predict_money()

        # res1 = {'numbers': [{...}], 'base_num': 170}
        # 写入库中
        print('于{}预测最新一期号码。。。'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
        number_res.number_res_write(res1, res2)

        # print(time.asctime)
        time_end = time.clock()
        time.sleep(86400 - (time_end - time_start))
    else:
        # 休眠一分钟
        time.sleep(60)
