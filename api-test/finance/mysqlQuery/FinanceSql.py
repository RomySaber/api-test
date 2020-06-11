#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018-07-16 下午 5:27
@Author     : 罗林
@File       : FinanceSql.py
@desc       : 
"""
import math

from common.mydb import MysqlClent
from finance.mysqlQuery import ManageSql
from finance.testAction import loginAction

db_info = ManageSql.db_info
db_info['dbname'] = ManageSql.get_finance_db_name()
DB_CONN = MysqlClent.get_conn(**db_info)


def get_device_id(deviceCode):
    # 获取设备ID
    return MysqlClent.select_one(DB_CONN, 'fk_gps', 'id',
                                 'code = "{}" and is_active = "Y" GROUP BY id DESC'.format(deviceCode))


def get_gps(install_status=0):
    # 根据安装状态查GPS 设备安装状态 0 未安装，1 已安装，2 已拆机
    return MysqlClent.select(DB_CONN, table='fk_gps', column='id, code',
                             condition='install_status = "{}" and is_active = "Y" GROUP BY id DESC LIMIT 1'
                             .format(install_status))


def get_gpscode(gpsid):
    #  根据GPSid获取GPS编号
    return MysqlClent.select_one(DB_CONN, 'fk_gps', 'code',
                                 'id = "{}" and is_active = "Y" GROUP BY id DESC '.format(gpsid))


def get_gpsid(gpscode):
    # 根据gpscode获取gpsid
    return MysqlClent.select_one(DB_CONN, 'fk_gps', 'id',
                                 'code="{}" and is_active = "Y" GROUP BY id DESC '.format(gpscode))


def get_gpscode_finance(finance_id, gpstype=1):
    # 根据车辆id查询GPScode
    return MysqlClent.select_join(DB_CONN, 'fk_gps as a,fk_gps_finance as b', 'a.code', 'a.id = b.gps_id',
                                  'b.finance_id = {0} AND a.type = {1} AND a.is_active = "Y" GROUP BY a.id '
                                  'DESC LIMIT 1'.format(finance_id, gpstype))[0][0]


def get_car_id(car_owner):
    # 获取车辆ID
    return MysqlClent.select_one(DB_CONN, 'fk_finance', 'id',
                                 'owner = "{}" and is_active = "Y" GROUP BY id DESC'.format(car_owner))


def get_car_info(car_owner, col='id'):
    # 获取车辆信息
    return MysqlClent.select_one(DB_CONN, 'fk_finance', col,
                                 'owner = "{}" and is_active = "Y" GROUP BY id DESC'.format(car_owner))


def get_car_info_by_financeid(financeid, col='owner'):
    # 根据车辆id获取车辆信息
    return MysqlClent.select_one(DB_CONN, 'fk_finance', col,
                                 'id = "{}" and is_active = "Y" GROUP BY id DESC'.format(financeid))


def get_carid_by_gpsid(gpsid):
    # 根据GPSid获取车辆id
    return MysqlClent.select_one(DB_CONN, 'fk_gps_finance', 'finance_id',
                                 'gps_id = "{}" and is_active = "Y" GROUP BY id DESC '.format(gpsid))


def get_gpsid_by_fid(finance_id):
    # 根据GPSid获取车辆id
    return MysqlClent.select_one(DB_CONN, 'fk_gps_finance', 'gps_id',
                                 'finance_id = "{}" and is_active = "Y" GROUP BY id DESC'.format(finance_id))


def get_carid_by_id_desc():
    # 查询最新车辆的id
    return MysqlClent.select_one(DB_CONN, 'fk_finance', 'id', 'is_active = "Y" GROUP BY id DESC')


def get_risk_id(risk_name):
    # 获取风险点ID
    return MysqlClent.select_one(DB_CONN, 'fk_risk', 'id',
                                 '`name` = "{}" and is_active = "Y" GROUP BY id DESC '.format(risk_name))


def get_rule_id(ruleType, risk_id):
    # 获取风险点的ruleID
    rule_id = MysqlClent.select_one(DB_CONN, 'fk_rule', 'id',
                                    'rule_type = "{0}" and risk_id = "{1}" and is_active = "Y" '
                                    'GROUP BY id DESC'.format(ruleType, risk_id))
    return rule_id


def get_threshold(thresholdid):
    # 获取阀值时间
    if thresholdid == 1:
        threshold_type = 'WIRE_OFFLINE'
    elif thresholdid == 2:
        threshold_type = 'WIRELESS_OFFLINE'
    elif thresholdid == 3:
        threshold_type = 'STATION_WARN'
    elif thresholdid == 4:
        threshold_type = 'TRAVEL_OUT'
    else:
        threshold_type = 'TRAVEL_OUT'
    threshold_time = int(MysqlClent.select_one(DB_CONN, 'fk_threshold', 'threshold',
                                               'threshold_type = "{}"'.format(threshold_type)))
    thresholdhour = math.ceil(threshold_time // 60)
    thresholdminute = threshold_time % 60
    return thresholdhour, thresholdminute


def get_role_id(role_name):
    # 根据风险点名称获取风险点id
    return MysqlClent.select_one(DB_CONN, 'fk_role', 'id',
                                 '`name` = "{}" and is_active = "Y" GROUP BY id DESC'.format(role_name))


def get_warn_id(warn_type=None, celname='id', warn_status=0, financeid=None):
    # 获取报警数据
    if warn_type is None:
        warn_types = ['FAULT', 'CIRCUIT', 'VOLTAGE', 'POWEROFF', 'LIGHT', 'DISMANTLE', 'LOWPOWER', 'OUT', 'IN',
                      'STAY', 'STATION', 'DIST', 'OFFLINE', 'OVERDUE', 'HLESS', 'BLESS', 'HBLESS']
    else:
        if 'sh' in warn_type:
            # 设备报警
            warn_types = ['FAULT', 'CIRCUIT', 'VOLTAGE', 'POWEROFF', 'LIGHT', 'DISMANTLE', 'LOWPOWER']
        elif 'wl' in warn_type:
            # 围栏报警
            warn_types = ['OUT', 'IN', 'STAY']
        elif 'tc' in warn_type:
            #  停车异常报警
            warn_types = ['STATION']
        elif 'jl' in warn_type:
            #  距离异常报警
            warn_types = ['DIST']
        elif 'lx' in warn_type:
            #  离线报警
            warn_types = ['OFFLINE']
        elif 'yq' in warn_type:
            #  逾期报警
            warn_types = ['OVERDUE']
        elif 'wh' in warn_type:
            #  未回家/公司报警
            warn_types = ['HLESS', 'BLESS', 'HBLESS']
        else:
            warn_types = []
    warntype = '\',\''.join(warn_types)
    condition_list = ["warn_type IN (\'{}\')".format(warntype), 'status = {}'.format(warn_status)]
    if financeid is not None:
        condition_list.append('finance_id = {}'.format(financeid))
    condition = ' AND '.join(condition_list) + ' GROUP BY id DESC'
    print(condition)
    return MysqlClent.select_one(DB_CONN, 'fk_warn_show', celname, condition)


def get_finance_id_bywarnid(warnid):
    # 根据报警ID获取车辆ID
    return MysqlClent.select_one(DB_CONN, 'fk_warn_show', 'finance_id', 'id = "{}"'.format(warnid))


def get_gps_finance_id(gpsid, financeid):
    # 根据gpsid和 financeid 获取安装记录id
    return MysqlClent.select_one(DB_CONN, 'fk_gps_finance', 'id',
                                 'gps_id = "{0}" and finance_id = "{1}" and is_active = "Y" '
                                 'GROUP BY id DESC'.format(gpsid, financeid))


def get_gps_group(groupname, orgcod, can_delete=1):
    # 根据分组名称和组织机构id，获取分组id
    return MysqlClent.select_one(DB_CONN, 'fk_gps_group', 'id', 'group_name = "{0}" AND org_code = "{1}" AND '
                                                                'is_active = "Y" AND can_delete = {2} GROUP BY id DESC '
                                 .format(groupname, orgcod, can_delete))


def get_warn_latest():
    # 查询最新报警的financeid
    return MysqlClent.select_one(DB_CONN, 'fk_warn_show', 'finance_id', 'status = 0')


def org_code(org_name):
    # 获取组织结构代码
    return MysqlClent.select_one(DB_CONN, 'fk_org', 'company_code', 'name="{}"'.format(org_name))


def get_role_count(role_id):
    # 查询角色的用户总数
    return MysqlClent.select_rows(DB_CONN, 'fk_role_user', 'id', 'role_id={}'.format(role_id))


def get_user_passwd(user_id):
    # 查询用户初始密码
    return MysqlClent.select_one(DB_CONN, 'fk_user', 'password', 'id={}'.format(user_id))


def activate_user(user_id):
    #  激活用户
    fk_user = {"password": "5b6b4267cec7633c66c13c9597acc0c5", "status": 11,
               "uuid": "0539a37d2e3048b69ef6ec3a00147b19", "is_active": "Y"}
    MysqlClent.update_dict(DB_CONN, 'fk_user', fk_user, 'id={}'.format(user_id))
    manage_user = {"user_status": 11, "available": 1}
    MysqlClent.update_dict(ManageSql.DB_CONN, 'biz_company_user', manage_user,
                      'user_id={0} AND company_id={1}'.format(user_id, ManageSql.get_company_id()))


def del_gps():
    # 删除gps
    gps_ids = MysqlClent.select_col(DB_CONN, 'fk_gps', 'id', 'POSITION("{}" IN code)'.format(loginAction.sign))
    gps_codes = MysqlClent.select_col(DB_CONN, 'fk_gps', 'code', 'POSITION("{}" IN code)'.format(loginAction.sign))
    MysqlClent.delete(DB_CONN, 'fk_gps', 'POSITION("{}" IN code)'.format(loginAction.sign))
    for gps_id in gps_ids:
        MysqlClent.delete(DB_CONN, 'fk_gps_finance', 'gps_id={}'.format(gps_id))
        MysqlClent.delete(DB_CONN, 'fk_gps_group_relation', 'gps_id={}'.format(gps_id))
    for gps_code in gps_codes:
        MysqlClent.delete(DB_CONN, 'fk_risk_except', 'gps_code={}'.format(gps_code))
        MysqlClent.delete(DB_CONN, 'fk_gps_location', 'gps_code={}'.format(gps_code))


def del_risks():
    # 删除风险点
    MysqlClent.delete(DB_CONN, 'fk_risk', 'POSITION("{}" IN name)'.format(loginAction.sign))


def del_group():
    # 删除分组
    group_ids = MysqlClent.select_col(DB_CONN, 'fk_gps_group', 'id',
                                      'POSITION("{}" IN group_name)'.format(loginAction.sign))
    MysqlClent.delete(DB_CONN, 'fk_gps_group', 'POSITION("{}" IN group_name)'.format(loginAction.sign))
    for group_id in group_ids:
        MysqlClent.delete(DB_CONN, 'fk_gps_group_relation', 'group_id={}'.format(group_id))


def del_finance():
    # 删除financeid
    finance_ids = MysqlClent.select_col(DB_CONN, 'fk_finance', 'id', 'POSITION("{}" IN owner)'.format(loginAction.sign))
    MysqlClent.delete(DB_CONN, 'fk_finance', 'POSITION("{}" IN owner)'.format(loginAction.sign))
    for finance_id in finance_ids:
        MysqlClent.delete(DB_CONN, 'fk_gps_finance', 'finance_id={}'.format(finance_id))
        MysqlClent.delete(DB_CONN, 'fk_risk_except', 'finance_id={}'.format(finance_id))
        MysqlClent.delete(DB_CONN, 'fk_gps_location', 'finance_id={}'.format(finance_id))


def del_role():
    # 删除角色
    roles = MysqlClent.select_col(DB_CONN, 'fk_role', 'id', 'POSITION("{}" IN name)'.format(loginAction.sign))
    MysqlClent.delete(DB_CONN, 'fk_role', 'POSITION("{}" IN name)'.format(loginAction.sign))
    for role_id in roles:
        MysqlClent.delete(DB_CONN, 'fk_role_moudel', 'role_id={}'.format(role_id))
        MysqlClent.delete(DB_CONN, 'fk_role_user', 'role_id={}'.format(role_id))


def del_user():
    # 删除角色
    user_ids = MysqlClent.select_col(DB_CONN, 'fk_user', 'id', 'POSITION("{}" IN name)'.format(loginAction.sign))
    MysqlClent.delete(DB_CONN, 'fk_user', 'POSITION("{}" IN name)'.format(loginAction.sign))
    for user_id in user_ids:
        MysqlClent.delete(DB_CONN, 'fk_user_jurisdiction', 'user_id={}'.format(user_id))
        condition = 'user_id={0} AND company_id={1}'.format(user_id, ManageSql.get_company_id())
        company_user_id = MysqlClent.select_col(ManageSql.DB_CONN, 'biz_company_user', 'id', condition)
        MysqlClent.delete(ManageSql.DB_CONN, 'biz_company_user', condition)
        MysqlClent.delete(ManageSql.DB_CONN, 'biz_company_user_device',
                          'company_user_id IN ({})'.format(tuple(company_user_id)))


def del_org():
    # 删除组织机构信息
    org_codes = MysqlClent.select_col(DB_CONN, 'fk_org', 'company_code',
                                      'POSITION("{}" IN name)'.format(loginAction.sign))
    MysqlClent.delete(DB_CONN, 'fk_org', 'POSITION("{}" IN name)'.format(loginAction.sign))
    for org_code in org_codes:
        MysqlClent.delete(DB_CONN, 'fk_org_invalid', 'org_code={}'.format(org_code))
        MysqlClent.delete(DB_CONN, 'fk_user', 'org_code={}'.format(org_code))
        MysqlClent.delete(DB_CONN, 'fk_user_jurisdiction', 'org_code={}'.format(org_code))
        MysqlClent.delete(DB_CONN, 'fk_rule', 'org_code={}'.format(org_code))
        MysqlClent.delete(DB_CONN, 'fk_role', 'org_code={}'.format(org_code))
        MysqlClent.delete(DB_CONN, 'fk_risk_except', 'org_code={}'.format(org_code))
        MysqlClent.delete(DB_CONN, 'fk_risk', 'org_code={}'.format(org_code))
        MysqlClent.delete(DB_CONN, 'fk_gps_group', 'org_code={}'.format(org_code))
        MysqlClent.delete(DB_CONN, 'fk_gps', 'org_code={}'.format(org_code))
        MysqlClent.delete(DB_CONN, 'fk_finance', 'org_code={}'.format(org_code))
