# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 12:54
'''数据驱动'''
import pytest
#pytest.mark.parametrize  做数据驱动

#一.pytest.mark.parametrize 装饰器
#一个变量
#后面的数据给前面   X=1,2,3
@pytest.mark.parametrize('x',[1,2,3])
def test_001(x):
	print('------')
	assert x==3


#多个变量
@pytest.mark.parametrize('x,y',[(1,2),(3,4)])
def test_002(x,y):
	print('------')
	assert x+y==3


#完成修改课程的