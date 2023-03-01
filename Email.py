from main import price_as_float,product_name
from email.message import EmailMessage
import ssl
import smtplib
import datetime as dt
now=dt.datetime.now()

import random

email_sender="mainiabc0@gmail.com"
email_password="yylkxowzyktekwgl"
email_receiver="vishallimaini2003@gmail.com"



if(price_as_float<=2000):

    subject = "Amazon Price Alert!!!!"
    body =f"{product_name} is now  Rs.{price_as_float}"
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())








