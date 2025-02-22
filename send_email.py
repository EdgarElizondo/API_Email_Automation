import os
import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    FROM = os.getenv("EMAIL_SHOWCASE")
    TO = os.getenv("EMAIL_SHOWCASE")
    password = os.getenv("PASSWORD_SHOWCASE")
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(FROM, password)
        server.sendmail(FROM, TO, message)
        
