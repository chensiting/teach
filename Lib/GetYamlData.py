# -*- coding: utf-8 -*-
# @Author: kololo
# @Time : 2020-11-15 17:35
import yaml,pprint,json

#操作yaml    任何文件都需要open打开
# yamlDir1 = '../data/test.yaml'
# yamlDir2 = '../data/test1.yaml'
#创建文件对象
#fo = open(yamlDir1,'r',encoding='utf-8') #读的文件有中文

#一组数据  load读操作
# res = yaml.load(fo,Loader=yaml.FullLoader)  #yaml 5.1版本为了安全都需要加上Loader=yaml.FullLoader 字符串转字典 获取数据
# print(res)

#两组数据---可迭代对象 迭代生成器 需要for循环取值
# res =yaml.load_all(fo,Loader=yaml.FullLoader)
# print(res)
# for one in res:
#     print(one)

#yaml写操作 dump
#追加'a'
# fo1 = open(yamlDir2,'a',encoding='utf-8')
# data1 ={'name':'tom','age':20}
# data2 =[10,20,30,{'name':'tom','age':20}] #列表里面套字典
# #yaml.dump(data2,fo1) #写一组数据
# #多个列表
# yaml.dump_all([data1,data2],fo1) #写多个数据
#
# fo1.close() #关闭文件
#
#

#-----------------------------------------------------------登录页面操作----------------------------------------------------
'''
json.dump()用于将dict类型的数据转成str，并写入到json文件中
json.dumps()用于将dict类型的数据转成str，因为如果直接将dict类型的数据写入json文件中会发生报错，因此在将数据写入时需要用到该函数。
json.load()用于从json文件中读取数据
json.loads()用于将str类型的数据转成dict
'''
def get_yaml_data():
    yamlDir3 = '../data/yaml_test.yaml'
    fo = open(yamlDir3,'r',encoding='utf-8') #读的文件有中文
    res =yaml.load(fo,Loader=yaml.FullLoader)
    #pprint.pprint(res)
    #封装数据
    resList =[]
    for one in res:   #res是个列表
        #print(res[one]['data'], res[one]['check'])  #TypeError: list indices must be integers or slices, not dict
        #print(one['data'], one['check'])  # one本来就是字典，取出来是个字典  用键去取值
        resList.append((json.dumps(one['data']),json.dumps(one['check'])))
    #print(resList)
    return resList
