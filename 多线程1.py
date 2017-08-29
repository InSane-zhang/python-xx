# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:04:38 2017

@author: pc
"""
#使用线程库
import threading
#队列
from Queue import Queue
#解析库
from lxml import etree
#请求处理
import requests
#json处理
import json

class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,dataQueue):
        #thread.Thread.__init(self)
        #调用父类初始化方法
        super(ThreadCrawl,self).__init__()
        self.threadName = threadName
        
        self.pageQueue = pageQueue
        
        self.dataQueue = dataQueue
        
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 OPR/46.0.2597.46"}
    
    def run(self):
        while not CRAWL_EXIT :
            try:
                #取出一个数字，先进先出
                #可选参数block
                #如果队列为空，block为true的话，就会进入阻塞状态，知道队列有信的数据
                #如果队列为空，block为false的话，就弹出一个Queue。empty（）异常
                page = self.pageQueue.get()
                url = "https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
                content = requests.get(url,headers = self.headers)
                self.dataQueue.put(content)
                
            except:
                pass
            
            
                
            
            


CRAWL_EXIT = False    
PARSE_EXIT = False    
def main():
    #页码的队列，存储10个，表示10个页面
    pageQueue = Queue(10)
    #放入1-10的数字，先进先出
    for i in range(1,11):
        
        pageQueue.put(i)
        
    dataQueue = Queue()
    
    crawllist = ["采集线程1号","采集线程2号","采集线程3号"]
    
    #存储3个采集线程
    threadcrawl = []
    
    for threadName in crawllist:
        thread = ThreadCrawl(threadName,pageQueue,dataQueue)
        thread.start()
        threadcrawl.append(thread)
    
    while not pageQueue.empty():
        pass
    global CRAWL_EXIT
    CRAWL_EXIT = True

    print("pageQueue为空")   

    for thread in threadcrawl:
        thread.join()
        
        print("i")
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()