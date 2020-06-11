#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-12 上午 9:35
@Author     : 罗林
@File       : testAiapi20.py
@desc       :  机审2.2 接口自动化
"""

import copy
import json
import os
import re
import time

import ddt
from faker import Faker

from ai.testAction import AiapiAction
from xqkj.testSource import ai_config
from common.myCommon import Assertion, TimeFormat
from common.myCommon.Logger import getlog
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import FileUtils, ExcelUtil

fake = Faker('zh_cn')
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


def special(key, value):
    """
    处理特殊规则
    :param key: 规则key值
    :param value: 修改规则值
    :return:
    """
    if key in ['V04_1010', 'V04_1011', 'V04_1012', 'V05_1015', 'V05_1016', 'V05_1017']:
        # value 传入数据格式 int 如5，-7
        result = TimeFormat.get_day_start_time(FileUtils.str_to_num(value))
    elif key in ['V01_3001', 'V01_3002', 'V01_1001']:
        # value 传入数据格式 int 如5，-7 , 0.0, 0.1
        result = FileUtils.str_to_num(value)
    elif key == 'V03_1045':
        V03_1045 = [{"call_cnt_6m": 304, "peer_num": "15775800488", "call_cnt_1m": 6,
                     "call_cnt_3m": 140, "call_cnt_1w": 9}]
        #  value 传入数据格式 phone;num
        v = re.split('[;；]', value)
        num = FileUtils.str_to_num(str(v[1]))
        tmp = {"call_cnt_6m": 304, "peer_num": v[0], "call_cnt_1m": num, "call_cnt_3m": 140, "call_cnt_1w": 9}
        V03_1045.append(tmp)
        result = V03_1045
    elif key == 'V03_1046':
        # value传入格式phone1;phone2;phone3
        v = re.split('[;；]', value)
        result = [{"top_item": [{"peer_number": v[0]}, {"peer_number": v[1]}, {"peer_number": v[2]}],
                   "key": "peer_num_top3_3m"},
                  {"top_item": [{"peer_number": v[3]}, {"peer_number": v[4]}, {"peer_number": v[5]}],
                   "key": "peer_num_top3_6m"}]
    elif key == 'V01_1010':
        # value传入格式 int
        result = str([{"name": "{}".format(fake.name()), "phones": ["{}".format(fake.phone_number())]}
                      for _ in range(int(FileUtils.str_to_num(value)))]).replace('\'', '\"')
    elif key == 'V03_1002':
        result = str(int(FileUtils.str_to_num(value)))
    else:
        result = value
    return result


def choose_sheet(param, param_dict, param_key, value):
    """
    判断规则值是否在 param_dict 中，不在时遍历 param 查找对应的param_key 进行修改
    :param param:  请求参数
    :param param_dict:  查找对象
    :param param_key: 查找key值
    :param value: 修改值
    :return:
    """
    if param_key in param[param_dict].keys():
        param[param_dict][param_key] = special(param_key, value)
    else:
        for k, v in param.items():
            if param_key in v.keys():
                param[k][param_key] = special(param_key, value)
                break


@ddt.ddt
class testAiapi20(TestBaseCase):
    @ddt.data(*read_excel('Aiapi20machinReview.xlsx'))
    def test_Aiapi20_machine_review(self, data):
        LOGGER.info(data)
        LOGGER.info(('开始执行【{0}】第【{1}】条测试用例：【{2}】'.format(
            data['sheet'], data['序号'], data['描述'])).center(80, '-'))
        t1 = time.clock()
        params = copy.deepcopy(ai_config.demo)
        if any(True if ext in data["修改key"] else False for ext in [',', '，']):
            keys = re.split('[,，]', re.sub('\s+', '', data["修改key"]))
            values = re.split('[,，]', re.sub('\s+', '', data["修改值"]))
            if len(keys) == len(values):
                for i in range(len(keys)):
                    choose_sheet(params, data['sheet'], keys[i], values[i])
            else:
                raise IndexError("修改key 和修改值长度不一致，【{}】".format(data))
        else:
            choose_sheet(params, data['sheet'], data["修改key"], data["修改值"])
        rs = json.loads(AiapiAction.test_risk_strategy(
            data=params, scene_id=ai_config.scene_id, version=ai_config.version))
        Assertion.verity(rs['risk_strategy']['status_des'], '成功返回数据', data)
        Assertion.verity(rs['risk_strategy']['status_id'], '100', data)
        Assertion.verity(rs['risk_score']['status_des'], '成功返回数据', data)
        Assertion.verity(rs['risk_score']['status_id'], '100', data)
        if re.sub('\s+', '', data['评分规则名称']) != '':
            for result_info_key, result_info_value in rs['risk_score']['data']['result_info'].items():
                if result_info_value['desc'] == data['评分规则名称']:
                    score_result = rs['risk_score']['data']['result_info'][result_info_key]['result']
                    break
            else:
                message = "失败原因: 找不到描述信息为【{1}】的规则名称，测试数据【{0}】".format(
                    data, data['评分规则名称'])
                raise Assertion.MyError(message)
            Assertion.verity(score_result, float(data['评分规则结果']), data)
        if re.sub('\s+', '', data['风险策略编号']) != '':
            my_num = str(int(FileUtils.str_to_num(data['风险策略编号'])))
            try:
                strategy_result = rs['risk_strategy']['data']['result_info'][my_num]['result']
            except Exception as e:
                message = "测试数据【{1}】，失败原因: 找不到['risk_strategy']['data']['result_info']" \
                          "['{2}']['result']，定位：【{0}】".format(e, data, my_num)
                raise Assertion.MyError(message)
            Assertion.verity(strategy_result, FileUtils.str_to_bool(data['风险策略结果']), data)
            LOGGER.info(('【{0}】第【{1}】条测试用例：【{3}】执行完成，执行时间【{2}】'.format(
                data['sheet'], data['序号'], float(time.clock() - t1), data['描述'])).center(80, '-'))
