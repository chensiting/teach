 # -*- coding: utf-8 -*-
# @Time    : 2020/9/16 19:35
# import json
# from Lib.ApiLogin import LoginClass

# '''登录模块'''
# def test_Login():
#     res = LoginClass().api_login('auto','sdfsdfsdf')[1]
#     assert json.loads(res)["retcode"] == 0

# #pytest 数据驱动
# import pytest
# #@pytest.mark.parametrize('x',[1,2,3])
# @pytest.mark.parametrize('x,y',[(1,2),(3,4),(5,6)])  #装饰器  值不能为int要传列表
# def test_001(x,y):
#     print('------------')
#     assert x+y==3
#一种数据放列表，两种数据列表里面放元组
#
import json
from Lib.ApiLogin import LoginClass
import pytest,allure  # 读取库
from Lib.GetExcelData import get_excelData
from Lib.GetYamlData import  get_yaml_data
#
# def get_excelData():
#     excelDir = r'..\data\松勤-教管系统接口测试用例-v1.4.xls'
#     workBook = xlrd.open_workbook(excelDir, formatting_info=True)  # 保存原样---样式
#     # 2-操作对应的用例表
#     workSheet = workBook.sheet_by_name('1_登录接口')  # 通过表名获取
#     dataList = []
#     for cnt in range(1, 5):   #到第四行
#         cellData = workSheet.cell_value(cnt, 6)  #取第6列  字符串类型
#         repsCellData = workSheet.cell_value(cnt, 8)  # 取第8列  字符串类型 预期结果
#         #dataList.append(cellData)
#         dataList.append((cellData,repsCellData))
#     return dataList   #返回列表


# '''登录模块'''
# @allure.feature('登录模块')    #一级标题特性场景  类标签
# @allure.story("登录接口")      #二级标题
# @allure.title("登录接口用例")  #某个接口标签
# @allure.severity("critical")    #严重缺陷
# @pytest.mark.login(order = 1)#标签--
# @pytest.mark.parametrize('inData,repsData',get_excelData('1-登录接口',2,5,6,8))
#
# def test_Login(inData,repsData):
#     res = LoginClass().api_login(inData,getSession =False)
#     assert json.loads(res)["retcode"] == json.loads(repsData)["retcode"]#断言
#
#
# @allure.severity("critical")   #严重缺陷
# @allure.story("登录界面")     #二级标题
# @allure.title("获取图片用例") #某个接口标签
# @allure.description("这里只是做一个web ui自动化的截图效果")
# def test_login_image():
#     allure.attach.file(r'../data/test.jpg', '我是附件截图的名字',
#                            attachment_type=allure.attachment_type.JPG)


'''登录模块'''
@allure.feature('登录模块')    #一级标题特性场景  类标签
@allure.story("登录接口")      #二级标题
@allure.title("登录接口用例")  #某个接口标签
@allure.severity("critical")    #严重缺陷
@pytest.mark.login(order = 1)#标签--
@pytest.mark.parametrize('inData,repsData',get_yaml_data())

def test_Login(inData,repsData):
    res = LoginClass().api_login(inData,getSession =False)
    assert json.loads(res)["retcode"] == json.loads(repsData)["retcode"]#断言


@allure.severity("critical")   #严重缺陷
@allure.story("登录界面")     #二级标题
@allure.title("获取图片用例") #某个接口标签
@allure.description("这里只是做一个web ui自动化的截图效果")
def test_login_image():
    allure.attach.file(r'../data/test.jpg', '我是附件截图的名字',
                           attachment_type=allure.attachment_type.JPG)





