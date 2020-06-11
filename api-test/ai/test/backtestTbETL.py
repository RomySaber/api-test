#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-10-23
@Author     : QA
@File       : testTbETL.py
@desc       : 淘宝接口etl测试用例 （使用爬虫中心后部署撤销，暂时作为备份使用）
"""

import copy
import os
import re

import ddt
import json
import requests
import time

from ai.testSource import etl_config, tb_analysis
from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.myCommon.TestBaseCase import TestBaseCase
from common.myConfig import ConfigUtils
from common.myConfig import MysqlConfig
from common.myFile.ExcelUtil import ExcelIter
from common.mydb import MysqlClent
from common.mydb.MyRedis import MyRedis

excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource')
TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('tbETL_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
redis_conn = MyRedis(**etl_config.mj_redis_info)
aggregation = "taobaoETL"
name = "taobao_autoAPITest"


def api_etl_taobao(reqId):
    """
    淘宝ETL
    :param reqId:
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1691')
    requesturl = baseUrl + "/api/etl_taobao"
    LOGGER.info("淘宝ETL请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqId
    # LOGGER.info("淘宝ETL请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("淘宝ETL请求参数：【{}】".format(params))
    # response = requests.request("POST", requesturl, headers=API_TEST_HEADERS, params=params, timeout=TIMEOUT)
    response = requests.request("POST", requesturl, params=params, timeout=TIMEOUT)
    LOGGER.info("淘宝ETL请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "淘宝ETL状态码检查")
    LOGGER.info("淘宝ETL请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


@ddt.ddt
class testTbETL(TestBaseCase):
    @ddt.data(*ExcelIter(excel_path, 'tb_etl.xlsx', 'tb_etl'))
    def testTbETL(self, data):
        LOGGER.info(data)
        LOGGER.info(('开始执行第【{0}】条测试用例：【{1}】'.format(data['序号'], data['描述'])).center(80, '-'))
        t1 = time.clock()
        params = copy.deepcopy(etl_config.tb_ETL)
        tb_analysis.modif_date(params)
        modif_keys = re.split('[;；]', data['修改key'])
        modif_values = re.split('[;；]', data['修改值'])
        for i in range(len(modif_keys)):
            tb_analysis.modif(params, modif_keys[i], modif_values[i])
        redis_name = aggregation + ":" + name
        redis_conn.redis_set(redis_name, json.dumps(params))
        redis_params = json.loads(redis_conn.redis_get(redis_name))
        LOGGER.info("redis查询结果: {}".format(redis_params))
        rs = json.loads(api_etl_taobao(name))
        Assertion.verity(rs['status_id'], '100', data)
        Assertion.verity(rs['status_des'], '成功返回数据', data)
        if data['结果key']:
            resutl_keys = re.split('[;；]', data['结果key'])
            resutls = re.split('[;；]', data['断言结果'])
            for i in range(len(resutl_keys)):
                Assertion.verity(
                    tb_analysis.get_result(rs, resutl_keys[i], redis_params), resutls[i], data)
        LOGGER.info('第【{0}】条测试用例：【{2}】执行完成，执行时间【{1}】'.format(
            data['序号'], float(time.clock() - t1), data['描述']).center(80, '-'))
