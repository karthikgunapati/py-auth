import email, smtplib, ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class emailUtil(object):
    def __init__(self, host, subject, sender, receivers, port=465, password=None):
        self.receivers = receivers
        self.sender = sender
        self.subject = subject
        self.password = password
        self.host = host
        self.port = port
    
    
    def message(self, msg_str, msg_type="plain", **kwargs):
        msg = MIMEMultipart()
        msg["Subject"] = self.subject
        msg["From"] = self.sender
        msg["To"] =  ", ".join(self.receivers)
        msg.attach(MIMEText(msg_str.format(**kwargs), msg_type))
        return msg.as_string()

    def send_mail(self, message):
        with smtplib.SMTP(self.host, self.port) as server:
            if self.password:
                server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receivers, message)
