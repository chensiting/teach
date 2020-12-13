#time:2020-11-28
import requests
from config import HOST


def logintest(username,password):
    login_url = f'{HOST}/api/mgr/loginReq'
    header = {'Content-Type':'application/x-www-form-urlencoded'}
    payload = {'username':username,'password':password}
    reps = requests.post(login_url,data=payload)
    reps.encoding = 'unicode_escape'#设置响应编码--显示中文
    #print(reps.text)
    # print(reps.cookies)
    #print(reps.cookies['sessionid'])
    return reps.cookies['sessionid']
#
if __name__ =="__main__":
    logintest('auto','sdfsdfsdf')

