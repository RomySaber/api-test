#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2020-01-10
@Author     : QA
@File       : mysql_data_check.py
@desc       :  mysql数据结构检查
"""
import json
import sys
import pymysql


def find_data_mysql(task_id):
    """
    查询MySQL数据
    :param task_id: 查询条件
    :return:
    """
    conn = pymysql.connect(host='192.168.15.236', port=3309, user='guest', passwd='guest', db='spideras')
    cursor = conn.cursor()
    conn.ping(reconnect=True)
    result = None
    query = ' '.join(['SELECT', 'notice_java_data', 'FROM', 'third_ai_callback', 'WHERE',
                      'task_id="{}"'.format(task_id), 'AND', 'status=10', ';'])
    try:
        rows_num = cursor.execute(query)
        conn.commit()
        if rows_num:
            fc = cursor.fetchone()
            if fc:
                result = json.loads(fc[0])
    except BaseException as e:
        conn.rollback()
        raise e
    cursor.close()
    conn.close()
    return result


def check_jindong(data):
    """
    检查京东数据
    :param data: 数据库存储数据
    :return:
    """
    _ = data['base_analysis_dict']['first_deal_delta_months']
    _ = data['base_analysis_dict']['first_deal_time']
    _ = data['order_result_dict']['address_max_city_1m']
    _ = data['order_result_dict']['address_max_city_3m']
    _ = data['order_result_dict']['address_max_city_6m']
    _ = data['order_result_dict']['address_max_detail_1m']
    _ = data['order_result_dict']['address_max_detail_3m']
    _ = data['order_result_dict']['address_max_detail_6m']
    _ = data['order_result_dict']['address_max_district_1m']
    _ = data['order_result_dict']['address_max_district_3m']
    _ = data['order_result_dict']['address_max_district_6m']
    _ = data['order_result_dict']['address_max_name_1m']
    _ = data['order_result_dict']['address_max_name_3m']
    _ = data['order_result_dict']['address_max_name_6m']
    _ = data['order_result_dict']['address_max_phone_1m']
    _ = data['order_result_dict']['address_max_phone_3m']
    _ = data['order_result_dict']['address_max_phone_6m']
    _ = data['order_result_dict']['address_max_province_1m']
    _ = data['order_result_dict']['address_max_province_3m']
    _ = data['order_result_dict']['address_max_province_6m']
    _ = data['order_result_dict']['order_avg_amount_1m']
    _ = data['order_result_dict']['order_avg_amount_3m']
    _ = data['order_result_dict']['order_avg_amount_6m']
    _ = data['order_result_dict']['order_avg_pkg_1m']
    _ = data['order_result_dict']['order_avg_pkg_3m']
    _ = data['order_result_dict']['order_avg_pkg_6m']
    _ = data['order_result_dict']['order_max_amount_1m']
    _ = data['order_result_dict']['order_max_amount_3m']
    _ = data['order_result_dict']['order_max_amount_6m']
    _ = data['order_result_dict']['order_max_pkg_1m']
    _ = data['order_result_dict']['order_max_pkg_3m']
    _ = data['order_result_dict']['order_max_pkg_6m']
    _ = data['order_result_dict']['order_sum_1m']
    _ = data['order_result_dict']['order_sum_3m']
    _ = data['order_result_dict']['order_sum_6m']
    _ = data['order_result_dict']['order_sum_amount_1m']
    _ = data['order_result_dict']['order_sum_amount_3m']
    _ = data['order_result_dict']['order_sum_amount_6m']
    _ = data['order_result_dict']['order_sum_pkg_1m']
    _ = data['order_result_dict']['order_sum_pkg_3m']
    _ = data['order_result_dict']['order_sum_pkg_6m']
    _ = data['original_data']
    _ = data['status_des']
    _ = data['status_id']
    _ = data['task_id']
    consumption_analysis_dict = data['consumption_analysis_dict']
    if not consumption_analysis_dict:
        raise Exception('consumption_analysis_dict Error')
    for v in consumption_analysis_dict.values():
        _ = v['all_cnt']
        _ = v['all_fee']
        _ = v['all_prd_cnt']
        _ = v['personal_cnt']
        _ = v['personal_fee']
        _ = v['personal_prd_cnt']
        _ = v['personal_proportion']
        _ = v['telephone_list']
        _ = v['virtual_cnt']
        _ = v['virtual_fee']
        _ = v['virtual_prd_cnt']
        _ = v['virtual_proportion']
    top_address_dict = data['top_address_dict']
    if not top_address_dict:
        raise Exception('top_address_dict Error')
    _ = top_address_dict['top_1']
    _ = top_address_dict['top_2']
    for v in top_address_dict.values():
        _ = v['first_create_time']
        _ = v['last_create_time']
        _ = v['order_cnt']
        _ = v['order_sum_fee']
        _ = v['receiver_name']
        _ = v['receiver_phone']
        _ = v['top_n_address']


def check_taobao(data):
    """
    检查淘宝数据
    :param data: 数据库存储数据
    :return:
    """
    _ = data['code']
    _ = data['msg']
    _ = data['original_data']
    _ = data['basic_info']['account_auth']
    _ = data['basic_info']['first_deal_month_differ']
    _ = data['basic_info']['first_deal_time']
    _ = data['basic_info']['idcard']
    _ = data['basic_info']['name']
    _ = data['order_summary']['address_max_city_1m']
    _ = data['order_summary']['address_max_city_3m']
    _ = data['order_summary']['address_max_city_6m']
    _ = data['order_summary']['address_max_detail_1m']
    _ = data['order_summary']['address_max_detail_3m']
    _ = data['order_summary']['address_max_detail_6m']
    _ = data['order_summary']['address_max_district_1m']
    _ = data['order_summary']['address_max_district_3m']
    _ = data['order_summary']['address_max_district_6m']
    _ = data['order_summary']['address_max_name_1m']
    _ = data['order_summary']['address_max_name_3m']
    _ = data['order_summary']['address_max_name_6m']
    _ = data['order_summary']['address_max_phone_1m']
    _ = data['order_summary']['address_max_phone_3m']
    _ = data['order_summary']['address_max_phone_6m']
    _ = data['order_summary']['address_max_province_1m']
    _ = data['order_summary']['address_max_province_3m']
    _ = data['order_summary']['address_max_province_6m']
    _ = data['order_summary']['order_avg_amount_1m']
    _ = data['order_summary']['order_avg_amount_3m']
    _ = data['order_summary']['order_avg_amount_6m']
    _ = data['order_summary']['order_avg_pkg_1m']
    _ = data['order_summary']['order_avg_pkg_3m']
    _ = data['order_summary']['order_avg_pkg_6m']
    _ = data['order_summary']['order_max_amount_1m']
    _ = data['order_summary']['order_max_amount_3m']
    _ = data['order_summary']['order_max_amount_6m']
    _ = data['order_summary']['order_max_pkg_1m']
    _ = data['order_summary']['order_max_pkg_3m']
    _ = data['order_summary']['order_max_pkg_6m']
    _ = data['order_summary']['order_sum_1m']
    _ = data['order_summary']['order_sum_3m']
    _ = data['order_summary']['order_sum_6m']
    _ = data['order_summary']['order_sum_amount_1m']
    _ = data['order_summary']['order_sum_amount_3m']
    _ = data['order_summary']['order_sum_amount_6m']
    _ = data['order_summary']['order_sum_pkg_1m']
    _ = data['order_summary']['order_sum_pkg_3m']
    _ = data['order_summary']['order_sum_pkg_6m']
    address_summary = data['address_summary']
    if not address_summary:
        raise Exception('address_summary Error')
    for v in address_summary.values():
        _ = v['first_deal_time']
        _ = v['last_deal_time']
        _ = v['order_amount']
        _ = v['order_cnt']
        _ = v['receiver_address']
        _ = v['receiver_name']
        _ = v['receiver_phone']
    consumption_analysis = data['consumption_analysis']
    if not consumption_analysis:
        raise Exception('consumption_analysis Error')
    for v in consumption_analysis.values():
        _ = v['all_cnt']
        _ = v['all_fee']
        _ = v['all_prd_cnt']
        _ = v['personal_cnt']
        _ = v['personal_cnt_proportion']
        _ = v['personal_fee']
        _ = v['personal_prd_cnt']
        _ = v['virtual_cnt']
        _ = v['virtual_fee']
        _ = v['virtual_prd_cnt']
        _ = v['virtual_proportion']
    receiver_summary = data['receiver_summary']
    if not receiver_summary:
        raise Exception('receiver_summary Error')
    for v in receiver_summary.values():
        _ = v['receiver_cnt']
        _ = v['receiver_pct']


def check_mobile(data):
    """
    检查运营商数据
    :param data:  数据库存储数据
    :return:
    """
    _ = data['code']
    _ = data['msg']
    _ = data['original_data']
    _ = data['result']['etl_active_degree']['app_point']
    _ = data['result']['etl_active_degree']['app_point_zh']
    _ = data['result']['etl_active_degree']['item']['avg_item_3m']
    _ = data['result']['etl_active_degree']['item']['avg_item_6m']
    _ = data['result']['etl_active_degree']['item']['item_1m']
    _ = data['result']['etl_active_degree']['item']['item_3m']
    _ = data['result']['etl_active_degree']['item']['item_6m']
    _ = data['result']['etl_basicinfo']['age']
    _ = data['result']['etl_basicinfo']['open_month']
    _ = data['result']['etl_basicinfo']['sex']
    _ = data['result']['etl_behavior_check']['contact_night_cnt_1m']
    _ = data['result']['etl_behavior_check']['contact_night_cnt_3m']
    _ = data['result']['etl_behavior_check']['contact_night_cnt_6m']
    _ = data['result']['etl_behavior_check']['contact_night_cnt_pct_1m']
    _ = data['result']['etl_behavior_check']['contact_night_cnt_pct_3m']
    _ = data['result']['etl_behavior_check']['contact_night_cnt_pct_6m']
    _ = data['result']['etl_behavior_check']['latest_call_hour']
    _ = data['result']['etl_consumption_detail']['app_point']
    _ = data['result']['etl_consumption_detail']['app_point_zh']
    _ = data['result']['etl_consumption_detail']['item']['avg_item_3m']
    _ = data['result']['etl_consumption_detail']['item']['avg_item_6m']
    _ = data['result']['etl_consumption_detail']['item']['item_1m']
    _ = data['result']['etl_consumption_detail']['item']['item_3m']
    _ = data['result']['etl_consumption_detail']['item']['item_6m']
    _ = data['result']['etl_contact_region']['desc']
    _ = data['result']['etl_contact_region']['key']
    etl_call_contact_detail = data['result']['etl_call_contact_detail']
    if not etl_call_contact_detail:
        raise Exception('etl_call_contact_detail Error')
    _ = etl_call_contact_detail['0']
    for v in etl_call_contact_detail.values():
        _ = v['call_cnt_1m']
        _ = v['call_cnt_3m']
        _ = v['call_cnt_6m']
        _ = v['call_cnt_7d']
        _ = v['call_cnt_afternoon_1m']
        _ = v['call_cnt_afternoon_3m']
        _ = v['call_cnt_afternoon_6m']
        _ = v['call_cnt_afternoon_7d']
        _ = v['call_cnt_evening_1m']
        _ = v['call_cnt_evening_3m']
        _ = v['call_cnt_evening_6m']
        _ = v['call_cnt_evening_7d']
        _ = v['call_cnt_morning_1m']
        _ = v['call_cnt_morning_3m']
        _ = v['call_cnt_morning_6m']
        _ = v['call_cnt_morning_7d']
        _ = v['call_cnt_night_1m']
        _ = v['call_cnt_night_3m']
        _ = v['call_cnt_night_6m']
        _ = v['call_cnt_night_7d']
        _ = v['call_cnt_noon_1m']
        _ = v['call_cnt_noon_3m']
        _ = v['call_cnt_noon_6m']
        _ = v['call_cnt_noon_7d']
        _ = v['dial_cnt_1m']
        _ = v['dial_cnt_3m']
        _ = v['dial_cnt_6m']
        _ = v['dial_cnt_7d']
        _ = v['dial_time_1m']
        _ = v['dial_time_3m']
        _ = v['dial_time_6m']
        _ = v['dial_time_7d']
        _ = v['dialed_cnt_1m']
        _ = v['dialed_cnt_3m']
        _ = v['dialed_cnt_6m']
        _ = v['dialed_cnt_7d']
        _ = v['dialed_time_1m']
        _ = v['dialed_time_3m']
        _ = v['dialed_time_6m']
        _ = v['dialed_time_7d']
        _ = v['duration_1m']
        _ = v['duration_3m']
        _ = v['duration_6m']
        _ = v['duration_7d']
        _ = v['first_call_time_1m']
        _ = v['first_call_time_3m']
        _ = v['first_call_time_6m']
        _ = v['first_call_time_7d']
        _ = v['last_call_time_1m']
        _ = v['last_call_time_3m']
        _ = v['last_call_time_6m']
        _ = v['last_call_time_7d']
        _ = v['location']
        _ = v['peer_number']
        _ = v['smses_cnt_1m']
        _ = v['smses_cnt_3m']
        _ = v['smses_cnt_6m']
        _ = v['smses_cnt_7d']
    etl_call_contact_detail_num = data['result']['etl_call_contact_detail_num']
    if not etl_call_contact_detail_num:
        raise Exception('etl_call_contact_detail_num Error')
    _ = etl_call_contact_detail_num['0']
    for v in etl_call_contact_detail_num.values():
        _ = v['call_cnt_1m']
        _ = v['call_cnt_3m']
        _ = v['call_cnt_6m']
        _ = v['call_cnt_7d']
        _ = v['call_cnt_afternoon_1m']
        _ = v['call_cnt_afternoon_3m']
        _ = v['call_cnt_afternoon_6m']
        _ = v['call_cnt_afternoon_7d']
        _ = v['call_cnt_evening_1m']
        _ = v['call_cnt_evening_3m']
        _ = v['call_cnt_evening_6m']
        _ = v['call_cnt_evening_7d']
        _ = v['call_cnt_morning_1m']
        _ = v['call_cnt_morning_3m']
        _ = v['call_cnt_morning_6m']
        _ = v['call_cnt_morning_7d']
        _ = v['call_cnt_night_1m']
        _ = v['call_cnt_night_3m']
        _ = v['call_cnt_night_6m']
        _ = v['call_cnt_night_7d']
        _ = v['call_cnt_noon_1m']
        _ = v['call_cnt_noon_3m']
        _ = v['call_cnt_noon_6m']
        _ = v['call_cnt_noon_7d']
        _ = v['dial_cnt_1m']
        _ = v['dial_cnt_3m']
        _ = v['dial_cnt_6m']
        _ = v['dial_cnt_7d']
        _ = v['dial_time_1m']
        _ = v['dial_time_3m']
        _ = v['dial_time_6m']
        _ = v['dial_time_7d']
        _ = v['dialed_cnt_1m']
        _ = v['dialed_cnt_3m']
        _ = v['dialed_cnt_6m']
        _ = v['dialed_cnt_7d']
        _ = v['dialed_time_1m']
        _ = v['dialed_time_3m']
        _ = v['dialed_time_6m']
        _ = v['dialed_time_7d']
        _ = v['duration_1m']
        _ = v['duration_3m']
        _ = v['duration_6m']
        _ = v['duration_7d']
        _ = v['first_call_time_1m']
        _ = v['first_call_time_3m']
        _ = v['first_call_time_6m']
        _ = v['first_call_time_7d']
        _ = v['last_call_time_1m']
        _ = v['last_call_time_3m']
        _ = v['last_call_time_6m']
        _ = v['last_call_time_7d']
        _ = v['location']
        _ = v['location_type_7d']
        _ = v['peer_number']
    etl_call_duration_detail = data['result']['etl_call_duration_detail']
    if not etl_call_duration_detail:
        raise Exception('etl_call_duration_detail Error')
    for k in etl_call_duration_detail:
        _ = k['desc']
        _ = k['key']
        duration_list = k['duration_list']
        if not duration_list:
            raise Exception('etl_call_duration_detail duration_list Error')
        _ = duration_list['afternoon']
        _ = duration_list['daybreak']
        _ = duration_list['dusk']
        _ = duration_list['evening']
        _ = duration_list['forenoon']
        _ = duration_list['midnight']
        _ = duration_list['morning']
        _ = duration_list['noon']
        for v in duration_list.values():
            _ = v['dial_cnt']
            _ = v['dialed_cnt']
            _ = v['duration']
            _ = v['farthest_call_time']
            _ = v['latest_call_time']
            _ = v['time_step_zh']
            _ = v['total_cnt']
            _ = v['uniq_num_cnt']
    etl_cell_behavior = data['result']['etl_cell_behavior']
    if not etl_cell_behavior:
        raise Exception('etl_cell_behavior Error')
    _ = etl_cell_behavior['0']
    for v in etl_cell_behavior.values():
        _ = v['bill_month']
        _ = v['call_cnt']
        _ = v['call_fees']
        _ = v['call_time']
        _ = v['dial_cnt']
        _ = v['dial_time']
        _ = v['dialed_cnt']
        _ = v['dialed_time']
        _ = v['sms_cnt']
        _ = v['sms_fees']
        _ = v['total_fee']
    etl_contact_region_region_list = data['result']['etl_contact_region']['region_list']
    if not etl_contact_region_region_list:
        raise Exception('etl_contact_region region_list Error')
    _ = etl_contact_region_region_list['0']
    for v in etl_contact_region_region_list.values():
        _ = v['location']
        _ = v['region_avg_dial_time']
        _ = v['region_avg_dialed_time']
        _ = v['region_call_cnt']
        _ = v['region_call_time']
        _ = v['region_dial_cnt']
        _ = v['region_dial_cnt_pct']
        _ = v['region_dial_time']
        _ = v['region_dial_time_pct']
        _ = v['region_dialed_cnt']
        _ = v['region_dialed_cnt_pct']
        _ = v['region_dialed_time']
        _ = v['region_dialed_time_pct']
        _ = v['region_uniq_num_cnt']
    etl_friend_circle = data['result']['etl_friend_circle']
    for k, v in etl_friend_circle.items():
        if k in ("location_top", "peer_num_top"):
            _ = v['top_item_1m']
            _ = v['top_item_3m']
            _ = v['top_item_6m']
            for t in v.values():
                _ = t['top1']
                _ = t['top2']
                _ = t['top3']
    location_top = data['result']['etl_friend_circle']['location_top']
    for k in location_top.values():
        for v in k.values():
            _ = v['location']
            _ = v['region_avg_dial_time']
            _ = v['region_avg_dialed_time']
            _ = v['region_call_cnt']
            _ = v['region_call_time']
            _ = v['region_dial_cnt']
            _ = v['region_dial_cnt_pct']
            _ = v['region_dial_time']
            _ = v['region_dial_time_pct']
            _ = v['region_dialed_cnt']
            _ = v['region_dialed_cnt_pct']
            _ = v['region_dialed_time']
            _ = v['region_dialed_time_pct']
            _ = v['region_uniq_num_cnt']
    peer_num_top = data['result']['etl_friend_circle']['peer_num_top']
    for k in peer_num_top.values():
        for v in k.values():
            _ = v['call_cnt']
            _ = v['call_cnt_afternoon']
            _ = v['call_cnt_evening']
            _ = v['call_cnt_morning']
            _ = v['call_cnt_night']
            _ = v['call_cnt_noon']
            _ = v['dial_cnt']
            _ = v['dial_time']
            _ = v['dialed_cnt']
            _ = v['dialed_time']
            _ = v['duration']
            _ = v['first_call_time']
            _ = v['last_call_time']
            _ = v['location']
            _ = v['peer_number']
            _ = v['smses_cnt']
    summary = data['result']['etl_friend_circle']['summary']
    _ = summary['friend_circle_detail_1m']
    _ = summary['friend_circle_detail_3m']
    _ = summary['friend_circle_detail_6m']
    for v in summary.values():
        _ = v['friend_city_center']
        _ = v['friend_num']
        _ = v['good_friend_num']
        _ = v['inter_peer_num']
        _ = v['is_city_match_friend_city_center']


def check_data(task_id):
    """
    检查task_id对应数据
    :param task_id: task_id
    :return:
    """
    check_type = task_id.split('_')[0]
    data = find_data_mysql(task_id)
    print('查询数据结果：', data)
    if check_type == 'jingdong':
        try:
            check_jindong(data)
            print('京东数据正确')
        except Exception as e:
            print('京东数据错误，错误原因：\n', e, '未定位')
    elif check_type == 'taobao':
        try:
            check_taobao(data)
            print('淘宝数据正确')
        except Exception as e:
            print('淘宝数据错误，错误原因：\n', e, '未定位')
    elif check_type.lower() in ('mobile', 'telecome', 'unicom'):
        try:
            check_mobile(data)
            print('运营商数据正确')
        except Exception as e:
            print('运营商数据错误，错误原因：\n', e, '未定位')
    else:
        raise TypeError('没有输入的{0}检查类型，请检查输入的task_id【{1}】'.format(check_type, task_id))


if __name__ == '__main__':
    check_data(sys.argv[1])
    # check_data('jingdong_72448d80630311eaad81d7d81883a25f')
