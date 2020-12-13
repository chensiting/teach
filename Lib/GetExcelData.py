# -*- coding: utf-8 -*-
# @Author: kololo
# @Time : 2020-11-01 23:04

# import xlrd  #读取库
# def get_excelData():
#
#     excelDir = r'../data/松勤-教管系统接口测试用例-v1.4.xls'
#     workBook = xlrd.open_workbook(excelDir, formatting_info=True)  # 保存原样---样式
#     # 2-操作对应的用例表
#     workSheet = workBook.sheet_by_name('2_课程模块')  # 通过表名获取
#     dataList = []
#     for cnt in range(1, 5):  # 到第四行
#         cellData = workSheet.cell_value(cnt, 6)  # 取第6列  字符串类型
#         repsCellData = workSheet.cell_value(cnt, 8)  # 取第8列  字符串类型 预期结果
#         dataList.append((cellData, repsCellData))
#     return dataList  # 返回列表

import xlrd,pprint#读取库
def get_excelData(sheetName,startRow,endRow,bodyCol,repsCol):
    '''
    :param sheetName: 表名
    :param startRow: 开始行数
    :param endRow: 结束函数
    :param bodyCol: 请求体列数
    :param repsCol: 响应体列数
    :return: [(请求体，响应体),(请求体，响应体)]
    '''
    excelDir = '../data/松勤-教管系统接口测试用例-v1.4.xls'
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)#保存原样--样式
    #2- 操作对应的用例表
    workSheet = workBook.sheet_by_name(sheetName)#通过表名获取
    dataList = []
    for cnt in range(startRow-1,endRow):
        cellData = workSheet.cell_value(cnt,bodyCol)#字符串类型  请求体
        repsCellData = workSheet.cell_value(cnt, repsCol)  # 字符串类型  预期结果
        # dataList.append(cellData)
        dataList.append((cellData,repsCellData))
    #pprint.pprint(dataList) #列表
    return dataList
