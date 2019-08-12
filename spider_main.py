#-*- coding: UTF-8 -*-
import url_manager,html_downloader,html_parser,html_outputer
import ssl
import urllib.parse
class SpiderMain(object):
    # 初始化各对象
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManager()
        # 下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 解析器
        self.parser = html_parser.HtmlParse()
        # 输出器        
        self.outputer = html_outputer.HtmlOutputer()
    # 爬虫的调用函数
    def craw(self, root_url):
        # 将入口url添加进url管理器
        self.urls.add_new_url(root_url)
        # count记录当前爬取的是第几个url
        count = 1
        # 启动爬虫的循环
        while self.urls.has_new_url():
            # 异常处理
            try:
                # 获取待爬取的url
                new_url = self.urls.get_new_url()
                # 输入第几个url
                print ('craw %d : %s' % (count,urllib.parse.unquote(new_url)))
                # 启动下载器下载页面
                html_cont = self.downloader.download(new_url)
                print(html_cont)
                # 调取解析器解析下载的页面
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                # 数据的处理，url添加入url管理器
                self.urls.add_new_urls(new_urls)
                # 收集数据
                self.outputer.collect_data(new_data)

                if count == 100:
                    break

                count = count + 1
            # 出现问题，标记爬取失败
            except:
                print ('craw failed')
        # 输出收集好的数据
        self.outputer.output_html()

if __name__ == "__main__":
# url的入口
    root_url = "https://baike.baidu.com/item/python/407313"
    obj_spider = SpiderMain()
# 启动爬虫
    obj_spider.craw(root_url)