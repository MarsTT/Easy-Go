#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 10:18:57 2017

@author: marsxia
"""
#import urllib
#import urllib2

#values = {"username":"wwwtianciking@126.com","password":"lovol12345"}
#data = urllib.urlencode(values)
#url = "http://weibo.com/u/2403941325/home?wvr=5&lf=reg"
'''
url = "https://www.zhihu.com/"
request = urllib2.Request(url)
response = urllib2.urlopen(request)
print response.read()
'''

'''
import urllib2

request = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(request)
except urllib2.HTTPError,e:
    if hasattr(e,"code"):
        print e.code
except urllib2.URLError,e:
    if hasattr(e,"reason"):
        print e.reason
else:
    print "ok"
'''
'''
import urllib2
import cookielib

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value= '+item.value

'''
#保存cookie的账号密码到文件中
'''
import urllib2
import cookielib

filename= 'cookie.txt'
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)
response = opener.open("http://weibo.com/u/2403941325/home?wvr=5&lf=reg")

cookie.save(ignore_discard = True,ignore_expires = True)
'''

#将保存的信息模拟网站登陆
'''
import urllib2
import cookielib

cookie = cookielib.MozillaCookieJar()

cookie.load("cookie.txt",ignore_discard = True,ignore_expires = True)

req = urllib2.Request("http://weibo.com/u/2403941325/home?wvr=5&lf=reg")
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

#response = urllib2.urlopen(req)
response = opener.open(req)
print response.read()
'''

#模拟新浪微博登陆并访问
'''
import urllib
import urllib2
import cookielib


filename = "cookie_network.txt"
cookie = cookielib.MozillaCookieJar(filename)

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

postdata = urllib.urlencode({
                             'Name':'wwwtianciking@126.com',
                             'Value':'lovol12345'})

login_url = 'http://weibo.com/'

result = opener.open(login_url,postdata)

cookie.save(ignore_discard = True,ignore_expires = True)

for item in cookie:
    print "name"+item.name
    print "value"+item.value

grad_url = 'http://weibo.com/zibuyu9?refer_flag=0000015010_&from=feed&loc=nickname'

result = opener.open(grad_url)

print result.read()
'''



