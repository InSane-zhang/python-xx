# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 13:41:42 2017

@author: pc
"""

import requests
from bs4 import BeautifulSoup
import time

def captcha(captcha_data):
    with open ("captcha.jpg","wb") as f:
        f.write(captcha_data)

def zhihuLogin():
    #构建session对象，可以保持cookie。
    sess = requests.Session()
    
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
    #首先获取登陆页面，找到需要post的数据（__xsrf),同时会记录当前网页的cookie值
    html = sess.get("http://www.zhihu.com/#signin",headers = headers).text
    bs = BeautifulSoup(html,"lxml")
    #_xsrf 作用是防止CSRF攻击（跨站请求伪造），通常叫跨域攻击
    #通常是通过伪装成信任的用户的请求（利用cookie），盗取用户信息，欺骗web服务器
    #所以网站通过设置隐藏字段存放这个MD5字符串
    _xsrf = bs.find("input",attrs = {"name":"_xsrf"}).get("value")
    #发送图片请求，找到图片流
    captcha_url = "http://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time()*1000)
    captcha_data = sess.get(captcha_url,headers = headers).content
    #print(captcha_url)
    #print(_xsrf)
    text = captcha(captcha_data)
    
    data = {
            "_xsrf":_xsrf,
            "phone_num":"18914711781",
            "password":"zhk123456",
            "captcha":text
            }
    response = sess.post("http://www.zhihu.com/login/phone_num",data = data,headers = headers)  
    #print(response.text)
    
    
    response = sess.get("https://www.zhihu.com/people/zhang-xiao-kang-7-47/activities")
    print(response.text)
    
    
    
if __name__ == "__main__":
    zhihuLogin()