# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 23:17:04 2017

@author: pc
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 22:49:46 2017

@author: pc
"""

import urllib
import requests

def loadPage(url,filename):
    """作用：根据url请求 获取服务器响应文件
        url：需要爬取的url地址
        filename:处理的文件名
    """
    print("正在下载" +filename)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
    response = requests.get(url,headers = headers)
    return response.text
    
    
def writePage(html,filename):   
    
    """作用：将html内容写到本地
        html：服务器相应文件内容
    """
    print("正在保存" + filename)
    #文件写入
    with open (filename,'w') as f:
       f.write(str(html) )
    print("-"*30)
    
def tiebaSpider(url,beginPage,endPage):
    """作用：贴吧爬虫调度器，负责组合处理每个页面的url
    URL：贴吧url的前部分
    bagainPage:起始页
    endPage：结束页
    """
    
    
    
    for page in range(beginPage,endPage + 1):
        pn = (page - 1) *50
        filename = "Page" +str(page) +".html"
        fullurl = url + "&&pn=" + str(pn)
        #print(fullurl)
    
        html = loadPage(fullurl,filename)
        #print(html)
        writePage(html,filename)
if __name__ == "__main__":
    kw = input("请输入需要爬取的贴吧名： ")
    beginPage = int(input("起始页： "))
    endPage = int(input("结束页： "))
   
    
    url = "https://tieba.baidu.com/f?"
    
    kw = {"kw":kw}
    
    key = urllib.parse.urlencode(kw)
    
    fullurl = url + key
    
    tiebaSpider(fullurl,beginPage,endPage)