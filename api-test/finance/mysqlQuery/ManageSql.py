#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018/5/22 0022 下午 1:32
@Author     : 罗林
@File       : ManageSql.py
@desc       : 
"""
from common.mydb import MysqlClent
from finance.testAction import loginAction


db_info = {"dbhost": "192.168.15.247", "dbport": 3306, "dbname": "car_manage", "dbuser": "carfinace",
           "dbpasswd": "carfinace_passwd"}
DB_CONN = MysqlClent.get_conn(**db_info)


def get_company_id(company_name=loginAction.companyName):
    #  获取数据库名称
    return MysqlClent.select_one(DB_CONN, 'biz_company', 'id', 'name= "{}"'.format(company_name))


def get_finance_db_id():
    #  获取数据库名称
    return '00' + str(
        MysqlClent.select_one(DB_CONN, 'biz_company', 'id', "`name` = \'{}\'".format(loginAction.companyName)))


def get_finance_db_name():
    #  获取数据库名称
    sqlname = MysqlClent.select_join(DB_CONN, 'biz_company_datasource as a,biz_company as b', 'a.db_name',
                                     'a.company_id = b.id', 'b.`name` = \'{}\''.format(loginAction.companyName))
    return sqlname[0][0]


def get_licence_file_id(company_name):
    # 查询公司licence_file_id
    return MysqlClent.select_one(DB_CONN, 'biz_company', 'licence_file_id', 'name= "{}"'.format(company_name))


def get_user_id(user_email):
    # 查询管理员id
    return MysqlClent.select_one(DB_CONN, 'biz_company_user', 'id', 'user_email = "{}"'.format(user_email))


def activate_user(user_email):
    # 激活管理员
    return MysqlClent.update(DB_CONN, 'biz_company_user', 'user_status=11', 'user_email = "{}"'.format(user_email))


def activate_manage_user(user_name):
    # 激活管理员
    return MysqlClent.update(DB_CONN, 'sys_manage', 'password="e1a4709bab6a4896c16008f6becb2dee",'
                                                    'uuid="e014dd1650e945f882144863167e503d",status=2',
                             'name = "{}"'.format(user_name))


def get_manage_user_id(user_name):
    # 查询所运营人员id
    return MysqlClent.select_one(DB_CONN, 'sys_manage', 'id', 'name="{}"'.format(user_name))


def get_manage_user_ids():
    # 模糊查询所运营人员id
    return MysqlClent.select_col(DB_CONN, 'sys_manage', 'id', 'POSITION("{}" IN name)'.format(loginAction.sign))


def drop_db():
    # 查询数据库名称
    db_names = MysqlClent.select_join(DB_CONN, 'biz_company_datasource as a,biz_company as b', 'a.db_name',
                                      'a.company_id = b.id', 'POSITION("{}" IN b.name)'.format(loginAction.sign))
    # 删除biz_company表中的企业
    MysqlClent.delete(DB_CONN, 'biz_company', 'POSITION("{}" IN name)'.format(loginAction.sign))
    # 删除 biz_company_datasource表中的数据库id
    for db_name in db_names:
        MysqlClent.delete(DB_CONN, 'biz_company_datasource', 'db_name="{}"'.format(db_name[0]))
        # 删除数据库
        MysqlClent.drop_database(DB_CONN, db_name[0])


def del_user():
    # 删除管理员
    user_ids = get_manage_user_ids()
    MysqlClent.delete(DB_CONN, 'biz_company_user',
                      'POSITION("{0}" IN user_email) or POSITION("{1}" IN user_name)'
                      .format(loginAction.sign, loginAction.sign))
    for user_id in user_ids:
        MysqlClent.delete(DB_CONN, 'biz_company_user_device', 'company_user_id="{}"'.format(user_id))


def del_manage_user():
    # 删除运营人员
    MysqlClent.delete(DB_CONN, 'sys_manage', 'POSITION("{}" IN name)'.format(loginAction.sign))
    for manage_id in get_manage_user_ids():
        # 删除运营人员权限
        MysqlClent.delete(DB_CONN, 'sys_manage_role', 'manage_id="{}"'.format(manage_id))


if __name__ == '__main__':
    print(get_finance_db_id())
