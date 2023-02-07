import requests
import smtplib
import os
import paramiko

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_email(email_message):
    with smtplib.SMTP('stapletonfamily-net02c.mail.protection.outlook.com', 25) as email:
        email.starttls()
        email.ehlo()
        email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Website is down!!!\n{email_message}"
        email.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)

# checks to see if a response is given from the server at all
try:
    response = requests.get('http://143.42.119.228:8080/')
    # checks to see if app is responding on listening port
    if False: #response.status_code == 200:
        print('Site is ok')
    else:
        print('Website is down!!!')
        # send email notification
        #send_email(f"Returned http status {response.status_code}.")

        # restart app
        ssh = paramiko.SSHClient()
        # this line avoids the prompt during first SSH connection
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname='143.42.119.228',
            username='root',
            key_filename='C:\\Users\\Robert\\.ssh\\id_rsa')
        stdin, stdout, stderr = ssh.exec_command('docker ps')
        print(stdout.readlines())
except Exception as ex:
    print(f'exception: {ex}')
    send_email(f"Connection timed out with the below exception:\n{ex}")