#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-12-03
@Author     : QA
@File       : TestCaseCover.py
@desc       : 计算接口测试覆盖率
"""
from common.mydb import MysqlClent


def get_case_cover(project):
    """
    获取接口测试覆盖率， 计算规则，已执行的接口数 / 排除废弃的接口后的接口总数
    :param project:  项目名
    :return:
    """
    CI_DB = MysqlClent.get_conn()
    id = MysqlClent.select_one(CI_DB, 't_dict', 'id', 'code="{}"'.format(project))
    wipe = '废弃|作废|停用|未使用|不做)|(废)|（废）|不做）|弃用'
    wipe_col = 'page,page_name,api_name'
    total = MysqlClent.select_rows(CI_DB, 't_rap', 'id',
                                   'dict_id={0} AND NOT CONCAT({1}) REGEXP "{2}"'.format(id, wipe_col, wipe))
    if total:
        is_exe = MysqlClent.select_rows(CI_DB, 't_rap', 'id', 'dict_id={} AND is_exe = "Y"'.format(id))
        return total, round(is_exe/total*100, 2)
    else:
        return 0, 0
