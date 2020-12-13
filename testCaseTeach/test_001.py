# -*- coding: utf-8 -*-
# @Author: kololo
# @Time : 2020-11-01 23:06
#批量运行
import pytest

@pytest.mark.testa   #只运行testa用例    pytest test_Lesson.py -s -m=testa   -m=mark 标签   -s输出打印  q简化输出
class Test1:
    def test_1(self):
        print("this is test1")
        assert 1==1

    def test_2(self):
        print("this is test2")
        assert 1+2 ==3

@pytest.mark.testb  #多个用例运行pytest test_Lesson.py -sq -m=testa,testb
#运行单个用例，通过测试类，类型过滤  pytest -sq test_Lesson.py ::Test1  可以对函数细分pytest -sq test_Lesson.py ::Test1::test_1
#通过用例名称进行筛选 pytest -sq -k 2 test_xt.py    2是筛选的内容
class Test2:
    def test_3(self):
        print("this is test3")
        assert 3+1 ==4

    def test_4(self):
        print("this is test4")
        assert 3+2 ==5