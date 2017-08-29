# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 22:02:21 2017

@author: pc
"""

import urllib.request
import re


class Spider():
    def __init__(self,page):
       
        #初始化其实页面
        self.page = 1
        #爬取开关，如果为true继续爬取
        self.switch = True
    
        
        
    def loadPage(self,):
        """
                 下载页面
        """
        print("正在下载数据...")
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
        url = "http://www.neihan8.com/article/index_"+ str(self.page) +".html"
        request = urllib.request.Request(url,headers = headers)
        response = urllib.request.urlopen(request)
        #获取每页的html源码字符串
        html = response.read().decode('utf-8')
        #创建正则表达式对象，匹配每页里的段子内容，re.S表示匹配全部字符串内容
        pattern = re.compile('<div\sclass="desc">(.*?)</div>',re.S)
        #将正则匹配对象应用到html源码字符串里，返回这个页面里的所有段子的列表
        content_list = pattern.findall(html)
        #for content in content_list:
            #汉字为gbk要转码
            #print (content.decode("gbk"))
        #调用dealPage（）出来段子的不需要的内容
        self.dealPage(content_list)
    def writePage(self,item): 
        """
            写入文件
        """
        #处理完后用self.write（）将段子写到文件中
        print("正在写入数据...")
        with open("duanzi.txt","a") as f:
            f.write(item)
    
    def dealPage(self,content_list):
        """
            处理页面
        """
        for item in content_list:
            #将集合里的每个段子挨个替换文字里的标签
            item = item.replace("<p>"," ").replace("</p>"," ").replace("</br>"," ")
            self.writePage(item)
            
    def startWork(self):
        
        """
            爬虫控制
        """
        
        while self.switch:
            self.loadPage()
            command = input("回车继续爬取(推出按quit）")
            if command =='quit':
                self.switch = False
            
            self.page += 1
            
            print ("谢谢使用...")

if __name__ == "__main__":
    duanziSpider = Spider()
    #duanziSpider.loadPage(page)
    duanziSpider.startWork()
    

    
    
