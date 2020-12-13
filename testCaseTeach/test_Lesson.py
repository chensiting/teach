# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 19:37
from Lib.ApiLogin import LoginClass
from Lib.ApiLesson import LessonClass
import json,pytest,allure
from Lib.GetExcelData import get_excelData
@allure.feature('课程模块')#一级标题特性场景  类标签
@allure.severity("normal")
@pytest.mark.Lesson(order =2) #类前面加标签  order对用例进行排序

class TestLesson: #测试用例类
    def setup_class(self):       #登录  去库里导入登录类，进行调用
        """课程模块-登录初始化"""
        self.session = LoginClass().api_login('{"username":"auto","password":"sdfsdfsdf"}')
        #封装的时候带有2个返回值（ApiLogin）取第一个值

    #1-新增课程接口
    #fixtrue---参数化---excel

    @pytest.mark.lesson_add
    # 标签--- 正常运行全部跑，只运行一个pytest test_Lesson.py -s -m=add  多个用逗号隔开
    @pytest.mark.parametrize('inData,repsData', get_excelData('2-课程模块', 2, 26, 6, 8))
    @allure.story("新增课程")   #二级标题
    @allure.title("新增课程用例")  #某个接口标签
    def test_add_lesson(self,inData,repsData):
        res = LessonClass().addcourse(self.session,inData)
        assert json.loads(res)["retcode"] == json.loads(repsData)["retcode"]

    #2- 列出课程
    @allure.story("列出课程")
    @allure.title("列出课程用例")
    @pytest.mark.lesson_list
    @pytest.mark.parametrize('inData,repsData', get_excelData('2-课程模块', 27, 38, 6, 8))
    def test_list_lesson(self,inData,repsData):
        """列出课程"""
        res = LessonClass().listcourse(self.session,json.loads(inData))
        assert  json.loads(res)['retcode'] == json.loads(repsData)['retcode']#断言

    #3- 修改课程
    @allure.story("修改课程")
    @allure.title("修改课程用例")
    @pytest.mark.lesson_modify
    @pytest.mark.parametrize('inData,repsData', get_excelData('2-课程模块', 47, 49, 6, 8))
    def test_modify_lesson(self,inData,repsData):
        res = LessonClass().modiycourse(self.session,inData)
        assert json.loads(res)['retcode'] == json.loads(repsData)['retcode']  # 断言

    #4- 删除课程
    @allure.story("删除课程")
    @allure.title("删除课程用例")
    @pytest.mark.lesson_delete
    @pytest.mark.parametrize('inData,repsData', get_excelData('2-课程模块', 39, 46, 6, 8))
    def test_delete_lesson(self,inData,repsData):
        res = LessonClass().deletecourse(self.session,inData)
        assert json.loads(res)['retcode'] == json.loads(repsData)['retcode']  # 断言


if __name__ =="__main__":
    pytest.main(['test_Lesson.py','-s'])
