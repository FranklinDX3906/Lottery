# coding:utf-8
"""
功能：  获取日志（方便手机上看）
"""

from . import config

log_path = config.log_path


def log_get(length=20):
    """
    功能：
        获取日志（默认最后20行）
    """

    res = []

    with open(log_path, 'r', encoding='utf-8') as f:
        res = f.readlines()

    res = res[-1 * length:] if len(res) > 20 else res
    for i in range(len(res)):
        res[i] = res[i].replace('\n', '')

    return res


if __name__ == "__main__":
    log_get()
