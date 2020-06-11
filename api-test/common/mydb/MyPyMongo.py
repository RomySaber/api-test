#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-02-21 下午 2:00
@Author     : 罗林
@File       : MyPyMongo.py
@desc       :   操作MongoDB

python -m pip install pymongo
"""
from pymongo import MongoClient
from common.myCommon.Logger import getlog


class MyPyMongo(object):
    LOG = getlog(__name__)

    def __init__(self, host, port, mydb, collist, username=None, password=None, use_db=None):
        """
        mongo连接信息
        :param host: mongo地址
        :param port: 端口
        :param username: 用户名
        :param password: 密码
        :param mydb: 登录默认数据库
        :param collist: 使用集合
        :param use_db: 使用的数据库
        """
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.mydb = mydb
        self.collist = collist
        self.use_db = use_db
        m = '连接信息：HOST:【{0}】，PORT：【{1}】，USERNAME：【{2}】，PASSWORD：【{3}】，DB：【{4}】，' \
            'COLLIST集合：【{5}】'.format(self.host, self.port, self.username, self.password, self.mydb, self.collist)
        try:
            myclient = MongoClient(self.host, self.port)
            mydb = myclient[self.mydb]
            if self.username != '' or self.username is not None:
                # 连接mydb数据库,账号密码认证
                mydb.authenticate(self.username, self.password)
            self.LOG.debug('SUCCESS client MongoDB : 【{}】'.format(m))
            if self.use_db is not None:
                self.LOG.debug('SUCCESS switch to MongoDB : 【{}】'.format(self.use_db))
                mydb = myclient[self.use_db]
            self.mycol = mydb[self.collist]
            self.LOG.debug('SUCCESS client collist : 【{}】'.format(self.collist))
        except Exception as e:
            message = 'FAIL client MongoDB : 【{0}】 ,Because : 【{1}】'.format(m, e)
            self.LOG.error(message)
            raise e

    def insert_one(self, mydict):
        """
        返回插入文档的 id 值
        :param mydict:  字典插入值
        :return:
        """
        return self.mycol.insert_one(mydict).inserted_id

    def insert_many(self, mylist):
        """
        返回插入的所有文档对应的 _id 值
        :param mylist:  数组字典插入值
        :return:
        """
        return self.mycol.insert_many(mylist).inserted_ids

    def find_one(self):
        """
        查询 sites 文档中的第一条数据
        :return:
        """
        return self.mycol.find_one()

    def find(self):
        """
        查找 sites 集合中的所有数据
        :return:
        """
        return [x for x in self.mycol.find()]

    def find_date(self, myquery):
        """
        查找 sites 集合中的所有数据
        :param myquery: 查询语句
        :return:
        """
        myresult = self.mycol.find(myquery)
        return [x for x in myresult]

    def find_limit(self, limit, myquery=None):
        """
        查找 sites 集合中的所有数据
        :param limit: 限制条数
        :param myquery: 查询语句
        :return:
        """
        myresult = self.mycol.find(myquery).limit(limit)
        return [x for x in myresult]

    def update_one(self, myquery, newvalues):
        """
        更新一条数据
        :param myquery: 查询语句
        :param newvalues: 更新值
        :return:
        """
        self.mycol.update_one(myquery, {"$set": newvalues})

    def update_many(self, myquery, newvalues):
        """
        更新多条数据
        :param myquery: 查询语句
        :param newvalues: 更新值
        :return:
        """
        self.mycol.update_many(myquery, {"$set": newvalues})

    def find_sort(self, myquery, sort=-1):
        """
        方法第一个参数为要排序的字段，第二个字段指定排序规则，1 为升序，-1 为降序，默认为升序
        :param myquery:  查询语句
        :param sort: 排序
        :return:
        """
        if sort in (1, -1):
            mydoc = self.mycol.find().sort(myquery, sort)
            return [x for x in mydoc]
        else:
            raise Exception('please input the sort in 1 or -1')

    def delete_one(self, myquery):
        """
        删除一条语句
        :param myquery: 查询语句
        :return:
        """
        self.mycol.delete_one(myquery)

    def delete_many(self, myquery=None):
        """
        删除多条数据
        :param myquery:  查询语句
        :return:
        """
        if myquery is None:
            # 传入的是一个空的查询对象，则会删除集合中的所有文档
            x = self.mycol.delete_many({})
        else:
            x = self.mycol.delete_many(myquery)
        self.LOG.debug('{}个文档已删除'.format(x.deleted_count))

    def drop(self):
        """
        删除使用的集合
        :return:
        """
        self.mycol.drop()
