#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-11-13
@Author     : QA
@File       : decorator_mongo.py
@desc       : 修改MongoDB数据的 装饰器
"""

from functools import wraps
from ai.testSource import ai_config
from common.mydb.MyPyMongo import MyPyMongo

mongo = MyPyMongo(**ai_config.mongo_db)


def update_mongo(querys, api_name, remark):
    """
    带参数的装饰函数
    :param querys: 查询条件，字典
    :param api_name: 接口名称，最后一个斜杠（/）后的字符串
    :param remark: 需要返回的参数名称，需要在MongoDB中查询
    :return:
    """

    def decorators(func):
        @wraps(func)
        def update(*args):
            query_condition = querys.copy()
            # 更新查询条件， 字典
            query_condition.update({"api_name": api_name, "remark": remark})
            # 修改MongoDB中的单个接口走打桩
            mongo.update_one(query_condition, {'used': True})
            try:
                msg = func(*args)
            except Exception as e:
                raise e
            finally:
                # 修改MongoDB中的单个接口关闭打桩
                mongo.update_one(query_condition, {'used': False})
            return msg

        return update

    return decorators


def close_pile(querys):
    """
    修改MongoDB 信息，结束打桩
    :param querys: 查询条件，字典
    :return:
    """

    def decorators(func):
        @wraps(func)
        def close(*args):
            # 关闭所有打桩数据
            mongo.update_many(querys, {'used': False})
            try:
                func(*args)
            except Exception as e:
                raise e

        return close

    return decorators
