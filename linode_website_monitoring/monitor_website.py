import requests
import smtplib
import os
import paramiko
import linode_api4

public_ip = '143.42.119.228'
docker_container_id = '75605139c86c'
linode_id = '42425285'

# set up env vars in system
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')

def send_email(email_message):
    print("Sending email...")
    with smtplib.SMTP('stapletonfamily-net02c.mail.protection.outlook.com', 25) as email:
        email.starttls()
        email.ehlo()
        email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"Website is down!!!\n{email_message}"
        email.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)

def restart_app():
    print("Restarting application...")
    ssh = paramiko.SSHClient()
    # this line avoids the prompt during first SSH connection
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=public_ip,
        username='root',
        key_filename='C:\\Users\\Robert\\.ssh\\id_rsa')
    stdin, stdout, stderr = ssh.exec_command(f'docker start {docker_container_id}')
    print(stdout.readlines())
    ssh.close()
    print("Application restarted")


# checks to see if a response is given from the server at all
try:
    response = requests.get(f'http://{public_ip}:8080/')
    # checks to see if app is responding on listening port
    if False: #response.status_code == 200:
        print('Site is ok')
    else:
        print('Website is down!!!')
        # send email notification
        #send_email(f"Returned http status {response.status_code}.")

        # restart app
        restart_app()

except Exception as ex:
    print(f'exception: {ex}')
    #send_email(f"Connection timed out with the below exception:\n{ex}")

    # restart server using linode library
    print('Rebooting server...')
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(linode_api4.Instance, linode_id)
    nginx_server.reboot()

    # restart app
    while True:
        nginx_server = client.load(linode_api4.Instance, linode_id)
        if nginx_server.status == 'running':
            restart_app()
            break
