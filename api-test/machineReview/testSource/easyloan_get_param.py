#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-21 上午 11:34
@Author     : 罗林
@File       : easyloan_get_param.py
@desc       : 好贷 修改json数据
"""
import json

from common.myCommon.Logger import getlog
from common.myFile import FileUtils

LOGGER = getlog(__name__)

def get_param_json(param_data_json, sheet_name, modif_key, modif_value):
    """
    根据sheet名称，选择修改的参数
    :param param_data_json: 原始json数据
    :param sheet_name: sheet名称
    :param modif_key:  需要修改的key
    :param modif_value:  修改后的值
    :return: 返回修改后的json
    """
    try:
        if sheet_name == 'basicinfo':
            json_data = param_data_json['data'][sheet_name]
        else:
            json_data = json.loads(param_data_json['data'][sheet_name])
    except Exception as e:
        LOGGER.error(e)
        raise e
    LOGGER.info('修改【{0}】的参数【{1}】值为【{2}】'.format(sheet_name, modif_key, modif_value))
    modif_value = FileUtils.str_to_num(modif_value)
    # param_data_json['data'][sheet_name] = json.dumps(
    #     eval("{}_modif".format(sheet_name))(json_data, modif_key, modif_value))
    if sheet_name == 'yys':
        param_data_json['data'][sheet_name] = json.dumps(yys_modif(json_data, modif_key, modif_value))
    elif sheet_name == 'tongdun':
        param_data_json['data'][sheet_name] = json.dumps(tongdun_modif(json_data, modif_key, modif_value))
    elif sheet_name == 'taobao':
        param_data_json['data'][sheet_name] = json.dumps(taobao_modif(json_data, modif_key, modif_value))
    elif sheet_name == 'jingdong':
        param_data_json['data'][sheet_name] = json.dumps(jingdong_modif(json_data, modif_key, modif_value))
    elif sheet_name == 'alipay':
        param_data_json['data'][sheet_name] = json.dumps(alipay_modif(json_data, modif_key, modif_value))
    elif sheet_name == 'basicinfo':
        param_data_json['data'][sheet_name] = basicinfo_modif(json_data, modif_key, modif_value)
    else:
        raise KeyError('the sheet_name {} is error'.format(sheet_name))
    return param_data_json


def basicinfo_modif(basicinfo_data, modif_key, modif_value):
    """
    basicinfo json 数据修改
    :param basicinfo_data: basicinfo json 数据
    :param modif_key: 需要修改的key
    :param modif_value: 修改后的值
    :return:
    V01_3001 : 3
    V01_3002 : 0.00
    V01_3003 : 1
    V01_3004 :
    V01_1009 : 15775800488
    V01_1008 : 18948195035
    V01_1007 : HYZK0001
    V01_1006 : 20280808
    V01_1004 : 530113198411283437
    V01_2004 : 8
    V01_1002 : 0
    V01_2003 : HYXZ0002
    V01_1001 : 29
    V01_1012 : 36.00
    V01_2002 : DWXZ0002
    V01_2001 : XL000001
    V01_1003 : 汉
    V01_1010 :
    V01_2005 : DWGM0001
    V01_3005 : DWGM0001
    """
    basicinfo_data[modif_key] = modif_value
    return basicinfo_data


def tongdun_modif(td_json, modif_key, modif_value):
    """
    同盾json 数据修改
    :param td_json:  同盾结果json
    :param modif_key: 需要修改的key值
    :param modif_value: 需要修改后的value值
    :return: td_data
    #key定义
    V02_1001 : 同盾欺诈分
    V02_1002 : 多平台借贷机构总量：7天
    V02_1003 : 多平台借贷机构总量：1个月
    V02_1004 : 多平台借贷机构总量：3个月
    V02_1005 : 3个月内身份证关联手机号码数
    V02_1006 : 3个月内身份证关联家庭地址数
    V02_1007 : 3个月内身份证关联邮箱数
    V02_1008 : 同盾风险项目（用于复合变量）
    V02_1009 : 身份证命中法院失信名单
    V02_1010 : 身份证命中法院执行名单
    """
    try:
        td_data = td_json['report']
        if modif_key == 'V02_1001':
            td_data["final_score"] = modif_value
        elif modif_key == 'V02_1002':
            for item in td_data["risk_items"]:
                if item['group'] == '多平台借贷申请检测' and item['item_name'] == "7天内申请人在多个平台申请借款":
                    item['item_detail']['platform_count'] = int(modif_value)
                    break
        elif modif_key == 'V02_1003':
            for item in td_data["risk_items"]:
                if item['group'] == '多平台借贷申请检测' and item['item_name'] == "1个月内申请人在多个平台申请借款":
                    item['item_detail']['platform_count'] = int(modif_value)
                    break
        elif modif_key == 'V02_1004':
            for item in td_data["risk_items"]:
                if item['group'] == '多平台借贷申请检测' and item['item_name'] == "3个月内申请人在多个平台申请借款":
                    item['item_detail']['platform_count'] = int(modif_value)
                    break
        elif modif_key == 'V02_1005':
            for item in td_data["risk_items"]:
                if (item['group'] == '客户行为检测') and (item['item_name'] == "3个月内身份证关联多个申请信息"):
                    for dic in item['item_detail']['frequency_detail_list']:
                        if str(dic['detail']).split("：")[0] == '3月内_身份证_手机号码_关联个数_全局':
                            dic['detail'] = '3月内_身份证_手机号码_关联个数_全局：{}'.format(modif_value)
                            break
                    break
        elif modif_key == 'V02_1006':
            for item in td_data["risk_items"]:
                if (item['group'] == '客户行为检测') and (item['item_name'] == "3个月内身份证关联多个申请信息"):
                    for dic in item['item_detail']['frequency_detail_list']:
                        if str(dic['detail']).split("：")[0] == '3个月身份证关联家庭地址数':
                            dic['detail'] = '3个月身份证关联家庭地址数：{}'.format(modif_value)
                            break
                    break
        elif modif_key == 'V02_1007':
            for item in td_data["risk_items"]:
                if (item['group'] == '客户行为检测') and (item['item_name'] == "3个月内身份证关联多个申请信息"):
                    for dic in item['item_detail']['frequency_detail_list']:
                        if str(dic['detail']).split("：")[0] == '3个月身份证关联邮箱数':
                            dic['detail'] = '3个月身份证关联邮箱数：{}'.format(modif_value)
                            break
                    break
        elif modif_key == 'V02_1008':
            td_data["risk_items"] = modif_value
        elif modif_key == 'V02_1009':
            v2_1009 = {"item_id": modif_value, "item_name": "身份证命中法院失信名单", "group": "风险信息扫描"}
            td_data["risk_items"].append(v2_1009)
        elif modif_key == 'V02_1010':
            v2_1010 = {"item_id": modif_value, "item_name": "身份证命中法院执行名单", "group": "风险信息扫描"}
            td_data["risk_items"].append(v2_1010)
        else:
            raise KeyError('the modif_key {} is error'.format(modif_key))
    except Exception as e:
        LOGGER.error(e)
    return td_json


def yys_modif(yys_data, modif_key, modif_value):
    """
    运营商json 数据修改
    :param yys_data: 运营商json 数据
    :param modif_key: 需要修改的key
    :param modif_value: 修改后的值
    :return: yys_data
    #key定义
    V03_1001 : 账户余额
    V03_1002 : 开户时长
    V03_1003 : 手机号是否实名认证
    V03_1004 : 黑中介分数
    V03_1005 : 直接联系人人数
    V03_1006 : 直接联系人中黑名单人数
    V03_1007 : 间接联系人中黑名单人数
    V03_1008 : 直接联系人中引起间接黑名单占比
    V03_1009 : 查询过该用户的相关企业数量
    V03_1010 : 电话号码注册过的相关企业数量
    V03_1011 : 申请人姓名+身份证号码是否出现在法院黑名单
    V03_1012 : 申请人姓名+身份证号码是否出现在金融机构黑名单
    V03_1013 : 申请人姓名+手机号码是否出现在金融机构黑名单
    V03_1014 : 近1月关机天数
    V03_1015 : 近3月关机天数
    V03_1016 : 近6月关机天数
    V03_1017 : 近1月连续3天以上关机次数
    V03_1018 : 近3月连续3天以上关机次数
    V03_1019 : 近6月连续3天以上关机次数
    V03_1020 : 近1月无通话天数
    V03_1021 : 近3月无通话天数
    V03_1022 : 近6月无通话天数
    V03_1023 : 近1月互通电话的号码数目
    V03_1024 : 近3月互通电话的号码数目
    V03_1025 : 近6月互通电话的号码数目
    V03_1026 : 与贷款公司近1月通话次数
    V03_1027 : 与贷款公司近3月通话次数
    V03_1028 : 与贷款公司近6月通话次数
    V03_1029 : 与贷款公司近1月通话时长
    V03_1030 : 与贷款公司近3月通话时长
    V03_1031 : 与贷款公司近6月通话时长
    V03_1032 : 与催收公司近1月通话次数
    V03_1033 : 与催收公司近3月通话次数
    V03_1034 : 与催收公司近6月通话次数
    V03_1035 : 与催收公司近1月通话时长
    V03_1036 : 与催收公司近3月通话时长
    V03_1037 : 与催收公司近6月通话时长
    V03_1038 : 近1月消费总金额
    V03_1039 : 近3月消费总金额
    V03_1040 : 近6月消费总金额
    V03_1041 : 近3月平均消费金额
    V03_1042 : 近6月平均消费金额
    V03_1043 : 近3月朋友圈数量
    V03_1044 : 近6月朋友圈数量
    V03_1045 : 通话详单
    V03_1046 : 朋友圈联系人top3列表
    V03_1047 : 夜间活动情况
    V03_1048 : 近3月朋友圈是否在本地
    V03_1049 : 近6月朋友圈是否在本地
    """
    try:
        if modif_key == 'V03_1001':
            for i in range(len(yys_data['cell_phone'])):
                if yys_data["cell_phone"][i]["key"] == "available_balance":  # 余额
                    yys_data["cell_phone"][i]["value"] = modif_value
                    break
        elif modif_key == 'V03_1002':
            for i in range(len(yys_data['cell_phone'])):
                if yys_data["cell_phone"][i]["key"] == "in_time":  # 开户时长(月)
                    yys_data["cell_phone"][i]["value"] = modif_value
                    break
        elif modif_key == 'V03_1003':
            for i in range(len(yys_data['cell_phone'])):
                if yys_data["cell_phone"][i]["key"] == "reliability":  # 是否实名
                    yys_data["cell_phone"][i]["value"] = modif_value
                    break
        elif modif_key == 'V03_1004':
            # 黑中介分数
            yys_data['user_info_check'][0]["check_black_info"]["phone_gray_score"] = modif_value
        elif modif_key == 'V03_1005':
            # 直接联系人数
            yys_data['user_info_check'][0]["check_black_info"]["contacts_class1_cnt"] = modif_value
        elif modif_key == 'V03_1006':
            # 直接联系人中黑名单人数
            yys_data['user_info_check'][0]["check_black_info"]["contacts_class1_blacklist_cnt"] = modif_value
        elif modif_key == 'V03_1007':
            # 间接联系人中黑名单人数
            yys_data['user_info_check'][0]["check_black_info"]["contacts_class2_blacklist_cnt"] = modif_value
        elif modif_key == 'V03_1008':
            # #直接联系人中引起间接黑名单占比
            yys_data['user_info_check'][0]["check_black_info"]["contacts_router_ratio"] = modif_value
        elif modif_key == 'V03_1009':
            # #查询过该用户的相关企业数量
            yys_data['user_info_check'][0]["check_search_info"]["searched_org_cnt"] = modif_value
        elif modif_key == 'V03_1010':
            # 电话号码注册过的相关企业数量
            yys_data['user_info_check'][0]["check_search_info"]["register_org_cnt"] = modif_value
        elif modif_key == 'V03_1011':
            # 申请人姓名+身份证号码是否出现在法院黑名单
            for i in range(len(yys_data['basic_check_items'])):
                if yys_data["basic_check_items"][i]["check_item"] == "is_name_and_idcard_in_court_black":
                    yys_data["basic_check_items"][i]["result"] = modif_value
                    break
        elif modif_key == 'V03_1012':
            # 申请人姓名+身份证号码是否出现在金融机构黑名单
            for i in range(len(yys_data['basic_check_items'])):
                if yys_data["basic_check_items"][i]["check_item"] == "is_name_and_idcard_in_finance_black":
                    yys_data["basic_check_items"][i]["result"] = modif_value
                    break
        elif modif_key == 'V03_1013':
            # # 申请人姓名+手机号码是否出现在金融机构黑名单
            for i in range(len(yys_data['basic_check_items'])):
                if yys_data["basic_check_items"][i]["check_item"] == "is_name_and_mobile_in_finance_black":
                    yys_data["basic_check_items"][i]["result"] = modif_value
                    break
        elif modif_key == 'V03_1014':
            active_degree = yys_data["active_degree"]
            for i in range(len(active_degree)):
                if active_degree[i]["app_point_zh"] == "关机天数":
                    active_degree[i]["item"]["item_1m"] = modif_value
                    break
        elif modif_key == 'V03_1015':
            active_degree = yys_data["active_degree"]
            for i in range(len(active_degree)):
                if active_degree[i]["app_point_zh"] == "关机天数":
                    active_degree[i]["item"]["item_3m"] = modif_value
                    break
        elif modif_key == 'V03_1016':
            active_degree = yys_data["active_degree"]
            for i in range(len(active_degree)):
                if active_degree[i]["app_point_zh"] == "关机天数":
                    active_degree[i]["item"]["item_6m"] = modif_value
                    break
        elif modif_key == 'V03_1017':
            active_degree = yys_data["active_degree"]
            for i in range(len(active_degree)):
                if active_degree[i]["app_point_zh"] == "连续3天以上关机次数":
                    active_degree[i]["item"]["item_1m"] = modif_value
                    break
        elif modif_key == 'V03_1018':
            active_degree = yys_data["active_degree"]
            for i in range(len(active_degree)):
                if active_degree[i]["app_point_zh"] == "连续3天以上关机次数":
                    active_degree[i]["item"]["item_3m"] = modif_value
                    break
        elif modif_key == 'V03_1019':
            active_degree = yys_data["active_degree"]
            for i in range(len(active_degree)):
                if active_degree[i]["app_point_zh"] == "连续3天以上关机次数":
                    active_degree[i]["item"]["item_6m"] = modif_value
                    break
        elif modif_key == 'V03_1020':
            active_degree = yys_data["active_degree"]
            for i in range(len(active_degree)):
                if active_degree[i]["app_point_zh"] == "无通话天数":
                    active_degree[i]["item"]["item_1m"] = modif_value
                    break
        elif modif_key == 'V03_1021':
            active_degree = yys_data["active_degree"]
            for i in range(len(active_degree)):
                if active_degree[i]["app_point_zh"] == "无通话天数":
                    active_degree[i]["item"]["item_3m"] = modif_value
                    break
        elif modif_key == 'V03_1022':
            active_degree = yys_data["active_degree"]
            for i in range(len(active_degree)):
                if active_degree[i]["app_point_zh"] == "无通话天数":
                    active_degree[i]["item"]["item_6m"] = modif_value
                    break
        elif modif_key == 'V03_1023':
            active_degree = yys_data["active_degree"]
            for i in range(len(active_degree)):
                if active_degree[i]["app_point_zh"] == "通话号码数目":
                    active_degree[i]["item"]["item_1m"] = modif_value
                    break
        elif modif_key == 'V03_1024':
            active_degree = yys_data["friend_circle"]["summary"]
            for i in range(len(active_degree)):
                if active_degree[i]["key"] == "inter_peer_num_3m":
                    active_degree[i]["value"] = modif_value
                    break
        elif modif_key == 'V03_1025':
            active_degree = yys_data["friend_circle"]["summary"]
            for i in range(len(active_degree)):
                if active_degree[i]["key"] == "inter_peer_num_6m":
                    active_degree[i]["value"] = modif_value
                    break
        elif modif_key == 'V03_1026':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "贷款":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_cnt_1m"] = modif_value
                    break
        elif modif_key == 'V03_1027':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "贷款":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_cnt_3m"] = modif_value
                    break
        elif modif_key == 'V03_1028':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "贷款":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_cnt_6m"] = modif_value
                    break
        elif modif_key == 'V03_1029':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "贷款":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_time_1m"] = modif_value
                    break
        elif modif_key == 'V03_1030':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "贷款":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_time_3m"] = modif_value
                    break
        elif modif_key == 'V03_1031':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "贷款":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_time_6m"] = modif_value
                    break
        elif modif_key == 'V03_1032':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "催收公司":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_cnt_1m"] = modif_value
                    break
        elif modif_key == 'V03_1033':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "催收公司":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_cnt_3m"] = modif_value
                    break
        elif modif_key == 'V03_1034':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "催收公司":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_cnt_6m"] = modif_value
                    break
        elif modif_key == 'V03_1035':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "催收公司":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_time_1m"] = modif_value
                    break
        elif modif_key == 'V03_1036':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "催收公司":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_time_3m"] = modif_value
                    break
        elif modif_key == 'V03_1037':
            for i in range(len(yys_data["call_risk_analysis"])):
                if yys_data["call_risk_analysis"][i]["analysis_desc"] == "催收公司":
                    yys_data["call_risk_analysis"][i]["analysis_point"]["call_time_6m"] = modif_value
                    break
        elif modif_key == 'V03_1038':
            for i in range(len(yys_data["consumption_detail"])):
                if yys_data["consumption_detail"][i]["app_point"] == "total_fee":
                    yys_data["consumption_detail"][i]["item"]["item_1m"] = modif_value
                    break
        elif modif_key == 'V03_1039':
            for i in range(len(yys_data["consumption_detail"])):
                if yys_data["consumption_detail"][i]["app_point"] == "total_fee":
                    yys_data["consumption_detail"][i]["item"]["item_3m"] = modif_value
                    break
        elif modif_key == 'V03_1040':
            for i in range(len(yys_data["consumption_detail"])):
                if yys_data["consumption_detail"][i]["app_point"] == "total_fee":
                    yys_data["consumption_detail"][i]["item"]["item_6m"] = modif_value
                    break
        elif modif_key == 'V03_1041':
            for i in range(len(yys_data["consumption_detail"])):
                if yys_data["consumption_detail"][i]["app_point"] == "total_fee":
                    yys_data["consumption_detail"][i]["item"]["avg_item_3m"] = modif_value
                    break
        elif modif_key == 'V03_1042':
            for i in range(len(yys_data["consumption_detail"])):
                if yys_data["consumption_detail"][i]["app_point"] == "total_fee":
                    yys_data["consumption_detail"][i]["item"]["avg_item_6m"] = modif_value
                    break
        elif modif_key == 'V03_1043':
            for i in range(len(yys_data["friend_circle"]["summary"])):
                if yys_data["friend_circle"]["summary"][i]["key"] == "is_city_match_friend_city_center_3m":
                    yys_data["friend_circle"]["summary"][i]["value"] = modif_value
                    break
        elif modif_key == 'V03_1044':
            for i in range(len(yys_data["friend_circle"]["summary"])):
                if yys_data["friend_circle"]["summary"][i]["key"] == "is_city_match_friend_city_center_6m":
                    yys_data["friend_circle"]["summary"][i]["value"] = modif_value
                    break
        elif modif_key == 'V03_1045':
            yys_data["call_contact_detail"] = modif_value
        elif modif_key == 'V03_1046':
            yys_data["friend_circle"]["peer_num_top_list"] = modif_value
        elif modif_key == 'V03_1047':
            for i in yys_data["behavior_check"]:
                if i["check_point"] == "contact_night":
                    i["evidence"] = '晚间活跃频率占全天的{}%'.format(modif_value)
                    break
        elif modif_key == 'V03_1048':
            for i in range(len(yys_data["friend_circle"]["summary"])):
                if yys_data["friend_circle"]["summary"][i]["key"] == "is_city_match_friend_city_center_3m":
                    yys_data["friend_circle"]["summary"][i]["value"] = modif_value
                    break
        elif modif_key == 'V03_1049':
            for i in range(len(yys_data["friend_circle"]["summary"])):
                if yys_data["friend_circle"]["summary"][i]["key"] == "is_city_match_friend_city_center_6m":
                    yys_data["friend_circle"]["summary"][i]["value"] = modif_value
                    break
        else:
            raise KeyError('the modif_key {} is error'.format(modif_key))
    except Exception as e:
        LOGGER.error(e)
    return yys_data


def jingdong_modif(jd_data, modif_key, modif_value):
    """
    京东 json 数据修改
    :param jd_data: 京东 json 数据
    :param modif_key: 需要修改的key
    :param modif_value: 修改后的值
    :return: jd_data
    #key定义
    V04_1001 : 京东中该用户的真实姓名
    V04_1002 : 该用户的小白信用的分数值
    V04_1003 : 该用户京东账户总资产金额
    V04_1004 : 该用户京东钱包的当前可用余额
    V04_1005 : 该用户白条的总信用额度
    V04_1006 : 该用户白条当前可用的信用额度之和
    V04_1007 : 该用户白条的欠款金额之和
    V04_1008 : 该用户白条的当前的逾期金额之和
    V04_1009 : 近6月本人消费次数
    V04_1010 : Top 1 的收货地址，最早一次的订单时间
    V04_1011 : Top 2 的收货地址，最早一次的订单时间
    V04_1012 : Top 3 的收货地址，最早一次的订单时间
    """
    try:
        if modif_key == 'V04_1001':
            jd_data["basic_info"]["user_and_account_basic_info"]["jd_name"] = modif_value
        elif modif_key == 'V04_1002':
            jd_data["basic_info"]["user_and_account_basic_info"]["xiao_bai_credit"] = modif_value
        elif modif_key == 'V04_1003':
            jd_data["wealth_info"]["totalssets"]["total_money"] = modif_value
        elif modif_key == 'V04_1004':
            jd_data["wealth_info"]["totalssets"]["wallet_money_available"] = modif_value
        elif modif_key == 'V04_1005':
            jd_data["wealth_info"]["totalssets"]["credit_limit"] = modif_value
        elif modif_key == 'V04_1006':
            jd_data["wealth_info"]["totalssets"]["available_limit"] = modif_value
        elif modif_key == 'V04_1007':
            jd_data["wealth_info"]["totalssets"]["credit_wait_pay"] = modif_value
        elif modif_key == 'V04_1008':
            jd_data["wealth_info"]["totalssets"]["delinquency_balance"] = modif_value
        elif modif_key == 'V04_1009':
            jd_data["consumption_analysis"]["receiving_consumption"]["self_consum_times"]["sum"] = modif_value
        elif modif_key == 'V04_1010':
            jd_data["address_analysis"]["commonly_used_address"]["deliver_address"][0][
                "first_deliver_time"] = modif_value
        elif modif_key == 'V04_1011':
            jd_data["address_analysis"]["commonly_used_address"]["deliver_address"][1][
                "first_deliver_time"] = modif_value
        elif modif_key == 'V04_1012':
            jd_data["address_analysis"]["commonly_used_address"]["deliver_address"][2][
                "first_deliver_time"] = modif_value
        else:
            raise KeyError('the modif_key {} is error'.format(modif_key))
    except Exception as e:
        LOGGER.error(e)
    return jd_data


def taobao_modif(tb_data, modif_key, modif_value):
    """
    淘宝 json 数据修改
    :param tb_data: 淘宝 json 数据
    :param modif_key: 需要修改的key
    :param modif_value: 修改后的值
    :return: tb_data
    V05_1001 : 淘宝中该用户的真实姓名
    V05_1002 : 淘宝中该用户绑定的邮箱
    V05_1003 : 淘宝中该用户绑定的手机号码
    V05_1004 : 淘宝中该用户绑定的支付宝账户
    V05_1005 : 淘气值
    V05_1006 : 是否实名认证
    V05_1007 : 该用户支付宝账户余额金额
    V05_1008 : 该用户余额宝账户金额
    V05_1009 : 当前该用户花呗的授信额度
    V05_1010 : 当前该用户花呗的可用授信额度
    V05_1011 : 支付宝的芝麻分
    V05_1012 : 支付宝的借呗总额度
    V05_1013 : 支付宝的借呗可用额度
    V05_1014 : 近6月本人消费次数
    V05_1015 : Top 1 的收货地址，最早一次的订单时间
    V05_1016 : Top 2 的收货地址，最早一次的订单时间
    V05_1017 : Top 3 的收货地址，最早一次的订单时间
    """
    try:
        if modif_key == 'V05_1001':
            tb_data["basic_info"]["user_and_account_basic_info"]["taobao_name"] = modif_value
        elif modif_key == 'V05_1002':
            tb_data["basic_info"]["user_and_account_basic_info"]["taobao_email"] = modif_value
        elif modif_key == 'V05_1003':
            tb_data["basic_info"]["user_and_account_basic_info"]["taobao_phone_number"] = modif_value
        elif modif_key == 'V05_1004':
            tb_data["basic_info"]["user_and_account_basic_info"]["alipay_account"] = modif_value
        elif modif_key == 'V05_1005':
            tb_data["basic_info"]["user_and_account_basic_info"]["tao_score"] = modif_value
        elif modif_key == 'V05_1006':
            tb_data["basic_info"]["user_and_account_basic_info"]["account_auth"] = modif_value
        elif modif_key == 'V05_1007':
            tb_data["wealth_info"]["totalssets"]["balance"] = modif_value
        elif modif_key == 'V05_1008':
            tb_data["wealth_info"]["totalssets"]["yue_e_bao_amt"] = modif_value
        elif modif_key == 'V05_1009':
            tb_data["wealth_info"]["totalssets"]["huai_bei_limit"] = modif_value
        elif modif_key == 'V05_1010':
            tb_data["wealth_info"]["totalssets"]["huai_bei_can_use_limit"] = modif_value
        elif modif_key == 'V05_1011':
            tb_data["wealth_info"]["totalssets"]["taobao_zmscore"] = modif_value
        elif modif_key == 'V05_1012':
            tb_data["wealth_info"]["totalssets"]["taobao_jiebei_amount"] = modif_value
        elif modif_key == 'V05_1013':
            tb_data["wealth_info"]["totalssets"]["taobao_jiebie_available_amount"] = modif_value
        elif modif_key == 'V05_1014':
            tb_data["consumption_analysis"]["receiving_consumption"]["self_consum_times"]["sum"] = modif_value
        elif modif_key == 'V05_1015':
            tb_data["address_analysis"]["commonly_used_address"]["first_deliver_time"]["top1"] = modif_value
        elif modif_key == 'V05_1016':
            tb_data["address_analysis"]["commonly_used_address"]["first_deliver_time"]["top2"] = modif_value
        elif modif_key == 'V05_1017':
            tb_data["address_analysis"]["commonly_used_address"]["first_deliver_time"]["top3"] = modif_value
        else:
            raise KeyError('the modif_key {} is error'.format(modif_key))
    except Exception as e:
        LOGGER.error(e)
    return tb_data


def alipay_modif(alipay_data, modif_key, modif_value):
    """
    阿里 json 数据修改
    :param alipay_data: 阿里 json 数据
    :param modif_key: 需要修改的key
    :param modif_value: 修改后的值
    :return: alipay_data
    #key定义
    V06_1001 : 平台中该用户的姓名
    V06_1002 : 平台中该用户的身份证号码
    V06_1003 : 该用户是否在平台中进行了实名验证
    V06_1004 : 该用户注册的时间距今的月份数
    V06_1005 : 当前该用户的账户余额金额
    V06_1006 : 当前该用户的余额宝账户金额
    V06_1007 : 当前该用户的招财宝金额
    V06_1008 : 当前该用户的基金金额
    V06_1009 : 当前该用户的存金宝金额
    V06_1010 : 当前该用户的淘宝理财金额
    V06_1011 : 当前该用户蚂蚁花呗的授信额度
    V06_1012 : 该用户最近6个月通过平台，进行其他贷款还款且交易成功的数量
    V06_1013 : 该用户最近6个月通过平台，进行其他贷款还款且交易成功的金额
    V06_1014 : 该用户平台最近6个月的交易中，收支类型为支出，且交易成功的非资金转移类交易的金额之和
    V06_1015 : 该用户平台最近6个月的交易中，收支类型为收入，且交易成功的交易金额之和
    """
    try:
        if modif_key == 'V06_1001':
            alipay_data["basic_info"]["user_and_account_basic_info"]["user_name"] = modif_value
        elif modif_key == 'V06_1002':
            alipay_data["basic_info"]["user_and_account_basic_info"]["card_number"] = modif_value
        elif modif_key == 'V06_1003':
            alipay_data["basic_info"]["user_and_account_basic_info"]["is_realname"] = modif_value
        elif modif_key == 'V06_1004':
            alipay_data["basic_info"]["user_and_account_basic_info"]["register_month"] = modif_value
        elif modif_key == 'V06_1005':
            alipay_data["wealth_info"]["total_assets"]["balance"] = modif_value
        elif modif_key == 'V06_1006':
            alipay_data["wealth_info"]["total_assets"]["yu_e_bao"] = modif_value
        elif modif_key == 'V06_1007':
            alipay_data["wealth_info"]["total_assets"]["zhao_cai_bao"] = modif_value
        elif modif_key == 'V06_1008':
            alipay_data["wealth_info"]["total_assets"]["fund"] = modif_value
        elif modif_key == 'V06_1009':
            alipay_data["wealth_info"]["total_assets"]["cun_jin_bao"] = modif_value
        elif modif_key == 'V06_1010':
            alipay_data["wealth_info"]["total_assets"]["taobao_finance"] = modif_value
        elif modif_key == 'V06_1011':
            alipay_data["wealth_info"]["total_assets"]["huabai_limit"] = modif_value
        elif modif_key == 'V06_1012':
            alipay_data["major_expenditure"]["repayment"]["other_rpy_cnt"]["sum"] = modif_value
        elif modif_key == 'V06_1013':
            alipay_data["major_expenditure"]["repayment"]["other_rpy_amt"]["sum"] = modif_value
        elif modif_key == 'V06_1014':
            alipay_data["basic_info"]["user_and_account_basic_info"]["total_expenses_amt_6m"] = modif_value
        elif modif_key == 'V06_1015':
            alipay_data["basic_info"]["user_and_account_basic_info"]["total_income_amt_6m"] = modif_value
        else:
            raise KeyError('the modif_key {} is error'.format(modif_key))
    except Exception as e:
        LOGGER.error(e)
    return alipay_data
