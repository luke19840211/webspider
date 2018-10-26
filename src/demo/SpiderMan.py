# -*- coding: UTF-8 -*-
'''
Created on 2018年10月26日

@author: luke
'''
from demo.UrlManager import UrlManager
from demo.HtmlDownloader import HtmlDownloader
from demo.HtmlParser import HtmlParser
from demo.DataOutput import DataOutput

class SpiderMan(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.manager = UrlManager
        self.downloader = HtmlDownloader
        self.parser = HtmlParser
        self.output = DataOutput
        
    
    def crawl(self,root_url):
        self.manager.add_new_url(root_url)
        
        while(self.manager.has_new_url( ) and self.manager.old_url_size() < 100):
            try:
                #从url管理器获取新的url
                new_url = self.manager.get_new_url()
                #html下载器下载网页
                html = self.downloader.download(new_url)
                #html解析器抽取网页数据
                new_urls,data = self.parser.parser(new_url,html)
                #将抽取的url添加到url管理器中
                self.manager.add_new_urls(new_urls)
                #数据存储器存储文件
                self.output.store_data(data)
                print('已经抓取%s个链接' %self.manager.old_url_size())
            except Exception as e:
                print('crawl failed')
        #self.output.output_html()

if __name__ =="__main__":
    spider_man = SpiderMan()
    #root_url = "http://baike.baidu.com/view/284853.htm"
    spider_man.crawl(root_url ="http://baike.baidu.com/view/284853.htm")