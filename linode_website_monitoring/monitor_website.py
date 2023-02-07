import requests
import smtplib

response = requests.get('http://143.42.119.228:8080/')
if response.status_code == 200:
    print('Site is ok')
else:
    print('Website is down!!!')
    # send email notification
    with smtplib.SMTP('stapletonfamily-net02c.mail.protection.outlook.com', 25) as email:
        email.starttls()
        email.ehlo()
        email.login("robert@stapleton-family.net", "")