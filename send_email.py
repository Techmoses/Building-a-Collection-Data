from email.mime.text import MIMEText
import smtplib

def send_email(email, height):
    from_email="oluwadamilare.m@yahoo.com"
    from_password="Bibleadewara"
    to_email=email

    subject="Height data"
    message="Hey there, your height is <strong>%s</strong>." % height

    msg=MIMEText(message, 'html')
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject




    sender='oluwadamilare.m@yahoo.com'
    receiver='oluwadamilare.m@yahoo.com'
    password='Bibleadewara'
    smtpserver=smtplib.SMTP("mail.smtp.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
