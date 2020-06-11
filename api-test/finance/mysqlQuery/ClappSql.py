#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-03 下午 3:10
@Author     : 罗林
@File       : ClappSql.py
@desc       : 
"""

from common.mydb import MysqlClent as mydb
from finance.mysqlQuery import ManageSql

db_info = ManageSql.db_info
db_info['dbname'] = ManageSql.get_finance_db_name()
DB_CONN = mydb.get_conn(**db_info)


def get_car_id():
    return mydb.select_one(DB_CONN, 'fk_finance', 'id', 'pay_status="HKZ" and is_active="Y"')


def get_device_id():
    return mydb.select_one(DB_CONN, 'fk_gps', 'id', 'is_active="Y"')


def get_gps_org_code(device_id):
    return mydb.select_one(DB_CONN, 'fk_gps', 'org_code', 'id={}'.format(device_id))


def get_gps_org_id(org_code):
    return mydb.select_one(DB_CONN, 'fk_org', 'id', 'company_code={}'.format(org_code))


def get_gps_group_id(org_code):
    return mydb.select_one(DB_CONN, 'fk_gps_group', 'id', 'org_code={}'.format(org_code))


def get_file_id(gps_finance_id):
    return mydb.select_one(DB_CONN, 'fk_gps_finance', 'file_id', 'id={}'.format(gps_finance_id))


if __name__ == '__main__':
    print(get_car_id())
