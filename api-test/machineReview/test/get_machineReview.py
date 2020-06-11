#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-21 上午 11:34
@Author     : 罗林
@File       : get_machineReview.py
@desc       :  好贷、小启信用 机审 公用方法和结果断言
"""

import copy
import json
import os
import time

from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.myFile import ExcelUtil
from common.myFile import FileUtils
from machineReview.testAction import EasyloanmachinereviewAction

LOGGER = getlog(__name__)


def read_excel(excel_name):
    """
    读取Excel中的所有sheet，组装成字典并加入数组
    :return:  返回多个字典组成的数组
    """
    excel_path = FileUtils.is_windows(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource'))
    sheets = ExcelUtil.get_sheets(os.path.join(excel_path, excel_name))
    excel_datas = list()
    for _sheet in sheets:
        for excel_data in ExcelUtil.ExcelUtil(excel_path, excel_name, _sheet).next():
            excel_data['sheet'] = _sheet
            excel_datas.append(excel_data)
    return excel_datas


def assert_info(data, rs):
    Assertion.verity(rs['risk_strategy']['status_des'], '成功返回数据', data)
    Assertion.verity(rs['risk_strategy']['status_id'], '100', data)
    Assertion.verity(rs['risk_score']['status_des'], '成功返回数据', data)
    Assertion.verity(rs['risk_score']['status_id'], '100', data)
    if data['评分规则名称'].strip(' ') != '' and data['评分规则结果'].strip(' ') != '':
        for result_info_key, result_info_value in rs['risk_score']['data']['result_info'].items():
            if result_info_value['desc'] == data['评分规则名称']:
                score_result = rs['risk_score']['data']['result_info'][result_info_key]['result']
                break
        else:
            message = "失败原因: 找不到描述信息为【{1}】的规则名称，测试数据【{0}】".format(data, data['评分规则名称'])
            raise Assertion.MyError(message)
        Assertion.verity(score_result, float(data['评分规则结果']), data)
    if data['风险策略编号'].strip(' ') != '' and data['风险策略结果'].strip(' ') != '':
        my_num = str(int(FileUtils.str_to_num(data['风险策略编号'])) - 1)
        try:
            strategy_result = rs['risk_strategy']['data']['result_info'][my_num]['result']
        except Exception as e:
            message = "测试数据【{1}】，失败原因: 找不到['risk_strategy']['data']['result_info']" \
                      "['{2}']['result']，定位：【{0}】".format(e, data, my_num)
            raise Assertion.MyError(message)
        Assertion.verity(strategy_result, FileUtils.str_to_bool(data['风险策略结果']), data)


def get_test_info(copy_dict, data, fun):
    # 单个变量修改后进行测试
    param_data_json = copy.deepcopy(copy_dict)
    LOGGER.info(('开始执行【{0}】第【{1}】条测试用例：【{2}】'
                 .format(data['sheet'], data['序号'], data['描述'])).center(80, '-'))
    t1 = time.clock()
    params_json = fun(param_data_json, data['sheet'], data['修改key'], data['修改值'])
    rs = json.loads(EasyloanmachinereviewAction.test_risk_strategy(params_json))
    assert_info(data, rs)
    LOGGER.info(('【{0}】第【{1}】条测试用例：【{3}】执行完成，执行时间【{2}】'.
                 format(data['sheet'], data['序号'], float(time.clock() - t1), data['描述'])).center(80, '-'))
