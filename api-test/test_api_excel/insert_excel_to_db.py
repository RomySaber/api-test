#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-02-22 上午 10:38
@Author     : 罗林
@File       : insert_excel_to_db.py
@desc       : 获取Excel中的数据，插入到auto_ci数据库t_rap表中
"""

import os
import re

import get_rap_api
from common.myCommon.Assertion import MyError
from common.myCommon.Logger import getlog
from common.myFile import ExcelUtil, FileUtils
from common.mydb import MysqlClent as mq

LOG = getlog(__name__)
DB_CONN = mq.get_conn()


def get_dict_id(project):
    dict_id = mq.select_one(DB_CONN, 't_dict', 'id', "code = '{}'".format(project))
    LOG.debug('The dict_id is :{}'.format(dict_id))
    return dict_id


def _read_excel(project, module_name):
    excel_path = os.path.join(os.path.dirname(__file__), '{}.xlsx'.format(project))
    excels = ExcelUtil.read_excel(excel_path, module_name, 1)
    LOG.debug('The data of excel is :{}'.format(excels))
    return excels


def insert_to_rap(project, module_name):
    dict_id = get_dict_id(project)
    raps = list()
    for excel_data in _read_excel(project, module_name):
        moudle, page, api_name, api_type, api_address, parameters, parameter_description, response_parameter, \
        response_parameter_description = excel_data
        api_address = get_rap_api.api_url_trim(api_address.strip('\xa0').strip('\n').strip(' ').lstrip(' '))
        parameter_description = re.sub('[\'\"]', '\\\"', parameter_description)
        response_parameter_description = re.sub('[\'\"]', '\\\"', response_parameter_description)
        api_name = re.sub('[\n\r\t]', '', api_name)
        api_types = get_rap_api.API_TYPE.values()
        if api_type.lower() not in api_types:
            raise MyError('接口类型错误，输入的接口类型为{0}，接口类型包括{1}'.format(api_type, api_types))
        param_valid = lambda x: False if any([FileUtils.is_ch(x), FileUtils.is_special_char(x)]) else True
        if not all([param_valid(r_p) for r_p in parameters.split(',')]):
            raise MyError('存在无效的参数'.format(parameters))
        if not all([param_valid(r_p) for r_p in response_parameter.split(',')]):
            raise MyError('存在无效的参数'.format(response_parameter))
        raps.append(
            [dict_id, module_name, moudle, page, api_name, api_type, api_address, parameters, parameter_description,
             response_parameter, response_parameter_description])
    LOG.debug(raps)
    get_rap_api.insert_rap([raps])


if __name__ == "__main__":
    print(insert_to_rap('finance', 'manage'))
    # if len(sys.argv) == 3:
    #     insert_to_rap(sys.argv[1], sys.argv[2])
    # else:
    #     LOG.error('Number of parameters input error, The max number of parameters is two')
