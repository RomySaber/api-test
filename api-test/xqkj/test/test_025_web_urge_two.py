#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@Time       :2019-09-29 上午 11:15
@Author     : 闫红
@File       : test_025_web_urge_two.py
@desc       : 催收管理自动化测试用例（电话催收）
"""

import json
import os

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction
from xqkj.testAction import loginAction

global_dict = loginAction.global_dict
fake = Factory().create('zh_CN')


class test_025_web_urge(TestBaseCase):
    def test_001_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,忘记还款
        """
        global app_user_uuid
        # app_user_uuid = loginAction.get_user_uuid()
        app_user_uuid = "bb9a44e01ce44b56a0f1aa3d7c7d478f"
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='forget_repay',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_002_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,还款不方便
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='inconve',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_003_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,收入少
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='revenue_decre',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_004_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,额外支出
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='extra_spend',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_005_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,恶意拖欠
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='deliberate',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_006_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,赌博、吸毒等恶习
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='bad_habit',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_007_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,代扣系统原因导致有钱代扣失败
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='system_reason',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_008_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,多头借贷
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='long_loan',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_009_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,联系不到客户和联系人
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='lose_contact',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_010_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,其他原因
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='other',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_011_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,上传mp3
        """
        mp3_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource', '1.mp3')
        datalist = [{"file": mp3_path, "key": "FjHpyILVVxjHksSyGsVKmQlnI01T"}]
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=app_user_uuid,overduereason='other',datalist=datalist,replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_012_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,客户uuid不存在
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_addMessage(communicatee='',condition='',remark='',
              useruuid=-1,overduereason='other',datalist=[],replyrepaytime=''))
        Assertion.verity(res['code'], '20000')

    def test_013_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,查询该催收人员催收历史记录
        """
        global userUuid
        userUuid = loginAction.global_dict.get('userUuid')
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryHistory(useruuid=userUuid,pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_014_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,催收人员为空
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryHistory(useruuid='',pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verityContain(res['msg'], '用户角色不可为空')

    def test_015_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,催收人员不存在
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryHistory(useruuid=-1,pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_016_api_78dk_platform_urge_queryuserandimageinfo_is_null(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :客户信息-v1.5.2,合同uuid为空
        """
        global contract_uuid
        contract_uuid = loginAction.global_dict.get('contract_uuid')
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryUserInfo(uid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '您提交的参数异常')

    def test_017_api_78dk_platform_urge_queryuserandimageinfo_not_exist(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :客户信息-v1.5.2,合同uuid不存在
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryUserInfo(uid=-1))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '合同UUID:-1不存在')

    def test_018_api_78dk_platform_urge_queryuserandimageinfo_not_exist(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :客户信息-v1.5.2,contract_uuid正常
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryUserInfo(uid=contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_019_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :联系人逾期贷款信息-v1.5.2
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryContactsOverdueLoan(uid=contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_020_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :联系人逾期贷款信息-v1.5.2，contract_uuid为空
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryContactsOverdueLoan(uid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '您提交的参数异常')

    def test_021_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :联系人逾期贷款信息-v1.5.2，contract_uuid不存在
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryContactsOverdueLoan(uid=-1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_022_api_78dk_platform_urge_queryMailList(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :通讯录信息-v1.5.2,用户uuid不存在
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryMailList(uid=-1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_023_api_78dk_platform_urge_queryMailList(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :通讯录信息-v1.5.2,用户uuid为空
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryMailList(uid=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_024_api_78dk_platform_urge_queryMailList(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :通讯录信息-v1.5.2,查询该用户的通讯录信息
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryMailList(uid=app_user_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_025_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期贷款信息-v1.5.2-v1.5.2,查询该contract_uuid相关的逾期贷款信息
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryOverdueLoan(uid=contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_026_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期贷款信息-v1.5.2,该contract_uuid不存在
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryOverdueLoan(uid=-1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_027_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :逾期贷款信息-v1.5.2,该contract_uuid为空
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryOverdueLoan(uid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '您提交的参数异常')

    def test_028_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,客户UUID为空
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryHistory(useruuid='',pagecurrent=1, pagesize=-10))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verityContain(res['msg'], '用户角色不可为空')

    def test_029_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,客户UUID正常
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryHistory(useruuid=app_user_uuid,pagecurrent=1, pagesize=-10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_030_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,客户UUID不存在
        """
        res = json.loads(PlatformAction.test_api_78dk_platform_urge_queryHistory(useruuid=-1,pagecurrent=1, pagesize=-10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')