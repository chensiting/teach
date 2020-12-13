# -*- coding: utf-8 -*-
# @Author: kololo
# @Time : 2020-11-08 20:54

import xlrd#第三方库 cmd---->   pip install xlrd----读取excel

#1- 读取excel测试用例
excelDir = r'../data/松勤-教管系统接口测试用例-v1.4.xls'
#1-1:打开excel
workbook = xlrd.open_workbook(excelDir)
#查看所有的子表名
print(workbook.sheet_names())#返回是list
# workSheet = workbook.sheet_names()[1]
workSheet = workbook.sheet_by_name('新增客户61个')
#读取一行
rows = workSheet.row_values(1)
#读取一列
clos = workSheet.col_values(1)
#读取指定单元格
cellData = workSheet.cell(1,6).value#行，列
print(cellData)

# print(workSheet.cell(1,6).ctype)#单元数据类型  0 1:字符串 2 3 4 5

#2- --------------------构建接口对应请求-------------------------------
import requests
import json
#1-2构建请求---获取token
token_url = 'http://47.96.181.17:9090/rest/toController'
token_data = {"userName":"J201903070064","password":"362387359"}
headers = {"Content-Type":"application/json"}
resp = requests.post(token_url,data = json.dumps(token_data),headers=headers)
token = resp.json()['token']
print(token)

#2- 新增用户
addUser_url = 'http://47.96.181.17:9090/rest/ac01CrmController'
addUser_data = json.loads(cellData)#请求参数
print(type(addUser_data))
addUser_headers = {"Content-Type":"application/json","X-AUTH-TOKEN":token}

addUser_resp  =requests.post(addUser_url,data=json.dumps(addUser_data),headers=addUser_headers)
print(addUser_resp.text)

res = addUser_resp.json()["message"]
if res == '成功':
    print('新增用户接口测试---->成功！，耗时:----> ',addUser_resp.elapsed.total_seconds())
    excel_res = 'pass'
else:
    print('新增用户接口测试---->失败！')
    excel_res = 'fail'

#3- 测试结果写入excel
# import xlutils
from xlutils.copy import copy#复制函数  xls  xlsx
# 1- 首页打开excel
# workbookWr = xlrd.open_workbook(excelDir)
#2- 复制
workbookWr = copy(workbook)
wrSheet = workbookWr.get_sheet(1)
wrSheet.write(1,9,excel_res)#写单元格
workbookWr.save(r'C:\Users\XinTian\Desktop\松勤VIP接口测试用例-res-v1.2.xlsx')
