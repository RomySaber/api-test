#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-10-22
@Author     : QA
@File       : testOperatorETL.py
@desc       : 运营商ETL接口测试用例 （使用爬虫中心后部署撤销，暂时作为备份使用）
"""

import copy
import json
import os
import re
import time

import ddt
import requests

from ai.testSource import etl_config, operator_analysis
from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.myCommon.TestBaseCase import TestBaseCase
from common.myConfig import ConfigUtils
from common.myConfig import MysqlConfig
from common.myFile.ExcelUtil import ExcelIter
from common.myFile.FileUtils import str_to_num
from common.myCommon import TimeFormat
from common.mydb import MysqlClent

TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('operatorETL_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource')


def operator_etl(data):
    """
    运营商ETL接口
    :param data: ,object
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1647')
    requesturl = baseUrl + "/operator/etl"
    LOGGER.info("运营商ETL接口请求地址:【{}】".format(requesturl))
    payload = dict()
    payload["data"] = json.dumps(data)
    LOGGER.info("运营商ETL接口请求参数：【{}】".format(data))
    response = requests.request("POST", requesturl, data=payload, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


@ddt.ddt
class testOperatorETL(TestBaseCase):
    @ddt.data(*ExcelIter(excel_path, 'operator_etl.xlsx', 'operator_etl'))
    def testOperatorETL(self, data):
        LOGGER.info(data)
        LOGGER.info(('开始执行第【{0}】条测试用例：【{1}】'.format(data['序号'], data['描述'])).center(80, '-'))
        t1 = time.clock()
        params = copy.deepcopy(etl_config.operatorETL)
        operator_analysis.modif_date(params)
        modif_keys = re.split('[;；]', data['修改key'])
        modif_values = re.split('[;；]', data['修改值'])
        for i in range(len(modif_keys)):
            operator_analysis.modif(params, modif_keys[i], modif_values[i])
        rs = json.loads(operator_etl(data=params))
        Assertion.verity(rs['status'], 200, data)
        Assertion.verity(rs['msg'], '成功', data)
        premise = re.split('[;；]', data['分析key'])
        result_keys = re.split('[;；]', data['结果key'])
        result_values = re.split('[;；]', data['断言结果'])
        for i in range(len(result_keys)):
            if data['分析key']:
                if premise[i] in ('power_off_day', 'continue_power_off_days', 'no_dial_day',
                                  'no_call_day') and result_keys[i] in ('item_1m', 'item_3m', 'item_6m'):
                    result_value = operator_analysis.get_days(result_values[i], premise[i], params)
                else:
                    result_value = str(str_to_num(result_values[i]))
                m = '{0}，第{1}条结果， {2}'.format(data, i + 1, result_keys[i])
                Assertion.verity(operator_analysis.get_result(rs, result_keys[i], premise[i]), result_value, m)
            elif data['结果key']:
                if result_keys[i] == 'call_month':
                    result_value = TimeFormat.get_month_around(-int(result_values[i]))
                else:
                    result_value = str(str_to_num(result_values[i]))
                m = '{0}，第{1}条结果， {2}'.format(data, i+1, result_keys[i])
                Assertion.verity(operator_analysis.get_result(rs, result_keys[i]), result_value, m)
        LOGGER.info(('第【{0}】条测试用例：【{2}】执行完成，执行时间【{1}】'.format(
            data['序号'], float(time.clock() - t1), data['描述'])).center(80, '-'))
