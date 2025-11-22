import os
import smtplib

def send_mail(to, subject, body):
    user = os.getenv("GMAIL_USER")
    app_password = os.getenv("GMAIL_APP_PASSWORD")

    message = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(user, app_password)
    server.sendmail(user, to, message)
    server.quit()
