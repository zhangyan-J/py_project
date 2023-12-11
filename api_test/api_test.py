from pithy import request

@request(url='http://httpbin.org/post',method='post')
def post(self,key1='value1'):
    """
    post method
    :param self:
    :param key1:
    :return:
    """
    data = {
        'key1':key1
    }
    return dict(data=data)

#使用
response = post('test').to_json() #解析json字符，输出为字典
response = post('test').json   #解析json字符串，输出为字典
response = post('test').to_content() #输出为字符串
response = post('test').content #输出为字符串
response = post('test').get_cookie() #输出cookie对象
response = post('test').cookie #输出cookie对象

#结果取值，假设此处response = {'a': 1,'b':{'c':[1,2,3,4]}}
response = post('12111111111','123abc').json
print(response.b.c)  #通过点号取值，结果为{1，2，3，4]

print(response('$.a'))