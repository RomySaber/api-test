#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-10 上午 10:59
@Author     : 罗林
@File       : MockData.py
@desc       : 随机生成测试数据
"""
import random
import string
import uuid


def uuid_random(string_length=32):
    """
    随机获取UUID字符串，默认最大32位
    :param string_length:  字符串长度
    :return:
    """
    return str(uuid.uuid4()).replace("-", "")[0:string_length]


def words_cn(num):
    """
    随机生成指定长度的中文字符
    :param num: 指定长度
    :return:
    """
    return ''.join([chr(random.randint(0x4e00, 0x9fbf)) for _ in range(num)])


def words_en_lower(num):
    """
    随机生成指定长度的小写英文字符
    :param num: 指定长度
    :return:
    """
    return ''.join([random.choice('zyxwvutsrqponmlkjihgfedcba') for _ in range(num)])


def words_en(num):
    """
    随机生成指定长度的大小写英文混合的字符
    :param num: 指定长度
    :return:
    """
    return ''.join([random.choice(string.ascii_letters) for _ in range(num)])


def strNumber(num):
    """
    随机生成指定长度的数字型字符串
    :param num: 指定长度
    :return:
    """
    start_num = str(random.randint(1, 9))
    end_num = ''.join([random.choice(string.digits) for _ in range(num - 1)])
    return start_num + end_num


def number(num):
    """
    随机生成指定长度的数字
    :param num: 指定长度
    :return:
    """
    return int(strNumber(num))


def wordAndNum(num):
    """
    生成指定数量的随机字符（包含字母，数字，特殊字符，空格、回车、tab等）
    :param num:  指定数量
    :return:
    """
    return ''.join([random.choice(string.printable) for _ in range(num)])


def phone(num=11):
    """
    随机生成手机号
    :param num:  手机号位数
    :return:
    """
    phonenumber_prefix = random.choice(
        ['153', '150', '188', '155', '189', '182', '186', '135', '139', '181', '152', '187',
         '134', '159', '133', '180', '156', '130', '136', '185', '131', '137', '138', '132'])
    return phonenumber_prefix + "".join(random.choice("0123456789") for _ in range(num - 3))


def bankAccount(num=13):
    prefix = random.choice(["622202", "622609", "511122", "621483", "622848", "622235", "622200"])
    return prefix + "".join(random.choice("0123456789") for _ in range(num - 6))


if __name__ == '__main__':
    # print(strNumber(100))
    print(bankAccount(18))
