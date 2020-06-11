#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-23 下午 5:24
@Author     : 罗林
@File       : easyloan_query.py
@desc       : 
"""

from common.mydb import MysqlClent as mydb
from easyloan.testAction import loginAction as la


def update_order(order_uuid, *value):
    # 更新订单状态
    mydb.update(la.DB, 'loan_order', ','.join(value), 'loan_order_uuid="{}"'.format(order_uuid))


def get_info(table_name, column, *condition):
    string_list = list()
    if len(condition) == 0:
        info = mydb.select(la.DB, table_name, column)
    else:
        info = mydb.select(la.DB, table_name, column, ','.join(condition))
    if len(info) == 0:
        string_list.append('')
    else:
        for _str in info[0]:
            if _str is None:
                _str = ''
            string_list.append(_str)
    return string_list


def delete_info(table_name, condition):
    mydb.delete(la.DB, table_name, condition)


def update_info(table_name, value, condition):
    mydb.update(la.DB, table_name, value, condition)
