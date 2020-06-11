#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-08 下午 5:50
@Author     : 宋超
@File       : PlatformSystem_query.py
@desc       :Pms系统的增、删、改、查功能
"""

from common.mydb import MysqlClent as mydb

db_info = {"dbhost": "192.168.15.161", "dbport": 3306, "dbname": "PlatformSystem", "dbuser": "i78dk",
           "dbpasswd": "i78dk.com"}
DB_CONN = mydb.get_conn(**db_info)


def get_info(table_name, column, *condition):
    string_list = list()
    if len(condition) == 0:
        info = mydb.select(DB_CONN, table_name, column)
    else:
        info = mydb.select(DB_CONN, table_name, column, ' AND '.join(condition))
    if len(info) > 0:
        string_list = [i if i is not None else '' for i in info[0]]
    return string_list


def get_tbl_infos(table_name, column, *condition):
    if len(condition) == 0:
        info_list = mydb.select_col(DB_CONN, table_name, column)
    else:
        info_list = mydb.select_col(DB_CONN, table_name, column, ' AND '.join(condition))
    return info_list


def delete_info(table_name, condition):
    mydb.delete(DB_CONN, table_name, condition)


def update_info(table_name, value, condition):
    mydb.update(DB_CONN, table_name, value, condition)


def select_PassWordReset_key(table_name, column, condition):
    rs = mydb.select_one(DB_CONN, table_name, column, condition)
    return rs


def insert_value(table_name, value_dict):
    mydb.insert(DB_CONN, table_name, value_dict)


def get_permission_id():
    # 返回一个
    id = mydb.select_one(conn=DB_CONN, column='id', table='Tbl_Role_Permission')
    return id


def get_permission_ids():
    # 返回列表
    ids = mydb.select(conn=DB_CONN, column='id', table='Tbl_Role_Permission')
    return ids


def get_permission_ids_to_str():
    # 返回列表并转换成字符串
    ids = mydb.select(conn=DB_CONN, table='Tbl_Permission', column='id')
    return ",".join([str(per_id[0]) for per_id in ids])
    # l = []
    # for per_id in ids:
    #     l.append(str(per_id[0]))
    # return ",".join(l)


def get_role_id(role_name):
    # 根据角色名查询角色id
    role_id = mydb.select_one(conn=DB_CONN, table='Tbl_Role', column='id',
                              condition='position("{}" in name)'.format(role_name))
    return role_id


def delete_role(role_name):
    # 根据角色名删除角色
    role_ids = mydb.select(conn=DB_CONN, table='Tbl_Role', column='id',
                           condition='position("{}" in name)'.format(role_name))
    for role_id in role_ids:
        mydb.delete(conn=DB_CONN, table='Tbl_Role_Permission', condition='role_id = {}'.format(role_id[0]))
        mydb.delete(conn=DB_CONN, table='Tbl_Role', condition='id = {}'.format(role_id[0]))


def get_business_id(business_name):
    # 根据系统名称查询一个系统id
    business_id = mydb.select_one(conn=DB_CONN, table='Tbl_Business_System', column='id',
                                  condition='position("{}" in name)'.format(business_name))
    return business_id


def delete_system(business_name):
    # 根据系统名称删除所有测试数据
    business_ids = mydb.select(conn=DB_CONN, table='Tbl_Business_System', column='id',
                               condition='position("{}" in name)'.format(business_name))
    for business_id in business_ids:
        mydb.delete(conn=DB_CONN, table='Tbl_Business_System_Permission',
                    condition='business_system_id = {}'.format(business_id[0]))
        mydb.delete(conn=DB_CONN, table='Tbl_Business_System_Config',
                    condition='business_system_id = {}'.format(business_id[0]))
        mydb.delete(conn=DB_CONN, table='Tbl_Business_System', condition='id = {}'.format(business_id[0]))


def get_tenantid(business_name, tenant_name):
    # 根据机构名称查询机构id
    business_id = mydb.select_one(conn=DB_CONN, table='Tbl_Business_System', column='id',
                                  condition='position("{}" in name)'.format(business_name))
    tenant_id = mydb.select_one(conn=DB_CONN, table='Tbl_Tenant', column='id',
                                condition='business_system_id = {} and position("{}" in name)'.format(
                                    business_id, tenant_name))
    return tenant_id


def get_tenant_adm_id(business_name, tenant_name, adm_name):
    # 根据机构管理员名称查询机构管理员id
    business_id = mydb.select_one(conn=DB_CONN, table='Tbl_Business_System', column='id',
                                  condition='position("{}" in name)'.format(business_name))
    tenant_id = mydb.select_one(conn=DB_CONN, table='Tbl_Tenant', column='id', condition='business_system_id = {} and '
                                                                                         'position("{}" in name)'.format(
        business_id, tenant_name))
    adm_id = mydb.select_one(conn=DB_CONN, table='Tbl_Tenant_Administrator', column='id',
                             condition='business_system_id = {} and '
                                       'tenant_id = {} and position("{}" in name)'.format(business_id, tenant_id,
                                                                                          adm_name))
    return adm_id


def delete_tanant_adm(business_name, tenant_name, adm_name):
    # 清除机构管理员测试数据
    business_ids = mydb.select(conn=DB_CONN, table='Tbl_Business_System', column='id',
                               condition='position("{}" in name)'.format(business_name))
    for business_id in business_ids:
        tenant_ids = mydb.select(conn=DB_CONN,table='Tbl_Tenant',column='id',
                                condition='business_system_id = {} and position("{}" in name)'.format(business_id[0], tenant_name))
        for tenant_id in tenant_ids:
            mydb.delete(conn=DB_CONN,table='Tbl_Tenant_Administrator',
                    condition='business_system_id = {} and tenant_id = {} and position("{}" in name)'.format(business_id[0], tenant_id[0], adm_name))
            mydb.delete(conn=DB_CONN, table='Tbl_Tenant', condition='id = "{}"'.format(tenant_id[0]))
    mydb.delete(conn=DB_CONN, table='Tbl_Business_System', condition='position("{}" in name)'.format(business_name))
    # business_id = mydb.select_one(conn=DB_CONN, table='Tbl_Business_System', column='id',
    #                               condition='position("{}" in name)'.format(business_name))
    # tenant_id = mydb.select_one(conn=DB_CONN, table='Tbl_Tenant', column='id',
    #                             condition='business_system_id = {} and position("{}" in name)'.format(
    #                                 business_id, tenant_name))
    # mydb.delete(conn=DB_CONN, table='Tbl_Business_System', condition='id = "{}"'.format(business_id))
    # mydb.delete(conn=DB_CONN, table='Tbl_Tenant', condition='id = "{}"'.format(tenant_id))
    # mydb.delete(conn=DB_CONN, table='Tbl_Tenant_Administrator',
    #             condition='business_system_id = {} and tenant_id = {} and position("{}" in name)'.format(
    #                 business_id, tenant_id, adm_name))


def delete_tanant_admi(business_name, tenant_name, adm_name):
    # 清除“消费分期”机构管理员测试数据，但不清除“消费分期”机构
    business_ids = mydb.select(conn=DB_CONN, table='Tbl_Business_System', column='id',
                               condition='position("{}" in name)'.format(business_name))
    for business_id in business_ids:
        tenant_ids = mydb.select(conn=DB_CONN,table='Tbl_Tenant',column='id',
                                condition='business_system_id = {} and position("{}" in name)'.format(business_id[0], tenant_name))
        for tenant_id in tenant_ids:
            mydb.delete(conn=DB_CONN,table='Tbl_Tenant_Administrator',
                    condition='business_system_id = {} and tenant_id = {} and position("{}" in name)'.format(business_id[0], tenant_id[0], adm_name))
            mydb.delete(conn=DB_CONN, table='Tbl_Tenant', condition='id = "{}"'.format(tenant_id[0]))
    # business_id = mydb.select_one(conn=DB_CONN, table='Tbl_Business_System', column='id',
    #                               condition='position("{}" in name)'.format(business_name))
    # tenant_id = mydb.select_one(conn=DB_CONN, table='Tbl_Tenant', column='id',
    #                             condition='business_system_id = {} and position("{}" in name)'.format(
    #                                 business_id, tenant_name))
    # mydb.delete(conn=DB_CONN, table='Tbl_Tenant', condition='id = "{}"'.format(tenant_id))
    # mydb.delete(conn=DB_CONN, table='Tbl_Tenant_Administrator',
    #             condition='business_system_id = {} and tenant_id = {} and position("{}" in name)'.format(
    #                 business_id, tenant_id, adm_name))


def get_user_id(user_name):
    # 根据用户名称查询用户id
    user_id = mydb.select_one(conn=DB_CONN, table='Tbl_User', column='id',
                              condition='position("{}"in realname)'.format(user_name))
    return user_id


def delete_user(user_name):
    # 根据用户名删除用户
    user_ids = mydb.select(conn=DB_CONN, table='Tbl_User', column='id',
                           condition='position("{}" in realname)'.format(user_name))
    for user_id in user_ids:
        mydb.delete(conn=DB_CONN, table='Tbl_User', condition='id = "{}"'.format(user_id[0]))


if __name__ == '__main__':
    print(1)
