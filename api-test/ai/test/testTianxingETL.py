#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2020-05-19
@Author     : QA
@File       : testTianxingETL.py
@desc       : 天行ETL测试
"""
import copy
import os
import re
import time

import ddt

from ai.testSource import etl_config, tianxing_etl
from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import ExcelUtil

excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource')
LOGGER = getlog(__name__)


@ddt.ddt
class testTianxingETL(TestBaseCase):
    @ddt.data(*ExcelUtil.read_excel_all_sheet(excel_path, 'tianxing_etl.xlsx'))
    def testTbETL(self, data):
        LOGGER.info(data)
        LOGGER.info(('开始执行第【{0}】条测试用例：【{1}】'.format(data['序号'], data['描述'])).center(80, '-'))
        t1 = time.clock()
        params = copy.deepcopy(etl_config.tianxing_etl)
        modif_type = data['sheet']
        modif_keys = re.split('[;；]', data['修改key'])
        modif_values = re.split('[;；]', data['修改值'])
        for i in range(len(modif_keys)):
            tianxing_etl.modif_data(params, modif_type, modif_keys[i], modif_values[i])
        rs = tianxing_etl.request_etl_tianxing(params)
        Assertion.verity(rs['code'], '10000', data)
        Assertion.verity(rs['msg'], '成功返回数据', data)
        if data['结果key']:
            Assertion.verity(tianxing_etl.get_result(rs, modif_type, data['结果时间'], data['结果key']),
                            int(data['断言结果']), data)
        tianxing_etl.assert_result(rs)
        Assertion.verityDict(params['json_data']['data']['report'], rs['score_data']['original_data']['report'])
        LOGGER.info('第【{0}】条测试用例：【{2}】执行完成，执行时间【{1}】'.format(
            data['序号'], float(time.clock() - t1), data['描述']).center(80, '-'))
