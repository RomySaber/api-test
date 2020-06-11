#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@Time       :2019-09-26 下午 09:30
@Author     : 闫红
@File       : test_024_web_urge.py
@desc       : 催收管理自动化测试用例（催收列表）
"""

import json
import unittest

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData as MD
from hmpt.query import xqkj_query as xq
from hmpt.testAction import WebAction
from hmpt.testAction import loginAction
from hmpt.query import xqkj_query

global_dict = loginAction.global_dict
fake = Factory().create('zh_CN')
# 系统用户基本信息
name = loginAction.sign + fake.name_male()
idcard = fake.ssn(min_age=18, max_age=20)
email = loginAction.sign + fake.email()


class test_024_web_urge(TestBaseCase):
    def test_001_api_78dk_platform_urge_collectionPersonnelList_null(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索分案状态为空的所有人员
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='', email='', mobile='', name='', pagesize=100, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        global mobile, name, platformUserProfileUuid, flag, userEmail
        userEmail = loginAction.super_email
        flag = True
        try:
            datalist = res['data']['dataList']
        except:
            datalist = []
        for data in datalist:
            if data['email'] == userEmail:
                mobile = data['mobile']
                name = data['name']
                platformUserProfileUuid = data['platformUserProfileUuid']
                flag = False

    def test_002_api_78dk_platform_urge_member_viewSystemMembers(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :查询可添加为催收人员的员工_v1.5.2
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_viewSystemMembers())
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        print(res)
        global userUuid, userName, userPhone, userEmail
        user_uuid = user_name = user_phone = ''
        for data in res['data']:
            if data['userEmail'] == userEmail:
                user_uuid = data['userUuid']
                user_name = data['userName']
                user_phone = data['userPhone']
        if flag:
            userUuid = user_uuid
            userName = user_name
            userPhone = user_phone
        else:
            userUuid = platformUserProfileUuid
            userName = name
            userPhone = mobile
        loginAction.global_dict.set(userUuid=userUuid)

    def test_003_api_78dk_platform_urge_member_addMemberUser(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :添加一个催收人员_v1.5.2,正常添加
        """
        # userUuid = loginAction.global_dict.get('userUuid')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_addMemberUser(useruuid=userUuid))
        if flag:
            Assertion.verity(res['code'], '10000')
            Assertion.verity(res['msg'], '成功')
        else:
            Assertion.verity(res['code'], '20000')
            Assertion.verity(res['msg'], '该用户已经是催收人员，重复的提交！')

    def test_004_api_78dk_platform_urge_member_viewSystemMembers(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :查询可添加为催收人员的员工_v1.5.2
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_viewSystemMembers())
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        global del_user_uuid
        del_user_uuid = res['data'][0]['userUuid']

    def test_005_api_78dk_platform_urge_member_addMemberUser(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :添加一个催收人员_v1.5.2,正常添加
        """
        # userUuid = loginAction.global_dict.get('userUuid')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_addMemberUser(useruuid=del_user_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        xqkj_query.del_collection(del_user_uuid)

    def test_006_api_78dk_platform_prompt_urge_manual_allocation(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :手动分案v1.5.2，手动分案时，催收员必须是 开启分案 状态
        """
        global app_user_uuid
        app_user_uuid = loginAction.get_user_uuid()
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_manual_allocation(urgeuuid=userUuid,
                                                                                        useruuids=[app_user_uuid]))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '您提交的参数异常')

    def test_007_api_78dk_platform_prompt_urge_manual_allocation(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :手动分案v1.5.2,客户uuid不存在
        """
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_manual_allocation(urgeuuid=userUuid,
                                                                                        useruuids=["-1"]))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '您提交的参数异常')

    def test_008_api_78dk_platform_prompt_urge_manual_allocation(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :手动分案v1.5.2,客户uuid为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_manual_allocation(urgeuuid=userUuid,
                                                                                        useruuids=['']))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '您提交的参数异常')

    def test_009_api_78dk_platform_urge_member_addMemberUser_multi(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :添加一个催收人员_v1.5.2,重复添加同一个人员为催收人员
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_addMemberUser(useruuid=userUuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], 'uuid不能为空')

    def test_010_api_78dk_platform_urge_member_addMemberUser_not_exist(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :添加一个催收人员_v1.5.2,添加不存在的人员为催收人员
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_addMemberUser(useruuid=-1))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '不能添加为催收人员')

    def test_011_api_78dk_platform_urge_member_addMemberUser_is_null(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :添加一个催收人员_v1.5.2,useruuid为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_addMemberUser(useruuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], 'uuid不能为空')

    def test_012_api_78dk_platform_urge_member_addMemberUser_overlong(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :添加一个催收人员_v1.5.2,useruuid超长
        """
        useruuid = MD.uuid_random(256)
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_addMemberUser(useruuid=useruuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '不能添加为催收人员')

    def test_013_api_78dk_platform_urge_member_addMemberUser_not_str(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :添加一个催收人员_v1.5.2,useruuid非字符串
        """
        useruuid = MD.words_cn(2)
        print(useruuid)
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_addMemberUser(useruuid=useruuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '不能添加为催收人员')

    def test_014_api_78dk_platform_urge_updateDivisionState_enable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,开启分案
        """
        global collection_uuid
        collection_uuid = xq.get_collection_uuid(userUuid)
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid=collection_uuid, divisionstate='division_enabled'))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_015_api_78dk_platform_urge_updateDivisionState_disable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,停止分案
        """
        # collection_uuid = xq.get_collection_uuid(userUuid)
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid=collection_uuid, divisionstate='division_disabled'))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_016_api_78dk_platform_urge_updateDivisionState_not_exist_enable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,userUuid不存在,开启分案
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid=-1, divisionstate='division_enabled'))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '传入的uuid 不合法')

    def test_017_api_78dk_platform_urge_updateDivisionState_not_exist_disable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,userUuid不存在,停止分案
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid=-1, divisionstate='division_disabled'))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '传入的uuid 不合法')

    def test_018_api_78dk_platform_urge_updateDivisionState_null_enable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,userUuid为空,开启分案
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid='', divisionstate='division_enabled'))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], 'CollectionUuid 不能为空')

    def test_019_api_78dk_platform_urge_updateDivisionState_null_disable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,userUuid为空,停止分案
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid='', divisionstate='division_disabled'))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], 'CollectionUuid 不能为空')

    def test_020_api_78dk_platform_urge_updateDivisionState_overlong_enable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,userUuid超长,开启分案
        """
        # userUuid = MD.uuid_random(256)
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid=MD.uuid_random(256), divisionstate='division_enabled'))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '传入的uuid 不合法!')

    def test_021_api_78dk_platform_urge_updateDivisionState_overlong_disable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,userUuid超长,停止分案
        """
        # userUuid = MD.uuid_random(256)
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid=MD.uuid_random(256), divisionstate='division_disabled'))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '传入的uuid 不合法')

    def test_022_api_78dk_platform_urge_updateDivisionState_null(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,divisionstate为空
        """
        # userUuid = loginAction.global_dict.get('userUuid')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid=userUuid, divisionstate=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], 'CollectionUuid 不能为空!')

    def test_023_api_78dk_platform_urge_updateDivisionState_overlong(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,divisionstate超长
        """
        # userUuid = loginAction.global_dict.get('userUuid')
        # divisionstate = MD.uuid_random(256)
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid=userUuid, divisionstate=MD.uuid_random(256)))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], 'CollectionUuid 不能为空!')

    def test_024_api_78dk_platform_urge_collectionPersonnelList_enable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索分案状态为开启的所有人员
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_enabled', email='', mobile='', name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_025_api_78dk_platform_urge_collectionPersonnelList_disable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索分案状态为停止的所有人员
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_disabled', email='', mobile='', name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_026_api_78dk_platform_urge_collectionPersonnelList_null(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索分案状态为空的所有人员
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='', email='', mobile='', name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_027_api_78dk_platform_urge_collectionPersonnelList_other(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索分案状态为其他状态的人员
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='other', email='', mobile='', name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_028_api_78dk_platform_urge_collectionPersonnelList_name(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定姓名的催收人员
        """
        # userName = loginAction.global_dict.get('userName')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='', email='', mobile='', name=userName, pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_029_api_78dk_platform_urge_collectionPersonnelList_mobile(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定手机号的催收人员
        """
        # userPhone = loginAction.global_dict.get('userPhone')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='', email='', mobile=userPhone, name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_030_api_78dk_platform_urge_collectionPersonnelList_email(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定邮箱的催收人员
        """
        # userEmail = loginAction.global_dict.get('userEmail')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='', email=userEmail, mobile='', name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_031_api_78dk_platform_urge_collectionPersonnelList_name(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定姓名、分案状态为开启的催收人员
        """
        # userName = loginAction.global_dict.get('userName')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_enabled', email='', mobile='', name=userName, pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_032_api_78dk_platform_urge_collectionPersonnelList_mobile(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定手机号、分案状态为开启的催收人员
        """
        # userPhone = loginAction.global_dict.get('userPhone')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_enabled', email='', mobile=userPhone, name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_033_api_78dk_platform_urge_collectionPersonnelList_email(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定邮箱、分案状态为开启的催收人员
        """
        # userEmail = loginAction.global_dict.get('userEmail')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_enabled', email=userEmail, mobile='', name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_034_api_78dk_platform_urge_collectionPersonnelList_name(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定姓名、分案状态为停止的催收人员
        """
        # userName = loginAction.global_dict.get('userName')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_disabled', email='', mobile='', name=userName, pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_035_api_78dk_platform_urge_collectionPersonnelList_mobile(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定手机号、分案状态为停止的催收人员
        """
        # userPhone = loginAction.global_dict.get('userPhone')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_disabled', email='', mobile=userPhone, name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_036_api_78dk_platform_urge_collectionPersonnelList_email(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定邮箱、分案状态为停止的催收人员
        """
        # userEmail = loginAction.global_dict.get('userEmail')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_disabled', email=userEmail, mobile='', name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_037_api_78dk_platform_urge_collectionPersonnelList_name(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定姓名、指定邮箱、分案状态为开启的催收人员
        """
        # userName = loginAction.global_dict.get('userName')
        # userEmail = loginAction.global_dict.get('userEmail')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_enabled', email=userEmail, mobile='', name=userName, pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_038_api_78dk_platform_urge_collectionPersonnelList_mobile(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定姓名、指定手机号、分案状态为开启的催收人员
        """
        # userPhone = loginAction.global_dict.get('userPhone')
        # userName = loginAction.global_dict.get('userName')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_enabled', email='', mobile=userPhone, name=userName, pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_039_api_78dk_platform_urge_collectionPersonnelList_email(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定邮箱、指定手机号、分案状态为开启的催收人员
        """
        # userEmail = loginAction.global_dict.get('userEmail')
        # userPhone = loginAction.global_dict.get('userPhone')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_enabled', email=userEmail, mobile=userPhone, name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_040_api_78dk_platform_urge_collectionPersonnelList_email(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定邮箱、指定手机号、指定姓名、分案状态为开启的催收人员
        """
        # userName = loginAction.global_dict.get('userName')
        # userEmail = loginAction.global_dict.get('userEmail')
        # userPhone = loginAction.global_dict.get('userPhone')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_enabled', email=userEmail, mobile=userPhone, name=userName, pagesize=10,
            pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_041_api_78dk_platform_urge_collectionPersonnelList_email(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定手机号、指定姓名、分案状态为开启的催收人员
        """
        # userName = loginAction.global_dict.get('userName')
        # userPhone = loginAction.global_dict.get('userPhone')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_enabled', email='', mobile=userPhone, name=userName, pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_042_api_78dk_platform_urge_collectionPersonnelList_name(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定姓名、指定邮箱、分案状态为停止的催收人员
        """
        # userName = loginAction.global_dict.get('userName')
        # userEmail = loginAction.global_dict.get('userEmail')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_disabled', email=userEmail, mobile='', name=userName, pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_043_api_78dk_platform_urge_collectionPersonnelList_mobile(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定姓名、指定手机号、分案状态为停止的催收人员
        """
        # userPhone = loginAction.global_dict.get('userPhone')
        # userName = loginAction.global_dict.get('userName')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_disabled', email='', mobile=userPhone, name=userName, pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_044_api_78dk_platform_urge_collectionPersonnelList_email(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定邮箱、指定手机号、分案状态为停止的催收人员
        """
        # userEmail = loginAction.global_dict.get('userEmail')
        # userPhone = loginAction.global_dict.get('userPhone')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_disabled', email=userEmail, mobile=userPhone, name='', pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_045_api_78dk_platform_urge_collectionPersonnelList_email(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定邮箱、指定手机号、指定姓名、分案状态为停止启的催收人员
        """
        # userName = loginAction.global_dict.get('userName')
        # userEmail = loginAction.global_dict.get('userEmail')
        # userPhone = loginAction.global_dict.get('userPhone')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_disabled', email=userEmail, mobile=userPhone, name=userName, pagesize=10,
            pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_046_api_78dk_platform_urge_collectionPersonnelList_email(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :催收人员管理列表-搜索-v1.5.2,搜索指定手机号、指定姓名、分案状态为开启的催收人员
        """
        # userName = loginAction.global_dict.get('userName')
        # userPhone = loginAction.global_dict.get('userPhone')
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_collectionPersonnelList(
            divisionstate='division_disabled', email='', mobile=userPhone, name=userName, pagesize=10, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_047_api_78dk_platform_prompt_urge_data_list(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :逾期用户列表v1.5.2,查询该催收员所负责的所有逾期用户列表
        """
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_overdue_user(
            idcard='', loandatebegin='',
            loandateend='', name='',
            overduedaybegin='', overduedayend='',
            overduestage='', mobile='',
            repaymentdatebegin='',
            repaymentdateend='',
            urgeuuid=userUuid, currentpage=1,
            currenturge='yes', pagesize=10,
            totalpage=100, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_048_api_78dk_platform_prompt_urge_data_list(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期用户列表v1.5.2,查询不存在的催收员所负责的所有逾期用户列表
        """
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_overdue_user(
            idcard='', loandatebegin='',
            loandateend='', name='',
            overduedaybegin='', overduedayend='',
            overduestage='', mobile='',
            repaymentdatebegin='',
            repaymentdateend='', urgeuuid=-1,
            currentpage=1, currenturge='yes',
            pagesize=10, totalpage=100, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_049_api_78dk_platform_prompt_urge_data_list(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期用户列表v1.5.2,查询该催收员所负责的所有逾期用户列表，逾期天数下限大于上限
        """
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_overdue_user(
            idcard='', loandatebegin='',
            loandateend='', name='',
            overduedaybegin=5, overduedayend=6,
            overduestage='', mobile='',
            repaymentdatebegin='',
            repaymentdateend='', urgeuuid=-1,
            currentpage=1, currenturge='yes',
            pagesize=10, totalpage=100, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_050_api_78dk_platform_prompt_urge_data_list_settle(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期用户列表v1.5.2,查询该催收员所负责的所有逾期用户列表，账单已结清
        """
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_overdue_user(
            idcard='', loandatebegin='',
            loandateend='', name='',
            overduedaybegin='', overduedayend='',
            overduestage='', mobile='',
            repaymentdatebegin='',
            repaymentdateend='', urgeuuid=-1,
            currentpage=1, currenturge='yes',
            pagesize=10, totalpage=100, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_051_api_78dk_platform_prompt_urge_data_list_part(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期用户列表v1.5.2,查询该催收员所负责的所有逾期用户列表，账单存在逾期
        """
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_overdue_user(
            idcard='', loandatebegin='',
            loandateend='', name='',
            overduedaybegin='', overduedayend='',
            overduestage='', mobile='',
            repaymentdatebegin='',
            repaymentdateend='', urgeuuid=-1,
            currentpage=1, currenturge='yes',
            pagesize=10, totalpage=100, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_052_api_78dk_platform_prompt_urge_data_list_part_unknown(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期用户列表v1.5.2,查询该催收员所负责的所有逾期用户列表，账单状态未知
        """
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_overdue_user(
            idcard='', loandatebegin='',
            loandateend='', name='',
            overduedaybegin='', overduedayend='',
            overduestage='', mobile='',
            repaymentdatebegin='',
            repaymentdateend='', urgeuuid=-1,
            currentpage=1, currenturge='yes',
            pagesize=10, totalpage=100, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_053_api_78dk_platform_prompt_urge_data_list_part_idcard_error(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期用户列表v1.5.2,身份证号错误
        """
        # idcard = MD.number(22)
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_overdue_user(
            idcard=MD.number(22), loandatebegin='',
            loandateend='', name='',
            overduedaybegin='', overduedayend='',
            overduestage='', mobile='',
            repaymentdatebegin='',
            repaymentdateend='',
            urgeuuid=userUuid, currentpage=1,
            currenturge='yes', pagesize=10,
            totalpage=100, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_054_api_78dk_platform_prompt_urge_data_list_part_mobile_error(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期用户列表v1.5.2,手机号号错误
        """
        # mobile = MD.number(22)
        res = json.loads(WebAction.test_api_78dk_platform_prompt_urge_overdue_user(
            idcard='', loandatebegin='',
            loandateend='', name='',
            overduedaybegin='', overduedayend='',
            overduestage='', mobile=MD.number(22),
            repaymentdatebegin='',
            repaymentdateend='',
            urgeuuid=userUuid, currentpage=1,
            currenturge='yes', pagesize=10,
            totalpage=100, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    @unittest.skip('待调试')
    def test_055_api_78dk_platform_prompt_urge_data_export(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期用户列表导出v1.5.2
        """
        useruuids = []
        json.loads(WebAction.test_api_78dk_platform_prompt_urge_data_export(useruuids))

    def test_056_api_78dk_platform_urge_updateDivisionState_enable(self):
        """
        Time       :2019-09-27
        author     : 闫红
        desc       :开始分案停止分案操作-v1.5.2,开启分案
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_updateDivisionState(
            collectionuuid=collection_uuid, divisionstate='division_enabled'))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
