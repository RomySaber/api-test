#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-20 上午 10:21
@Author     : 罗林
@File       : MyThread.py
@desc       : 重新定义带返回值的线程类
"""

import threading
from common.myCommon.Logger import getlog

LOG = getlog(__name__)


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        threading.Thread.__init__(self)
        # super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.result = None
        LOG.debug('线程名: {}'.format(threading.current_thread().getName()))
        LOG.debug('当前的线程变量: {}'.format(threading.current_thread()))
        LOG.debug('线程正在运行的方法: {}'.format(self.func))
        LOG.debug('正在运行的线程: {}'.format(threading.enumerate()))
        LOG.debug('正在运行的线程数量: {}'.format(threading.activeCount()))

    def run(self):
        # 创建线程锁，由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突
        # threading.Lock().acquire()
        self.result = self.func(*self.args,)
        # 释放线程锁
        # threading.Lock().release()

    def get_result(self):
        return self.result
