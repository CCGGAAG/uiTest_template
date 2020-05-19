#coding=utf-8
import smtplib
from tools import sample_tools
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailHandle(object):
    def __init__(self):
        email_settings=sample_tools.get_project_config(config_file="email.yaml")
        self.SMTP_HOST=email_settings.get("SMTP_HOST")
        self.SMTP_PORT=email_settings.get("SMTP_PORT")
        self.MAIL_USER=email_settings.get("MAIL_USER")
        self.MAIL_PASSWORD=email_settings.get("MAIL_PASSWORD")


    # 发送邮件
    def send_email(self,content, project_name=None, to="xx.com", fname=None):
        try:
            smtp_obj = smtplib.SMTP(self.SMTP_HOST,self.SMTP_PORT)
            smtp_obj.ehlo()
            smtp_obj.starttls()
            smtp_obj.ehlo()

            smtp_obj.login(self.MAIL_USER, self.MAIL_PASSWORD)
            msg = MIMEMultipart()

            att1 = MIMEText(content, _subtype='html', _charset='gbk')
            # 构造邮件附件
            att1["Content-Type"] = 'application/octet-stream'
            att1["Content-Disposition"] = 'attachment; filename="' + fname
            msg.attach(att1)

            # 构造邮件内容
            msg.attach(MIMEText(content, _subtype='html', _charset='gbk'))
            msg['Subject'] = project_name + "接口自动化测试报告"
            msg['from'] = self.MAIL_USER
            msg['To'] = to
            smtp_obj.sendmail(self.MAIL_USER, to.split(','), msg.as_string())

            smtp_obj.quit()

        except Exception as e:
            print(e)


    with io.open(report_path,"rb") as fp:
        content=fp.read()
        EmailHandle().send_email(content=content,project_name="example Api",fname="example_report.html",to=to)
