# -*- coding: UTF-8 -*-
'''
Created on 2018年10月26日

@author: luke
'''
import codecs

class DataOutput(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.datas = []
    
    def store_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fout = codecs.open('baike.html','w',encoding = 'utf-8')
        fout.write("<html>")
        fout.write("<head><meta charset ='utf-8' /></head>")
        