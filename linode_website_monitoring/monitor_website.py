import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

response = requests.get('http://143.42.119.228:8080/')
if response.status_code == 200:
    print('Site is ok')
else:
    print('Website is down!!!')
    # send email notification
    with smtplib.SMTP('stapletonfamily-net02c.mail.protection.outlook.com', 25) as email:
        email.starttls()
        email.ehlo()
        email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = "Website is down!!!\nfix it, yo"
        email.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)