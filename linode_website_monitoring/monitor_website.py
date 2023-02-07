import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_email(email_message):
    with smtplib.SMTP('stapletonfamily-net02c.mail.protection.outlook.com', 25) as email:
        email.starttls()
        email.ehlo()
        email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Website is down!!!\n{email_message}"
        email.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)

try:
    response = requests.get('http://143.42.119.228:8080/')
    if response.status_code == 200:
        print('Site is ok')
    else:
        print('Website is down!!!')
        # send email notification
        send_email(f"Returned http status {response.status_code}.")
except Exception as ex:
    print(f'exception: {ex}')
    send_email(f"Connection timed out with the below exception:\n{ex}")