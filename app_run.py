# -*- coding: utf-8 -*-
# @Author: kololo
# @Time : 2020-11-02 21:24
import pytest,os

if __name__ =="__main__":
# 执行pytest单元测试，生成 Allure 报告需要的数据存在 /tmp 目录
    pytest.main(['test_lesson.py','-s','--alluredir', '../report/tmp'])
#  执行命令 allure generate ./tmp -o ./report --clean ，生成测试报告
    os.system('allure generate ../report/tmp -o ../report/report --clean')