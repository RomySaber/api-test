#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-31 下午 2:59
@Author     : 罗林
@File       : ApiActionAuto.py
@desc       : 获取auto_ci数据库中的接口数据，自动生成并封装接口
            根据输入的项目名和模块名自动生成，若不输入项目名和模块名，则自动获取数据库中的所有项目和模块
"""

import os
import re
import sys

from common.myCommon.Assertion import MyError
from common.myCommon.Logger import getlog
from common.myFile import FileUtils
from common.mydb import MysqlClent

LOGGER = getlog(__name__)
DB_CONN = MysqlClent.get_conn()

# 不需要导入登录或特别文件信息的项目
PASS_PROJECT = ['tzy', 'machineReview', 'ai', 'gw', 'xqwx']
# 不需要参数的项目
NO_PARAM = ['machineReview']
# 参数不需要dumps的项目
NO_DUMPS = {'finance': '', 'xqkj': ['pms'], 'ai': ['tbETL', 'jdETL']}
# 需要打印json的项目
PRINT_JSON = ['machineReview', 'ai']
# 需要添加头文件的项目
ADD_HEAD = ['reborn', 'xqkj', 'easyloan', 'dp', 'mjjry', 'ymjry', 'xyf', 'hmpt']
# 对应模块添加的头文件
HEAD_NAME = {'xqkj_app_finance_consumption': 'authorization', 'easyloan_web': 'AuthorToken',
             'easyloan_app': 'Authorization', 'pms': 'token', 'dp_web': 'token', 'dp_app': 'token',
             'xqkj_web_finance_consumption': 'mytoken', 'appserver': 'mytoken', 'platform': 'mytoken',
             'sht': 'token', 'app': 'authorization', 'web': 'mytoken', 'creditpay_ur': 'myToken'}
# 需要删除的参数
DEL_PARAM = {'finance': ['licences', 'licence', 'token', 'signature'], 'center': ['SignMsg'], 'dp': ['token'],
             'xqkj': ['MyToken', 'token'], 'mjjry': ['MyToken', 'token'], 'ymjry': ['MyToken', 'token'],
             'xyf': ['token'], 'hmpt': ['MyToken', 'token']}
# API_TYPE = {"get": "params=params", "post": "data=json.dumps(params)"}
# 接口中心需要加密的模块
center_encryption = ['center_qd', 'center_xq', 'xqkjcenter']
# 参数关键字转换
keywords = ['from']
is_keyword = lambda x: "{}_param".format(x) if x in keywords else x


def get_project(project_name=None):
    """
    获取项目名称
    :param project_name:项目名称
    :return:返回项目名称数组
    """
    pro = list()
    if project_name is None:
        projects = MysqlClent.select(DB_CONN, 't_dict', 'code')
        pro = [project[0] for project in projects]
    else:
        if MysqlClent.select_rows(DB_CONN, 't_dict', 'code', 'code={}'.format(project_name)):
            pro.append(project_name)
        else:
            raise MyError('项目{}在auto_ci中不存在，需要使用请在表t_dict中新增！'.format(project_name))
    LOGGER.debug('The project is {}'.format(pro))
    return pro


def get_module(project_name):
    """
    获取项目模块
    :param project_name:  项目名称
    :return: 返回模块数组
    """
    modules = MysqlClent.select_join(DB_CONN, 't_rap,t_dict', 'distinct t_rap.module', 't_dict.id=t_rap.dict_id',
                                     "t_dict.code = '{}'".format(project_name))
    module_result = [m[0] for m in modules]
    LOGGER.debug("The module is {}".format(module_result))
    return module_result


def get_api(project_name, module_name):
    """
    获取auto_ci数据库中的接口信息
    :param project_name:  项目名称
    :param module_name: 模块名称
    :return: 返回接口二维数组
    """
    col_list = ['r.id', 'r.api_name', 'r.api_type', 'r.api_address', 'r.parameters', 'r.parameter_description']
    rap_api = MysqlClent.select_join(DB_CONN, 't_rap as r,t_dict as d', ','.join(col_list), 'd.id=r.dict_id',
                                     "d.code = '{0}' AND r.module='{1}'".format(project_name, module_name))
    LOGGER.debug('The rap_api is {}'.format(rap_api))
    return rap_api


def get_dir(project_name):
    """
    创建文件夹和文件
    :param project_name: 项目名称
    :return:
    """
    path = FileUtils.is_windows(os.path.dirname(__file__))
    FileUtils.mkdir(os.path.join(path, project_name))
    FileUtils.create_file(os.path.join(path, project_name, '__init__.py'))
    FileUtils.mkdir(os.path.join(path, project_name, 'test'))
    FileUtils.create_file(os.path.join(path, project_name, 'test', '__init__.py'))
    FileUtils.mkdir(os.path.join(path, project_name, 'testAction'))
    FileUtils.create_file(os.path.join(path, project_name, 'testAction', '__init__.py'))


def doHeader(project, module_name):
    """
    生成头文件信息
    :param project: 项目名称
    :param module_name: 模块名称
    :return:
    """
    seq = list()
    LOGGER.debug("开始成头文件信息")
    seq.append("#!/usr/bin/env python \n")
    seq.append("# -*- coding: utf-8 -*- \n\n")
    seq.append("\"\"\"\n")
    seq.append("@Author     : QA \n")
    seq.append("@File       : {}Action.py\n".format(module_name.capitalize()))
    seq.append("@desc       : 项目：{0} 模块：{1} 接口方法封装\n".format(project, module_name))
    seq.append("\"\"\"\n\n")
    if project in PASS_PROJECT:
        pass
    elif project == 'center' and module_name in center_encryption:
        seq.append("from {}.testAction import encryption\n".format(project))
    elif project == 'center':
        pass
    else:
        seq.append("from {}.testAction import loginAction\n".format(project))
    seq.append("import requests, json, time\n")
    seq.append("from common.myCommon import Assertion\n")
    seq.append("from common.myConfig import ConfigUtils\n")
    seq.append("from common.myCommon.Logger import getlog\n")
    seq.append("from common.mydb import MysqlClent\n")
    seq.append("from common.myConfig import MysqlConfig\n\n\n")
    seq.append("TIMEOUT = ConfigUtils.getint('report', 'time_out')\n")
    seq.append("baseUrl = MysqlConfig.get('{0}_apiURL', '{1}')\n".format(module_name, project))
    seq.append("LOGGER = getlog(__name__)\n")
    seq.append("rq = requests.Session()\n")
    seq.append('API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}\n')
    if project in PASS_PROJECT:
        pass
    elif project in ADD_HEAD:
        seq.append("LICENCES = loginAction.test_{}_login()\n".format(module_name))
        if module_name in HEAD_NAME.keys():
            seq.append("API_TEST_HEADERS['{}'] = LICENCES\n".format(HEAD_NAME[module_name]))
        if module_name == 'xqkj_app_finance_consumption':
            seq.append("API_TEST_HEADERS['tenantUuid'] = 'xqkj001'\n")
    elif project == 'center':
        seq.append("appkey = '1552893617253867'\n")
    else:
        seq.append("LICENCES = loginAction.test_{}_login()\n".format(module_name))
    seq.append("\n\n")
    LOGGER.debug("头文件信息:{}".format(seq))
    return ''.join(seq)


def getparam(str_param, project_name, split_str):
    """
    获取参数，并去掉licences参数
    :param str_param:  参数字符串
    :param project_name:  项目名称
    :param split_str: 分隔符字符串f
    :return:  返回参数数组
    """
    LOGGER.debug("开始获取参数")
    param = list()
    if str_param:
        params = re.sub('\s+', '', str_param).split(split_str)
        if project_name in DEL_PARAM.keys():
            for p in DEL_PARAM[project_name]:
                if p in params:
                    params.remove(p)
        param = [p for p in params]
        param = sorted(list(set(param)))
    LOGGER.debug("获取参数:{}".format(param))
    return param


def getMethodHeadParam(str_param, project_name):
    """
     生成方法头参数
     :param str_param:  参数字符串
     :param project_name:  项目名称
     :return:  返回方法字符串
     """
    LOGGER.debug("开始生成方法头参数")
    params = getparam(str_param, project_name, ',')
    if len(params) == 0:
        headparam = ""
    else:
        headparam = ", ".join([is_keyword(p) for p in params if p])
    LOGGER.debug("方法头参数为：{}".format(headparam.rstrip(",")))
    return headparam.rstrip(",").strip().lower()


def get_special_project_method_body_param(project_name, str_param, bodyparam):
    """
    特殊项目的方法体修改
    :param project_name: 项目名称
    :param str_param: 字符串参数
    :param bodyparam: 传入的方法体
    :return: 修改后的方法体字符串
    """
    LOGGER.debug('项目名称：{}'.format(project_name))
    LOGGER.debug("参数字符串{}".format(str_param))
    LOGGER.debug("传入的方法体参数:{}".format(bodyparam))
    if project_name in DEL_PARAM.keys():
        del_params = [i for i in DEL_PARAM[project_name] for j in str_param.split(',') if i == j.strip()]
        LOGGER.debug('删除的参数：{}'.format(del_params))
        for del_param in del_params:
            if del_param in ['licences', 'licence', 'token', 'MyToken']:
                bodyparam += ' ' * 4 + 'params["{}"] = LICENCES\n'.format(del_param)
                LOGGER.debug('添加的参数：{}'.format(bodyparam))
            if del_param == 'signature':
                bodyparam += ' ' * 4 + 'params = loginAction.getsignature(params)\n'
                LOGGER.debug('添加的参数signature：{}'.format(bodyparam))
            if del_param == 'SignMsg':
                bodyparam += ' ' * 4 + 'params = encryption.get_encryption_param(params, appkey)\n'
                LOGGER.debug('添加的参数SignMsg：{}'.format(bodyparam))
    LOGGER.debug("修改后的方法体参数:{}".format(bodyparam))
    return bodyparam


def getMethodBodyParam(str_param, project_name):
    """
    生成方法体参数
    :param str_param:  参数字符串
    :param project_name:  项目名称
    :return:  返回方法字符串
    """
    str_param = re.sub('\s+', '', str_param)
    LOGGER.debug("开始生成方法体参数")
    LOGGER.debug("参数字符串{}".format(str_param))
    LOGGER.debug('项目名称：{}'.format(project_name))
    params = getparam(str_param, project_name, ',')
    LOGGER.debug('清洗后的项目参数：{}'.format(params))
    bodyparam = "params = dict()\n"
    if str_param and params:
        param = [" " * 4 + "params[\"{0}\"] = {1}\n".format(p, is_keyword(p.lower())) for p in params if p]
        LOGGER.debug('方法参数:{}'.format(param))
        bodyparam += ''.join(param)
    bodyparam = get_special_project_method_body_param(project_name, str_param, bodyparam)
    LOGGER.debug("方法体参数:{}".format(bodyparam))
    return bodyparam


def getMethoddesc(str_param, parameter_description, api_name, project_name):
    """
    生成方法备注
    :param str_param:  接口参数字符串
    :param parameter_description: 接口描述信息
    :param api_name:  接口名称
    :param project_name:  项目名称
    :return:
    """
    seq = list()
    LOGGER.debug("开始生成方法备注")
    seq.append(" " * 4 + '"""\n')
    seq.append(" " * 4 + api_name + "\n")
    if str_param:
        descparam = str_param.split(',')
        if parameter_description:
            descinfo = parameter_description.split("==")
            if len(descparam) == len(descinfo):
                i = 0
                while i < len(descinfo):
                    seq.append(''.join([" " * 4, ":param ", is_keyword(descparam[i].lower()), ": ", descinfo[i], "\n"]))
                    i = i + 1
            else:
                LOGGER.warn('{0}数组长度不一致，请检查数据库中的参数间隔","是否错误,参数列表:{3}长度：'
                            '{1},参数说明:{4}长度：{2}'.format(api_name, len(descparam), len(descinfo), descparam, descinfo))
    if project_name in DEL_PARAM.keys():
        for p in DEL_PARAM[project_name]:
            seq_remove(seq, ':param {}'.format(is_keyword(p.lower())))
    seq.append(" " * 4 + ":return: response.text\n")
    seq.append(" " * 4 + '"""\n')
    LOGGER.debug("方法备注:{}".format("".join(seq)))
    return "".join(seq)


