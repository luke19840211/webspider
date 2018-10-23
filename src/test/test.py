
'''
Created on 2018年3月31日

@author: luke
'''
# -*- coding: UTF-8 -*-
import urllib.request

#url
url='http://www.zhihu.com'

#get请求
html=urllib.request.urlopen(url).read()

print(html)

