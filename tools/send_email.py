# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/17 15:42
@Auth ： 你赖大爷
@File ：send_email.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class sendEmai():
    @staticmethod
    def Sendemail(newfile):
        f=open(newfile,'rb')
        mail_body=f.read()
        f.close()
        # smtpserver = 'smtp.exmail.qq.com'
        smtpserver = 'smtp.163.com'
        user = 'firefly1995823@163.com'
        password = 'YJJAFZGKFGKBZOCV' #这里是密码 codingLaiyi823@
        sender="firefly1995823@163.com"
        # xuli@mogul-tech.com
        receiver=["firefly1995823@163.com"]
        subject='自动化测试报告'
        msg = MIMEMultipart('mixed')
        msg_html1 = MIMEText(mail_body,'html','utf-8')
        msg.attach(msg_html1)
        msg_html = MIMEText(mail_body,'html','utf-8')
        msg_html["Content-Disposition"] = 'attachment;filename="result.html"'
        msg.attach(msg_html)
        msg['From'] = 'firefly1995823@163.com'
        msg['To'] = ";".join(receiver)
        msg['Subject'] = Header(subject,'utf-8')
        smtp = smtplib.SMTP_SSL(smtpserver,465)
        # smtp.connect(smtpserver,465)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
