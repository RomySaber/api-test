#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2020-05-09
@Author     : QA
@File       : testSpiderETL.py
@desc       : 
"""


import copy
import os
import re

import ddt
import time

from ai.testAction import SpiderETLAction
from ai.testSource import etl_config, tb_analysis, jd_analysis, operator_analysis
from common.myCommon import Assertion, TimeFormat
from common.myCommon.Logger import getlog
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile.ExcelUtil import ExcelIter
from common.myFile.FileUtils import str_to_num
from common.mydb.MyPyMongo import MyPyMongo

excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource')
LOGGER = getlog(__name__)
tb_mongo_info = etl_config.mongo_info
tb_mongo_info['collist'] = 'taobao'

tb_mongo = MyPyMongo(**tb_mongo_info)
jd_mongo_info = etl_config.mongo_info
jd_mongo_info['collist'] = 'jingdong'
jd_mongo = MyPyMongo(**jd_mongo_info)

yys_mongo_info = etl_config.mongo_info
yys_mongo_info['collist'] = 'unicom'
yys_mongo = MyPyMongo(**yys_mongo_info)

taskId = 'autoAPITest'


@ddt.ddt
class testSpiderETL(TestBaseCase):
    # @ddt.data(*ExcelIter(excel_path, 'tb_etl.xlsx', 'tb_etl'))
    # def testSpiderTbETL(self, data):
    #     LOGGER.info(data)
    #     LOGGER.info(('开始执行第【{0}】条测试用例：【{1}】'.format(data['序号'], data['描述'])).center(80, '-'))
    #     t1 = time.clock()
    #     params = copy.deepcopy(etl_config.tb_ETL)
    #     tb_analysis.modif_date(params)
    #     modif_keys = re.split('[;；]', data['修改key'])
    #     modif_values = re.split('[;；]', data['修改值'])
    #     for i in range(len(modif_keys)):
    #         tb_analysis.modif(params, modif_keys[i], modif_values[i])
    #     if tb_mongo.find_date({"taskId": taskId}):
    #         tb_mongo.update_one({"taskId": taskId}, {"data": params})
    #     else:
    #         tb_mongo.insert_one({"data": params, "code": "", "taskId": taskId, "m": ""})
    #     LOGGER.info("MongoDB原始数据：【{}】".format(tb_mongo.find_date({"taskId": taskId})))
    #     rs = SpiderETLAction.api_etl_taobao(True, False, '', '', taskId)
    #     Assertion.verity(rs['code'], '10000', data)
    #     Assertion.verity(rs['msg'], '成功返回数据', data)
    #     if data['结果key']:
    #         resutl_keys = re.split('[;；]', data['结果key'])
    #         resutls = re.split('[;；]', data['断言结果'])
    #         for i in range(len(resutl_keys)):
    #             Assertion.verity(
    #                 tb_analysis.get_result(rs, resutl_keys[i], params), resutls[i], data)
    #     LOGGER.info('第【{0}】条测试用例：【{2}】执行完成，执行时间【{1}】'.format(
    #         data['序号'], float(time.clock() - t1), data['描述']).center(80, '-'))

    @ddt.data(*ExcelIter(excel_path, 'jd_etl.xlsx', 'jd_etl'))
    def testSpiderJdETL(self, data):
        LOGGER.info(data)
        LOGGER.info(('开始执行第【{0}】条测试用例：【{1}】'.format(data['序号'], data['描述'])).center(80, '-'))
        t1 = time.clock()
        params = copy.deepcopy(etl_config.jd_ETL)
        jd_analysis.modif_date(params)
        modif_keys = re.split('[;；]', data['修改key'])
        modif_values = re.split('[;；]', data['修改值'])
        for i in range(len(modif_keys)):
            jd_analysis.modif(params, modif_keys[i], modif_values[i])
        # update_mongo(jd_mongo, params)
        if jd_mongo.find_date({"taskId": taskId}):
            jd_mongo.update_one({"taskId": taskId}, {"data": params})
        else:
            jd_mongo.insert_one({"data": params, "inserttime": "2020-04-14 02:41:58", "taskId": taskId})
        LOGGER.info("MongoDB原始数据：【{}】".format(jd_mongo.find_date({"taskId": taskId})))
        rs = SpiderETLAction.etl_jingdong(False, False, '', '', taskId)
        Assertion.verity(rs['status_id'], '10000', data)
        Assertion.verity(rs['status_des'], '成功返回数据', data)
        if data['结果key']:
            resutl_keys = re.split('[;；]', data['结果key'])
            resutls = re.split('[;；]', data['断言结果'])
            for i in range(len(resutl_keys)):
                Assertion.verity(
                    jd_analysis.get_result(rs, resutl_keys[i], params), str(str_to_num(resutls[i])), data)
        LOGGER.info('第【{0}】条测试用例：【{2}】执行完成，执行时间【{1}】'.format(
            data['序号'], float(time.clock() - t1), data['描述']).center(80, '-'))

    # @ddt.data(*ExcelIter(excel_path, 'operator_etl.xlsx', 'operator_etl'))
    # def testSpiderOperatorETL(self, data):
    #     LOGGER.info(data)
    #     LOGGER.info(('开始执行第【{0}】条测试用例：【{1}】'.format(data['序号'], data['描述'])).center(80, '-'))
    #     t1 = time.clock()
    #     params = copy.deepcopy(etl_config.operatorETL)
    #     operator_analysis.modif_date(params)
    #     modif_keys = re.split('[;；]', data['修改key'])
    #     modif_values = re.split('[;；]', data['修改值'])
    #     for i in range(len(modif_keys)):
    #         operator_analysis.modif(params, modif_keys[i], modif_values[i])
    #     # update_mongo(yys_mongo, params)
    #     if yys_mongo.find_date({"taskId": "unicom_" + taskId}):
    #         yys_mongo.update_one({"taskId": "unicom_" + taskId}, {"data": params})
    #     else:
    #         yys_mongo.insert_one({"data": params, "taskId": "unicom_" + taskId, "inserttime": "2020-03-18 16:54:04"})
    #     LOGGER.info("MongoDB原始数据：【{}】".format(yys_mongo.find_date({"taskId": "unicom_" + taskId})))
    #     rs = SpiderETLAction.api_etl_yys(False, 0, '', '', "unicom_" + taskId)
    #     Assertion.verity(rs['code'], '10000', data)
    #     Assertion.verity(rs['msg'], '成功', data)
    #     premise = re.split('[;；]', data['分析key'])
    #     result_keys = re.split('[;；]', data['结果key'])
    #     result_values = re.split('[;；]', data['断言结果'])
    #     for i in range(len(result_keys)):
    #         if data['分析key']:
    #             if premise[i] in ('power_off_day', 'continue_power_off_days', 'no_dial_day',
    #                               'no_call_day') and result_keys[i] in ('item_1m', 'item_3m', 'item_6m'):
    #                 result_value = operator_analysis.get_days(result_values[i], premise[i], params)
    #             else:
    #                 result_value = str(str_to_num(result_values[i]))
    #             m = '{0}，第{1}条结果， {2}'.format(data, i + 1, result_keys[i])
    #             Assertion.verity(operator_analysis.get_result(rs, result_keys[i], premise[i]), result_value, m)
    #         elif data['结果key']:
    #             if result_keys[i] == 'call_month':
    #                 result_value = TimeFormat.get_month_around(-int(result_values[i]))
    #             else:
    #                 result_value = str(str_to_num(result_values[i]))
    #             m = '{0}，第{1}条结果， {2}'.format(data, i+1, result_keys[i])
    #             Assertion.verity(operator_analysis.get_result(rs, result_keys[i]), result_value, m)
    #     LOGGER.info(('第【{0}】条测试用例：【{2}】执行完成，执行时间【{1}】'.format(
    #         data['序号'], float(time.clock() - t1), data['描述'])).center(80, '-'))