def seq_remove(seq, str_info):
    """
    去除多余备注信息
    :param seq: 备注信息数组
    :param str_info: 需要删除的备注信息
    :return: 删除后的备注信息数组
    """
    for i in seq:
        if str_info in i:
            seq.remove(i)
    return seq


def doMethod(project_name, module_name, rap_api_id, api_name, api_type, api_address, str_param, parameter_description):
    """
    生成方法
    :param project_name:  项目名称
    :param module_name:  模块名称
    :param rap_api_id: 接口id
    :param api_name: 接口名称
    :param api_type: 接口类型
    :param api_address: 接口地址
    :param str_param: 字符串参数
    :param parameter_description: 参数描述信息
    :return:
    """
    seq = list()
    LOGGER.debug("开始生成方法")
    LOGGER.debug("获取方法名称")
    if project_name == 'center':
        apiname = "test" + re.sub('[/-]', '_', api_address.strip()) + '_' + str(rap_api_id)
    else:
        apiname = "test" + re.sub('[/-]', '_', api_address.strip())
    seq.append("def " + apiname + "(" + getMethodHeadParam(str_param, project_name) + "):\n")
    desc = getMethoddesc(str_param, parameter_description, api_name, project_name)
    LOGGER.debug("注释：{}".format(desc))
    if desc:
        seq.append(desc)
    seq.append(" " * 4 + "start_time = time.time()\n")
    seq.append(
        " " * 4 + "MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = \"Y\"', 'id = {}')\n".format(rap_api_id))
    seq.append(" " * 4 + "requesturl = baseUrl + \"" + api_address.strip() + "\"\n")
    seq.append(''.join([" " * 4, "LOGGER.info(\"", api_name, "请求地址:【{}】\".format(requesturl))\n"]))
    param = getMethodBodyParam(str_param, project_name)
    if project_name not in NO_PARAM:
        seq.append(" " * 4 + param)
        seq.append(''.join([" " * 4, "LOGGER.info(\"", api_name, "请求头参数：【{}】\".format(API_TEST_HEADERS))\n"]))
        seq.append(''.join([" " * 4, "LOGGER.info(\"", api_name, "请求参数：【{}】\".format(params))\n"]))
    if project_name in NO_DUMPS.keys():
        if NO_DUMPS[project_name] == '':
            seq.append(''.join([" " * 4, "response = rq.", api_type.strip().lower(),
                                "(requesturl, params=params, headers=API_TEST_HEADERS, ", "timeout=TIMEOUT", ")\n"]))
        elif module_name in NO_DUMPS[project_name]:
            seq.append(''.join([" " * 4, "response = rq.", api_type.strip().lower(),
                                "(requesturl, params=params, headers=API_TEST_HEADERS, ", "timeout=TIMEOUT", ")\n"]))
        else:
            seq.append(''.join([" " * 4, "response = rq.", api_type.strip().lower(),
                                "(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, ",
                                "timeout=TIMEOUT", ")\n"]))
    else:
        # seq.append(''.join([" " * 4, "response = rq.", api_type.strip().lower(), "(requesturl, ",
        #                     API_TYPE[api_type.strip().lower()], ", headers=API_TEST_HEADERS)\n"]))
        seq.append(''.join([" " * 4, "response = rq.", api_type.strip().lower(),
                            "(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, ",
                            "timeout=TIMEOUT", ")\n"]))
    # seq.append(''.join([" " * 4, "response = rq.", api_type.strip().lower(),
    #                     "(requesturl, params=params, data=json.dumps(params), headers=API_TEST_HEADERS)\n"]))
    if project_name in PRINT_JSON:
        seq.append(" " * 4 + "LOGGER.info(\"请求结果参数：【{}】\".format(response.json()))\n")
    else:
        seq.append(" " * 4 + "LOGGER.info(\"请求结果参数：【{}】\".format(response.text))\n")
    seq.append(" " * 4 + "Assertion.verity(response.status_code, 200, \"状态码检查\")\n")
    seq.append(" " * 4 + "LOGGER.info(\"请求接口耗时：【{}】\".format(time.time() - start_time))\n")
    seq.append(" " * 4 + "return response.text\n\n\n")
    LOGGER.debug("方法内容:{}".format(seq))
    return "".join(seq)


