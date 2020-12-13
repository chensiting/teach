# -*- coding: utf-8 -*-
# @Author: kololo
# @Time : 2020-11-08 20:18
import pytest
@pytest.mark.parametrize('x,y',[(1,2),(3,4)])

def test_sum(x,y):
    sum = x + y
    print(sum)

if __name__ =="__main__":
    pytest.main(['test_sample.py','-s'])

# import pytest
# @pytest.mark.smoke
#
# def test_sum(login):
#     token = login[0]
#     guid = login[1]
#     print(token)
#     print(guid)
#
# def test_2():
#     print('测试用例')
#
# if __name__ =="__main__":
#     pytest.main(['test_sample.py','-s','-m=smoke'])