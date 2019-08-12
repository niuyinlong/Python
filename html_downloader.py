#-*- coding: UTF-8 -*-
import urllib.request
import ssl
# python2.7升级到python3需要对ssl进行校验，需引入ssl模块，取消全局验证
ssl._create_default_https_context = ssl._create_unverified_context
# 创建html下载类，实现对html的下载
class HtmlDownloader(object):
    
    def download(self,url):
        # 如果url为空，则返回空
        if url is None:
           return None
        # 请求url的内容
        response = urllib.request.urlopen(url)
        print(response.getcode())
        # 如果结果为200，返回下载好的内容
        if response.getcode() == 200:
        	# 将返回的代码转化为utf-8
            return response.read().decode('UTF-8')
        # 如果请求结果不为200，则请求失败
        else:
            return None