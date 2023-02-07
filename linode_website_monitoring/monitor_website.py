import requests

response = requests.get('http://143.42.119.228:8080/')
if response.status_code == 200:
    print('Site is ok')
else:
    print('Website is down!!!')