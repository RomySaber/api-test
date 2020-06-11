#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-02-21 下午 2:29
@Author     : 罗林
@File       : MyRedis.py
@desc       : 操作Redis
"""

import redis


class MyRedis(object):
    def __init__(self, host, port, db=None, passwd=None, timeout=10):
        self.host = host
        self.port = port
        self.db = db
        self.timeout = timeout
        self.passwd = passwd
        pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, password=self.passwd,
                                    socket_timeout=self.timeout, decode_responses=True)
        self.r = redis.Redis(connection_pool=pool, max_connections=10)

    def redis_set(self, name, value):
        self.r.set(name, value)

    def redis_get(self, name):
        return self.r.get(name)

    def get_list(self):
        return self.r.client_list()

    def get_name(self):
        return self.r.client_getname()

    def hget(self, name):
        # 获取哈希
        return self.r.hgetall(name)

    def get_keys(self):
        return [str(i) for i in self.r.keys()]

    def del_name(self, *name):
        self.r.delete(*name)
