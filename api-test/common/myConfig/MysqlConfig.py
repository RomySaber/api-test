#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-02-18 上午 10:19
@Author     : 罗林
@File       : MysqlConfig.py
@desc       :  读取数据库auto_ci的表t_config中的数据
"""

from common.mydb import MysqlClent as mq

DB_CONN = mq.get_conn()


def get(conf_name, dict_id_code=None):
    # 读取数据库auto_ci的表t_config中的数据，获取str类型的配置数据
    if dict_id_code is None:
        result = mq.select_one(DB_CONN, 't_config', 'conf_valve', 'conf_name= "{}"'.format(conf_name))
    else:
        if isinstance(dict_id_code, int):
            result = mq.select_one(DB_CONN, 't_config', 'conf_valve',
                                   'conf_name= "{0}" AND dict_id = {1}'.format(conf_name, dict_id_code))
        else:
            result = mq.select_join(DB_CONN, 't_config as c,t_dict as d', 'c.conf_valve', 'c.dict_id=d.id',
                                    'c.conf_name="{0}" AND d.code="{1}" LIMIT 1'.format(conf_name, dict_id_code))[0][0]
    return result


def getint(conf_name, dict_id=None):
    # 读取数据库auto_ci的表t_config中的数据，获取int类型的配置数据
    return int(get(conf_name, dict_id))


def getfloat(conf_name, dict_id=None):
    # 读取数据库auto_ci的表t_config中的数据，获取float类型的配置数据
    return float(get(conf_name, dict_id))


def getboolean(conf_name, dict_id=None):
    # 读取数据库auto_ci的表t_config中的数据，获取boolean类型的配置数据
    bool_str = str(get(conf_name, dict_id)).strip('').lower()
    if bool_str == 'true':
        flag = True
    else:
        flag = False
    return flag


def getlist(conf_name, split_str, dict_id=None):
    # 读取数据库auto_ci的表t_config中的数据，获取str类型的配置数据，根据提供的分隔符拆分成list
    return get(conf_name, dict_id).split(split_str)


if __name__ == "__main__":
    print(get('finance_apiURL', 'finance'))
