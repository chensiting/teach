#time:2020-09-16
import requests,json,xlrd
from config import HOST

#json.dumps()用于将字典形式的数据转化为字符串，json.loads()用于将字符串形式的数据转化为字典

class LessonClass:
    #1- 新增接口
    #这个课程功能模块，每一个接口需要登录
    # def setup_class(self):
    #     session =
    #不写死indata为了方便后面测试用例请求参数调用
    def addcourse(self,session,inData):
        user_cookie = {'sessionid':session}
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}    #字典
        # 2- 参数   payload为字典   data为json,表单格式所以header可以不写  多行用三引号  不加引号是以表单形式 &符合进行拼接
        payload = {
                     'action': 'add_course',
                      'data': inData#转json  传进来输入是字符串，接口文档要求json格式，最好强转为json
                    }
        reps = requests.post(api_url, data=payload, headers=header, cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码---显示中文
        return reps.text

    #2- 列出课程
    def listcourse(self,session,inData):
        user_cookie = {'sessionid': session}
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/json'}
        payload = inData
        reps = requests.get(api_url, params=payload, headers=header, cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码---显示中文
        return reps.text

    #3- 删除课程
    def deletecourse(self,session,inId):
        user_cookie = {'sessionid': session}
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {
                   'action':'delete_course',
                   'id':int(inId)}  #强转为数值型   int可以转字符串和数字，如果是字母转换不了
        reps = requests.delete(api_url, data=payload, headers=header, cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码---显示中文
        return reps.json()


    #4- 修改课程
    def modiycourse(self,session,inData):
        user_cookie = {'sessionid': session}
        api_url = f'{HOST}/api/mgr/sq_mgr/'
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {
                    'action': 'modify_course',
                    'id': 1100,
                    'newdata': json.dumps(inData)}
        reps = requests.put(api_url, data=payload, headers=header, cookies=user_cookie)
        reps.encoding = 'unicode_escape'  # 设置响应编码---显示中文
        return reps.text


