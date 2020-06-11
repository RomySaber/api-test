#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018/5/2 0002 下午 5:37
@Author     : 罗林
@File       : RunTestApi.py
@desc       : 批量运行测试用例
"""

import os
import time
import unittest
import sys
from common.myCommon import MyThread
from common.myFile import total_line
from common.myCommon.Logger import getlog
from common.myConfig import ConfigUtils
from common.myFile import FileUtils
from common.HTMLTestRunner import HTMLTestRunner
from common.mydb import MysqlClent as ms
from common.myCommon import TestCaseCover

LOGGER = getlog(__name__)


class RunTestApi(object):
    def __init__(self, project_name, moudle=None):
        self.project_name = project_name
        self.moudle = moudle
        self.top_level_dir = FileUtils.is_windows(os.path.split(os.path.abspath(__file__))[0])
        LOGGER.info('项目路径：{}'.format(self.top_level_dir))
        self.project_path = FileUtils.is_windows(os.path.join(self.top_level_dir, self.project_name))
        self.case_path = FileUtils.is_windows(os.path.join(self.project_path, 'test'))
        # 报告存放路径
        self.report_path = FileUtils.is_windows(os.path.join(self.top_level_dir, 'testReport/report/'))
        FileUtils.mkdir(self.report_path)
        LOGGER.info('case存放路径：{0}'.format(self.case_path))
        LOGGER.info('报告存放路径：{0}'.format(self.report_path))

    def is_valid_path(self):
        flag = False
        if os.path.exists(self.case_path) and os.path.isdir(self.case_path):
            file_lists = FileUtils.getFileList(self.case_path, [])
            for file in file_lists:
                file_name = os.path.basename(file)
                if file_name.startswith('test'):
                    flag = True
                    break
        return flag

    def case(self):
        testcase = unittest.TestSuite()
        if self.is_valid_path():
            if self.moudle in (None, '', ' '):
                discover = unittest.defaultTestLoader.discover(self.case_path, pattern="test*.py",
                                                               top_level_dir=self.top_level_dir)
                LOGGER.info('运行路径【{}】测试用例:所有包含test的py的测试用例'.format(self.case_path))
            else:
                pattern = self.moudle.capitalize()
                discover = unittest.defaultTestLoader.discover(self.case_path, pattern='test*{}*.py'.format(pattern),
                                                               top_level_dir=self.top_level_dir)
                LOGGER.info('运行路径【{1}】测试用例:包含所有{0}的测试用例'.format(pattern, self.case_path))
            for test_suite in discover:
                for test_case in test_suite:
                    # 添加用例到 testcase
                    testcase.addTests(test_case)
        else:
            LOGGER.error('测试用例路径无效')
        return testcase

    def _runcase(self, _project_name):
        t1 = time.time()
        result_dict = dict()
        if self.is_valid_path():
            # 1、获取当前时间，这样便于下面的使用。
            now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
            # 2、html报告文件路径
            report_abspath = os.path.join(self.report_path, "result_" + _project_name + "_" + now + ".html")
            LOGGER.info('生成报告路径：{0}'.format(report_abspath))
            # 3、打开一个文件，将result写入此file中
            fp = open(report_abspath, "wb")
            projectname = ms.select_one(ms.get_conn(), 't_dict', 'name', 'code="{}"'.format(_project_name))
            title = projectname + '-' + ConfigUtils.get('report', 'REPORT_NAME')
            runner = HTMLTestRunner(stream=fp, title=title + u',运行情况如下：', description=u'用例执行情况：')
            # 4、调用add_case函数返回值
            r = runner.run(self.case())
            passed = r.success_count
            faild = r.failure_count + r.error_count
            result_dict['passed'] = passed
            result_dict['faild'] = faild
            fp.close()
        LOGGER.info('接口测试总耗时: {}秒'.format(time.time() - t1))
        return result_dict

    def runcase(self):
        result_dict = self._runcase(self.project_name)
        thread = list()
        # 获取testlink测试用例总数
        t1 = MyThread.MyThread(TestCaseCover.get_case_cover, (self.project_name,))
        # start 在这里代表异步执行，因为多个方法里面调用了mysql，导致mysql连接失败
        t1.start()
        thread.append(t1)
        # 获取测试代码总行数
        t2 = MyThread.MyThread(total_line.total_line, (self.project_path,))
        t2.start()
        thread.append(t2)
        results = list()
        for t in thread:
            # t.setDaemon(True)
            # start放在这里代表顺序执行，即在同一个线程中执行
            # t.start()
            t.join()
            results.append(t.get_result())
        rap_api_num, test_case_cover = results[0]
        all_lines = results[1]
        passed = result_dict['passed']
        faild = result_dict['faild']
        count = passed + faild
        if count > 0:
            pass_rate = float("%.2f" % (float(passed) / float(count) * 100))
        else:
            pass_rate = 0.00
        result_dict['count'] = count
        result_dict['pass_rate'] = pass_rate
        result_dict['total_line'] = all_lines
        result_dict['rap_api_num'] = rap_api_num
        result_dict['test_case_cover'] = test_case_cover
        LOGGER.info('API INTERFACE TEST RESULT: {}'.format(result_dict))


if __name__ == "__main__":
    # if len(sys.argv) == 1:
    #     RunTestApi('xqkj').runcase()
    if len(sys.argv) == 2:
        RunTestApi(sys.argv[1]).runcase()
    elif len(sys.argv) == 3:
        RunTestApi(sys.argv[1], sys.argv[2]).runcase()
    else:
        LOGGER.error('Number of parameters input error, The max number of parameters is two')
        sys.exit()
