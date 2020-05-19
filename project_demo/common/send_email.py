# -*-coding:utf-8-*-
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from utils.loadyaml import *
import os


def send_mail(report_file):
    # 发送邮箱
    sender = sender_username()
    # 接收邮箱
    receiver = receiver_username()
    # 发送邮件服务器
    smtpserver = "smtp.163.com"
    # 发送邮箱账号和授权码
    username = sender_username()
    password = sender_psw()
    # 读取测试报告的内容
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg['from'] = sender
    msg['to'] = receiver
    # 加上时间戳
    msg["date"] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, 'rb').read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    # 登录邮箱
    smtp = smtplib.SMTP()
    # 连接邮箱服务器
    smtp.connect(smtpserver)
    # 使用用户名和密码登录
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


def find_latest():
    """找到最新生成的报告文件"""
    result_dir = os.path.abspath('..') + "/report/"
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "/" + fn))
    lateset_report_file = os.path.join(result_dir, lists[-1])
    return lateset_report_file


def send_report():
    report_file = find_latest()
    send_mail(report_file)
