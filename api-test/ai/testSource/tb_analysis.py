#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-10-22
@Author     : 罗林
@File       : tb_analysis.py
@desc       :  淘宝ETL数据解析， 请求数据和结果数据解析
"""
import copy
import re

from common.myCommon import TimeFormat


def get_data(times=None):
    if times == '1':
        start = TimeFormat.get_month_ago(1)
        end = TimeFormat.get_day_end_time(-7)
    elif times == '3':
        start = TimeFormat.get_month_ago(3)
        end = TimeFormat.get_month_ago(2)
    elif times == '6':
        start = TimeFormat.get_month_ago(6)
        end = TimeFormat.get_month_ago(5)
    elif times == '9':
        start = TimeFormat.get_month_ago(9)
        end = TimeFormat.get_month_ago(7)
    elif times == '7':
        start, end = TimeFormat.get_day_start_time(-6), TimeFormat.get_day_start_time(-2)
    else:
        start, end = TimeFormat.get_day_start_time(-6), TimeFormat.get_day_start_time(-2)
    return start, end


def modif_date(data):
    """
    初始化请求时修改时间
    :param data:
    :return:
    """
    data['inserttime'] = TimeFormat.getnow()
    start, end = get_data()
    c_time = TimeFormat.random_time(start, end)
    data["tbBuyGoodsInfo"][0]["orderInfo"]['createTime'] = c_time


def modif(data, modif_key, modif_value):
    """
    修改 淘宝请求数据
    :param data: 请求数据
    :param modif_key: 请求数据修改参数
    :param modif_value: 请求值
    :return:
    certification ： 实名认证信息 名字-身份证-认证
    phone ：手机
    actualFee ： 总价	
    subOrders ： 商品总量 条数
    tbBuyGoodsInfo ： 淘宝订单记录	条数
    orderReceiverName ：订单收件人姓名	
    orderReceiverPhone ： 订单收件人电话号码	
    orderReceiverAddress ： 订单收件人地址	
    text ： 交易成功的订单
    postType ： 虚拟物品
    createTime ： 创建时间， 当前时间前的时间 1： 近1月， 3：近3月 ， 6： 近6月， 7 近一周
    """
    if modif_key == 'certification':
        n, c, r = modif_value.split('-')
        data["alipay_bindings"]["certification"] = "{0}\u00a0|\u00a0{1}\u00a0{2}".format(n, c, r)
    elif modif_key == 'phone':
        data['user_info']['phone'] = modif_value
    elif modif_key == "actualFee":
        data["tbBuyGoodsInfo"][0]["payInfo"]["actualFee"] = modif_value
    elif modif_key == "subOrders":
        subOrders = data["tbBuyGoodsInfo"][0]["subOrders"][0]
        data["tbBuyGoodsInfo"][0]["subOrders"] = [subOrders for _ in range(int(modif_value))]
    elif modif_key == "tbBuyGoodsInfo":
        tbBuyGoodsInfo = data["tbBuyGoodsInfo"][0]
        data["tbBuyGoodsInfo"] = [tbBuyGoodsInfo for _ in range(int(modif_value))]
    elif modif_key == 'orderReceiverName':
        data["tbBuyGoodsInfo"][0]["orderReceiver"]["orderReceiverName"] = modif_value
    elif modif_key == 'orderReceiverPhone':
        data["tbBuyGoodsInfo"][0]["orderReceiver"]["orderReceiverPhone"] = modif_value
    elif modif_key == 'orderReceiverAddress':
        data["tbBuyGoodsInfo"][0]["orderReceiver"]["orderReceiverAddress"] = modif_value
    elif modif_key == 'text':
        data["tbBuyGoodsInfo"][0]["statusInfo"]["text"] = modif_value
    elif modif_key == 'text1':
        tbBuyGoodsInfo = data["tbBuyGoodsInfo"][0]
        tb_order = copy.deepcopy(tbBuyGoodsInfo)
        tb_order["statusInfo"]["text"] = modif_value
        data["tbBuyGoodsInfo"][0] = tb_order
    elif modif_key == 'postType':
        data["tbBuyGoodsInfo"][0]["payInfo"]["postType"] = modif_value
    elif modif_key == "createTime":
        start, end = get_data(modif_value)
        data["tbBuyGoodsInfo"][0]["orderInfo"]['createTime'] = TimeFormat.random_time(start, end)
    elif modif_key == 'first_deal_time':
        start, end = get_data(modif_value)
        c_time = TimeFormat.random_time(start, end)
        data['first_deal_time'] = c_time


def get_result(data, result_key, params):
    """
    获取验证结果
    :param data:
    :param result_key:
    :param params:
    :return:
    name
    idcard
    account_auth
    order_sum_1m
    order_sum_3m
    order_sum_6m
    order_sum_amount_1m
    order_max_amount_1m
    order_avg_amount_1m
    order_sum_amount_3m
    order_max_amount_3m
    order_avg_amount_3m
    order_sum_amount_6m
    order_max_amount_6m
    order_avg_amount_6m
    order_sum_pkg_1m
    order_max_pkg_1m
    order_avg_pkg_1m
    order_sum_pkg_3m
    order_max_pkg_3m
    order_avg_pkg_3m
    order_sum_pkg_6m
    order_max_pkg_6m
    order_avg_pkg_6m
    address_max_name_1m
    address_max_name_3m
    address_max_name_6m
    address_max_phone_1m
    address_max_phone_3m
    address_max_phone_6m
    address_max_detail_1m
    address_max_province_1m
    address_max_city_1m
    address_max_district_1m
    address_max_detail_3m
    address_max_province_3m
    address_max_city_3m
    address_max_district_3m
    address_max_detail_6m
    address_max_province_6m
    address_max_city_6m
    address_max_district_6m
    all_fee
    all_prd_cnt
    all_cnt
    personal_fee
    personal_prd_cnt
    personal_cnt
    virtual_fee
    virtual_prd_cnt
    virtual_cnt
    virtual_proportion
    personal_cnt_proportion
    receiver_cnt
    receiver_pct
    """
    createTime = params["tbBuyGoodsInfo"][0]["orderInfo"]['createTime']
    month = ''.join(createTime.split('-')[:2])
    month_now = ''.join(TimeFormat.getnow().split('-')[:2])
    consumption = data["data"]["consumption_analysis"]
    if month in consumption:
        consumption_analysis = consumption[month]
    else:
        consumption_analysis = consumption[month_now]
    phone = params["tbBuyGoodsInfo"][0]["orderReceiver"]["orderReceiverPhone"]
    if result_key in ("name", "idcard", "account_auth", "first_deal_month_differ"):
        return str(data["data"]["basic_info"][result_key])
    elif result_key in (
            "order_sum_1m", "order_sum_amount_1m", "order_max_amount_1m", "order_avg_amount_1m", "order_sum_pkg_1m",
            "order_max_pkg_1m", "order_avg_pkg_1m", "address_max_name_1m", "address_max_phone_1m",
            "address_max_province_1m", "address_max_city_1m", "address_max_district_1m", "order_sum_3m",
            "order_sum_amount_3m", "order_max_amount_3m", "order_avg_amount_3m", "order_sum_pkg_3m", "order_max_pkg_3m",
            "order_avg_pkg_3m", "address_max_name_3m", "address_max_phone_3m", "address_max_province_3m",
            "address_max_city_3m", "address_max_district_3m", "order_sum_6m", "order_sum_amount_6m",
            "order_max_amount_6m", "order_avg_amount_6m", "order_sum_pkg_6m", "order_max_pkg_6m", "order_avg_pkg_6m",
            "address_max_name_6m", "address_max_phone_6m", "address_max_province_6m", "address_max_city_6m",
            "address_max_district_6m"):
        return str(data["data"]["order_summary"][result_key])
    elif result_key in ('address_max_detail_1m', 'address_max_detail_3m', 'address_max_detail_6m'):
        return re.sub('\s+', '', data["data"]["order_summary"][result_key])
    elif result_key in (
            'all_fee', 'all_prd_cnt', 'all_cnt', 'personal_fee', 'personal_prd_cnt', 'personal_cnt', 'virtual_fee',
            'virtual_prd_cnt', 'virtual_cnt', 'virtual_proportion', 'personal_cnt_proportion'):
        return str(consumption_analysis[result_key])
    elif result_key in ('receiver_cnt', 'receiver_pct'):
        return str(data["data"]["receiver_summary"][phone][result_key])
    elif result_key in (
            "first_deal_time", "last_deal_time", "order_amount", "order_cnt", "receiver_name", "receiver_phone"):
        return str(data["data"]["address_summary"]["0"][result_key])
    elif result_key == "receiver_address":
        return re.sub('\s+', '', data["data"]["address_summary"]["0"][result_key])
