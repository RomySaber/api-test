#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-17 上午 11:35
@Author     : 罗林
@File       : TestLink.py
@desc       : 从testlink获取回归测试用例数量
"""
import re

from common.myConfig import MysqlConfig
from common.mydb import MysqlClent as mydb


def get_testlink_name(project):
    """
    从auto_ci获取testlink 项目名称 ,并在testlink数据库中查询项目id
    :param project: 项目英文名称
    :return:  testlink 项目名称
    """
    db = mydb.get_conn()
    testlink_project = ''
    testlink = mydb.select_one(db, 't_dict', 'testlink', 'code="{}"'.format(project))
    if testlink not in ('NoneType', 'null', 'Null', '', ' ', None):
        if ':' in testlink or '：' in testlink:
            testlink_name = re.split('[:：]', testlink)[-1]
            # node_type_id=1获取testlink项目名称
            testlink_project = select_str('node_type_id=1', 'name="{}"'.format(testlink_name))
    return testlink_project


def get_testlink_db():
    """
    从auto_ci获取testlink 数据库信息
    :return:  testlink 数据库信息
    """
    testlink_db = {"dbhost": MysqlConfig.get("testlink_db_host"), "dbport": MysqlConfig.getint("testlink_db_port"),
                   "dbname": MysqlConfig.get("testlink_db_db"), "dbuser": MysqlConfig.get("testlink_db_name"),
                   "dbpasswd": MysqlConfig.get("testlink_db_passwd")}
    return mydb.get_conn(**testlink_db)


def select_list(*condition):
    """
    查询nodes_hierarchy表id字段，转换成数组
    :param condition: 查询条件
    :return: 返回数组查询结果
    """
    db = get_testlink_db()
    results = mydb.select(db, 'nodes_hierarchy', 'id', ' AND '.join(condition))
    return [_result[0] for _result in results]


def select_str(*condition):
    """
    查询nodes_hierarchy表id字段，转换成字符串
    :param condition:  查询条件
    :return: 返回查询结果字符串
    """
    db = get_testlink_db()
    return mydb.select_one(db, 'nodes_hierarchy', 'id', ' AND '.join(condition))


def get_testsuites(parent_id_list, suite_list):
    """
    从nodes_hierarchy表 循环获取 node_type_id=2的测试套件
    :param parent_id_list: 父类ID数组
    :param suite_list: 返回数组
    :return: 返回数组
    """
    suite_list.extend(parent_id_list)
    if len(parent_id_list) == 1:
        testsuites = select_list('node_type_id=2', 'parent_id={}'.format(*parent_id_list))
    else:
        testsuites = select_list('node_type_id=2', 'parent_id in {}'.format(tuple(parent_id_list)))
    suite_list.extend(testsuites)
    if len(testsuites) > 0:
        get_testsuites(testsuites, suite_list)
    suite_list = list(set(suite_list))
    return suite_list


def get_test_suites(testlink_project_id):
    """
    从nodes_hierarchy表 获取 node_type_id=2的测试套件
    :param testlink_project_id: testlink的项目id
    :return: 返回 测试套件 数组
    """
    testsuites_list = list()
    if testlink_project_id not in ('NoneType', 'null', 'Null', '', ' ', None):
        # node_type_id=2获取testlink测试套件
        case_statistics_condition = MysqlConfig.get("testlink_case_statistics")
        if case_statistics_condition == '':
            testsuites = select_list('node_type_id=2', 'parent_id={}'.format(testlink_project_id))
        else:
            testsuites = select_list('node_type_id=2', 'parent_id={}'.format(testlink_project_id),
                                     'name like "%{}%"'.format(case_statistics_condition))
        if len(testsuites) > 0:
            testsuites_list = get_testsuites(testsuites, [])
    return testsuites_list


def get_testlink_num(project):
    """
    查询测试用例数量
    :param project:  项目英文名称
    :return: 返回count
    """
    count = 0
    testlink_project = get_testlink_name(project)
    testsuites_list = get_test_suites(testlink_project)
    if len(testsuites_list) > 0:
        # node_type_id=3获取testlink测试用例
        # testcases = select_list('node_type_id=3', 'parent_id in {}'.format(tuple(testsuites_list)))
        # count = len(list(set(testcases)))
        count = mydb.select_rows(get_testlink_db(), 'nodes_hierarchy', 'id',
                                 'node_type_id=3 AND parent_id in {}'.format(tuple(testsuites_list)))
    return count


if __name__ == '__main__':
    print(get_testlink_num('reborn'))
