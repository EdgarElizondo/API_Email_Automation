import os
import smtplib, ssl


def send_email(info):
    host = "smtp.gmail.com"
    port = 465

    FROM = os.getenv("EMAIL_SHOWCASE")
    TO = os.getenv("EMAIL_SHOWCASE")
    password = os.getenv("PASSWORD_SHOWCASE")
    
    context = ssl.create_default_context()

    # Add Subject
    SUBJECT = "Daily News"
    TEXT = ""
    for title, description in info:
        TEXT += f"Title: {title}\n" \
                + f"Description:{description}\n\n" \
                + "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n"
                

    # message to be sent       
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(FROM, password)
        server.sendmail(FROM, TO, message.encode("UTF-8"))
        
