#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019/02/21 0015 下午 5:14
@Author     : 罗林
@File       : Assertion.py
@desc       : unittest 常用的断言方法
"""

from unittest import TestCase
from common.myCommon.Logger import getlog


LOG = getlog(__name__)


class MyError(Exception):
    #  自定义异常
    def __init__(self, ErrorInfo):
        # 初始化父类
        super().__init__(self)
        self.errorinfo = ErrorInfo
        LOG.error(self.errorinfo)

    def __str__(self):
        return self.errorinfo


tc = TestCase()


def verityIn(actual, exceptStr, message=None):
    # 验证actual实际值是否包含预期值exceptStr
    m = mylog(actual, exceptStr, message, "包含")
    try:
        tc.assertIn(actual, exceptStr, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityNotIn(actual, exceptStr, message=None):
    # 验证actual实际值是否包含预期值exceptStr
    m = mylog(actual, exceptStr, message, "不包含")
    try:
        tc.assertNotIn(actual, exceptStr, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityContain(actual, exceptStr, message=None):
    # 验证actual实际值是否包含预期值exceptStr
    m = mylog(actual, exceptStr, message, "包含")
    flag = True if exceptStr in str(actual) else False
    try:
        tc.assertTrue(flag, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityNotContain(actual, exceptStr, message=None):
    # 验证actual实际值是否包含预期值exceptStr
    m = mylog(actual, exceptStr, message, "不包含")
    flag = True if exceptStr in str(actual) else False
    try:
        tc.assertFalse(flag, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verity(actual, exceptStr, message=None):
    # 验证实际值actual与预期值exceptStr是否相等
    m = mylog(actual, exceptStr, message)
    try:
        tc.assertEqual(actual, exceptStr, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityNot(actual, exceptStr, message=None):
    # 验证实际值actual与预期值exceptStr是否不相等
    m = mylog(actual, exceptStr, message, "不相等")
    try:
        tc.assertNotEqual(actual, exceptStr, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityFalse(flagboolean, message=None):
    # 验证实际值str是否为false
    m = mylog(flagboolean, False, message)
    if any([flagboolean in ("true", "True", "TRUE", True),
            (isinstance(flagboolean, bool) and flagboolean is True)]):
        fb = True
    else:
        fb = False
    flag = True if fb is True else False
    print(flag)
    try:
        tc.assertFalse(flag, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityTrue(flagboolean, message=None):
    # 验证实际值str是否为True
    m = mylog(flagboolean, True, message)
    if any([flagboolean in("true", "True", "TRUE", True),
            (isinstance(flagboolean, bool) and flagboolean is True)]):
        fb = True
    else:
        fb = False
    flag = True if fb is True else False
    try:
        tc.assertTrue(flag, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityIs(str1, str2, message=None):
    # a is b.
    m = mylog(str1, str2, message)
    try:
        tc.assertIs(str1, str2, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityIsNot(str1, str2, message=None):
    # a is not b.
    m = mylog(str1, str2, message, "不相等")
    try:
        tc.assertIsNot(str1, str2, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityList(list1, list2, message=None):
    # List1与list2是否相等
    if all([isinstance(list1, list), isinstance(list2, list)]):
        # list1 = ['abcd', 786, 2.23, 'runoob', 70.2, 123, 'runoob']
        m = mylog(list1, list2, message)
        try:
            tc.assertListEqual(list1, list2, message)
            passLog()
        except Exception as e:
            failedLog()
            getError(e, m)
    else:
        getError('please set de vargs type is list')


def verityTuple(tuple1, tuple2, message=None):
    if all([isinstance(tuple1, tuple), isinstance(tuple2, tuple)]):
        # tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
        # 验证元组tuple1、tuple2相等，不等则fail，同时报错信息返回具体的不同的地方
        m = mylog(tuple1, tuple2, message)
        try:
            tc.assertTupleEqual(tuple1, tuple2, message)
            passLog()
        except Exception as e:
            failedLog()
            getError(e, m)
    else:
        getError('please set de vargs type is tuple')


def veritySet(set1, set2, message=None):
    if all([isinstance(set1, set), isinstance(set2, set)]):
        # set1 = {'a', 's', 'd'}
        # 验证集合set1、set2相等，不等则fail，同时报错信息返回具体的不同的地方
        m = mylog(set1, set2, message)
        try:
            tc.assertSetEqual(set1, set2, message)
            passLog()
        except Exception as e:
            failedLog()
            getError(e, m)
    else:
        getError('please set de vargs type is set')


def verityDict(d1, d2, message=None):
    if all([isinstance(d1, dict), isinstance(d2, dict)]):
        # d1 = {'name': 'runoob', 'site': 'www.runoob.com', 'code': 1}
        # 前后字典是否相同
        m = mylog(d1, d2, message)
        try:
            tc.assertDictEqual(d1, d2, message)
            passLog()
        except Exception as e:
            failedLog()
            getError(e, m)
    else:
        getError('please set the vargs is dict')


def veritySeq(seq1, seq2, message=None):
    if all([isinstance(seq1, tuple), isinstance(seq2, tuple)]):
        # seq = (3, 4, 5)
        # seq1 = 3, 4, 5
        # 有序序列的相等断言
        m = mylog(seq1, seq2, message)
        try:
            tc.assertSequenceEqual(seq1, seq2, message)
            passLog()
        except Exception as e:
            failedLog()
            getError(e, m)
    else:
        getError('please set de vargs type is tuple')


def verityLine(actual, exceptStr, message=None):
    # 断言，2个多行字符串是相等的
    m = mylog(actual, exceptStr, message)
    try:
        tc.assertMultiLineEqual(actual, exceptStr, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityInstance(obj, cls, msg=None):
    # 验证参数obj是cls的类型，不是则fail
    m = mylog(obj, cls, msg)
    try:
        tc.assertIsInstance(obj, cls, msg)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityNotInstance(obj, cls, msg=None):
    # 验证参数obj不是cls的类型，不是则fail
    m = mylog(obj, cls, msg)
    try:
        tc.assertNotIsInstance(obj, cls, msg)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityGreater(actual, exceptStr, message=None):
    # actual 大于 exceptStr，否则fail
    m = mylog(actual, exceptStr, message, "大于")
    try:
        tc.assertGreater(actual, exceptStr, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityGreaterEqual(actual, exceptStr, message=None):
    # actual ≥ exceptStr，否则fail
    m = mylog(actual, exceptStr, message, "大于等于")
    try:
        tc.assertGreaterEqual(actual, exceptStr, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityLess(actual, exceptStr, message=None):
    # actual < exceptStr，否则fail
    m = mylog(actual, exceptStr, message, "小于")
    try:
        tc.assertLess(actual, exceptStr, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityLessEqual(actual, exceptStr, message=None):
    # actual ≤ exceptStr，否则fail
    m = mylog(actual, exceptStr, message, "小于等于")
    try:
        tc.assertLessEqual(actual, exceptStr, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, m)


def verityNone(actual, message=None):
    # 判断是否为空
    if message is None:
        str1 = "【Assert验证】:【实际值：{}】,是否为空".format(actual)
    else:
        str1 = "【Assert验证】:【实际值：{0}】,是否为空,描述信息：{1}".format(actual, message)
    LOG.info(str1)
    try:
        if any([actual is None, actual == '', len(actual) == 0]):
            actual = None
    except Exception as e:
        LOG.info(e)
        actual = actual
    try:
        tc.assertIsNone(actual, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, str1)


def verityNotNone(actual, message=None):
    # 判断是否不为空
    if message is None:
        str1 = "【Assert验证】:【实际值：{}】,是否不为空".format(actual)
    else:
        str1 = "【Assert验证】:【实际值：{0}】,是否不为空,描述信息：{1}".format(actual, message)
    LOG.info(str1)
    try:
        if any([actual is None, actual == '', len(actual) == 0]):
            actual = None
    except Exception as e:
        LOG.info(e)
        actual = actual
    try:
        tc.assertIsNotNone(actual, message)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, str1)


def verityAlmost(actual, exceptStr, places=2, message=None, delta=None):
    # 验证actual约等于exceptStr ， palces: 指定精确到小数点后多少位，默认为2，如果delta指定了值，则first和second之间的差值必须≤delta
    if all([message is None, delta is None]):
        str1 = (
            "【Assert验证】:判断【约等于】：【实际值：{0},预期值：{1}】,"
            "实际值是否【约等于】预期值,精确到小数点后{2}位".format(actual, exceptStr, places)
        )
    elif all([delta is None, message is not None]):
        str1 = (
            "【Assert验证】:判断【约等于】：【实际值：{0},预期值：{1}】,"
            "实际值是否【约等于】预期值,精确到小数点后{2}位，"
            "描述信息：{3}".format(actual, exceptStr, places, message)
        )
    else:
        str1 = (
            "【Assert验证】:判断【约等于】：【实际值：{0},预期值：{1}】,"
            "实际值是否【约等于】预期值,精确到小数点后{2}位，差值必须≤{4},"
            "描述信息：{3}".format(actual, exceptStr, places, message, delta)
        )
    LOG.info(str1)

    try:
        tc.assertAlmostEqual(actual, exceptStr, places, message, delta)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, str1)


def verityNotAlmost(actual, exceptStr, places=2, message=None, delta=None):
    # 验证actual约等于exceptStr ， palces: 指定精确到小数点后多少位，默认为2，如果delta指定了值，则first和second之间的差值必须≤delta
    if all([message is None, delta is None]):
        str1 = (
            "【Assert验证】:判断【不约等于】：【实际值：{0},预期值：{1}】,"
            "实际值是否【不约等于】预期值,精确到小数点后{2}位".format(actual, exceptStr, places)
        )
    elif all([delta is None, message is not None]):
        str1 = (
            "【Assert验证】:判断【不约等于】：【实际值：{0},预期值：{1}】,"
            "实际值是否【不约等于】预期值,精确到小数点后{2}位，"
            "描述信息：{3}".format(actual, exceptStr, places, message)
        )
    else:
        str1 = (
            "【Assert验证】:判断【不约等于】：【实际值：{0},预期值：{1}】,"
            "实际值是否【不约等于】预期值,精确到小数点后{2}位，差值必须≤{4},"
            "描述信息：{3}".format(actual, exceptStr, places, message, delta)
        )
    LOG.info(str1)

    try:
        tc.assertNotAlmostEqual(first=actual, second=exceptStr, places=places, msg=message, delta=delta)
        passLog()
    except Exception as e:
        failedLog()
        getError(e, str1)


def passLog():
    LOG.info("【Assert验证  pass!】")


def failedLog():
    LOG.error("【Assert验证  failed!】")


def mylog(actual, exceptStr, message=None, atype="相等"):
    if message is None:
        str1 = "【Assert验证】:判断【比较】：【实际值：{0},预期值：{1}】,实际值是否【{2}】预期值".format(
            actual, exceptStr, atype
        )
    else:
        str1 = "【Assert验证】:判断【比较】：【实际值：{0},预期值：{1}】,实际值是否【{3}】预期值,描述信息：{2}".format(
            actual, exceptStr, message, atype
        )
    LOG.info(str1)
    return str1


def getError(e, m=None):
    if m is None:
        message = '错误内容：【{0}】'.format(e)
    else:
        message = '错误原因:【{0}】\n错误内容：【{1}】'.format(m, e)
    raise MyError(message)