def get_action(project_name, module_name):
    """
    获取接口信息
    :param project_name: 项目名称
    :param module_name: 模块名称
    :return:
    """
    result = list()
    api_datas = get_api(project_name, module_name)
    for api_data in api_datas:
        rap_api_id, api_name, api_type, api_address, parameters, parameter_description = api_data
        api_name = re.sub('\s+', '', api_name)
        seq = doMethod(project_name, module_name, rap_api_id, api_name, api_type, api_address, parameters,
                       parameter_description)
        result.append(seq)
    return result


def get_module_api_code(project_name, module_name):
    """
    获取一个模块的代码
    :param project_name:  项目名称
    :param module_name:   模块名称
    :return:
    """
    results = list()
    if len(get_api(project_name, module_name)) != 0:
        seq = doHeader(project_name, module_name)
        seq += ''.join(get_action(project_name, module_name))
        results.append([seq, project_name, module_name])
    return results


def writeFile(seq, project_name, module_name):
    """
    将数组写入文件
    :param seq: 需要写入的数组
    :param project_name: 项目名称
    :param module_name: 模块名称
    :return:
    """
    LOGGER.info("开始数组写入文件")
    LOGGER.debug("数组:{}".format(seq))
    get_dir(project_name)
    path = FileUtils.is_windows(os.path.join(os.path.dirname(__file__), project_name, 'testAction'))
    LOGGER.debug("The basedir is : {}".format(path))
    filepath = FileUtils.is_windows(os.path.join(path, module_name.capitalize() + "Action.py"))
    LOGGER.info("The filepath is : {}".format(filepath))
    with open(filepath, "w", encoding="utf8") as fp:
        fp.write(seq)
    LOGGER.info("The file write is success")


def get_project_module(project_name=None, module_name=None):
    if all([project_name, module_name]):
        return True
    elif all([project_name is None, module_name is None]):
        return True
    elif project_name is not None and module_name is None:
        return True
    elif project_name is None and module_name is not None:
        LOGGER.warn('module_name is not none, but project_name is None')
        return False
    else:
        return False


def autoCode(project_name=None, module_name=None):
    results = list()
    if not get_project_module(project_name, module_name):
        raise MyError('The project {0} and module {1} input error'.format(project_name, module_name))
    if module_name is not None:
        results.extend(get_module_api_code(project_name, module_name))
    else:
        for project_name in get_project(project_name):
            for module_name in get_module(project_name):
                results.extend(get_module_api_code(project_name, module_name))
    for result in results:
        writeFile(result[0], result[1], result[2])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        autoCode()
    elif len(sys.argv) == 2:
        autoCode(sys.argv[1])
    elif len(sys.argv) == 3:
        autoCode(sys.argv[1], sys.argv[2])
    else:
        LOGGER.error('Number of parameters input error, The max number of parameters is two')
        sys.exit()
