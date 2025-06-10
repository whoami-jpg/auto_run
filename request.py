import requests
import os
from bs4 import BeautifulSoup
#为了模拟正常用户的访问，我们可以修改request的请求头参数：包含主机域名，User-Agent(正常访问时会带有浏览器类型和版本，以及电脑操作系统等),Accept等

def GetSourceInfo():
    #设定要get info的网址
    url = {
        'cs2':"https://steamdt.com/cs2/%E2%98%85%20M9%20Bayonet%20|%20Gamma%20Doppler%20(Factory%20New)"
    }
    #获取网页信息
    response = requests.get(url['cs2'])
    response.encoding = 'utf-8'
    with open('target_web.html','w') as f:
        f.write(response.text)
    #解析html
    soup = BeautifulSoup(response.text,"html.parser")
    soup_text = soup.prettify()
    with open('soup_text.html','w') as f1:
        f1.write(soup_text)
    #从页面中找到某些东西
    # findAll：树状查找
    # find：查找某个
    typelist = soup.find_all("div",attrs={"class":"relative mr-10 w-486"})#.find("div",attrs={"class":"text-color-green"})
    typelist_text = str(typelist)
    with open('typelist.html','w') as f2:
        f2.write(typelist_text)

def main():
    GetSourceInfo()


if __name__ == '__main__':
    main()
