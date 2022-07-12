# coding:utf-8
"""
大乐透随机生成器
作者：      DX3906 993628121@qq.com
修改时间：  2021/10/31
"""

import random

front_zone = [i for i in range(1, 36)]  # 前区所有
# print(front_zone)
back_zone = [i for i in range(1, 13)]  # 后区所有

front_real = []
for i in range(5):
    val = random.choice(front_zone)
    front_real.append(val)
    # front_real.append(random.choice(front_zone))
    front_zone.remove(val)
# print(front_real)
front_real.sort()

back_real = []
# front_real = []
for i in range(2):
    val = random.choice(back_zone)
    back_real.append(val)
    # front_real.append(random.choice(front_zone))
    back_zone.remove(val)
back_real.sort()

print("前区：\t", front_real, "\n后区：\t", back_real)
print("\n守号：\n前区：\t", [7, 10, 17, 19, 30], "\n后区：\t", [9, 11])
getattr()
