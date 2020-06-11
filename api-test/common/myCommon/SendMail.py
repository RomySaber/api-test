#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@Time       :2018/5/8 0008 上午 11:02
@Author     : 罗林
@File       : SendMail.py
@desc       : 发送邮件
"""

import os
import platform
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.myCommon.Logger import getlog
from common.myConfig import ConfigUtils as conf


class SendMail(object):
    LOG = getlog(__name__)
    reportPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/testReport/report/"
    logPath = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/testReport/log/"
    if "Windows" in platform.system():
        reportPath = reportPath.replace("/", "\\")
        logPath = logPath.replace("/", "\\")

    # 邮箱服务器地址
    MAIL_HOST = conf.get('mail', 'MAIL_HOST')
    # 登录邮箱服务器账号
    MAIL_USER = conf.get('mail', 'MAIL_USER')
    # 登录邮箱服务器账号密码
    MAIL_PASSWORD = conf.get('mail', 'MAIL_PASSWORD')
    # 邮箱服务器端口
    MAIL_PORT = conf.getint('mail', 'MAIL_PORT')
    # 收件人邮箱,使用 , 隔开
    MAIL_RECEIVER = conf.get('mail', 'MAIL_RECEIVER').split(',')
    # 抄送人
    MAIL_CC_RECEIVER = conf.get('mail', 'MAIL_CC_RECEIVER').split(',')
    # 邮件标题
    MAIL_SUBJECT = conf.get('mail', 'MAIL_SUBJECT')
    # 邮件类型，普通邮件为 plain ,包含HTML时用html
    MAIL_TYPE = conf.get('mail', 'MAIL_TYPE')
    # 邮件附件地址
    MAIL_ATTACHMENT = conf.get('mail', 'MAIL_ATTACHMENT').split(',')

    LOG.info('服务器地址：【{0}】，登录邮箱服务器账号：【{1}】，'
             '登录邮箱服务器账号密码：【{2}】，'
             '邮箱服务器端口：【{3}】，收件人邮箱：【{4}】，邮件标题：【{5}】'
             .format(MAIL_HOST, MAIL_USER, MAIL_PASSWORD, MAIL_PORT, MAIL_RECEIVER, MAIL_SUBJECT))

    def sendSMTP(self, sendcontent):
        """
         发送包普通邮件
         :param sendcontent:   正文
         """
        message = MIMEText(sendcontent, self.MAIL_TYPE, "utf-8")
        message["From"] = Header(self.MAIL_USER, "utf-8")
        for toName in self.MAIL_RECEIVER:
            message["To"] = Header(toName, "utf-8")
        message["Subject"] = Header(self.MAIL_SUBJECT, "utf-8")
        self.LOG.info("开始发送邮件".center(40, "*"))
        try:
            smtpObj = smtplib.SMTP()

            smtpObj.connect(self.MAIL_HOST, self.MAIL_PORT)  # 25 为 SMTP 端口号
            smtpObj.login(self.MAIL_USER, self.MAIL_PASSWORD)
            smtpObj.sendmail(
                self.MAIL_USER, self.MAIL_RECEIVER, message.as_string()
            )
            smtpObj.quit()
            self.LOG.info("邮件发送成功".center(40, "*"))
        except smtplib.SMTPException:
            self.LOG.error("Error: 无法发送邮件".center(40, "*"))

    def sendAttachment(self, sendcontent):
        """
        发送包含附件的邮件
        :param sendcontent:   正文
        :return:
        """
        self.LOG.info(u"开始发送邮件".center(40, "*"))
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message["From"] = Header(self.MAIL_USER, "utf-8")
        for toName in self.MAIL_RECEIVER:
            message["To"] = Header(toName, "utf-8")
        message["Subject"] = Header(self.MAIL_SUBJECT, "utf-8")

        # 邮件正文内容
        message.attach(MIMEText(sendcontent, self.MAIL_TYPE, "utf-8"))

        for attfile in self.MAIL_ATTACHMENT:
            # 构造附件1，传送当前目录下的 test.txt 文件
            att = MIMEText(open(attfile, "rb").read(), "base64", "utf-8")
            fileName = open(attfile, "w+").name
            att["Content-Type"] = "application/octet-stream"
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att["Content-Disposition"] = "attachment; filename=" + fileName
            message.attach(att)

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.MAIL_HOST, self.MAIL_PORT)  # 25 为 SMTP 端口号
            smtpObj.login(self.MAIL_USER, self.MAIL_PASSWORD)
            smtpObj.sendmail(
                self.MAIL_USER, self.MAIL_RECEIVER, message.as_string()
            )
            smtpObj.quit()
            self.LOG.info(u"邮件发送成功".center(40, "*"))
        except smtplib.SMTPException:
            self.LOG.error(u"Error: 无法发送邮件".center(40, "*"))

    def __get_report(self):
        """获取最新测试报告"""
        self.LOG.info("The report path is : {}".format(self.reportPath))
        dirs = os.listdir(self.reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        self.LOG.info("The new report name: {0}".format(newreportname))
        return newreportname

    def __get_logpath(self):
        """获取最新日志"""
        self.LOG.info("The log path is : {}".format(self.logPath))
        logdirs = os.listdir(self.logPath)
        logdirs.sort()
        logname = logdirs[-1]
        self.LOG.info("The new log path name: {0}".format(logname))
        return logname

    @staticmethod
    def __read_file(fpath):
        # 读取文件
        BLOCK_SIZE = 1024
        with open(fpath, 'rb') as f:
            while True:
                block = f.read(BLOCK_SIZE)
                if block:
                    yield block
                else:
                    return

    def send(self):
        """发送测试结果报告邮件"""
        self.LOG.info(u"开始发送邮件".center(40, "*"))
        logname = self.__get_logpath()
        newreportname = self.__get_report()
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message["From"] = Header(self.MAIL_USER, "utf-8")
        for toName in self.MAIL_RECEIVER:
            message["To"] = Header(toName, "utf-8")
        """生成邮件的内容，和html报告附件"""
        message["Subject"] = Header(self.MAIL_SUBJECT, "utf-8")
        message["date"] = time.strftime("%a, %d %b %Y %H:%M:%S %z")

        # 读取报告内容，并添加到正文
        newreportPath = os.path.join(self.reportPath, newreportname)
        self.LOG.info(u"添加附件{}".format(newreportPath))
        # with open(newreportPath, "rb") as f:
        #     mailbody = f.read()
        mailbody = ''
        for item in self.__read_file(newreportPath):
            mailbody += bytes.decode(item)
        html = MIMEText(mailbody, _subtype="html", _charset="utf-8")
        message.attach(html)

        # html附件
        att1 = MIMEText(mailbody, "base64", "gb2312")
        att1["Content-Type"] = "application/octet-stream"
        att1["Content-Disposition"] = "attachment; filename={0}".format(
            newreportname
        )  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        message.attach(att1)
        # log日志附件
        newlogPath = os.path.join(self.logPath, logname)
        self.LOG.info(u"添加附件{}".format(newlogPath))
        att2 = MIMEText(open(newlogPath, "rb").read(), "base64", "gb2312")
        att2["Content-Type"] = "application/octet-stream"
        att2["Content-Disposition"] = "attachment; filename={0}".format(
            logname
        )  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        message.attach(att2)
        smtpObj = smtplib.SMTP()
        try:

            smtpObj.connect(self.MAIL_HOST, self.MAIL_PORT)  # 25 为 SMTP 端口号

            smtpObj.login(self.MAIL_USER, self.MAIL_PASSWORD)
            smtpObj.sendmail(
                self.MAIL_USER, self.MAIL_RECEIVER, message.as_string()
            )

            self.LOG.info(u"邮件发送成功".center(40, "*"))
        except smtplib.SMTPException as e:
            self.LOG.error("Error: 无法发送邮件".center(40, "*"))
            self.LOG.error("错误原因：{}".format(e))
        finally:
            smtpObj.quit()

    def send_report(self, project, report_path):
        """发送测试结果报告邮件"""
        self.LOG.info(u"开始发送邮件".center(40, "*"))
        logname = self.__get_logpath()
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message["From"] = Header(self.MAIL_USER, "utf-8")
        for toName in self.MAIL_RECEIVER:
            message["To"] = Header(toName, "utf-8")
        message["Cc"] = ';'.join(self.MAIL_CC_RECEIVER)
        """生成邮件的内容，和html报告附件"""
        subject = project + self.MAIL_SUBJECT + time.strftime("%Y%m%d", time.localtime(time.time()))
        message["Subject"] = Header(subject, "utf-8")
        message["date"] = time.strftime("%a, %d %b %Y %H:%M:%S %z")

        # 读取报告内容，并添加到正文
        self.LOG.info(u"添加附件{}".format(report_path))
        with open(report_path, "rb") as f:
            mailbody = f.read()
        # mailbody = ''.join(FileUtils.readfile(report_path))
        # for item in self.__read_file(report_path):
        #     mailbody += bytes.decode(item)
        html = MIMEText(mailbody, _subtype="html", _charset="utf-8")
        message.attach(html)

        # html附件
        att1 = MIMEText(mailbody, "base64", "gb2312")
        att1["Content-Type"] = "application/octet-stream"
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = "attachment; filename={0}".format(report_path)
        message.attach(att1)
        # log日志附件
        newlogPath = os.path.join(self.logPath, logname)
        self.LOG.info(u"添加附件{}".format(newlogPath))
        att2 = MIMEText(open(newlogPath, "rb").read(), "base64", "gb2312")
        att2["Content-Type"] = "application/octet-stream"
        att2["Content-Disposition"] = "attachment; filename={0}".format(
            logname
        )  # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        message.attach(att2)
        smtpObj = smtplib.SMTP()
        try:

            smtpObj.connect(self.MAIL_HOST, self.MAIL_PORT)  # 25 为 SMTP 端口号
            smtpObj.login(self.MAIL_USER, self.MAIL_PASSWORD)
            smtpObj.sendmail(
                self.MAIL_USER, self.MAIL_RECEIVER, message.as_string()
            )
            self.LOG.info(u"邮件发送成功".center(40, "*"))
        except smtplib.SMTPException as e:
            self.LOG.error("Error: 无法发送邮件".center(40, "*"))
            self.LOG.error("错误原因：{}".format(e))
        finally:
            smtpObj.quit()


if __name__ == "__main__":
    sm = SendMail()
    sm.send()
    # # print(sm.reportPath)
    # # sm.testsend()
