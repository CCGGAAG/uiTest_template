# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


def send_email(report_file="E:\\111test\\blog_ui\\report\\2019-04-02 18_22_44.html"):
    try:
        # 发送邮箱
        sender = "yanhaiyuan@bdfint.com"
        # 接收邮箱
        receiver = "ilovefoever@foxmail.com"
        # 发送邮件服务器
        smtpserver = "smtp.bdfint.com"
        port = "465"
        # 发送邮箱账号和授权码
        username = "yanhaiyuan@bdfint.com"
        password = "Yan123456"

        # 读取测试报告的内容
        mail_body = open(report_file,"r" , encoding="utf-8").read()

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
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename= "report.html"'
        msg.attach(att)

        smtp = smtplib.SMTP()
        # 连接邮箱服务器
        smtp.connect(host=smtpserver, port=port)
        # 用户名密码
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('test report email has send out !')
    except Exception as e:
        print(e)


send_email()
