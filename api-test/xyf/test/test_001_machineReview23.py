#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-11-05
@Author     : 罗林
@File       : test_001_machineReview23.py
@desc       :  机审2.3 接口自动化
"""

import copy
import json
import os
import re
import time

import ddt
from faker import Faker

from ai.testAction import AiapiAction
from common.myCommon import Assertion, TimeFormat
from common.myCommon.Logger import getlog
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import FileUtils, ExcelUtil

excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource')
fake = Faker('zh_cn')
LOGGER = getlog(__name__)
scene_id = '9'
version = {"yys": "test", "taobao": "test", "jingdong": "test", "tongdun": "test", "xuexin": "test"}
demo = {
    "tongdun": {"V02_1001": "51", "V02_1005": "1", "V02_1006": "1", "V02_1009": "是", "V02_1010": "否", "V02_2010": "1",
                "V02_2011": "2", "V02_2012": "3", "V02_2013": "否","V02_2015":"1",
        "V02_2016":1,
        "V02_2017":1,
        "V02_2018":1,
        "V02_2019":1,
        "V02_2020":1,
        "V02_2021":1,
        "V02_2022":"否",
        "V02_2023":"否",
        "V02_2024":"否",
        "V02_2025":1,
        "V02_2026":1,
        "V02_2027":1},
    "yys": {"V03_1002": "12", "V03_1003": "是", "V03_1014": "1", "V03_1015": "0", "V03_1016": "1", "V03_1022": "1",
            "V03_1024": "2", "V03_1041": "33", "V03_1042": "44", "V03_1043": "否", "V03_1044": "是", "V03_1045": {
            "0": {"call_cnt_1m": "5", "call_cnt_3m": "5", "call_cnt_6m": "5", "call_cnt_7d": "1",
                  "peer_number": "13603177647"},
            "1": {"call_cnt_1m": "3", "call_cnt_3m": "5", "call_cnt_6m": "19", "call_cnt_7d": "1",
                  "peer_number": "15282318670"}}, "V03_1046": {
            "top_item_1m": {"top1": {"call_cnt": 5, "peer_number": "13603177647"},
                            "top2": {"call_cnt": 3, "peer_number": "15282318670"},
                            "top3": {"call_cnt": 1, "peer_number": "84117828"}},
            "top_item_3m": {"top1": {"call_cnt": 5, "peer_number": "13603177647"},
                            "top2": {"call_cnt": 5, "peer_number": "15282318670"},
                            "top3": {"call_cnt": 2, "peer_number": "4006103721"}},
            "top_item_6m": {"top1": {"call_cnt": 19, "peer_number": "15282318670"},
                            "top2": {"call_cnt": 10, "peer_number": "18183258220"},
                            "top3": {"call_cnt": 6, "peer_number": "4008004462"}}}, "V03_1048": "1", "V03_1049": "1",
            "V03_1050": "1", "V03_1055": "190", "V03_1057": "1", "V03_1058": "1", "V03_1060": "1", "V03_1061": "1"},
    "jingdong": {"V04_1002": "345", "V04_1005": "3000", "V04_1008": "2000", "V04_1009": "1",
                 "V04_1010": "2017-06-05 12:44:33", "V04_1011": "2017-06-05 12:44:33",
                 "V04_1012": "2017-06-05 12:44:33", "V04_1015": "30", "V04_1018": "20", "V04_1020": "1",
                 "V04_1021": {"135****1045": 4, "176****0604": 10}, "V04_1024": "222", "V04_1025": "是"},
    "taobao": {"V05_1006": "已认证", "V05_1009": "1234", "V05_1010": "124", "V05_1014": "3",
               "V05_1015": "2017-06-05 12:44:33", "V05_1016": "2017-06-05 12:44:33", "V05_1017": "2017-06-05 12:44:33",
               "V05_1023": "3", "V05_1026": "11", "V05_1028": "1", "V05_1029": {"13500001045": 4, "17600000604": 10},
               "V05_1032": "22"},
    "basicinfo": {"V01_1006": "20200202", "V01_1003": "汉", "V01_1002": "1", "V01_1001": 23, "V01_1014": "20190202",
                  "V01_1004": "123456789112345678", "V01_1007": "已婚", "V01_1008": "18383838383",
                  "V01_1009": "18483838383", "V01_1010": "noreport", "V01_1016": "0.9", "V01_1018": "18383838383",
                  "V01_2001": "初中及以下"},
    "xuexin": {"V08_1005": "123456789112345678", "V08_1017": "毕业", "V08_1020": "全日制"}}


def special(param, key, value):
    """
    处理特殊规则
    :param param:
    :param key: 规则key值
    :param value: 修改规则值
    :return:
    """
    if key in ['V04_1010', 'V04_1011', 'V04_1012', 'V05_1015', 'V05_1016', 'V05_1017']:
        # value 传入数据格式 int 如5，-7
        return TimeFormat.get_day_start_time(FileUtils.str_to_num(value))
    elif key in ['V01_3001', 'V01_3002', 'V01_1001']:
        # value 传入数据格式 int 如5，-7 , 0.0, 0.1
        return FileUtils.str_to_num(value)
    elif key == 'V03_1045':
        V03_1045 = dict(param["yys"]["V03_1045"])
        # value 传入数据格式 phone0;num0;phone1;num1
        phone_nums = re.split('[;；]', value)
        if len(phone_nums) == 2:
            phone0, num0 = phone_nums
            V03_1045["0"]["call_cnt_1m"] = num0
            V03_1045["0"]["peer_number"] = phone0
        elif len(phone_nums) == 4:
            phone0, num0, phone1, num1 = phone_nums
            V03_1045["0"]["call_cnt_1m"] = num0
            V03_1045["0"]["peer_number"] = phone0
            V03_1045["1"]["call_cnt_1m"] = num1
            V03_1045["1"]["peer_number"] = phone1
        return V03_1045
    elif key == 'V03_1046':
        # value传入格式phone1;phone2;phone3;phone1;phone2;phone3 , 修改top_item_3m和top_item_6m的3个peer_number
        V03_1046 = dict(param["yys"]["V03_1046"])
        phones = re.split('[;；]', value)
        if len(phones) == 1:
            V03_1046["top_item_3m"]["top1"]["peer_number"] = phones[0]
        elif len(phones) == 3:
            top1, top2, top3 = phones
            V03_1046["top_item_3m"]["top1"]["peer_number"] = top1
            V03_1046["top_item_3m"]["top2"]["peer_number"] = top2
            V03_1046["top_item_3m"]["top3"]["peer_number"] = top3
        elif len(phones) == 6:
            top1, top2, top3, top11, top12, top13 = phones
            V03_1046["top_item_3m"]["top1"]["peer_number"] = top1
            V03_1046["top_item_3m"]["top2"]["peer_number"] = top2
            V03_1046["top_item_3m"]["top3"]["peer_number"] = top3
            V03_1046["top_item_6m"]["top1"]["peer_number"] = top11
            V03_1046["top_item_6m"]["top2"]["peer_number"] = top12
            V03_1046["top_item_6m"]["top3"]["peer_number"] = top13
        return V03_1046
    elif key == 'V01_1010':
        if not re.sub('\s+', '', value):
            return str([{}])
        elif re.search('[;；]', value):
            # value 如果存在分号，则判定为传入的电话号码，生成对应的电话号码列表， phone1;phone2;phone3
            phones = re.split('[;；]', value)
            return str([{"name": "{}".format(fake.name()), "phones": [phone]} for phone in phones]).replace('\'', '\"')
        elif value.isdigit() and len(value) >= 4:
            # value 传入一个手机号
            return str([{"name": "{}".format(fake.name()), "phones": [value]}]).replace('\'', '\"')
        else:
            # value传入格式 int, 如果是数字，就生成响应数量的 随机号码数量
            return str([{"name": "{}".format(fake.name()), "phones": ["{}".format(fake.phone_number())]}
                        for _ in range(int(FileUtils.str_to_num(value)))]).replace('\'', '\"')
    elif key == 'V03_1002':
        return str(int(FileUtils.str_to_num(value)))
    elif key in ('V05_1029',  'V04_1021'):
        # value 传入数据格式 phone0;num0;phone1;num1
        if re.search('[;；]', value):
            phone_nums = re.split('[;；]', value)
            V05_1029 = dict()
            for i in range(0, len(phone_nums), 2):
                V05_1029[phone_nums[i]] = int(phone_nums[i + 1])
            return V05_1029
        else:
            return {}
    else:
        return value


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
        param[param_dict][param_key] = special(param, param_key, value)
    else:
        for k, v in param.items():
            if param_key in v.keys():
                param[k][param_key] = special(param, param_key, value)
                break


@ddt.ddt
class testAiapi23(TestBaseCase):
    @ddt.data(*ExcelUtil.read_excel_all_sheet(excel_path, 'Aiapi23machinReview.xlsx'))
    def test_Aiapi23_machine_review(self, data):
        LOGGER.info(data)
        LOGGER.info(('开始执行【{0}】第【{1}】条测试用例：【{2}】'.format(
            data['sheet'], data['序号'], data['描述'])).center(80, '-'))
        t1 = time.clock()
        params = copy.deepcopy(demo)
        if any(True if ext in data["修改key"] else False for ext in [',', '，']):
            keys = re.split('[,，]', re.sub('\s+', '', data["修改key"]))
            values = re.split('[,，]', re.sub('\s+', '', data["修改值"]))
            if len(keys) != len(values):
                raise IndexError("修改key 和修改值长度不一致，【{}】".format(data))
            for i in range(len(keys)):
                choose_sheet(params, data['sheet'], keys[i], values[i])
        else:
            choose_sheet(params, data['sheet'], data["修改key"], data["修改值"])
        rs = json.loads(AiapiAction.test_risk_strategy(
            data=params, scene_id=scene_id, version=version))
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
