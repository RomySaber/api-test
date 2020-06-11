#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018-07-16 下午 4:33
@Author     : 罗林
@File       : testApp.py
@desc       :  小启控车clapp测试用例
"""

import json
import os

from faker import Faker

from common.myCommon import Assertion as ass
from common.myCommon import TimeFormat as tf
from common.myCommon.TestBaseCase import TestBaseCase
from finance.mysqlQuery import ClappSql as cls, FinanceSql as fis
from finance.testAction import ClappAction as cla, FinanceAction as fa
from finance.testAction import loginAction

f = Faker(locale='zh_CN')

sim = f.ean13()
new_device_code = loginAction.sign + str(f.random_int())
car_owner = loginAction.sign + f.name()
ownermoble = f.phone_number()
carNo = loginAction.sign + f.license_plate()
installer = loginAction.sign + f.name()
org_code = cls.get_gps_org_code(cls.get_device_id())
org_id = cls.get_gps_org_id(org_code)


class testClapp(TestBaseCase):
    def test_001_userinfo(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :获取我的信息
        """
        rs1 = cla.test_userinfo()
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_002_notification_update(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :修改通知设定
        """
        rs1 = cla.test_notification_update(notificationid=32, ison=False)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_003_device_caralldevice(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :获取同车设备
        """
        carid = cls.get_car_id()
        rs1 = cla.test_device_caralldevice(carid=carid)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_004_device_updateposition(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :获取设备最新状态
        """
        deviceid = cls.get_device_id()
        rs1 = cla.test_device_updateposition(deviceid=deviceid)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_005_device_tracklist(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :获取设备轨迹
        """
        deviceid = cls.get_device_id()
        rs1 = cla.test_device_tracklist(starttime=tf.string_toTimestamp_10(tf.get_day_around(-7) + " 00:00:00"),
                                        endtime=tf.get_now_time(), positiontype=-1, deviceid=deviceid)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_006_organization_list(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :组织列表
        """
        rs1 = cla.test_organization_list()
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_007_device_getList(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :监控首页列表
        """
        rs1 = cla.test_device_getList(keyword='', type=0, organizationid=org_id, groupid='', pagesize=1, pagenum=10)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_008_device_more(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :获取组内更多设备
        """
        groupid = cls.get_gps_group_id(cls.get_gps_org_code(cls.get_device_id()))
        rs1 = cla.test_device_more(groupid=groupid, pagenum=1, pagesize=10, type=0, keyword='')
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_009_warning_list(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :获取报警列表
        """
        devicenum = fis.get_gpscode(cls.get_device_id())
        rs1 = cla.test_warning_list(pagesize=10, warningtype='', issolved='', devicenum=devicenum, keyword='',
                                    pagenum=1)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_010_warningType_list(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :获取报警类型
        """
        rs1 = cla.test_warningType_list()
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_011_warning_handleinit(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :动态获取情况反馈与风险等级
        """
        warnid = fis.get_warn_id()
        rs1 = cla.test_warning_handleinit(warnid=warnid)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_012_warning_resolve(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :提交报警处理数据
        """
        warnid = fis.get_warn_id()
        rs1 = cla.test_warning_resolve(dangervalue=1, warningid=warnid, feedbackvalue=1, mark='', feedbackothertext='')
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_013_warning_detail(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :获取报警详情信息
        """
        warnid = fis.get_warn_id()
        rs1 = cla.test_warning_detail(warningid=warnid)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_014_warning_mapinfo(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :获取报警详情地图信息
        """
        warnid = fis.get_warn_id()
        rs1 = cla.test_warning_mapinfo(warningid=warnid)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_015_warning_stationdetail(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :未回家/公司获取停车记录
        """
        warnid = fis.get_warn_id('whj')
        rs1 = cla.test_warning_stationdetail(warnid=warnid)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_016_equipment_model(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       : 获取设备型号
        """
        rs1 = cla.test_equipment_model(type=1)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_017_equipment_update(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :新增设备/编辑设备
        """
        model = json.loads(cla.test_equipment_model(type=1))["data"][0]["code"]
        rs1 = cla.test_equipment_update(sim=sim, model=model, organizationid=org_id, type=1, no=new_device_code,
                                        id='',
                                        instoragedate=tf.get_now_time())
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_018_equipment_update(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :新增设备/编辑设备
        """
        device_id = fis.get_device_id(new_device_code)
        model = json.loads(cla.test_equipment_model(type=1))["data"][-1]["code"]
        rs1 = cla.test_equipment_update(sim=sim, model=model, organizationid=org_id, type=1, no=new_device_code,
                                        id=device_id, instoragedate=tf.get_now_time())
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_019_equipment_details(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :获取设备详情
        """
        device_id = fis.get_device_id(new_device_code)
        rs1 = cla.test_equipment_details(id=device_id)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_020_install_equipment_search(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :搜索设备
        """
        rs1 = cla.test_install_equipment_search(keyword=new_device_code, organizationid=org_id)
        ass.verity(json.loads(rs1)['message'], '请求成功')
        ass.verity(json.loads(rs1)['data'][0]['no'], new_device_code)

    def test_021_finance_save(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :新增车辆
        """
        rs = fa.test_finance_save(pledge=0, borrowtypename='', orgname='', repaymannername='', repaystatusname='',
                                  broadendays='', gpscount='', candelete=True, deletemessage='', finance='', id='',
                                  owner=car_owner, repaymanner='DBDX', carmodel=1, borrowdate='', borrownum=1,
                                  owneraddress='四川省成都市武侯区桂溪街道天府大道北段', ownercoord='104.068402,30.572893',
                                  companyaddress='四川省成都市武侯区桂溪街道益州大道中段674号成都高新孵化园',
                                  companycoord='104.06432,30.572869', borrowtype='XZ', carshelf='', cartype=1,
                                  carengine='', buytime='', repaystatus='', repayTimes=1,
                                  carno=carNo, orgcode=org_code, ownermoble=ownermoble)
        ass.verity(json.loads(rs)['data']['owner'], car_owner)

    def test_022_install_car_search(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :搜索车辆
        """
        rs1 = cla.test_install_car_search(keyword=car_owner, organizationid=org_id)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_023_install_add(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :创建安装
        """
        car_id = fis.get_car_id(car_owner)
        device_id = fis.get_device_id(new_device_code)
        rs1 = cla.test_install_add(carid=car_id, equipmentids=device_id, username=installer)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_024_file_upload(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :上传文件
        """
        file_path = os.path.join(os.path.dirname(__file__), 'testSource/image/1.jpg')
        rs1 = cla.test_file_upload(file=file_path, appversion='2.6.0')
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_025_install_update(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :修改安装
        """
        gps_finance_id = fis.get_gps_finance_id(fis.get_device_id(new_device_code), fis.get_car_info(car_owner))
        imageid = cls.get_file_id(gps_finance_id)
        rs1 = cla.test_install_update(date=tf.get_now_time(), position='电瓶', imageid=imageid, username=installer,
                                      id=gps_finance_id)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_026_install_detection(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :定位
        """
        rs1 = cla.test_install_detection(no=new_device_code)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_027_install_uninstall(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :拆机
        """
        gps_finance_id = fis.get_gps_finance_id(fis.get_device_id(new_device_code), fis.get_car_info(car_owner))
        rs1 = cla.test_install_uninstall(id=gps_finance_id)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_028_install_remove(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :删除安装记录
        """
        gps_finance_id = fis.get_gps_finance_id(fis.get_device_id(new_device_code), fis.get_car_info(car_owner))
        rs1 = cla.test_install_remove(id=gps_finance_id)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_029_equipment_remove(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       :删除设备
        """
        device_id = fis.get_device_id(new_device_code)
        rs1 = cla.test_equipment_remove(id=device_id)
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_030_del_gps(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       : 删除数据库中的设备信息
        """
        gps_finance_id = fis.get_gps_finance_id(fis.get_device_id(new_device_code), fis.get_car_info(car_owner))
        cls.del_gps_finance(gps_finance_id)
        cls.del_gps(new_device_code)
        fis.del_finance(car_owner)

    def test_031_sys_version(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       : 获取最新版本信息
        """
        rs1 = cla.test_sys_version()
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_032_sys_uploadRegister(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       : 更新registerId
        """
        rs1 = cla.test_sys_uploadRegister(uuid='')
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_033_logout(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       : 退出登录
        """
        rs1 = cla.test_logout()
        ass.verity(json.loads(rs1)['message'], '请求成功')

    def test_034_login(self):
        """
        Time       :2019-04-08
        author     : 罗林
        desc       : 退出登录
        """
        rs1 = cla.test_login(sysversion='', appversion='', pwd=loginAction.financePasswd, deviceversion='', sysname='',
                             phone=loginAction.financeUser, uuid='')
        ass.verity(json.loads(rs1)['message'], '请求成功')
