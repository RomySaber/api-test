#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-28 上午 9:41
@Author     : 罗林
@File       : get_rap_api.py
@desc       :  获取rap数据，并存储到auto_ci数据库中
"""

import re
import sys
from common.myCommon import TimeFormat
from common.myCommon.Logger import getlog
from common.myConfig import MysqlConfig
from common.myFile import FileUtils
from common.mydb import MysqlClent

LOG = getlog(__name__)
API_TYPE = {'1': 'get', '2': 'post', '3': 'put', '4': 'delete'}
CI_DB = MysqlClent.get_conn()


def api_url_trim(api_url):
    """
    格式化URL
    :param api_url:  接口url字符串
    :return: 返回url
    """
    api_url = re.sub('\s+', '', api_url)
    if re.findall('[;?；？]', api_url):
        urls = [_url for _url in re.split('[;?；？]', api_url) if _url]
        return api_url_trim(re.sub('\s+', '', urls[0]))
    elif api_url and FileUtils.is_valid(api_url):
        if api_url.startswith('http'):
            return api_url_trim('/'.join(api_url.split('/')[3:]))
        elif FileUtils.is_start_num(str(api_url)):
            return api_url_trim('/'.join(api_url.split('/')[1:]))
        else:
            return api_url if api_url.startswith('/') else '/' + api_url
    else:
        return ''


def get_rap_db():
    """
    从auto_ci获取rap 数据库信息
    :return:  rap 数据库连接信息
    """
    rap_db = {"dbhost": MysqlConfig.get("rap_db_host"), "dbport": MysqlConfig.getint("rap_db_port"),
              "dbname": MysqlConfig.get("rap_db"), "dbuser": MysqlConfig.get("rap_db_name"),
              "dbpasswd": MysqlConfig.get("rap_db_passwd")}
    return MysqlClent.get_conn(**rap_db)


def get_version(ci_db, dict_id):
    """
    获取项目版本值
    :param ci_db: ci数据库连接
    :param dict_id: dict_id
    :return: 返回version_id
    """
    version_id = MysqlClent.select_one(ci_db, 't_version', 'id',
                                       'dict_id = {} ORDER BY id DESC'.format(dict_id))
    LOG.debug('ci数据库，dict_id 的版本信息：{}'.format(version_id))
    return version_id


def get_rap_corporations_none_rap(rap_db, ci_db, project=None):
    """
    从rap数据库获取 corporation_id
    :param rap_db: rap数据库连接
    :param ci_db: ci数据库连接
    :param project: 项目名称
    :return: [{'dict_id': dict_id, 'corporation_id': id}, {'dict_id': dict_id, 'corporation_id': id}]
    """
    rap_corporations_ids = list()
    condition = None if project is None else 'name regexp "{}$"'.format(project)
    corporations = MysqlClent.select(rap_db, 'tb_corporation', 'id,name', condition)
    LOG.debug('从rap数据库获取 corporation信息：{}'.format(corporations))
    for corporation_id, corporation_name in corporations:
        project_name = re.split('[-—]', corporation_name)[-1]
        LOG.debug('从rap数据库获取项目名称信息：{}'.format(project_name))
        rap = MysqlClent.select(ci_db, 't_dict', 'id,rap', 'code="{}"'.format(project_name))
        LOG.debug('从auto_ci数据库获取项目名称信息：{}'.format(rap))
        if rap:
            id_dict = {'dict_id': rap[0][0], 'corporation_id': corporation_id}
            LOG.debug('rap数据库和auto_ci数据库获取项目名称有对应关系：{}'.format(id_dict))
            rap_corporations_ids.append(id_dict)
            if rap[0][1] != corporation_name:
                LOG.debug('rap数据库和auto_ci数据库项目{1}名称不同，更新项目名称：{0}'.format(corporation_name, project_name))
                MysqlClent.update(ci_db, 't_dict', 'rap="{}"'.format(corporation_name),
                                  'code="{}"'.format(project_name))
        else:
            LOG.warning('项目{0}在数据库中不存在，请确认是否需要在auto_ci中增加项目{1}'.format(corporation_name, project_name))
    LOG.debug('dict_id和corporation_id对应关系：{}'.format(rap_corporations_ids))
    return rap_corporations_ids


def get_rap_corporations(rap_db, ci_db, project=None):
    """
    从rap数据库获取 corporation_id
    :param rap_db: rap数据库连接
    :param ci_db: ci数据库连接
    :param project: 项目名称
    :return: [{'dict_id': dict_id, 'corporation_id': id}, {'dict_id': dict_id, 'corporation_id': id}]
    """
    rap_corporations_ids = list()
    corporations = MysqlClent.select(rap_db, 'tb_corporation', 'id,name')
    LOG.debug('从rap数据库获取 corporation信息：{}'.format(corporations))
    condition = None
    if project:
        condition = 'code="{}"'.format(project)
    raps = MysqlClent.select(ci_db, 't_dict', 'id,code,rap', condition)
    LOG.debug('从auto_ci数据库获取项目名称信息：{}'.format(raps))
    for rap_info in raps:
        dict_id, code, rap = rap_info
        if rap:
            corporation = list(filter(lambda x: x[1] == rap, corporations))
            if len(corporation) == 1:
                rap_corporations_ids.append({'dict_id': dict_id, 'corporation_id': corporation[0][0]})
            else:
                LOG.warning('请确认项目{0}在auto_ci中rap信息{1}是否正确'.format(code, rap))
                get_rap_corporations_none_rap(rap_db, ci_db, code)
        else:
            get_rap_corporations_none_rap(rap_db, ci_db, code)
    LOG.debug('dict_id和corporation_id对应关系：{}'.format(rap_corporations_ids))
    return rap_corporations_ids


def get_rap_groups(rap_db, ci_db, rap_info):
    """
    获取rap项目groups
    :param rap_db: rap数据库连接
    :param ci_db: ci数据库连接
    :param rap_info: {'dict_id': dict_id, 'corporation_id': id}
    :return: [dict_id, {'module1': [40, 42, 55, 80], 'module2': [...]}]
    """
    rap_group_result, groups = list(), dict()
    dict_id, corporation_id = rap_info['dict_id'], rap_info['corporation_id']
    rap_group_result.append(dict_id)
    production_lines = MysqlClent.select(rap_db, 'tb_production_line', 'id,name',
                                         'corporation_id="{}"'.format(corporation_id))
    LOG.debug('产品线信息{}'.format(production_lines))
    for production_line_id, production_line_name in production_lines:
        module_code = re.split('[-—]', production_line_name)[-1]
        if not FileUtils.is_valid(module_code):
            LOG.warning('模块名称{}无效，请确认是否需要修改'.format(module_code))
            continue
        LOG.debug('英文模块名{}'.format(module_code))
        group_infos = MysqlClent.select_join(rap_db, 'tb_project as p,tb_group as g', 'p.id,p.name', 'g.id=p.group_id',
                                             'g.production_line_id={} GROUP BY p.id'.format(production_line_id))
        LOG.debug('rap_group信息{}'.format(group_infos))
        rap_groups = list()
        for group_id, group_name in group_infos:
            rap_groups.append(group_id)
            rap_group_name = MysqlClent.select_col(ci_db, 't_rap_group', 'rap_group_name',
                                                   'dict_id={0} AND module="{1}"'.format(dict_id, module_code))
            LOG.debug('auto_ci库t_rap_group表对应关系查询结构{}'.format(rap_group_name))
            if not [gn for gn in rap_group_name if gn == group_name]:
                insert_value = {"dict_id": dict_id, "module": module_code, "rap_group_name": group_name}
                LOG.debug('auto_ci库t_rap_group表没有对应关系，新增数据：{}'.format(insert_value))
                MysqlClent.insert(ci_db, 't_rap_group', insert_value)
        LOG.debug('rap库tb_group表对应id{}'.format(rap_groups))
        if rap_groups:
            groups[module_code] = rap_groups
    rap_group_result.append(groups)
    LOG.debug('项目、模块、rap_group对应关系：{}'.format(rap_group_result))
    return rap_group_result


def get_action(rap_db, group_ids):
    """
    获取action信息, 并对信息进行数据清洗
    :param rap_db: rap数据库连接
    :param group_ids:  group_id 数组
    :return:  action信息二维数组
    """
    result_actions = list()
    LOG.debug('获取的group_id 数组信息：{}'.format(group_ids))
    condition = 'm.project_id={}'.format(group_ids[0]) if len(group_ids) == 1 else 'm.project_id IN {}'.format(
        tuple(group_ids))
    condition += ' GROUP BY a.id'
    table_list = ['tb_action as a', 'tb_action_and_page as ap', 'tb_page as p', 'tb_module as m']
    col_list = ['m.name', 'p.name', 'a.id', 'a.name', 'a.request_type', 'a.request_url']
    join_list = ['a.id=ap.action_id', 'p.id=ap.page_id', 'm.id=p.module_id']
    actions = MysqlClent.select_join(rap_db, ','.join(table_list), ','.join(col_list), ','.join(join_list), condition)
    LOG.debug("rap数据库action表数据：{}".format(actions))
    for action in actions:
        url = api_url_trim(action[-1])
        LOG.debug("url数据清洗结果：{}".format(url))
        if not url:
            LOG.warning('The rap data is error,because the url is not valid,pleas check the data {}'.format(action))
            continue
        action[-1] = url
        action[-2] = API_TYPE[str(action[-2])]
        result_actions.append(action)
    LOG.debug("rap数据库action表数据清洗后的结果：{}".format(result_actions))
    return result_actions


def get_request_parameter(rap_db, action_id):
    """
    获取请求接口参数
    :param rap_db:  rap数据库连接
    :param action_id:  rap tb_action的id值
    :return: request_parameter 和 request_parameter_desc字符串
    """
    table_list = ['tb_parameter as p', 'tb_request_parameter_list_mapping as pm']
    col_list = ['p.identifier', 'p.name', 'p.data_type', 'p.remark']
    request_parameters = MysqlClent.select_join(rap_db, ','.join(table_list), ','.join(col_list),
                                                'p.id=pm.parameter_id',
                                                'pm.action_id={} GROUP BY p.id'.format(action_id))
    request_parameter = list()
    request_parameter_desc = list()
    for _request_parameter in request_parameters:
        request_parameter.append(_request_parameter[0])
        request_parameter_desc.append(','.join(_request_parameter[1:-1]))
    LOG.debug("The action_id is {0} in request_parameter {1}".format(action_id, request_parameter))
    LOG.debug("The action_id is {0} in request_parameter_desc {1}".format(action_id, request_parameter_desc))
    return ','.join(request_parameter), re.sub('[\'\"]', '\\\"', '=='.join(request_parameter_desc))


def get_response_parameter(rap_db, action_id):
    """
    获取返回结果参数
    :param rap_db:   rap数据库连接
    :param action_id: rap tb_action的id值
    :return:  response_parameter 和 response_parameter_desc 字符串
    """
    table_list = ['tb_parameter as p', 'tb_response_parameter_list_mapping as pm']
    col_list = ['p.identifier', 'p.name', 'p.data_type', 'p.remark']
    response_parameters = MysqlClent.select_join(rap_db, ','.join(table_list), ','.join(col_list),
                                                 'p.id=pm.parameter_id',
                                                 'pm.action_id={} GROUP BY p.id'.format(action_id))
    response_parameter = list()
    response_parameter_desc = list()
    for _response_parameter in response_parameters:
        response_parameter.append(_response_parameter[0])
        response_parameter_desc.append(','.join(_response_parameter[1:-1]))
    LOG.debug("The action_id is {0} in response_parameter {1}".format(action_id, response_parameter))
    LOG.debug("The action_id is {0} in response_parameter_desc {1}".format(action_id, response_parameter_desc))
    return ','.join(response_parameter), re.sub('[\'\"]', '\\\"', '=='.join(response_parameter_desc))


def get_module_rap(rap_db, rap_info):
    """
    获取模块下的接口信息
    :param rap_db:  rap数据库连接
    :param rap_info: [dict_id, {'module1': [40, 42, 55, 80], 'module2': [...]}]
    :return:  返回二维数组
    """
    LOG.debug('获取的rap_info信息数据：{}'.format(rap_info))
    dict_id, module_info = rap_info
    for module_code, groups_list in module_info.items():
        actions = get_action(rap_db, groups_list)
        if not actions:
            continue
        for action in actions:
            tmp_action = list()
            request = get_request_parameter(rap_db, action[2])
            response = get_response_parameter(rap_db, action[2])
            # 判断参数是否有效，存在中文或特殊字符无效
            if any(filter(lambda x: FileUtils.is_ch(x) or FileUtils.is_special_char(x) or re.findall('[.:/]', x),
                          request[0].split(','))):
                LOG.warning('The rap data is error,because the parameter is not valid,pleas check the action is '
                         '{0}, the parameter is {1}'.format(action, request[0].split(',')))
                continue
            del action[2]
            tmp_action.append(dict_id)
            tmp_action.append(module_code)
            tmp_action.extend(action)
            tmp_action.extend(request)
            tmp_action.extend(response)
            LOG.debug('单个模块整合后的数据信息：{}'.format(tmp_action))
            yield tmp_action


def get_rap(project=None):
    """
    获取rap的所有清洗后的接口数据
    :param project:  需要获取的项目
    :return:  返回二维数组
    """
    rap_db = get_rap_db()
    for info in get_rap_corporations(rap_db, CI_DB, project):
        rap_info = get_rap_groups(rap_db, CI_DB, info)
        yield get_module_rap(rap_db, rap_info)


def get_select_info(rap, version_id):
    """
    获取查询信息
    :param rap: rap数据
    :param version_id: 版本信息
    :return: 查询列 select_col， 数据字典 value_dict
    """
    is_exe, update_date = 'N', TimeFormat.getnow_day()
    select_col = ['dict_id', 'module', 'page', 'page_name', 'api_name', 'api_type', 'api_address', 'parameters',
                  'parameter_description', 'response_parameter', 'response_parameter_description']
    value_dict = dict(zip(select_col, rap))
    if version_id != '':
        value_dict['version_id'] = version_id
    value_dict['is_exe'] = is_exe
    value_dict['update_date'] = update_date
    value_dict['api_name'] = re.sub('[\n\t\r]', '', value_dict['api_name'])
    if value_dict['dict_id'] == 1 and 'manage' in value_dict['api_name']:
        value_dict['module'] = 'manage'
    select_col.insert(1, 'version_id')
    LOG.debug('查询列{}'.format(select_col))
    LOG.debug('数据字典{}'.format(value_dict))
    return select_col, value_dict


def update_rap_api(ci_db, rap, version_id, select_col, value_dict, condition):
    """
    更新rap数据表
    :param ci_db: ci数据库连接信息
    :param rap: rap数据
    :param version_id: 版本信息
    :param select_col: 查询字段列表
    :param value_dict: 更新值字典
    :param condition:查询条件
    :return:
    """
    LOG.debug('rap数据{}'.format(rap))
    LOG.debug('版本信息数据{}'.format(version_id))
    LOG.debug('查询字段列表{}'.format(select_col))
    LOG.debug('更新值字典{}'.format(value_dict))
    LOG.debug('查询条件{}'.format(condition))
    rap.insert(1, version_id)
    LOG.debug('rap数据{}'.format(rap))
    ci_rap = MysqlClent.select(ci_db, 't_rap', ','.join(select_col), condition)[0]
    LOG.debug('ci_rap数据{}'.format(ci_rap))
    if ci_rap != rap:
        LOG.debug('更新接口，数据如下：【{}】'.format(value_dict))
        MysqlClent.update_dict(ci_db, 't_rap', value_dict, condition)


def insert_or_update(ci_db, rap, version_id, num, select_col, value_dict, condition):
    """
    接口中心，判断是进行新增还是更新接口数据
    :param ci_db: auto_ci数据库连接
    :param rap: 接口数据
    :param version_id: 版本信息
    :param num: ci_rap数量
    :param select_col: 查询字段列表
    :param value_dict: 更新值字典
    :param condition:查询条件
    :return:
    """
    LOG.debug('版本信息数据{}'.format(version_id))
    LOG.debug('ci数据库接口条数{}'.format(num))
    LOG.debug('查询字段列表{}'.format(select_col))
    LOG.debug('更新值字典{}'.format(value_dict))
    LOG.debug('查询条件{}'.format(condition))
    if num in (None, 'null', 'NoneType', ' ', '', 'Null', 0):
        LOG.debug('新增接口，数据如下：【{}】'.format(rap))
        LOG.debug('新增数据字典{}'.format(value_dict))
        MysqlClent.insert(ci_db, 't_rap', value_dict)
    elif num == 1:
        LOG.debug('更新接口，数据如下：【{}】'.format(rap))
        update_rap_api(ci_db, rap, version_id, select_col, value_dict, condition)
    else:
        LOG.warning('表t_rap查询出{}的数据大于1条，请检查数据库数据'.format(condition))


def insert_rap(raps):
    """
    rap数据写入ci数据库
    :param raps:  rap二维数组
    :return:
    """
    for _raps in raps:
        for rap in _raps:
            LOG.debug('the rap is {}'.format(rap))
            dict_id, module_code, api_address, parameters = rap[0], rap[1], rap[6], rap[7]
            version_id = get_version(CI_DB, dict_id)
            select_col, value_dict = get_select_info(rap, version_id)
            if dict_id == 7:
                # 接口中心，所有接口地址一样，根据参数值不同进行判断
                condition = 'dict_id ={0} AND parameters="{1}" AND module="{2}"'.format(
                    dict_id, parameters, module_code)
            else:
                if api_address.strip('/') in ('', ' ', None):
                    continue
                condition = 'dict_id={0} AND api_address="{1}" AND module="{2}"'.format(dict_id, api_address,
                                                                                        module_code)
            num = MysqlClent.select_rows(CI_DB, 't_rap', 'id', condition)
            insert_or_update(CI_DB, rap, version_id, num, select_col, value_dict, condition)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        insert_rap(get_rap())
    elif len(sys.argv) == 2:
        insert_rap(get_rap(sys.argv[1]))
    else:
        LOG.error('Number of parameters input error, The max number of parameters is two')
        sys.exit()
