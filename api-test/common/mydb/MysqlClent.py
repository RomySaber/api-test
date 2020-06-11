#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-02-21 下午 5:44
@Author     : 罗林
@File       : MysqlClent.py
@desc       :  操作mysql数据库
"""

import pymysql.cursors

from common.myCommon.Logger import getlog
from common.myConfig import ConfigUtils as conf

LOG = getlog(__name__)


def get_conn(dbhost=conf.get('mysql', 'DB_HOST'), dbport=conf.getint('mysql', 'DB_PORT'),
             dbname=conf.get('mysql', 'DB_NAME'), dbuser=conf.get('mysql', 'DB_USER'),
             dbpasswd=conf.get('mysql', 'DB_PASSWORD'), charset='utf8'):
    """
    获取sql连接
    :param dbhost:  数据库地址
    :param dbport: 数据库端口
    :param dbname: 数据库名称
    :param dbuser: 数据库账号
    :param dbpasswd: 数据库密码
    :param charset: 数据库字符集
    :return:返回数据库连接对象
    """
    LOG.debug("The mysql host is :" + dbhost)
    LOG.debug("The mysql port is :" + str(dbport))
    LOG.debug("The mysql user is :" + dbuser)
    LOG.debug("The mysql passwd is :" + dbpasswd)
    LOG.debug("The mysql db is :" + dbname)
    return pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpasswd, db=dbname, charset=charset)


def get_cursor(conn):
    """
    创建游标
    :param conn: 连接
    :return: 返回游标对象
    """
    cursor = conn.cursor()
    conn.ping(reconnect=True)  # 在每次运行sql之前，ping一次，如果连接断开就重连
    return cursor


def close_cursor(conn, cursor):
    """
     关闭游标 ，关闭连接
    :param conn: 连接
    :param cursor: 游标
    :return:
    """
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


def commit_query(conn, cursor, query):
    """
    提交查询语句
    :param conn: 数据库连接信息
    :param cursor:  游标
    :param query:  数据库查询语句
    :return: 返回执行行数
    """
    try:
        # 执行sql语句
        rows_num = cursor.execute(query)
        # 提交到数据库执行
        conn.commit()
        num = int(rows_num) if rows_num not in (None, 'NoneType', 'null', 'Null', '', ' ') else 0
        LOG.debug("The result rows count is : {}".format(num))
        return num
    except BaseException as e:
        LOG.error("The mysql {0} exec sql error: {1}".format(query, e))
        # 发生错误时回滚
        conn.rollback()


def executed_one(conn, query):
    """
    查询一条数据
    :param conn: 数据库连接信息
    :param query: 数据库查询语句
    :return: 返回字符串，默认取第一列第一行
    """
    cursor = get_cursor(conn)
    LOG.debug("The mysql exec :" + query)
    commit_query(conn, cursor, query)
    fc = cursor.fetchone()
    close_cursor(conn, cursor)
    if fc in (None, 'NoneType', 'null', 'Null', '', ' '):
        result = ''
    else:
        result = fc[0]
    LOG.debug("The result is : {}".format(result))
    return result


def executed_all(conn, query):
    """
    查询所有数据
    :param conn: 数据库连接信息
    :param query: 数据库查询语句
    :return: 二元数组
    """
    result = []
    cursor = get_cursor(conn)
    LOG.debug("The mysql exec :" + query)
    commit_query(conn, cursor, query)
    fc = cursor.fetchall()
    for r in fc:
        result.append(list(r))
    LOG.debug("The result is :" + str(result))
    close_cursor(conn, cursor)
    return result


def executed_rows(conn, query):
    """
    获取执行sql的总数
    :param conn: 数据库连接信息
    :param query: 数据库查询语句
    :return: 返回执行行数
    """
    cursor = get_cursor(conn)
    LOG.debug("The mysql exec :" + query)
    num = commit_query(conn, cursor, query)
    LOG.debug("The result is :" + str(num))
    close_cursor(conn, cursor)
    return num


def execute_many(conn, query, values_list):
    """
    执行多条SQL语句，用于批量新增和更新
    :param conn: 连接
    :param query: 查询语句
    :param values_list: 二维元组
    :return:
    """
    cursor = get_cursor(conn)
    try:
        # 执行sql语句
        LOG.debug("The mysql exec :" + query)
        rows_num = cursor.executemany(query, values_list)
        # 提交到数据库执行
        conn.commit()
        num = int(rows_num) if rows_num not in (None, 'NoneType', 'null', 'Null', '', ' ') else 0
        LOG.debug("The result rows count is : {}".format(num))
        return num
    except BaseException as e:
        LOG.error("The mysql {0} exec sql error: {1}".format(query, e))
        # 发生错误时回滚
        conn.rollback()
    close_cursor(conn, cursor)


def select(conn, table, column='*', condition=None):
    """
    查询所有数据
    :param conn: 数据库连接信息
    :param table: 需要查询的表
    :param column: 需要查询的列，为空时查询所有， col1,col2
    :param condition: 查询条件
    :return: 返回二元数组
    """
    query_list = ["SELECT", column, "FROM", table, ";"]
    if condition is not None:
        query_list.insert(-1, 'WHERE')
        query_list.insert(-1, condition)
    query = ' '.join(query_list)
    return executed_all(conn, query)


def select_join(conn, table, column, equivalent, condition=None):
    """
    查询有关联的表len(table.split(,)) = len(equivalent) + 1
    :param conn:  数据库连接信息
    :param table: 需要join的表，txx1,txx2,txx3
    :param column: 需要查询的列名， txx1.col1,txx2.col2,...
    :param equivalent: on等式 txx1.col1 = tx2.col2,txx3.col1=txx4.clo3
    :param condition: 查询条件 txx.xxcol1="xx" and txx.xxcol2 = "xx"
    :return:  二维数组
    """
    tables, equivalents = table.split(','), equivalent.split(',')
    if len(tables) == (len(equivalents) + 1):
        join_sql = list()
        for i in range(len(equivalents)):
            if i == 0:
                join_sql.extend([tables[i], "JOIN ", tables[i + 1], "ON", equivalents[i]])
            else:
                join_sql.extend(["JOIN ", tables[i + 1], "ON ", equivalents[i]])
        join_sql.append(';')
        query_list = ["SELECT", column, "FROM"]
        query_list.extend(join_sql)
        if condition:
            query_list.insert(-1, 'WHERE')
            query_list.insert(-1, condition)
        query = ' '.join(query_list)
    else:
        raise IndexError('table and equivalent the index not equality!')
    return executed_all(conn, query)


def select_col(conn, table, column, condition=None):
    """
    单独查询某列
    :param conn: 数据库连接信息
    :param table: 需要查询的表
    :param column: 需要查询的列，只能查询一列
    :param condition: 查询条件
    :return:  返回数组，展示一列的查询结果
    """
    query_list = ["SELECT", column, "FROM", table, ";"]
    if condition is not None:
        query_list.insert(-1, 'WHERE')
        query_list.insert(-1, condition)
    query = ' '.join(query_list)
    return [r[0] for r in executed_all(conn, query)]


def select_one(conn, table, column, condition=None):
    """
    单独查询某个值
    :param conn: 数据库连接信息
    :param table: 需要查询的表
    :param column: 需要查询的列，只能查询一列
    :param condition: 查询条件
    :return: 返回对应字段值，多条数据时只取第一条
    """
    query_list = ["SELECT", column, "FROM", table, "LIMIT 1;"]
    if condition is not None:
        query_list.insert(-1, 'WHERE')
        query_list.insert(-1, condition)
    query = ' '.join(query_list)
    return executed_one(conn, query)


def select_rows(conn, table, column='*', condition=None):
    """
    查询执行行数
    :param conn: 数据库连接信息
    :param table: 需要查询的表
    :param column: 需要查询的列，为空时查询所有， col1,col2
    :param condition: 查询条件
    :return: 返回查询条数
    """
    query_list = ["SELECT", column, "FROM", table, ";"]
    if condition is not None:
        query_list.insert(-1, 'WHERE')
        query_list.insert(-1, condition)
    query = ' '.join(query_list)
    return executed_rows(conn, query)


def insert(conn, table, value_dict):
    """
    插入语句
    :param conn:  数据库连接信息
    :param table:  需要插入的表
    :param value_dict: 插入信息 {"列名1"：值1，"列名2"：值2}
    :return: 返回执行条数
    """
    quotation = lambda x: '"{}"'.format(x) if isinstance(x, str) else "{}".format(x)
    values = ','.join([quotation(value) for value in value_dict.values()])
    clos = ','.join(value_dict.keys())
    query = ' '.join(["INSERT", "INTO ", table, "(", clos, ")", "VALUE", "(", values, ")", ";"])
    return executed_rows(conn, query)


def insert_many(conn, table, col_list, values_tuple):
    """
    插入多条语句  'insert into test (sdf,asd,aaa) VALUES ("%s","%s","%s")', ((1,2,3),(2,3,4),(3,4,5))
    :param conn: 数据库连接信息
    :param table: 表名
    :param col_list: 列名，数组或元组 (sdf,asd,aaa)
    :param values_tuple: 插入值，二维元组，二级元组或数组长度必须和列名数组长度一致 ((1,2,3),(2,3,4),(3,4,5))
    :return:  执行行数
    """

    col_num = len(col_list)
    query = ' '.join(["INSERT", "INTO ", table, "(", ','.join(col_list), ")", "VALUE",
                      "(", (',%s' * col_num).lstrip(','), ")", ";"])
    values_list = list()
    for value in values_tuple:
        if col_num != len(value):
            raise IndexError('the index of col_list and the index of values_tuple is not equality!')
        values_list.append(tuple(value))
    execute_many(conn, query, values_list)


def update_many(conn, table, col_list, values_tuple, col_condition_list):
    """
    更新多条语句，元组顺序一致，查询条件在 元组最后
    update user_tb set name=%s, sex=%s where id=%s and s_id=%s,
    (('小孙', '男'， 2， 1),
    ('小白', '女'， 3， 2),
    ('小猪', '男'， 4， 1),
    ('小牛', '男'， 5， 3),
    ('小唐', '女'， 6， 2))
    :param conn: 连接
    :param table: 表名
    :param col_list: 列名，数组或元组 (sdf,asd,aaa)
    :param values_tuple: 插入值，二维元组，二级元组或数组长度必须和列名数组长度一致 ((1,2,3),(2,3,4),(3,4,5))
    :param col_condition_list: 查询条件列名
    :return:  执行行数
    """
    query_list = list()
    query_list.append("UPDATE")
    query_list.append(table)
    query_list.append("SET")
    query_list.append(','.join(['{}=%s'.format(col_1) for col_1 in col_list]))
    if col_condition_list:
        query_list.append('WHERE')
        query_list.append(' AND '.join(['{}=%s'.format(col_2) for col_2 in col_condition_list]))
    query_list.append(';')
    values_list = list()
    col = col_list
    col.extend(col_condition_list)
    col_num = len(col)
    for value in values_tuple:
        if col_num != len(value):
            raise IndexError('the index of col_list and the index of values_tuple is not equality!')
        values_list.append(tuple(value))
    query = ' '.join(query_list)
    return execute_many(conn, query, values_list)


def insert_update_many(conn, table, col_list, values_tuple):
    """
    插入或更新多条语句
    'insert into test_tbl (id,dr) values  (1,'2'),(2,'3'),...(x,'y') on duplicate key update dr=values(dr);
    这个语法和适合用在需要判断记录是否存在，不存在则插入存在则更新的记录
    :param conn:
    :param table: 表名
    :param col_list: 列名，数组或元组 (sdf,asd,aaa)
    :param values_tuple: 插入值，二维元组，二级元组或数组长度必须和列名数组长度一致 ((1,2,3),(2,3,4),(3,4,5))
    :return:  执行行数
    """
    col_condition = ','.join(['{0}=VALUES({0})'.format(t) for t in col_list])
    for value in values_tuple:
        if len(col_list) != len(value):
            raise IndexError('the index of col_list and the index of values_tuple is not equality!')
    query = ["INSERT", "INTO ", table, "(", ','.join(col_list), ")", "VALUE", ','.join(values_tuple),
             'ON', 'DUPLICATE', 'KEY', 'UPDATE', col_condition, ";"]
    executed_rows(conn, ' '.join(query))


def update(conn, table, value, condition=None):
    """
    更新数据库语句
    :param conn: 数据库连接
    :param table: 需要更新的表
    :param value:  更新值 列名1=值1，列名2=值2
    :param condition: 查询条件
    :return:  返回执行条数
    """
    query_list = ["UPDATE", table, "SET", value, ";"]
    if condition is not None:
        query_list.insert(-1, 'WHERE')
        query_list.insert(-1, condition)
    query = ' '.join(query_list)
    return executed_rows(conn, query)


def update_dict(conn, table, value_dict, condition=None):
    """
    更新数据库语句
    :param conn: 数据库连接
    :param table: 需要更新的表
    :param value_dict:  更新值 {"列名1"：值1，"列名2"：值2}
    :param condition: 查询条件
    :return:  返回执行条数
    """
    # 判断value是否需要添加引号
    quotation = lambda x: '"{}"'.format(x) if isinstance(x, str) else "{}".format(x)
    value_list = [col + '=' + quotation(value) for col, value in value_dict.items()]
    value = ','.join(value_list)
    query_list = ["UPDATE", table, "SET", value, ";"]
    if condition is not None:
        query_list.insert(-1, 'WHERE')
        query_list.insert(-1, condition)
    query = ' '.join(query_list)
    return executed_rows(conn, query)


def delete(conn, table, condition):
    """
    删除语句
    :param conn: 数据库连接
    :param table: 需要删除的表
    :param condition: 查询条件
    :return: 返回执行条数
    """
    query_list = ["DELETE", "FROM", table, "WHERE", condition, ";"]
    query = ' '.join(query_list)
    return executed_rows(conn, query)


def drop_database(conn, database_name):
    """
    删除数据库
    :param conn:  数据库连接
    :param database_name:  要删除的数据库名称
    :return: 返回执行条数
    """
    query_list = ['drop', 'database', database_name, ';']
    query = ' '.join(query_list)
    return executed_rows(conn, query)
