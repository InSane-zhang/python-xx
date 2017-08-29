# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:02:13 2017

@author: pc
"""

#第二种反爬虫方式,使用代理进行爬虫
import urllib.request

#代理开关，表示是否启用代理
proxyswitch = False

httpproxy_handler = urllib.request.ProxyHandler({
        "http":"124.88.67.54:80"
        
   #http:ip:端口号   开放代理 
   
   #私密代理x
        })

nullproxy_handler = urllib.request.ProxyHandler({})


if proxyswitch:
    #验证代理
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)
    

#构建了一个全局的opener，之后所有的请求都可以用URLopen（）的方式去发送，也附带Handler的功能
urllib.request.install_opener(opener)

request = urllib.request.Request("http://www.baidu.com/")

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
    


#代理名和密码可以写到环境变量里，也可以写成一个模块进行导入
#可以使用方式“http":"名称”：“密码”@“ip：端口”