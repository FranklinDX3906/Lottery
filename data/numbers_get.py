# coding:utf-8
"""
功能：  获取历史所有大乐透号码，存入数据库
作者：  DX3906 993628121@qq.com
"""


def numbers_get():
    """
    功能：  获取历史所有大乐透号码，存入数据库
    """

    numbers = [[[], []] for _ in range(100)]
    '''
    test_text = requests.get(config.LOTTERY_URL)
    soup = BeautifulSoup(test_text.text, 'lxml')
    data = soup.select(config.LOTTERY_SELECTOR)

    print(data)
    '''

    data_1 = []
    for i in range(1, 91):
        url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo=1'
        data = requests.get(url).text
        data = str(bs(data, 'lxml').p.next).split(',')
        # data = data.body
        # print(data.a)
        data.replace('false', 'False')
        data = eval(data)
        data = data.find('tbody id="historyData"')
        data = data['lotteryUnsortDrawresult']
        for content in data:
            number = content.get_text().strip().replace('\r', '').replace(
                '\t', '').replace('\n', ' ')
            with open('data_recent', 'a') as f:
                f.write(number + '\n')
    f.close()

    pass


if __name__ == "__main__":
    get_numbers()
