
'''
Created on 2018年3月31日

@author: luke
'''
# -*- coding: UTF-8 -*-
import requests


#url
urls=['http://www.baidu.com/','https://www.zhihu.com']

#get请求
for url in urls: 
    html=requests.get(url).content.decode('utf-8')
    print(html)

