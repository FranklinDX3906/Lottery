# 超级大乐透v0.1.1.1

## 说明

- 与体彩超级大乐透相关，推荐号码等功能
- 版本0.1.1.1
- 语言：python

## 功能及流程

- 爬取体彩大乐透所有开奖号码，存入数据库
- 运行时：
    1. 爬取最新的开奖号码
    2. 存入数据库（有重复则覆盖）
    3. 使用大乐透相同的出球方法，不停的随机出一组号码
    4. 匹配，如果这个号码未中奖，则输出

## 系统划分

## 后续预计

- 可能会用到神经网络序列预测，预测号码

## 提示

- 本人相信大乐透纯随机，所以理论上与机选获奖概率一致
- 彩票有风险，投注需谨慎