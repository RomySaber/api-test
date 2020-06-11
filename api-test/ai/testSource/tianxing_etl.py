#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2020-05-18
@Author     : QA
@File       : tianxing_etl.py
@desc       : 
"""
import json
import time

import requests

from ai.testSource.etl_config import tianxing_etl
from common.myCommon import Assertion, TimeFormat
from common.myCommon.Logger import getlog
from common.myConfig import ConfigUtils

rq = requests.Session()
LOGGER = getlog(__name__)
TIMEOUT = ConfigUtils.getint('report', 'time_out')
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
baseUrl = 'http://192.168.15.247:5128'


def request_etl_tianxing(request_data):
    """
    天行ETL接口
    :param request_data: 请求数据
    :return: response.text
    """
    start_time = time.time()
    requesturl = baseUrl + "/etl_tianxing"
    request_data = json.dumps(request_data)
    LOGGER.info("天行ETL接口请求地址:【{}】".format(requesturl))
    LOGGER.info("天行ETL接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("天行ETL接口请求参数：【{}】".format(request_data))
    response = rq.post(requesturl, data=request_data, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.json()


def get_data(times):
    start_time = tianxing_etl['json_data']['data']['report_time']
    start = start_time.split(' ')[0]
    if times == '1' or times == 1:
        end = TimeFormat.get_day_around(-27, start)
    elif times == '3' or times == 3:
        end = TimeFormat.get_month_ago(2, start_time)
    elif times == '6' or times == 6:
        end = TimeFormat.get_month_ago(5, start_time)
    elif times == '7' or times == 7:
        end = TimeFormat.get_day_around(-6, start)
    elif times == '12' or times == 12:
        end = TimeFormat.get_month_ago(11, start_time)
    else:
        end = TimeFormat.get_month_ago(8, start_time)
    return end


def modif_application_data(data, modif_key, modif_value):
    """
    修改申请分
    :param data:
    :param modif_key:
        count: 次数
        bank: 银行，非银行
        time: 时间，1,3,6,7,12
    :param modif_value:
    :return:
    """
    if modif_key == 'count':
        tmp = data['loanApplicationDetails']
        data['loanApplicationDetails'] = [tmp[0] for _ in range(int(modif_value))]
    elif modif_key == 'bank':
        data['loanApplicationDetails'][0]['type'] = modif_value
    elif modif_key == 'time':
        data['loanApplicationDetails'][0]['time'] = get_data(int(modif_value))


def modif_registration_data(data, modif_key, modif_value):
    """
    修改注册分
    :param data:  修改数据
    :param modif_key: 修改值
        count: 次数
        bank: 银行，非银行
        time: 时间，1,3,6,7,12
    :param modif_value: 修改参数
    :return:
    """
    if modif_key == 'count':
        tmp = data['creditPlatformRegistrationDetails']
        data['creditPlatformRegistrationDetails'] = [tmp[0] for _ in range(int(modif_value))]
    elif modif_key == 'bank':
        data['creditPlatformRegistrationDetails'][0]['type'] = modif_value
    elif modif_key == 'time':
        data['creditPlatformRegistrationDetails'][0]['time'] = get_data(int(modif_value))


def modif_loanDetails_data(data, modif_key, modif_value):
    """
    修改 批核分-放贷
    :param data:  修改数据
    :param modif_key: 修改值
        count: 次数
        time: 时间，1,3,6,7,12
    :param modif_value: 修改参数
    :return:
    """
    if modif_key == 'count':
        tmp = data['loanDetails']
        data['loanDetails'] = [tmp[0] for _ in range(int(modif_value))]
    elif modif_key == 'time':
        data['loanDetails'][0]['time'] = get_data(int(modif_value))


def modif_loanRejectDetails_data(data, modif_key, modif_value):
    """
    修改 批核分-拒绝
    :param data:  修改数据
    :param modif_key: 修改值
        count: 次数
        time: 时间，1,3,6,7,12
    :param modif_value: 修改参数
    :return:
    """
    if modif_key == 'count':
        tmp = data['loanRejectDetails']
        data['loanRejectDetails'] = [tmp[0] for _ in range(int(modif_value))]
    elif modif_key == 'time':
        data['loanRejectDetails'][0]['time'] = get_data(int(modif_value))


def modif_overdue_data(data, modif_key, modif_value):
    """
    修改 还款分
    :param data:  修改数据
    :param modif_key: 修改值
        count: 次数
        money: 还款分金额区间最大金额
    :param modif_value: 修改参数
    :return:
    """
    if modif_key == 'count':
        data['overduePlatformDetails'][0]['counts'] = modif_value
    elif modif_key == 'money':
        data['overduePlatformDetails'][0]['money'] = "0W～{}W".format(int(modif_value)/10000)


def modif_blacklist_data(data, modif_key, modif_value):
    """
    修改 黑名单分
    :param data:  修改数据
    :param modif_key: 修改值
        ktggResultSize：命中开庭公告,1,0
        zxggResultSize： 被执行命中,1,0
        sxggResultSize： 失信名单命中,1,0
        fyggResultSize： 命中法院公告,1,0
        wdhmdResultSize： 命中网贷黑名单,1,0
        bgtResultSize： 命中曝光台,1,0
        status： 命中结案,结案
        all : 修改全部为0或1
    :param modif_value: 修改参数
    :return:
    """
    keys = ['ktggResultSize', 'zxggResultSize', 'sxggResultSize', 'fyggResultSize', 'wdhmdResultSize',
                     'bgtResultSize']
    if modif_key in keys:
        data['statistic'][modif_key] = int(modif_value)
    elif modif_key == 'status':
        data_index = 0
        pageDatas = data['pageData']
        for page in pageDatas:
            if page['dataType'] == 'AJLC':
                data_index = pageDatas.index(page)
        pageDatas[data_index]['status'] = modif_value
    elif modif_key == 'all':
        for k in keys:
            data['statistic'][k] = int(modif_value)
        data_index = 0
        pageDatas = data['pageData']
        for page in pageDatas:
            if page['dataType'] == 'AJLC':
                data_index = pageDatas.index(page)
        if modif_value == '1':
            pageDatas[data_index]['status'] = '结案'


def modif_data(data, modif_type, modif_key, modif_value):
    """
    修改天行ETL请求数据
    :param data:  原始请求数据
    :param modif_type:  修改数据类型
    :param modif_key:  修改key
    :param modif_value:  修改值
    :return:
    """
    B = data['json_data']['data']['report']['B']
    A = data['json_data']['data']['report']['A']
    if modif_type == 'application':
        modif_application_data(B, modif_key, modif_value)
    elif modif_type == 'registration':
        modif_registration_data(B, modif_key, modif_value)
    elif modif_type == 'loanDetails':
        modif_loanDetails_data(B, modif_key, modif_value)
    elif modif_type == 'loanRejectDetails':
        modif_loanRejectDetails_data(B, modif_key, modif_value)
    elif modif_type == 'overdue':
        modif_overdue_data(B, modif_key, modif_value)
    elif modif_type == 'blacklist':
        modif_blacklist_data(A, modif_key, modif_value)


def get_result(result_data, modif_type, modif_time, result_key):
    """
    获取单项结果
    :param result_data: 请求结果
    :param modif_type:  修改类型
    :param modif_time:  时间
    :param result_key: 断言结果
    :return:
    """
    m_type = {"1": "1m", "3": "3m", "6": "6m", "7": "7d", "12": "7_12m"}
    score = result_data['score_data']['original_score_dict']
    result = None
    if modif_type in ('application', 'registration'):
        result = score[modif_type][m_type[modif_time]][result_key]
    elif modif_type in ('loanDetails', 'loanRejectDetails'):
        result = score['loanAndReject'][m_type[modif_time]][result_key]
    elif modif_type in ('overdue', 'blacklist'):
        result = score[modif_type][result_key]
    return result


def assert_result(result_data):
    """
    结果内部数据检查
    :param result_data:
    :return:
    """
    orig = result_data['score_data']['original_score_dict']
    stat = result_data['score_data']['score_stat_dict']
    sum_score = lambda x: sum(x.values())
    sum_all = lambda x: sum([sum(y.values()) for y in x.values()])
    Assertion.verity(stat['application']['1m_score'], sum_score(orig['application']['1m']))
    Assertion.verity(stat['application']['3m_score'], sum_score(orig['application']['3m']))
    Assertion.verity(stat['application']['6m_score'], sum_score(orig['application']['6m']))
    Assertion.verity(stat['application']['7_12m_score'], sum_score(orig['application']['7_12m']))
    Assertion.verity(stat['application']['7d_score'], sum_score(orig['application']['7d']))
    Assertion.verity(stat['application_score'], sum_all(orig['application']))
    Assertion.verity(stat['application_score'], sum_score(stat['application']))
    Assertion.verity(stat['blacklist_score'], sum_score(orig['blacklist']))
    Assertion.verity(stat['loanAndReject']['1m_score'], sum_score(orig['loanAndReject']['1m']))
    Assertion.verity(stat['loanAndReject']['3m_score'], sum_score(orig['loanAndReject']['3m']))
    Assertion.verity(stat['loanAndReject']['6m_score'], sum_score(orig['loanAndReject']['6m']))
    Assertion.verity(stat['loanAndReject']['7_12m_score'], sum_score(orig['loanAndReject']['7_12m']))
    Assertion.verity(stat['loanAndReject']['7d_score'], sum_score(orig['loanAndReject']['7d']))
    Assertion.verity(stat['loanAndReject_score'], sum_all(orig['loanAndReject']))
    Assertion.verity(stat['loanAndReject_score'], sum_score(stat['loanAndReject']))
    Assertion.verity(stat['overdue_score'], sum_score(orig['overdue']))
    Assertion.verity(stat['registration']['1m_score'], sum_score(orig['registration']['1m']))
    Assertion.verity(stat['registration']['3m_score'], sum_score(orig['registration']['3m']))
    Assertion.verity(stat['registration']['6m_score'], sum_score(orig['registration']['6m']))
    Assertion.verity(stat['registration']['7_12m_score'], sum_score(orig['registration']['7_12m']))
    Assertion.verity(stat['registration']['7d_score'], sum_score(orig['registration']['7d']))
    Assertion.verity(stat['registration_score'], sum_all(orig['registration']))
    Assertion.verity(stat['registration_score'], sum_score(stat['registration']))
    Assertion.verity(stat['final_score'], (stat['application_score'] + stat['blacklist_score'] +
                                           stat['loanAndReject_score'] + stat['overdue_score'] +
                                           stat['registration_score']))
    final_score, risk_suggest = stat['final_score'],  stat['risk_suggest']
    Assertion.verityTrue(0 <= final_score <= 840)
    if 0 <= final_score <= 60:
        Assertion.verity(risk_suggest, "建议通过")
    elif 61 <= final_score <= 120:
        Assertion.verity(risk_suggest, "建议人工审核")
    elif final_score >= 121:
        Assertion.verity(risk_suggest, "建议拒绝")
