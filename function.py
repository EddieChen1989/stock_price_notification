import smtplib
import email.message
from win10toast import ToastNotifier
from pwd import mail, pwd1

m = mail()
p = pwd1()


def send_email(msg_text):
    msg = email.message.EmailMessage()
    msg['From'] = m
    msg['To'] = m
    msg['Subject'] = 'Python Project-Stock value notification'
    msg.set_content(msg_text)

    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login(m, p)
    smtp.send_message(msg)
    smtp.close()
