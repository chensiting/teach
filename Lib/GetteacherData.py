#time:2020-11-28

import xlrd  #读取库
def get_teacherData():

    excelDir = r'../data/松勤-教管系统接口测试用例-v1.4.xls'
    workBook = xlrd.open_workbook(excelDir, formatting_info=True)  # 保存原样---样式
    # 2-操作对应的用例表
    workSheet = workBook.sheet_by_name('3-老师模块')  # 通过表名获取
    dataList = []
    for cnt in range(1, 2):  # 到第四行
        cellData = workSheet.cell_value(cnt, 6)  # 取第6列  字符串类型
        repsCellData = workSheet.cell_value(cnt, 8)  # 取第8列  字符串类型 预期结果
        dataList.append((cellData, repsCellData))
    return dataList  # 返回列表

get_teacherData()




