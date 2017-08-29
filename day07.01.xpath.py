# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 21:25:36 2017

@author: pc
"""

import urllib
import urllib.request
from lxml import etree

def loadPage():
    
    
    print("正在下载" + filename)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
    
    request = urllib.request.Request(url,headers = headers)
    
    response = urllib.request.urlopen(request)
    
    html = response.read().decode('utf-8')
    #解析html文档为Html Dom模型
    xml = etree.HTML(html)
    link_list = content.xpath("")
    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link

def wirtePage(html):
    with open (filename,'w') as f:
        f.write()