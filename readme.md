# 超级大乐透

## 说明

- 与体彩超级大乐透相关，推荐号码等功能
- 语言：python

## 使用

- 修改source/config.py中的参数，按照个人喜好
- 运行lottery_console.py在命令行中预测
- 运行lottery_check.py查询号码
- 进入[DX3906的简单大乐透预测](http://124.221.214.139/)使用网页版

## 功能及流程

- 爬取体彩大乐透所有开奖号码，存入数据库
- 后台不断运行，九点更新大乐透最新结果
- 运行lottery_console.py时：
    1. 使用大乐透相同的出球方法，不停的随机出一组号码
    2. 匹配，如果这个号码在对应的期数内从未中奖，则输出

## 系统划分

- 说明：
  - 按照文件目录->文件->函数的结构
  - 未完成或需要修改的部分，<u>**下划线加粗**</u>
- lottery_console.py：以控制台的形式输出预测结果的函数
- lottery_maintain.py：大乐透维护，更新数据库，并把分析结果存入数据库
- lottery_check.py：大乐透号码在100期查询（自用）
- lottery_route.py：大乐透后端
- data：静态计算数据文件夹
  - numbers_get.py：获取历史所有大乐透号码，存入数据库
  - lottery.sql：大乐透历史号码表
- source：用于调用的文件夹
  - config.py：配置文件
  - number_get.py：获取大乐透对应数量的号码列表
  - number_create.py：随机生成一组大乐透号码
  - number_analyze.py：分析一个号码在一组号码中的中奖情况
    - number_analyze()：分析一个号码在一组号码中的中奖情况
    - number_analyze_money()：分析一个号码在一组号码中的中奖情况，并且区分中奖金额
  - number_update.py：持续运行，将最新号码同步至数据库
  - number_predict.py：大乐透预测
    - number_predict()：号码预测，最小中奖次数原则
    - number_predict_money()：号码预测，最小中奖金额原则
  - number_res.py：预测结果读写
    - number_res_write()：写入两种预测结果
    - number_res_get()：读取两种预测结果

## 后续预计

- 预测加入奖金机制，选取最近n期中奖金最少的
- 可能会用到神经网络序列预测，预测号码
- 可能形成完整的前后端系统，包括前端页面等等
- 可能使用C#重构项目

## 提示

- 本人相信大乐透纯随机，所以理论上与机选获奖概率一致
- 彩票有风险，投注需谨慎
- 目前看来，基本上250期内不存在一个号码，使得其在250期内一块钱也不中

