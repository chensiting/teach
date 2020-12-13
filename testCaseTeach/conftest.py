# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 11:31
import pytest,json
from Lib.ApiLogin import LoginClass
from Lib.ApiLesson import LessonClass
@pytest.fixture(scope='module',autouse=True) #环境初始化、数据清除
# function只要是测试用例函数都会执行一遍    module每个py执行一次用例清除一遍

def delete_all_lesson(request):
    print('-----测试环境初始化-----')

    #1-登录
    session =LoginClass().api_login('{"username":"auto","password":"sdfsdfsdf"}',getSession =True)#getSession =True缺省

    #2-列出所有课程
    inData ={
         'action':'list_course',
         'pagenum':'1',
         'pagesize':'20'
     }
    resList =json.loads(LessonClass().listcourse(session,inData))['retlist']
    # while resList !=[]:
    for one in resList:
        lessonId = one['id']  #获取课程id
    #3-删除所有的课程
        LessonClass().deletecourse(session,lessonId)

    #4-创建课程测试数据
    for one in range(1,7):
        lessoninData = {"name": f"xin{one:0>3}","desc":f"课程{one:0>3}", "display_idx": f"{one}"}
        LessonClass().addcourse(session,lessoninData)

    #5-环境数据清除-------teardown
    def fin():
        print('-----测试环境恢复-----')
    request.addfinalizer(fin)

