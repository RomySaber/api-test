#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-10-21
@Author     : 罗林
@File       : operator_analysis.py
@desc       :  运营商ETL数据解析， 请求数据和结果数据解析
    请求参数有多个key值时，用 ； 分隔 ，如 open_month；idcard
    修改参数值对应多个key时 用；分隔，同一个key有多个修改值时用，分隔 如:total_size;duration 对应 1,2,上午；10
    断言结果 同上
"""
import copy
import random
import re

from common.myCommon import TimeFormat

carriers = {"联通": "CHINA_UNICOM", "移动": "CHINA_MOBILE", "电信": "CHINA_TELECOM"}


def get_time_step(time_day, time_step):
    # 前开后闭
    if time_step == '早晨':
        start_time, end_time = time_day + " " + "5:30:00", time_day + " " + "9:00:00"
    elif time_step == '上午':
        start_time, end_time = time_day + " " + "9:00:00", time_day + " " + "11:30:00"
    elif time_step == '中午':
        start_time, end_time = time_day + " " + "11:30:00", time_day + " " + "13:30:00"
    elif time_step == '下午':
        start_time, end_time = time_day + " " + "13:30:00", time_day + " " + "17:30:00"
    elif time_step == '傍晚':
        start_time, end_time = time_day + " " + "17:30:00", time_day + " " + "19:30:00"
    elif time_step == '晚上':
        start_time, end_time = time_day + " " + "19:30:00", time_day + " " + "23:30:00"
    elif time_step == '凌晨':
        start_time1, end_time1 = time_day + " " + "23:30:00", time_day + " " + "23:59:59"
        start_time2, end_time2 = time_day + " " + "00:00:00", time_day + " " + "01:30:00"
        start_time, end_time = random.choice(((start_time1, end_time1), (start_time2, end_time2)))
    elif time_step == '深夜':
        start_time, end_time = time_day + " " + "01:30:00", time_day + " " + "05:30:00"
    else:
        start_time, end_time = time_day + " " + "13:30:00", time_day + " " + "17:30:00"
    e_time = TimeFormat.random_time(start_time, end_time)
    e_day, e_hms = e_time.split(' ')
    now = TimeFormat.getnow()
    n_hms = now.split(' ')[-1]
    e_time_num = int(TimeFormat.string_toTimestamp_13(e_time))
    n_time_num = int(TimeFormat.string_toTimestamp_13(e_day + ' ' + n_hms))
    if e_time_num <= n_time_num:
        e_time = TimeFormat.get_day_around(1, e_day) + ' ' + e_hms
    return e_time


def get_time_step2(time_day, time_step):
    # 前开后闭
    if time_step == '早晨':
        start_time, end_time = time_day + " " + "5:30:00", time_day + " " + "11:30:00"
    elif time_step == '中午':
        start_time, end_time = time_day + " " + "11:30:00", time_day + " " + "13:30:00"
    elif time_step == '下午':
        start_time, end_time = time_day + " " + "13:30:00", time_day + " " + "17:30:00"
    elif time_step == '晚上':
        start_time, end_time = time_day + " " + "17:30:00", time_day + " " + "23:30:00"
    elif time_step == '凌晨':
        start_time1, end_time1 = time_day + " " + "23:30:00", time_day + " " + "23:59:59"
        start_time2, end_time2 = time_day + " " + "00:00:00", time_day + " " + "05:30:00"
        start_time, end_time = random.choice(((start_time1, end_time1), (start_time2, end_time2)))
    else:
        start_time, end_time = time_day + " " + "13:30:00", time_day + " " + "17:30:00"
    e_time = TimeFormat.random_time(start_time, end_time)
    e_day, e_hms = e_time.split(' ')
    now = TimeFormat.getnow()
    n_hms = now.split(' ')[-1]
    e_time_num = int(TimeFormat.string_toTimestamp_13(e_time))
    n_time_num = int(TimeFormat.string_toTimestamp_13(e_day + ' ' + n_hms))
    if e_time_num <= n_time_num:
        e_time = TimeFormat.get_day_around(1, e_day) + ' ' + e_hms
    return e_time


def get_time_step07(time_day):
    # 前开后闭
    start_time, end_time = time_day + " " + "00:00:00", time_day + " " + "07:00:00"
    e_time = TimeFormat.random_time(start_time, end_time)
    e_day, e_hms = e_time.split(' ')
    now = TimeFormat.getnow()
    n_hms = now.split(' ')[-1]
    e_time_num = int(TimeFormat.string_toTimestamp_13(e_time))
    n_time_num = int(TimeFormat.string_toTimestamp_13(e_day + ' ' + n_hms))
    if e_time_num <= n_time_num:
        e_time = TimeFormat.get_day_around(1, e_day) + ' ' + e_hms
    return e_time


def get_days(month, premise, params):
    """
    几月距离今天的天数
    :param month:  几月
    :param premise:  请求参数
    :param params:  请求参数
    :return:
    """
    calls_items = list()
    for items in params['calls']:
        calls_items.extend(items['items'])
    calls_days = list()
    if premise == 'no_dial_day':
        dial_calls_days = list(filter(lambda x: x['dial_type'] == 'dial', calls_items))
        calls_days = [t['time'] for t in dial_calls_days]
    elif premise == 'no_call_day':
        calls_days = [t['time'] for t in calls_items]
    elif premise in ('power_off_day', 'continue_power_off_days'):
        calls_days = [t['time'] for t in calls_items]
        smses_items = list()
        for items in params['smses']:
            smses_items.extend(items['items'])
        smses_days = ['-'.join(t['time'].split('-')[:3]) + ' ' + t['time'].split('-')[-1] for t in smses_items]
        calls_days.extend(smses_days)
    on_days = list(set(calls_days))
    now, times = TimeFormat.getnow().split(' ')
    now_time = TimeFormat.get_now_time_13()
    if month == '7':
        day = TimeFormat.get_day_around(-7)
    else:
        time_day = TimeFormat.get_month_ago(int(month))
        day = time_day.split(' ')[0]
    day_time = TimeFormat.string_toTimestamp_13(day + ' ' + times)
    days_num = len(list(
        filter(lambda x: day_time < int(TimeFormat.string_toTimestamp_13(x)) <= now_time, on_days)))
    return str(TimeFormat.time_between_day(day, now) - days_num)


def modif_date(data):
    """
    初始化请求时修改时间
    :param data:
    :return:
    """
    sev_time = TimeFormat.get_month_ago(1)
    sev_month = '-'.join(sev_time.split('-')[:2])
    sev_day = sev_time.split(' ')[0]
    sev_hms = data["calls"][0]['items'][0]['time'].split(' ')[-1]
    month_start_date, month_end_date = TimeFormat.get_FirstAndLastDay_month(sev_day)
    time_sec = sev_day + ' ' + sev_hms
    data["bills"][0]['bill_month'] = sev_month
    data["bills"][0]['bill_start_date'] = month_start_date
    data["bills"][0]['bill_end_date'] = month_end_date
    data["calls"][0]['bill_month'] = sev_month
    data["calls"][0]['items'][0]['time'] = time_sec
    data["smses"][0]['bill_month'] = sev_month
    data["smses"][0]['items'][0]['time'] = time_sec.replace(' ', '-')


def modif(data, modif_key, modif_value):
    """
    修改请求数据
    :param data: 请求数据
    :param modif_key:  修改请求数据参数
    :param modif_value: 修改值
    :return:
    carrier: 运营商类型 （联通、移动、电信）
    open_time: 开户时长 （天）
    sex：男，女
    age： 年龄
    total_fee：账期内所有费用
    web_fee：网络流量消费金额（分）
    voice_fee：通话消费金额（分）
    sms_fee：短信消费金额（分）
    extra_service_fee：增值业务消费金额（分）
    extra_fee：其它消费金额（分）
    base_fee：基础消费金额
    sms_cnt：短信次数 （数字）
    sms_fees：短信费用
    location：朋友圈中心城市
    peer_number：朋友联系数量
    location_type：号码类型;国内通话
    dial_type：主叫，被叫 DAIL,DAILED
    duration: 通话时长(秒)
    fee: 通话费用
    time: 通话时段 (早晨,上午,中午,下午,傍晚,晚上,凌晨,深夜)
        早晨(5:30:00-9:00:00)
        上午(9:00:00-11:30:00)
        中午(11:30:00-13:30:00)
        下午(13:30:00-17:30:00)
        傍晚(17:30:00-19:30:00)
        晚上(19:30:00-23:30:00)
        凌晨(23:30:00-01:30:00)
        深夜(01:30:00-05:30:00)
    time2: 通话时段
        早晨（5:30-11:30）
        中午（11:30-13:30）
        下午（13:30-17:30）
        晚上（17:30-23:30）
        凌晨（23:30-5:30）
    time3: 通话时段 0-7点，不用输入参数修改值
    total_size：通话次数
    bill_month：通话月份 （7,1,3,6）
    calls: 通话信息条数 （数字）
    """
    if re.sub('\s+', '', modif_value) == '':
        modif_value = 'null'
    if modif_key == 'carrier':
        # modif_value 输入 联通、移动、电信
        if modif_value in carriers.keys():
            modif_value = carriers[modif_value]
        data["carrier"] = modif_value
    elif modif_key == 'open_time':
        # 输入数字，距离当前时间的天数
        if modif_value.isdigit():
            modif_value = TimeFormat.get_day_around(-int(modif_value))
        data["open_time"] = modif_value
    elif modif_key == 'sex':
        # 输入男、女，自动生成 idcard
        idcard = list(data["idcard"])
        if modif_value == '女':
            v = random.choice('02468')
            idcard[16] = str(v)
            data["idcard"] = ''.join(idcard)
        elif modif_value == '男':
            v = random.choice('13579')
            idcard[16] = str(v)
            data["idcard"] = ''.join(idcard)
        else:
            data["idcard"] = modif_value
    elif modif_key == 'age':
        # 输入年龄，自动生成 idcard
        if modif_value.isdigit():
            idcard = list(data["idcard"])
            time_now = TimeFormat.getnow_day()
            year, month, day = time_now.split('-')
            y = int(year) - int(modif_value)
            idcard[6:14] = ''.join([str(y), month, day])
            data["idcard"] = ''.join(idcard)
        else:
            data["idcard"] = modif_value
    elif modif_key == 'city':
        data["city"] = modif_value
    elif modif_key == 'total_fee':
        data["bills"][0]["total_fee"] = modif_value
    elif modif_key == 'web_fee':
        data["bills"][0]["web_fee"] = modif_value
    elif modif_key == 'voice_fee':
        data["bills"][0]["voice_fee"] = modif_value
    elif modif_key == 'sms_fee':
        data["bills"][0]["sms_fee"] = modif_value
    elif modif_key == 'extra_service_fee':
        data["bills"][0]["extra_service_fee"] = modif_value
    elif modif_key == 'extra_fee':
        data["bills"][0]["extra_fee"] = modif_value
    elif modif_key == 'base_fee':
        data["bills"][0]["base_fee"] = modif_value
    elif modif_key == 'sms_cnt':
        # 输入数字， 自动生成对应数字的短信条数
        if modif_value.isdigit():
            sms = data['smses'][0]
            data['smses'] = [sms for _ in range(int(modif_value))]
        else:
            data['smses'] = []
    elif modif_key == 'sms_fees':
        data['smses'][0]['items'][0]['fee'] = modif_value
    elif modif_key == 'location':
        data["calls"][0]['items'][0]['location'] = modif_value
    elif modif_key == 'peer_number':
        data["calls"][0]['items'][0]['peer_number'] = modif_value
    elif modif_key == 'location_type':
        data["calls"][0]['items'][0]['location_type'] = modif_value
    elif modif_key == 'dial_type':
        # 输入 DAIL 或者 DAILED
        calls = data["calls"][0]
        call = copy.deepcopy(calls)
        call['items'][0]['dial_type'] = modif_value
        data["calls"][0] = call
    elif modif_key == 'duration':
        if modif_value.isdigit():
            modif_value = int(modif_value)
        data["calls"][0]['items'][0]['duration'] = modif_value
    elif modif_key == 'fee':
        data["calls"][0]['items'][0]['fee'] = modif_value
    elif modif_key == 'time':
        # 输入时间段
        #         早晨(5:30:00-9:00:00)
        #         上午(9:00:00-11:30:00)
        #         中午(11:30:00-13:30:00)
        #         下午(13:30:00-17:30:00)
        #         傍晚(17:30:00-19:30:00)
        #         晚上(19:30:00-23:30:00)
        #         凌晨(23:30:00-01:30:00)
        #         深夜(01:30:00-05:30:00)
        if modif_value in ('早晨', '上午', '中午', '下午', '傍晚', '晚上', '凌晨', '深夜'):
            sev_time = data["calls"][0]['items'][0]['time']
            sev_day = sev_time.split(' ')[0]
            data["calls"][0]['items'][0]['time'] = get_time_step(sev_day, modif_value)
        else:
            data["calls"][0]['items'][0]['time'] = modif_value
    elif modif_key == 'time2':
        # 输入时间段
        #         早晨（5:30-11:30）
        #         中午（11:30-13:30）
        #         下午（13:30-17:30）
        #         晚上（17:30-23:30）
        #         凌晨（23:30-5:30）
        if modif_value in ('早晨', '中午', '下午', '晚上', '凌晨'):
            sev_time = data["calls"][0]['items'][0]['time']
            sev_day = sev_time.split(' ')[0]
            data["calls"][0]['items'][0]['time'] = get_time_step2(sev_day, modif_value)
        else:
            data["calls"][0]['items'][0]['time'] = modif_value
    elif modif_key == 'time3':
        # 输入时间段， 不用输入修改参数值， 直接获取 0-7点
        sev_time = data["calls"][0]['items'][0]['time']
        sev_day = sev_time.split(' ')[0]
        data["calls"][0]['items'][0]['time'] = get_time_step07(sev_day)
    elif modif_key == 'total_size':
        if modif_value.isdigit():
            modif_value = int(modif_value)
        data["calls"][0]['total_size'] = modif_value
    elif modif_key == 'bill_month':
        # 输入修改的月份 7,1,3,6； 7代表7天，其余的都是月份
        times = data["calls"][0]['items'][0]['time']
        time_hmc = times.split(' ')[-1]
        if modif_value == '7':
            start_day = TimeFormat.get_day_around(-7)
            bill_month = '-'.join(start_day.split('-')[:2])
            month_start_date, month_end_date = TimeFormat.get_FirstAndLastDay_month(bill_month)
            e_time = start_day + ' ' + time_hmc
            e_time_num = int(TimeFormat.string_toTimestamp_13(e_time))
            n_hms = TimeFormat.getnow().split(' ')[-1]
            n_time_num = int(TimeFormat.string_toTimestamp_13(start_day + ' ' + n_hms))
            if e_time_num <= n_time_num:
                e_time = TimeFormat.get_day_around(1, start_day) + ' ' + time_hmc
            data["calls"][0]['bill_month'] = bill_month
            data["calls"][0]['items'][0]['time'] = e_time
            data["smses"][0]['bill_month'] = bill_month
            data["smses"][0]['items'][0]['time'] = e_time.replace(' ', '-')
            data["bills"][0]['bill_month'] = bill_month
            data["bills"][0]['bill_start_date'] = month_start_date
            data["bills"][0]['bill_end_date'] = month_end_date
        elif modif_value in ('1', '3', '6'):
            month_day = TimeFormat.get_month_day_ago(int(modif_value))
            year, month, day = month_day.split('-')
            bill_month = year + '-' + month
            month_start_date, month_end_date = TimeFormat.get_FirstAndLastDay_month(bill_month)
            data["calls"][0]['bill_month'] = bill_month
            e_time = month_day + ' ' + time_hmc
            e_time_num = int(TimeFormat.string_toTimestamp_13(e_time))
            n_hms = TimeFormat.getnow().split(' ')[-1]
            n_time_num = int(TimeFormat.string_toTimestamp_13(month_day + ' ' + n_hms))
            if e_time_num <= n_time_num:
                e_time = TimeFormat.get_day_around(1, month_day) + ' ' + time_hmc
            data["calls"][0]['items'][0]['time'] = e_time
            data["smses"][0]['bill_month'] = bill_month
            data["smses"][0]['items'][0]['time'] = e_time.replace(' ', '-')
            data["bills"][0]['bill_month'] = bill_month
            data["bills"][0]['bill_start_date'] = month_start_date
            data["bills"][0]['bill_end_date'] = month_end_date
        else:
            data["calls"][0]['bill_month'] = modif_value
            data["smses"][0]['bill_month'] = modif_value
            data["bills"][0]['bill_month'] = modif_value
    elif modif_key == 'calls':
        # 输入数字，自动生成通话条数
        if modif_value.isdigit():
            calls = data["calls"][0]
            call = copy.deepcopy(calls)
            data["calls"] = [call for _ in range(int(modif_value))]
        else:
            data["calls"] = []


def get_result(result_json, result_key, premise=None):
    """
    获取对应字段返回值
    :param result_json:  请求结果json
    :param result_key:  修改的字段值
        结果检查项
        sex:性别
        age:年龄
        open_month:开户时长
        call_month:月份
        sms_cnt:短信次数
        call_time:通话时长（秒）
        dial_time:主叫时长（秒）
        dialed_time:被叫时长（秒）
        sms_fees:短信费用
        call_fees:通话费用
        call_cnt_1w:近1周通话次数
        call_cnt_1m:近1月通话次数
        call_cnt_3m:近3月通话次数
        call_cnt_6m:近6月通话次数
        duration_7d:近1周通话时长
        duration_1m:近1月通话时长
        duration_3m:近3月通话时长
        duration_6m:近6月通话时长
        dial_cnt_7d:近1周主叫次数
        dial_cnt_1m:近1月主叫次数
        dial_cnt_3m:近3月主叫次数
        dial_cnt_6m:近6月主叫次数
        dialed_cnt_7d:近1周被叫次数
        dialed_cnt_1m:近1月被叫次数
        dialed_cnt_3m:近3月被叫次数
        dialed_cnt_6m:近6月被叫次数
        call_cnt_morning_7d:近1周早晨通话次数
        call_cnt_morning_1m:近1月早晨通话次数
        call_cnt_morning_3m:近3月早晨通话次数
        call_cnt_morning_6m:近6月早晨通话次数
        call_cnt_noon_7d:近1周中午通话次数
        call_cnt_noon_1m:近1月中午通话次数
        call_cnt_noon_3m:近3月中午通话次数
        call_cnt_noon_6m:近6月中午通话次数
        call_cnt_afternoon_7d:近1周下午通话次数
        call_cnt_afternoon_1m:近1月下午通话次数
        call_cnt_afternoon_3m:近3月下午通话次数
        call_cnt_afternoon_6m:近6月下午通话次数
        call_cnt_evening_7d:近1周晚上通话次数
        call_cnt_evening_1m:近1月晚上通话次数
        call_cnt_evening_3m:近3月晚上通话次数
        call_cnt_evening_6m:近6月晚上通话次数
        call_cnt_night_7d:近1周凌晨通话次数
        call_cnt_night_1m:近1月凌晨通话次数
        call_cnt_night_3m:近3月凌晨通话次数
        call_cnt_night_6m:近6月凌晨通话次数
        contact_night_cnt_pct_1m:近一月夜间通话次数百分比
        contact_night_cnt_pct_3m:近三月夜间通话次数百分比
        contact_night_cnt_pct_6m:近六月夜间通话次数百分比
        latest_call_hour:最近一次通话距今时间（h）

        friend_num:朋友联系数量(1,3,6个月)
        good_friend_num:好朋友联系数量（联系10次以上）(1,3,6个月)
        friend_city_center:朋友圈中心城市(1,3,6个月)
        is_city_match_friend_city_center:朋友圈中心地是否与手机归属地一致(1,3,6个月)
        inter_peer_num:互通电话号码数目(1,3,6个月)
        peer_number:对方号码(1,3,6个月的top1)
        location:通话地(1,3,6个月的top1)
        location_type:号码类型(1,3,6个月的top1)
        call_cnt:通话次数(1,3,6个月的top1)
        duration:通话时长(秒)(1,3,6个月的top1)
        call_cnt_morning:早晨通话次数(1,3,6个月的top1)
        call_cnt_noon:中午通话次数(1,3,6个月的top1)
        call_cnt_afternoon:下午通话次数(1,3,6个月的top1)
        call_cnt_evening:晚上通话次数(1,3,6个月的top1)
        call_cnt_night:凌晨通话次数(1,3,6个月的top1)
        region_uniq_num_cnt:通话号码数(1,3,6个月的top1)
        region_call_cnt:通话次数(1,3,6个月的top1)
        region_call_time:通话时长（秒）(1,3,6个月的top1)
        region_dial_cnt:主叫次数(1,3,6个月的top1)
        region_dialed_cnt:被叫次数(1,3,6个月的top1)
        region_dial_time:主叫时长(秒)(1,3,6个月的top1)
        region_dialed_time:被叫时长（秒）(1,3,6个月的top1)
        region_avg_dial_time:平均主叫时长(1,3,6个月的top1)
        region_avg_dialed_time:平均被叫时长(1,3,6个月的top1)
        region_dialed_cnt_pct:主叫次数占比(1,3,6个月的top1)
        region_dialed_cnt_pct:被叫次数占比(1,3,6个月的top1)
        region_dial_time_pct:主叫时长占比(1,3,6个月的top1)
        region_dialed_time_pct:被叫时长占比(1,3,6个月的top1)

        app_point_zh：分析项（中文）（和分析项搭配使用）
        item_1m：近1月数量（和分析项搭配使用）
        item_3m：近3月数量（和分析项搭配使用）
        item_6m：近6月数量（和分析项搭配使用）
        avg_item_3m： 近3月平均数量（和分析项搭配使用）
        avg_item_6m： 近6月平均数量（和分析项搭配使用）

        time_step_zh:时间段 (需要和月，时间段配合使用)
        total_cnt:通话次数 (需要和月，时间段配合使用)
        uniq_num_cnt:通话号码数 (需要和月，时间段配合使用)
        duration:通话时长(需要和月，时间段配合使用)
        dial_cnt:主叫次数 (需要和月，时间段配合使用)
        dialed_cnt:被叫次数 (需要和月，时间段配合使用)
        latest_call_time:最后一次通话时间 (需要和月，时间段配合使用)
        farthest_call_time:第一次通话时间 (需要和月，时间段配合使用)
    :param premise:  前提条件
        分析项
        1：1月数据
        3：3月数据
        6：6月数据

        call_day：通话活跃天数
        sms_day：短信活跃天数
        call_cnt：通话次数
        peer_num_cnt：通话号码数目
        peer_loc_cnt：通话号码归属地总数
        dial_cnt：主叫次数
        dialed_cnt：被叫次数
        dial_peer_num_cnt：主叫号码数
        dialed_peer_num_cnt：被叫号码数
        sms_cnt：短信次数
        call_time：通话时长（秒）
        dial_time：主叫时长（秒）
        dialed_time：被叫时长（秒）
        avg_call_time：均次通话时长（秒）
        no_dial_day：无呼出天数
        no_dial_day_pct：无呼出天数占比
        no_call_day：无通话天数
        no_call_day_pct：无通话天数占比
        max_power_on_day：最大连续开机天数
        power_off_day：关机天数
        power_off_day_pct：关机天数占比
        continue_power_off_cnt：连续3天以上关机次数
        continue_power_off_days：连续3天以上最大关机天数
        total_fee：消费总金额（分）
        net_fee：网络流量消费金额（分）
        voice_fee：通话消费金额（分）
        sms_fee：短信消费金额（分）
        vas_fee：增值业务消费金额（分）
        extra_fee：其它消费金额（分）

        morning:早晨[5:30-9:00]（需要与月份配合使用，如noon-1）
        forenoon:上午[9:00-11:30]（需要与月份配合使用，如noon-1）
        noon:中午[11:30-13:30]（需要与月份配合使用，如noon-1）
        afternoon:下午[13:30-17:30]（需要与月份配合使用，如noon-1）
        dusk:傍晚[17:30-19:30]（需要与月份配合使用，如noon-1）
        evening:晚上[19:30-23:30]（需要与月份配合使用，如noon-1）
        daybreak:凌晨[23:30-1:30]（需要与月份配合使用，如noon-1）
        midnight:深夜[1:30-5:30]（需要与月份配合使用，如noon-1）

    :return:
    """
    result = result_json['result']
    if result_key == 'age':
        return result['etl_basicinfo']['age']
    elif result_key == 'open_month':
        return result['etl_basicinfo']['open_month']
    elif result_key == 'sex':
        return result['etl_basicinfo']['sex']
    elif result_key == 'call_cnt':
        behavior = str(int(result['etl_cell_behavior']['0']['call_cnt']))
        premise = 'top_item_{}m'.format(premise) if premise else 'top_item_1m'
        circle = str(int(result['etl_friend_circle']['peer_num_top'][premise]['top1']['call_cnt']))
        return behavior if behavior == circle else 'etl_cell_behavior and etl_friend_circle are difference'
    elif result_key in ('dial_cnt', 'dialed_cnt'):
        behavior = str(int(result['etl_cell_behavior']['0'][result_key]))
        if premise and '-' not in premise:
            top = 'top_item_{}m'.format(premise)
            circle = str(int(result['etl_friend_circle']['peer_num_top'][top]['top1'][result_key]))
            return behavior if behavior == circle else 'etl_cell_behavior and etl_friend_circle are difference'
        elif '-' in premise:
            p, n = premise.split('-')
            n_dict = {'1': 0, '3': 1, '6': 2}
            num = n_dict[n] if n in n_dict else 0
            top = 'top_item_{}m'.format(n) if premise else 'top_item_1m'
            circle = str(int(result['etl_friend_circle']['peer_num_top'][top]['top1'][result_key]))
            detail = str(int(result['etl_call_duration_detail'][num]['duration_list'][p][result_key].split('.')[0]))
            return behavior if behavior == circle == detail else 'etl_cell_behavior and etl_friend_circle and ' \
                                                                 'etl_call_duration_detail are difference'
        else:
            return behavior
    elif result_key == 'peer_number':
        premise = 'top_item_{}m'.format(premise) if premise else 'top_item_1m'
        friend_circle = result['etl_friend_circle']['peer_num_top'][premise]['top1']['peer_number']
        call_contact_detail = result['etl_call_contact_detail']['0']['peer_number']
        return friend_circle if friend_circle == call_contact_detail else \
            'etl_friend_circle and etl_call_duration_detail are difference'
    elif result_key == 'location':
        premise = premise if premise else 1
        num = 0
        contact_region = result['etl_contact_region']
        for contact in contact_region:
            if contact['key'] == 'contact_region_{}m'.format(premise):
                num = contact_region.index(contact)
        region = contact_region[num]['region_list']['0']['location']
        detail = result['etl_call_contact_detail']['0']['location']
        peer_num_top = result['etl_friend_circle']['peer_num_top']['top_item_{}m'.format(premise)]['top1']['location']
        location_top = result['etl_friend_circle']['location_top']['top_item_{}m'.format(premise)]['top1']['location']
        return peer_num_top if peer_num_top == location_top == region == detail else \
            'etl_friend_circle and etl_call_duration_detail and etl_contact_region are difference'
    elif premise and any(filter(premise.startswith,
                                ['morning', 'forenoon', 'noon', 'afternoon', 'dusk', 'evening', 'daybreak',
                                 'midnight'])):
        p, n = premise.split('-')
        n_dict = {'1': 0, '3': 1, '6': 2}
        num = n_dict[n] if n in n_dict else 0
        return result['etl_call_duration_detail'][num]['duration_list'][p][result_key]
    elif premise in ['call_day', 'sms_day', 'call_cnt', 'peer_num_cnt', 'peer_loc_cnt', 'dial_peer_num_cnt',
                     'dialed_peer_num_cnt', 'sms_cnt', 'call_time', 'dial_time', 'dialed_time', 'avg_call_time',
                     'no_dial_day', 'no_dial_day_pct', 'no_call_day', 'no_call_day_pct', 'max_power_on_day',
                     'power_off_day', 'power_off_day_pct', 'continue_power_off_cnt', 'continue_power_off_days',
                     'dial_cnt', 'dialed_cnt', "cnt_1min_within", "cnt_5min_within", "cnt_10min_within",
                     "cnt_10min_over", "continue_power_off_date_list"]:
        etl_active_degree = result['etl_active_degree']
        num = 0
        for app_point in etl_active_degree:
            if app_point['app_point'] == premise:
                num = etl_active_degree.index(app_point)
        if result_key == 'app_point_zh':
            return str(etl_active_degree[num][result_key])
        else:
            return str(etl_active_degree[num]['item'][result_key])
    elif premise in ['total_fee', 'net_fee', 'voice_fee', 'sms_fee', 'vas_fee', 'extra_fee', 'extra_service_fee']:
        etl_active_degree = result['etl_consumption_detail']
        num = 0
        for app_point in etl_active_degree:
            if app_point['app_point'] == premise:
                num = etl_active_degree.index(app_point)
        if result_key == 'app_point_zh':
            return str(etl_active_degree[num][result_key])
        else:
            return str(etl_active_degree[num]['item'][result_key])
    elif result_key in ['friend_num', 'good_friend_num', 'friend_city_center', 'is_city_match_friend_city_center',
                        'inter_peer_num']:
        premise_key = 'friend_circle_detail_{}m'.format(premise) if premise else 'friend_circle_detail_1m'
        return str(result['etl_friend_circle']['summary'][premise_key][result_key])
    elif result_key in ['peer_number', 'duration', 'call_cnt_morning', 'call_cnt_noon',
                        'call_cnt_afternoon', 'call_cnt_evening', 'call_cnt_night', 'smses_cnt']:
        premise = 'top_item_{}m'.format(premise) if premise else 'top_item_1m'
        return str(result['etl_friend_circle']['peer_num_top'][premise]['top1'][result_key])
    elif result_key in ["region_avg_dial_time", "region_avg_dialed_time", "region_call_cnt", "region_call_time",
                        "region_dial_cnt", "region_dial_time", "region_dialed_cnt", "region_dialed_time",
                        "region_dial_cnt_pct", "region_dial_time_pct", "region_dialed_cnt_pct",
                        "region_dialed_time_pct", "region_uniq_num_cnt"]:
        premise = premise if premise else 1
        num = 0
        contact_region = result['etl_contact_region']
        for contact in contact_region:
            if contact['key'] == 'contact_region_{}m'.format(premise):
                num = contact_region.index(contact)
        region = str(int(contact_region[num]['region_list']['0'][result_key].split('.')[0]))
        friend = str(int(result['etl_friend_circle']['location_top']['top_item_{}m'.format(
            premise)]['top1'][result_key].split('.')[0]))
        return friend if friend == region else 'etl_friend_circle and etl_contact_region are difference'
    elif result_key in ['call_month', 'sms_cnt', 'call_time', 'sms_fees', 'call_fees', 'total_fee']:
        return str(result['etl_cell_behavior']['0'][result_key])
    elif result_key in ['call_cnt_7d', 'call_cnt_1m', 'call_cnt_3m', 'call_cnt_6m', 'duration_7d', 'duration_1m',
                        'duration_3m', 'duration_6m', 'dial_cnt_7d', 'dial_cnt_1m', 'dial_cnt_3m', 'dial_cnt_6m',
                        'dialed_cnt_7d', 'dialed_cnt_1m', 'dialed_cnt_3m', 'dialed_cnt_6m', 'call_cnt_morning_7d',
                        'call_cnt_morning_1m', 'call_cnt_morning_3m', 'call_cnt_morning_6m', 'call_cnt_noon_7d',
                        'call_cnt_noon_1m', 'call_cnt_noon_3m', 'call_cnt_noon_6m', 'call_cnt_afternoon_7d',
                        'call_cnt_afternoon_1m', 'call_cnt_afternoon_3m', 'call_cnt_afternoon_6m',
                        'call_cnt_evening_7d', 'call_cnt_evening_1m', 'call_cnt_evening_3m', 'call_cnt_evening_6m',
                        'call_cnt_night_7d', 'call_cnt_night_1m', 'call_cnt_night_3m', 'call_cnt_night_6m',
                        "dial_cnt_7d", "dial_cnt_1m", "dial_cnt_3m", "dial_cnt_6m", "dialed_cnt_7d", "dialed_cnt_1m",
                        "dialed_cnt_3m", "dialed_cnt_6m", "first_call_time_7d", "first_call_time_1m",
                        "first_call_time_3m", "first_call_time_6m", "last_call_time_7d", "last_call_time_1m",
                        "last_call_time_3m", "last_call_time_6m", "smses_cnt_7d", "smses_cnt_1m", "smses_cnt_3m",
                        "smses_cnt_6m"]:
        return str(result['etl_call_contact_detail']['0'][result_key])
    elif result_key in ['contact_night_cnt_pct_1m', 'contact_night_cnt_pct_3m', 'contact_night_cnt_pct_6m',
                        'latest_call_hour', 'contact_night_cnt_1m', 'contact_night_cnt_3m', 'contact_night_cnt_6m']:
        return result['etl_behavior_check'][result_key]
    elif result_key in ['dial_time', 'dialed_time']:
        if premise:
            premise = 'top_item_{}m'.format(premise) if premise else 'top_item_1m'
            return str(result['etl_friend_circle']['peer_num_top'][premise]['top1'][result_key])
        else:
            return str(result['etl_cell_behavior']['0'][result_key])
