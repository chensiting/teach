#time:2020-11-28
import requests,json
from config import HOST
from Lib.login_test import logintest

'''
1- json参数---建议使用
reps = requests.post(api_url,json=payload2)

2- data参数
import json
reps = requests.post(api_url,data=json.dumps(payload2),headers = header)
'''

def add_teacher():
    user_session= logintest('auto','sdfsdfsdf')
    user_cookie = {'sessionid':user_session}
    api_url = f'{HOST}/api/mgr/sq_mgr/'
    header ={'Content-Type':'application/x-www-form-urlencoded'}
    payload ={

               'action':'add_teacher',
               'data':'''{
                    "username":"lishiming1",
                    "password":"sq888",
                    "realname":"李世民1",
                    "desc":"李世民老师",
                    "courses":[{"id":2195,
                                "name":"初中化学课程"}],
                    "display_idx":1
                    }'''
             }
    reps = requests.post(api_url,data=payload,cookies=user_cookie)
    reps.encoding = 'unicode_escape' #设置响应编码---显示中文
    #print(reps.text)
    return reps.text
def list_teacher():
    user_session= logintest('auto','sdfsdfsdf')
    user_cookie = {'sessionid':user_session}#
    api_url = f'{HOST}/api/mgr/sq_mgr/?action=list_teacher&pagenum=1&pagesize=20'
    reps = requests.get(api_url,cookies=user_cookie)
    reps.encoding = 'unicode_escape' #设置响应编码---显示中文
    #print(reps.text)
    return reps.text

def modify_teacher():
    user_session= logintest('auto','sdfsdfsdf')
    user_cookie = {'sessionid':user_session}
    api_url = f'{HOST}/api/mgr/sq_mgr/'
    payload ={
               'action':'modify_teacher',
               'id':'260',
               'newdata':'''{
                    "username":"cst1",
                    "password":"sq888",
                    "realname":"cst1",
                    "desc":"cst老师",
                    "courses":[{"id":2195,
                                "name":"初中化学课程"}],
                    "display_idx":1
                    }'''
             }
    reps = requests.put(api_url,data=payload,cookies=user_cookie)
    reps.encoding = 'unicode_escape' #设置响应编码---显示中文
    #print(reps.text)
    return reps.text

def delete_teacher():
    user_session= logintest('auto','sdfsdfsdf')
    user_cookie = {'sessionid':user_session}
    api_url = f'{HOST}/api/mgr/sq_mgr/'
    payload ={
               'action':'delete_teacher',
               'id':'262'
             }
    reps = requests.delete(api_url,data=payload,cookies=user_cookie)
    reps.encoding = 'unicode_escape' #设置响应编码---显示中文
    #print(reps.text)
    return reps.text



