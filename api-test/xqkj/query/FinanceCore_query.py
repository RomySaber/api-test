#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-18 下午 2:00
@Author     : 闫红
@File       : FinanceCore_query.py
@desc       :对外控制系统的增、删、改、查功能
"""

from common.mydb import MysqlClent as mydb

db_info = {"dbhost": "192.168.15.161", "dbport": 3306, "dbname": "FinanceCore", "dbuser": "xqkji78dk",
           "dbpasswd": "dfljlcl39*33$@e"}
DB_CONN = mydb.get_conn(**db_info)


def delete_databases(tanant_name):
    # 根据机构名删除Tbl_PlatformUser表中对应数据、删除Tbl_CompanyDataSource表中对应数据，
    # 并删除数据库，删除Tbl_Business表中数据
    tenantUuids = mydb.select(conn=DB_CONN, table='Tbl_Business', column='tenantUuid',
                              condition='position("{}" in name)'.format(tanant_name))
    for tenantUuid in tenantUuids:
        # 查询dbname
        dbname = mydb.select(conn=DB_CONN, table='Tbl_CompanyDataSource',
                             column='db_name', condition='tenantUuid = "{}"'.format(tenantUuid[0]))
        # 根据dbname删除db
        mydb.drop_database(conn=DB_CONN, database_name="{}".format(dbname[0][0]))
        # 删除Tbl_CompanyDataSource表中删除db的记录数据
        mydb.delete(conn=DB_CONN, table='Tbl_CompanyDataSource', condition='tenantUuid = "{}"'.format(tenantUuid[0]))
        # 删除Tbl_PlatformUser表中该机构的用户
        mydb.delete(conn=DB_CONN, table='Tbl_PlatformUser', condition='tenantUuid = "{}" '.format(tenantUuid[0]))
    # 删除Tbl_Business表中name为tanant_name的数据
    mydb.delete(conn=DB_CONN, table='Tbl_Business', condition='position("{}" in name)'.format(tanant_name))


if __name__ == '__main__':
    print(1)
