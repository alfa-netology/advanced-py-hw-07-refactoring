import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Postman:
    def __init__(self, **options):
        self.login = options.get('login')
        self.password = options.get('password')
        self.smtp_server = options.get('smtp_server')

    def send_message(self, message):
        smtp_obj = smtplib.SMTP(self.smtp_server, 587)
        smtp_obj.ehlo()
        smtp_obj.starttls()
        smtp_obj.login(self.login, self.password)
        smtp_obj.sendmail(message['From'], message['To'], message.as_string())
        smtp_obj.quit()

    @staticmethod
    def prepare_message_to_send(sender, recipients, subject, message_content):
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = ', '.join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(message_content))
        return message
