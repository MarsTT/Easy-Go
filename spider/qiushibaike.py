# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 18:24:05 2017

@author: Mars
"""

'''
import urllib2
import urllib
import re

page=1
url = 'http://www.qiushibaike.com/text/page/'+str(page)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; \
.NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; \
.NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'
headers = {'User-Agent':user_agent}

try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
 #   print response.read()
    content = response.read().decode('utf-8')
    pattern = re.compile('',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.search("img",item[2])
        if not haveImg:
            print item[0],item[1],item[3]
 #       print item[0],item[1]
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
'''

import urllib
import urllib2
import re
import thread
import time

class QSBK:
    
    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; \
.NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; \
.NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko'
        self.headers = {'User-Agent':self.user_agent}
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
        
    #传入某一页的索引获得页面代码    
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/text/page/'+str(pageIndex)
            request = urllib2.Request(url,headers = self.headers)
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"糗事百科连接失败，错误原因为",e.reason
                return None   
                
    #传入某一页代码，返回本页不带图片的段子列表            
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败。。。。"
            return None
        pattern = re.compile('',re.S)
        items = re.findall(pattern,pageCode)
        #用来存储每页的段子们
        pageStories = []
        for item in items:
            haveImg = re.search("img",item[3])
            #如果不含有图片，把它加入list中
            if not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR,"\n",item[1])
                #item[0]是一个段子的发布者，item[1]是内容，item[2]是发布时间,item[4]是点赞数
                pageStories.append([item[0].strip(),text.strip(),\
                                    item[2].strip(),item[4].strip()])
        return pageStories
        
    #加载并提取页面的内容，加入到列表中    
    def loadPage(self):
        if self.enable == True:
            #如果当前未看的页数少于2页，则加载新一页
            if len(self.stories)<2:
                 #获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                #将该页的段子存放到全局list中
                if pageStories:
                    self.storis.append(pageStories)
                    #获取完之后页码索引加一，表示下次读取下一页
                    self.pageIndex += 1
                    
    #调用该方法，每次敲回车打印输出一个段子                
    def getOneStory(self,pageStories,page):
        #遍历一页的段子
        for story in pageStories:
            #等待用户输入
            input = raw_input()
            #每当输入回车一次，判断一下是否要加载新页面
            self.loadPage()
            #如果输入Q则程序结束
            if input == "Q":
                self.enable = False
                return 
            print u"第%d页\t发布人:%s\t发布时间:%s\t赞:%s\n%s" \
                    %(page,story[0],story[2],story[3],story[1])
    #开始方法
    def start(self):
        print u"正在读取糗事百科，按回车查看新段子，按Q结束"
        #使变量为True，程序可以正常运行
        self.enable = True
        #先加载一页内容
        self.loadPage()
        #局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.storis)>0:
                #从全局list中获取一页的段子
                pageStories = self.stories[0]
                #当前读到的页数加一
                nowPage += 1
                #将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                #输出该页的段子
                self.getOneStory(pageStories,nowPage)
spider = QSBK()
spider.start()                
                
                
                
                
                
                
        
       


