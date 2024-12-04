import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


def sendsimple(emailto, text1, subject):
    login = "foreveryproject@yandex.ru"
    password = "yrcpxihogvidmojj"

    text = MIMEMultipart()
    text["Subject"] = Header(subject, "utf-8")
    text["From"] = login
    text["To"] = emailto
    text.attach(MIMEText(text1, "plain"))
    server = smtplib.SMTP("smtp.yandex.ru", 587, timeout=0.5)
    try:
        server.starttls()
        server.login(login, password)
        server.sendmail(login, emailto, text.as_string())
        return True
    except Exception as ex:
        return ex
    finally:
        server.quit()
