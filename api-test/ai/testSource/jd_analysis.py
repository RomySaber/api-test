#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-10-23
@Author     : 罗林
@File       : jd_analysis.py
@desc       : 
"""
import copy

from common.myCommon import TimeFormat
from common.myFile import FileUtils, MockData


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
    elif times == '7':
        start, end = TimeFormat.get_day_start_time(-6), TimeFormat.getnow()
    else:
        start, end = TimeFormat.get_day_start_time(-6), TimeFormat.getnow()
    return start, end


def modif_date(data):
    """
    初始化请求时修改时间
    :param data:
    :return:
    """
    data["order"][0]['inserttime'] = TimeFormat.getnow()
    start, end = get_data()
    data["order"][0]["dealtime"] = TimeFormat.random_time(start, end)


def modif(data, modif_key, modif_value):
    """
    修改京东请求数据
    :param data:
    :param modif_key:
    :param modif_value:
    :return:
    address： 收件人地址
    status：订单状态
    dealtime：下单时间
    name：收件人姓名
    telephone：收件人电话
    amount：订单总价
    goodsPrice：商品单价
    goodsNum：商品数量
    goodsName：商品名称
    amount_total： 总价格
    orderNum：订单数量，查询第一条订单后循环生成相同订单，配合其他条件使用
    """
    if modif_key == "address":
        data["order"][0]["address"] = modif_value
    elif modif_key == "status":
        data["order"][0]["status"] = modif_value
    elif modif_key == "dealtime":
        start, end = get_data(modif_value)
        data["order"][0]["dealtime"] = TimeFormat.random_time(start, end)
    elif modif_key == "first_deal_time":
        if modif_value == '7':
            data["first_deal_time"] = TimeFormat.get_day_end_time(-7)
        else:
            # num = int(modif_value) * 30
            data["first_deal_time"] = TimeFormat.get_month_ago(int(modif_value))
    elif modif_key == "name":
        data["order"][0]["name"] = modif_value
    elif modif_key == "telephone":
        data["order"][0]["telephone"] = modif_value
    elif modif_key == "amount":
        data["order"][0]["amount"] = modif_value
    elif modif_key == "goodsPrice":
        data["order"][0]["goods"][0]["goodsPrice"] = FileUtils.str_to_num(modif_value)
    elif modif_key == "goodsNum":
        data["order"][0]["goods"][0]["goodsNum"] = FileUtils.str_to_num(modif_value)
    elif modif_key == "goodsName":
        data["order"][0]["goods"][0]["goodsName"] = modif_value
    elif modif_key == "amount_total":
        data["order"][0]["amount_total"] = "商品总金额：￥{}".format(FileUtils.str_to_num(modif_value))
    elif modif_key == 'orderNum':
        order_info = data["order"][0]
        dealtime = order_info['dealtime'].split(' ')[0]
        orders_info = list()
        for _ in range(int(modif_value)):
            o = copy.deepcopy(order_info)
            o['orderid'] = MockData.strNumber(11)
            o['dealtime'] = TimeFormat.random_time(dealtime + ' 00:00:01', dealtime + ' 23:59:59')
            orders_info.append(o)
        data["order"] = orders_info


def get_result(result, result_key, params):
    """
    获取 测试结果数据
    :param result: 请求结果数据
    :param result_key: 结果key值
    :param params: 请求数据
    :return:
    address_max_city_1m:最近1个月订单中收货最多的收货地址所在市
    address_max_city_3m:最近3个月订单中收货最多的收货地址所在市
    address_max_city_6m:最近6个月订单中收货最多的收货地址所在市
    address_max_detail_1m:最近1个月订单中收货最多的收货地址
    address_max_detail_3m:最近3个月订单中收货最多的收货地址
    address_max_detail_6m:最近6个月订单中收货最多的收货地址
    address_max_district_1m:最近1个月订单中收货最多的收货地址所在区县
    address_max_district_3m:最近3个月订单中收货最多的收货地址所在区县
    address_max_district_6m:最近6个月订单中收货最多的收货地址所在区县
    address_max_name_1m:最近1个月订单中收货最多的收货人
    address_max_name_3m:最近3个月订单中收货最多的收货人
    address_max_name_6m:最近6个月订单中收货最多的收货人
    address_max_phone_1m:最近1个月订单中收货最多的手机号码
    address_max_phone_3m:最近3个月订单中收货最多的手机号码
    address_max_phone_6m:最近6个月订单中收货最多的手机号码
    address_max_province_1m:最近1个月订单中收货最多的收货地址所在省
    address_max_province_3m:最近3个月订单中收货最多的收货地址所在省
    address_max_province_6m:最近6个月订单中收货最多的收货地址所在省
    order_avg_amount_1m:最近1个月订单的平均金额
    order_avg_amount_3m:最近3个月订单的平均金额
    order_avg_amount_6m:最近6个月订单的平均金额
    order_avg_pkg_1m:最近1个月订单的平均商品数
    order_avg_pkg_3m:最近3个月订单的平均商品数
    order_avg_pkg_6m:最近6个月订单的平均商品数
    order_max_amount_1m:最近1个月订单的最高金额
    order_max_amount_3m:最近3个月订单的最高金额
    order_max_amount_6m:最近6个月订单的最高金额
    order_max_pkg_1m:最近1个月订单的最高商品数
    order_max_pkg_3m:最近3个月订单的最高商品数
    order_max_pkg_6m:最近6个月订单的最高商品数
    order_sum_1m:最近1个月订单的总订单数
    order_sum_3m:最近3个月订单的总订单数
    order_sum_6m:最近6个月订单的总订单数
    order_sum_amount_1m:最近1个月订单的总金额
    order_sum_amount_3m:最近3个月订单的总金额
    order_sum_amount_6m:最近6个月订单的总金额
    order_sum_pkg_1m:最近1个月订单的总商品数
    order_sum_pkg_3m:最近3个月订单的总商品数
    order_sum_pkg_6m:最近6个月订单的总商品数
    all_fee:订单总额
    all_cnt:订单数量
    all_prd_cnt:订单商品数量
    personal_fee:本人订单总额
    personal_cnt:本人订单数量
    personal_proportion:本人订单商品占比
    personal_prd_cnt:本人订单商品数量
    virtual_fee:虚拟物品订单总额
    virtual_cnt:虚拟物品订单数量
    virtual_prd_cnt:虚拟物品订单商品数量
    virtual_proportion:虚拟物品订单总额占比
    telephone_cnt_dict:收货人联系电话次数统计字典
    telephone_proportion_dict:收货人联系电话占比统计字典
    telephone_list:收货人联系电话列表
    """
    orders = params["order"]
    if any(filter(lambda x: x['status'] in ['充值成功', '已完成'], orders)):
        status_num = 0
        for i in range(len(orders)):
            if orders[i]['status'] in ['充值成功', '已完成']:
                status_num = i
        month = "".join(orders[status_num]["dealtime"].split('-')[:2])
    else:
        month = ''.join(TimeFormat.getnow().split('-')[:2])
    consumption_analysis_dict = result["consumption_analysis_dict"][month]
    if result_key in ("order_sum_1m", "order_sum_amount_1m", "order_max_amount_1m", "order_avg_amount_1m",
                      "order_sum_pkg_1m", "order_max_pkg_1m", "order_avg_pkg_1m", "address_max_name_1m",
                      "address_max_phone_1m", "address_max_detail_1m", "address_max_province_1m", "address_max_city_1m",
                      "address_max_district_1m", "order_sum_3m", "order_sum_amount_3m", "order_max_amount_3m",
                      "order_avg_amount_3m", "order_sum_pkg_3m", "order_max_pkg_3m", "order_avg_pkg_3m",
                      "address_max_name_3m", "address_max_phone_3m", "address_max_detail_3m", "address_max_province_3m",
                      "address_max_city_3m", "address_max_district_3m", "order_sum_6m", "order_sum_amount_6m",
                      "order_max_amount_6m", "order_avg_amount_6m", "order_sum_pkg_6m", "order_max_pkg_6m",
                      "order_avg_pkg_6m", "address_max_name_6m", "address_max_phone_6m", "address_max_detail_6m",
                      "address_max_province_6m", "address_max_city_6m", "address_max_district_6m"):
        return str(result["order_result_dict"][result_key])
    elif result_key in ("all_fee", "all_cnt", "all_prd_cnt", "personal_fee", "personal_cnt", "personal_prd_cnt",
                        "virtual_fee", "virtual_cnt", "virtual_prd_cnt", "personal_proportion", "virtual_proportion"):
        return str(consumption_analysis_dict[result_key])
    elif result_key in ("telephone_cnt_dict", "telephone_proportion_dict"):
        result_dict = consumption_analysis_dict[result_key]
        value_list = [t for t in result_dict.values()]
        if len(result_dict) >= 1:
            return str(value_list[0])
        else:
            return ''
    elif result_key == "telephone_list":
        telephone_list = consumption_analysis_dict["telephone_list"]
        if len(telephone_list) >= 1:
            return str(telephone_list[0])
        else:
            return ''
    elif result_key in ("top_n_address", "receiver_name", "receiver_phone", "first_create_time",
                        "last_create_time", "order_sum_fee", "order_cnt"):
        top_address_dict = result["top_address_dict"]
        if "top_1" in top_address_dict.keys():
            return str(top_address_dict["top_1"][result_key])
        else:
            return ''
    elif result_key == "first_deal_delta_monhs":
        return str(result["base_analyse_dict"][result_key])
