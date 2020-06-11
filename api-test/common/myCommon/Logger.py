#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018/5/2 0002 下午 3:49
@Author     : 罗林
@File       : Logger.py
@desc       : 指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
"""
import logging, time, platform, os.path
from common.myConfig import ConfigUtils as conf
from common.myFile import FileUtils


LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


class Logger(object):

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 创建日志名称。
        log_level = conf.get('report', 'LogLevel').lower()
        level = LEVELS[log_level]
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        # os.getcwd()获取当前文件的路径，os.path.dirname()获取指定文件路径的上级路径
        log_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/testReport/log/'
        if 'Windows' in platform.system():
            log_path = log_path.replace('/', '\\')
        FileUtils.mkdir(log_path)
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(level)

        log_name = log_path + rq + '.log'
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(filename=log_name, mode='a', encoding='utf-8')
        fh.setLevel(level)

        # 创建一个handler，用于写入error及以上级别的日志文件
        e_name = log_path + 'ERROR' + rq + '.log'
        eh = logging.FileHandler(filename=e_name, mode='a', encoding='utf-8')
        eh.setLevel(logging.ERROR)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(level)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)s %(name)s [line:%(lineno)d] %(levelname)s '
                                      '%(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        eh.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        self.logger.addHandler(eh)


def getlog(logger):
    return Logger(logger).logger


if __name__ == "__main__":
    log = getlog(__name__)
    log.info("看见好的借口给甲方了")
    # log.error("error")
    log.debug("debug")
    # log.exception("excep")
