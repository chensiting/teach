#time:2020-11-17
#数据加密
url = 'https://120.55.190.222/mgr/login/login.html'
import requests
reps = requests.get(url,verify=False)
#不加verify，报错requests.exceptions.SSLError: HTTPSConnectionPool(host='120.55.190.222', port=443)
print(reps.text)

