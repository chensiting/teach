#time:2020-09-16
import requests, json
from config import HOST
#json.dumps()用于将字典形式的数据转化为字符串，json.loads()用于将字符串形式的数据转化为字典

class LoginClass:

    def api_login(self,inData,getSession =True):

        api_url = f'{HOST}/api/mgr/loginReq'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = json.loads(inData)
        print(payload)
        reps = requests.post(api_url, data=payload)
        reps.encoding = 'unicode_escape'  # 设置响应编码---显示中文
        #user_cookie = reps.cookies  # 作为返回值return
        if getSession:
            return reps.cookies['sessionid']
        else:
            return reps.text

if __name__=="__main__":
    print(LoginClass().api_login('{"username":"auto","password":"sdfsdfsdf"}'))
