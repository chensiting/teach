 # -*- coding: utf-8 -*-
# @Time    : 2020/9/16 19:35
import json
from Lib.ApiLogin import LoginClass

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
import pytest
import xlrd  # 读取库

def get_excelData():
    excelDir = r'C:\Users\chensiting\Desktop\接口自动化\松勤-教管系统接口测试用例-v1.4.xls'
    workBook = xlrd.open_workbook(excelDir, formatting_info=True)  # 保存原样---样式
    # 2-操作对应的用例表
    workSheet = workBook.sheet_by_name('1_登录接口')  # 通过表名获取
    dataList = []
    for cnt in range(1, 5):   #到第四行
        cellData = workSheet.cell_value(cnt, 6)  #取第6列  字符串类型
        repsCellData = workSheet.cell_value(cnt, 8)  # 取第8列  字符串类型 预期结果
        #dataList.append(cellData)
        dataList.append((cellData,repsCellData))
    return dataList   #返回列表


'''登录模块'''
@pytest.mark.parametrize('inData,repsData',get_excelData())
def test_Login(inData,repsData):
    res = LoginClass().api_login(inData,getSession =False)
    assert json.loads(res)["retcode"] == json.loads(repsData)["retcode"]  #断言










