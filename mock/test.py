#time:2020-11-28
'''
场景：helloworld 首页么有开发好
接口测试：需要做？
方案：mock技术 （python java flask django）
moco框架--是mock一种实现方案--简单方便    moco是个方案
学习目标：
1- 什么是mock技术?
2- 测试为什么需要mock?
3- moco是什么？
4- 构建请求
5- https---key ----- keyTool
'''
import requests,json
# api_url = 'http://127.0.0.1:9999/demo'
# reps = requests.get(api_url)
# print(reps.text)
# print(reps.status_code)
# 后续逻辑处理

#2-登录接口
# api_url = 'http://127.0.0.1:9999/api/mgr/loginReq'
# payload = {'username':'auto','password':'sdfsdfsdf'}
# reps = requests.post(api_url,data=payload)
# print(reps.text)
# print(reps.status_code)

#3-支付接口
api_url = "http://127.0.0.1:9999/trade/purchase"
payload={
        "out_trade_no":"20150320010101001",
        "auth_code":"28763443825664394",
        "buyer_id":"2088202954065786",
        "seller_id":"2088102146225135",
        "subject":"Iphone6",
        "total_amount":"88.88"
}
reps = requests.post(api_url,json=payload)
print(reps.text)
print(reps.status_code)










