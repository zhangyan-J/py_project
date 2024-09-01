import requests


#地址
url = "http://www.netbian.com/mei/"
#发送请求
#专门解析xpath的工具 lxml
from lxml import etree

resp = requests.get(url,headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"})
resp.encoding = 'gbk' #告诉软件用中文显示
print(resp.text)#打印文本结果

xp = etree.HTML(resp.text)

#提取图片地址
img_urls = xp.xpath("//ul/li/a/img/@src")
img_names = xp.xpath("//ul/li/a/img/@alt")


#保存数据
for u,n in zip(img_urls,img_names):
    print(f"图片名： {n} 地址：{u}")
    #图片结果
    img_resp = requests.get(url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"})
    with open(f"./request_test/image_generate/img/{n}.jpg",'wb') as f:
        f.write(img_resp.content)