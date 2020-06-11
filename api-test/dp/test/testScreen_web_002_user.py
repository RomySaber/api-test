#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-12 下午 14:20
@Author     : 闫红
@File       : testScreen_web_002_user.py
@desc       : web端用户相关测试用例
"""
import json
from common.myCommon.TestBaseCase import TestBaseCase
from dp.testAction import Dp_webAction as dpweb
from common.myCommon import Assertion as ass


class testScreen_web_002_user(TestBaseCase):
    def test_001_appuser_addAppUser(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :新增app端用户
        """
        rs = dpweb.test_appuser_addAppUser('成都','link','13123232323','123','apitest','123456')
        ass.verity(json.loads(rs)['code'], "20000")

    def test_002_appuer_updateAppUser(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :编辑app端用户
        """
        rs = dpweb.test_appuser_updateAppUser('成都','link','13123232323','123','apitest','123456',13)
        ass.verity(json.loads(rs)['code'],'20000')

    def test_003_appuser_deleteAppUser(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :删除app端用户
        """
        rs = dpweb.test_appuser_deleteAppUser(12)
        ass.verity(json.loads(rs)['code'],'20000')

    def test_004_appuser_deleteAppUser(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :删除app端不存在用户
        """
        rs = dpweb.test_appuser_deleteAppUser(55)
        ass.verity(json.loads(rs)['code'],'20000')

    def test_005_appuser_getAppUserOrgList(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :获取App用户机构树列表
        """
        rs = dpweb.test_appuser_getAppUserOrgList(12)
        ass.verity(json.loads(rs)['code'],'20000')

    def test_006_appuser_updateAppUserOrgRange(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :App用户数据范围(机构范围)修改
        """
        selectorg = "00450008,004500080001,004500080002,004500080003,004500080004," \
                    "004500080005,004500080006,004500080007"
        rs = dpweb.test_appuser_updateAppUserOrgRange(userid='12',selectedorg=selectorg)
        ass.verity(json.loads(rs)['code'],'20000')

    def test_007_appuser_getOrgTreeAll(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :获取全部机构树
        """
        rs = dpweb.test_appuser_getOrgTreeAll()
        ass.verity(json.loads(rs)['code'],'20000')

    def test_008_appuser_getAppUserList(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :获取App用户列表
        """
        rs = dpweb.test_appuser_getAppUserList('',1,10)
        ass.verity(json.loads(rs)['code'],'20000')
