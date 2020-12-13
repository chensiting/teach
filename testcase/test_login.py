#time:2020-09-15

import pytest

def add_func(x):
    return x+1



def test_01():
    print('-------测试用例01---开始------')
    assert add_func(2) ==3
    print('-------测试用例01---结束------')

def test_02():
    print('-------测试用例02---开始------')
    assert add_func(2) == 4
    print('-------测试用例02---结束------')



if __name__=="__main__":
    pytest.main(['-s'])