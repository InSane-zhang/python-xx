# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 21:59:52 2017

@author: pc
"""

#cookielib模块：主要作用是提供这些cookie的对象

import urllib
import urllib.request
import http.cookiejar #原先为cookielib。

#通过Cookiejar()类构建一个cookiejar()对象，用来保存cookie的值，

cookie = http.cookiejar.CookieJar()

#通过HTTPCookieProcessor（）处理器类构建一个处理器对象，用来处理cookie
#参数就是构建的CookieJar（）对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

#构建一个自定义的opener
opener = urllib.request.build_opener(cookie_handler)

#通过自定义的opener的addheaders的参数，可以添加HTTP报头参数，代替headers使用。
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.57")]


#人人网的登陆接口
url = "http://www.renren.com/PLogin.do"

data = {"email":"1021639035@qq.com","password":"zhk123456"}

data = urllib.parse.urlencode(data).encode("utf-8")

#第一次是post请求，发送登陆需要的参数，获取cookie
request = urllib.request.Request(url,data = data)

#第二次可以是get请求买这个请求讲保存生成的cookie一并发到web服务器，服务器会验证cookie通过
response = opener.open(request)

print(response.read().decode('utf-8'))





