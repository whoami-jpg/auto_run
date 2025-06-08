import requests
import os
#为了模拟正常用户的访问，我们可以修改request的请求头参数：
    #包含主机域名，User-Agent(正常访问时会带有浏览器类型和版本，以及电脑操作系统等),Accept等
head = {}
#设定要get info的网址
url = "https://www.youpin898.com/"
url_info = "url.html"
#创建存储url信息的文件
result = os.system("mkdir %s" %(url_info))
#获取网页信息
response = requests.get(url)
if response.ok:
    print("请求成功")
else:
    print("请求失败")
