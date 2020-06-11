#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-10-23
@Author     : QA
@File       : testJdETL.py
@desc       : 京东etl接口测试用例 （使用爬虫中心后部署撤销，暂时作为备份使用）
"""

import copy
import json
import os
import re
import time
import ddt

from ai.testAction import JdetlAction
from ai.testSource import etl_config, jd_analysis
from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile.ExcelUtil import ExcelIter
from common.myFile.FileUtils import str_to_num
from common.mydb.MyRedis import MyRedis

LOGGER = getlog(__name__)
excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource')
redis_conn = MyRedis(**etl_config.redis_info)
aggregation = "jingdongETL"
name = "jingdong_autoAPITest"
JdetlAction.API_TEST_HEADERS = {'Accept': "*/*", 'Cache-Control': "no-cache", 'Accept-Encoding': "gzip, deflate",
                                'Connection': "keep-alive", 'cache-control': "no-cache"}


@ddt.ddt
class testJdETL(TestBaseCase):
    @ddt.data(*ExcelIter(excel_path, 'jd_etl.xlsx', 'jd_etl'))
    def testTbETL(self, data):
        LOGGER.info(data)
        LOGGER.info(('开始执行第【{0}】条测试用例：【{1}】'.format(data['序号'], data['描述'])).center(80, '-'))
        t1 = time.clock()
        params = copy.deepcopy(etl_config.jd_ETL)
        jd_analysis.modif_date(params)
        modif_keys = re.split('[;；]', data['修改key'])
        modif_values = re.split('[;；]', data['修改值'])
        for i in range(len(modif_keys)):
            jd_analysis.modif(params, modif_keys[i], modif_values[i])
        redis_name = aggregation + ":" + name
        redis_conn.redis_set(redis_name, json.dumps(params))
        redis_params = json.loads(redis_conn.redis_get(redis_name))
        LOGGER.info("redis查询结果: {}".format(redis_params))
        rs = json.loads(json.loads(JdetlAction.test_api_etl_jd(name)))
        Assertion.verity(rs['status_id'], '100', data)
        Assertion.verity(rs['status_des'], '成功返回数据', data)
        if data['结果key']:
            resutl_keys = re.split('[;；]', data['结果key'])
            resutls = re.split('[;；]', data['断言结果'])
            for i in range(len(resutl_keys)):
                Assertion.verity(
                    jd_analysis.get_result(rs, resutl_keys[i], redis_params), str(str_to_num(resutls[i])), data)
        LOGGER.info('第【{0}】条测试用例：【{2}】执行完成，执行时间【{1}】'.format(
            data['序号'], float(time.clock() - t1), data['描述']).center(80, '-'))
