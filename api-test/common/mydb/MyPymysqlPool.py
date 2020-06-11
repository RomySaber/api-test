#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-06 下午 4:27
@Author     : 罗林
@File       : MyPymysqlPool.py
@desc       :  多线程连接数据库
"""

import pymysql
from DBUtils.PooledDB import PooledDB

from common.myCommon import MyThread
from common.myCommon.Logger import getlog
from common.myConfig import ConfigUtils as conf

LOG = getlog(__name__)
QUOTATION = lambda x: '"{}"'.format(x) if isinstance(x, str) else "{}".format(x)


class MyPymysqlPool(object):
    def __init__(self, dbhost=conf.get('mysql', 'DB_HOST'), dbport=conf.getint('mysql', 'DB_PORT'),
                 dbname=conf.get('mysql', 'DB_NAME'), dbuser=conf.get('mysql', 'DB_USER'),
                 dbpasswd=conf.get('mysql', 'DB_PASSWORD'), charset='utf8', maxconnections=20):
        """
        数据库构造函数，从连接池中取出连接，并生成操作游标
        :param dbhost: 数据库地址
        :param dbport: 数据库端口
        :param dbname: 数据库名称
        :param dbuser:  数据库账号
        :param dbpasswd: 数据库密码
        :param charset: 数据库字符集
        :param maxconnections:连接池通常允许的最大连接数，0或None表示任意数量的连接
        """
        # mincached 最少的空闲连接数，如果空闲连接数小于这个数，pool会创建一个新的连接,0表示启动时没有连接
        # maxcached 最大的空闲连接数，如果空闲连接数大于这个数，pool会关闭空闲连接，0或None表示无限制的池大小
        # use_unicode=False, cursorclass=DictCursor（返回字典格式）
        # ping:确定何时使用ping()检查连接(0=None=never,1=default=每当从池中获取时,2=创建游标时,4 =执行查询时,7=always)
        self.conn = PooledDB(creator=pymysql, mincached=0, maxcached=5, maxconnections=maxconnections, host=dbhost,
                             port=dbport, user=dbuser, passwd=dbpasswd, db=dbname, charset=charset, ping=4).connection()
        self.cursor = self.conn.cursor()

    def close_conn(self):
        """
         关闭游标 ，关闭连接
        """
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()

    def commit_query(self, query):
        """
        提交查询语句
        :param query:  数据库查询语句
        :return: 返回执行行数
        """
        # self.conn.ping(reconnect=True)
        try:
            # 执行sql语句
            rows_num = self.cursor.execute(query)
            # 提交到数据库执行
            self.conn.commit()
            num = int(rows_num) if rows_num not in (None, 'NoneType', 'null', 'Null', '', ' ') else 0
            LOG.debug("The result rows count is : {}".format(num))
            return num
        except BaseException as e:
            LOG.error("The mysql {0} exec sql error: {1}".format(query, e))
            # 发生错误时回滚
            self.conn.rollback()
        finally:
            self.close_conn()

    def executed_one(self, query):
        """
        查询一条数据
        :param query: 数据库查询语句
        :return: 返回字符串，默认取第一列第一行
        """
        LOG.debug("The mysql exec :" + query)
        num = self.commit_query(query)
        result = ''
        if num > 0:
            result = self.cursor.fetchone()[0]
        LOG.debug("The result is : {}".format(result))
        return result

    def executed_all(self, query):
        """
        查询所有数据
        :param query: 数据库查询语句
        :return: 二维数组
        """
        LOG.debug("The mysql exec :" + query)
        num = self.commit_query(query)
        result = list()
        if num > 0:
            result = [list(fc) for fc in self.cursor.fetchall()]
        LOG.debug("The result is : {}".format(result))
        return result

    def executed_rows(self, query):
        """
        获取执行sql的总数
        :param query: 数据库查询语句
        :return: 返回执行行数
        """
        LOG.debug("The mysql exec :" + query)
        num = self.commit_query(query)
        LOG.debug("The result is :" + str(num))
        return num

    def executed_many(self, query, value_tuple):
        """
        批量执行 SQL语句，用于批量插入或批量更新
        :param query:  插入语句/更新语句
        :param value_tuple:  二维元组
        :return:
        """
        try:
            # 执行sql语句
            rows_num = self.cursor.executemany(query, value_tuple)
            # 提交到数据库执行
            self.conn.commit()
            num = int(rows_num) if rows_num else 0
            LOG.debug("The result rows count is : {}".format(num))
            return num
        except BaseException as e:
            LOG.error("The mysql {0} exec sql error: {1}".format(query, e))
            # 发生错误时回滚
            self.conn.rollback()

    def select(self, table, column='*', *condition):
        """
        查询所有数据
        :param table: 需要查询的表
        :param column: 需要查询的列，为空时查询所有， col1,col2
        :param condition: 查询条件
        :return: 返回数组,元素是字典
        """
        query_list = ["SELECT", column, "FROM", table, ";"]
        if len(condition) > 0:
            query_list.insert(-1, 'WHERE')
            query_list.insert(-1, ' AND '.join(condition))
        query = ' '.join(query_list)
        return self.executed_all(query)

    def select_join(self, table, column, equivalent, *condition):
        """
        查询有关联的表len(table.split(,)) = len(equivalent) + 1
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
            if len(condition) > 0:
                query_list.insert(-1, 'WHERE')
                query_list.insert(-1, ' AND '.join(condition))
            query = ' '.join(query_list)
        else:
            raise IndexError('table and equivalent the index not equality!')
        return self.executed_all(query)

    def select_col(self, table, column, *condition):
        """
        单独查询某列
        :param table: 需要查询的表
        :param column: 需要查询的列，只能查询一列
        :param condition: 查询条件
        :return:  返回数组，展示一列的查询结果
        """
        query_list = ["SELECT", column, "FROM", table, ";"]
        if len(condition) > 0:
            query_list.insert(-1, 'WHERE')
            query_list.insert(-1, ' AND '.join(condition))
        query = ' '.join(query_list)
        return [result[0] for result in self.executed_all(query)]

    def select_one(self, table, column, *condition):
        """
        单独查询某个值
        :param table: 需要查询的表
        :param column: 需要查询的列，只能查询一列
        :param condition: 查询条件
        :return: 返回对应字段值，多条数据时只取第一条
        """
        query_list = ["SELECT", column, "FROM", table, "LIMIT 1;"]
        if len(condition) > 0:
            query_list.insert(-1, 'WHERE')
            query_list.insert(-1, ' AND '.join(condition))
        query = ' '.join(query_list)
        return self.executed_one(query)

    def select_rows(self, table, column='*', *condition):
        """
        查询执行行数
        :param table: 需要查询的表
        :param column: 需要查询的列，为空时查询所有， col1,col2
        :param condition: 查询条件
        :return: 返回查询条数
        """
        query_list = ["SELECT", column, "FROM", table, ";"]
        if len(condition) > 0:
            query_list.insert(-1, 'WHERE')
            query_list.insert(-1, ' AND '.join(condition))
        query = ' '.join(query_list)
        return self.executed_rows(query)

    def insert(self, table, value_dict):
        """
        插入语句
        :param table:  需要插入的表
        :param value_dict: 插入信息 {"列名1"：值1，"列名2"：值2}
        :return: 返回执行条数
        """
        values = ','.join([QUOTATION(value) for value in value_dict.values()])
        clos = ','.join(value_dict.keys())
        query = ' '.join(["INSERT", "INTO ", table, "(", clos, ")", "VALUE", "(", values, ")", ";"])
        return self.executed_rows(query)

    def insert_many(self, table, col_list, values_tuple):
        """
        插入多条语句  'insert into test (sdf,asd,aaa) VALUES ("%s","%s","%s")', ((1,2,3),(2,3,4),(3,4,5))
        :param table: 表名
        :param col_list: 列名，数组或元组 (sdf,asd,aaa)
        :param values_tuple: 插入值，二维元组，二级元组或数组长度必须和列名数组长度一致 ((1,2,3),(2,3,4),(3,4,5))
        :return:  执行行数
        """
        col_num = len(col_list)
        query = ' '.join(["INSERT", "INTO ", table, "(", ','.join(col_list), ")", "VALUE",
                          "(", (',%s' * col_num).lstrip(','), ")", ";"])
        LOG.debug("The mysql exec :" + query)
        values_list = list()
        for value in values_tuple:
            if col_num != len(value):
                raise IndexError('the index of col_list and the index of values_tuple is not equality!')
            values_list.append(tuple(value))
        return self.executed_many(query, values_list)

    def update_many(self, table, col_list, values_tuple, col_condition_list):
        """
        更新多条语句，元组顺序一致，查询条件在 元组最后
        update user_tb set name=%s, sex=%s where id=%s and s_id=%s,
        (('小孙', '男'， 2， 1),
        ('小白', '女'， 3， 2),
        ('小猪', '男'， 4， 1),
        ('小牛', '男'， 5， 3),
        ('小唐', '女'， 6， 2))
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
        LOG.debug("The mysql exec :" + query)
        return self.executed_many(query, values_list)

    def insert_update_many(self, table, col_list, values_tuple):
        """
        插入或更新多条语句
        'insert into test_tbl (id,dr) values  (1,'2'),(2,'3'),...(x,'y') on duplicate key update dr=values(dr);
        这个语法和适合用在需要判断记录是否存在，不存在则插入存在则更新的记录
        :param table: 表名
        :param col_list: 列名，数组或元组 (sdf,asd,aaa)
        :param values_tuple: 插入值，二维元组，二级元组或数组长度必须和列名数组长度一致 ((1,2,3),(2,3,4),(3,4,5))
        :return:  执行行数
        """
        col_condition = ','.join(['{0}=VALUES({0})'.format(t) for t in col_list])
        col_num = len(col_list)
        for value in values_tuple:
            if col_num != len(value):
                raise IndexError('the index of col_list and the index of values_tuple is not equality!')
        query = ["INSERT", "INTO ", table, "(", ','.join(col_list), ")", "VALUE", ','.join(values_tuple),
                 'ON', 'DUPLICATE', 'KEY', 'UPDATE', col_condition, ";"]
        self.executed_rows(' '.join(query))

    def update_case(self, table, col_list, values_tuple, col_condition, condition_tuple, *condition):
        """
        更新数据库语句
        :param table: 需要更新的表
        :param col_list:  更新列名列表
        :param values_tuple:  更新值二维元组
        :param col_condition:  CASE列名
        :param condition_tuple:  CASE值，元组
        :param condition: 查询条件
        :return:  返回执行条数
        """
        query_list = ["UPDATE", table, "SET"]
        for values in values_tuple:
            if len(col_list) != len(values):
                raise IndexError('the index of col_list and the index of values_tuple is not equality!')
        update_value = list()
        for i in range(len(col_list)):
            case_value = list()
            case_value.append('{0} = CASE {1}'.format(col_list[i], col_condition))
            for value in values_tuple:
                case_value.append('WHEN {0} THEN {1}'.format(col_list[i], value[i]))
            case_value.append('END')
            update_value.append(' '.join(case_value))
        query_list.append(','.join(update_value))
        query_list.append('WHERE')
        query_list.append(col_condition)
        query_list.append('IN {}'.format(condition_tuple))
        if len(condition) > 0:
            query_list.append('AND')
            query_list.append(' AND '.join(condition))
        query_list.append(';')
        query = ' '.join(query_list)
        return self.executed_rows(query)

    def update(self, table, value, *condition):
        """
        更新数据库语句
        :param table: 需要更新的表
        :param value:  更新值 列名1=值1，列名2=值2
        :param condition: 查询条件
        :return:  返回执行条数
        """
        query_list = ["UPDATE", table, "SET", value, ";"]
        if len(condition) > 0:
            query_list.insert(-1, 'WHERE')
            query_list.insert(-1, ' AND '.join(condition))
        query = ' '.join(query_list)
        return self.executed_rows(query)

    def update_dict(self, table, value_dict, *condition):
        """
        更新数据库语句
        :param table: 需要更新的表
        :param value_dict:  更新值 {"列名1"：值1，"列名2"：值2}
        :param condition: 查询条件
        :return:  返回执行条数
        """
        # 判断value是否需要添加引号
        value_list = [col + '=' + QUOTATION(value) for col, value in value_dict.items()]
        value = ','.join(value_list)
        query_list = ["UPDATE", table, "SET", value, ";"]
        if len(condition) > 0:
            query_list.insert(-1, 'WHERE')
            query_list.insert(-1, ' AND '.join(condition))
        query = ' '.join(query_list)
        return self.executed_rows(query)

    def delete(self, table, condition):
        """
        删除语句
        :param table: 需要删除的表
        :param condition: 查询条件
        :return: 返回执行条数
        """
        query_list = ["DELETE", "FROM", table, "WHERE", condition, ";"]
        query = ' '.join(query_list)
        return self.executed_rows(query)

    def drop_database(self, database_name):
        """
        删除数据库
        :param database_name:  要删除的数据库名称
        :return: 返回执行条数
        """
        query_list = ['drop', 'database', database_name, ';']
        query = ' '.join(query_list)
        return self.executed_rows(query)


if __name__ == '__main__':
    c = MyPymysqlPool()
    c1 = MyPymysqlPool()
    print(c.select_one('t_dict', 'rap', 'code="finance"', 'name="小启控车"'))
    print(c.select_rows('t_dict', 'rap'))
    t1 = MyThread.MyThread(c.select, ('t_dict', 'rap', 'code="finance"', 'name="小启控车"',))
    t1.start()
    t2 = MyThread.MyThread(c1.select_rows, ('t_dict', 'rap',))
    t2.start()
    t1.join()
    t2.join()
    print(t1.get_result())
    print(t2.get_result())
    # th = list()
    # for i in range(2):
    #     t = MyThread.MyThread(c1.select_rows, ('t_dict', 'rap',))
    #     t.start()
    #     th.append(t)
    # for t in th:
    #     t.join()
    # 执行完成操作后手动执行关闭数据库连接
    c.close_conn()
    c1.close_conn()
