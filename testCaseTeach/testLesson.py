# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 19:37
from Lib.ApiLogin import LoginClass
from Lib.ApiLesson import LessonClass
import json,pytest

class TestLesson: #测试用例类
    #这个课程功能模块，每一个接口需要登录

    def setup_class(self):       #登录  去库里导入登录类，进行调用
        print('------------登录模块-----开始--------')
        self.session = LoginClass().api_login('{"username":"auto","password":"sdfsdfsdf"}', getSession=True)   #封装的时候带有2个返回值（ApiLogin）取第一个值
        print('------------登录模块-----结束--------')

    @pytest.mark.add#标签--- 正常运行全部跑，只运行一个pytest testLesson.py -s -m=add  多个用逗号隔开
    #1-新增课程接口
    #fixtrue---参数化
    def test_add_lesson(self):
        indata ={"name":"xin123","desc":"pe","display_idx":"5"}
        print('------------新增课程模块-----开始--------')
        res = LessonClass().addcourse(self.session,indata)
        assert json.loads(res)['retcode'] == 0
        print('------------新增课程模块-----结束--------')

    #2- 列出课程
    def test_list_lesson(self):
        # indata ={"name":"xin1234","desc":"pe","display_idx":"5"}
        print('------------列出课程模块-----开始--------')
        # res = LessonClass().listcourse(self.session,indata)
        # assert json.loads(res)['retcode'] == 0
        # print('------------列出课程模块-----结束--------')

    # #3- 修改课程
    # def test_modify_lesson(self):
    #     indata ={"name":"xin1234","desc":"pe","display_idx":"5"}
    #     print('------------执行修改课程模块的用例-----开始--------')
    #     res = LessonClass().modiycourse(self.session,indata)
    #     assert json.loads(res)['retcode'] == 0
    #     print('------------执行修改课程模块的用例-----结束--------')
    # #4- 删除课程
    # def test_delete_lesson(self):
    #     print('------------执行删除课程模块的用例-----开始--------')
    #     res = LessonClass().deletecourse(self.session)
    #     print(res)
    #     assert res['retcode'] == 0
    #     print('------------执行删除课程模块的用例-----结束--------')

if __name__ =="__main__":
    pytest.main(['testLesson.py','-s'])
