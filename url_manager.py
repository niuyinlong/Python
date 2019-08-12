# coding:utf8
# 建立url管理类，实现对未爬URL和已爬URL的管理
class UrlManager(object):
    # 初始化UrlManager属性，创建未爬集合和已爬集合
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    # 定义新加url是否为未读url方法
    def add_new_url(self,url):
        # 如果url为空则不添加
        if url is None:
            return
        # 如果这个url既不在待爬取的列表中也不再已经爬取过的列表中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 定义获取新url的方法
    def add_new_urls(self,urls):
        # 如果列表为空则不添加
        if urls is None or len(urls) == 0:
            return
        # 进行单个url的循环
        for url in urls:
            self.add_new_url(url)

    # 返回是否还有未爬取的url
    def has_new_url(self):
        # 如果new_urls长度不为0，则代表有待爬取的url
        return len(self.new_urls) != 0

    # 将未爬取的url逐个取出
    def get_new_url(self): 
        # pop方法，在列表中获得这个url，并且在列表中移除这个url
        new_url = self.new_urls.pop()
        # 将获得的url添加进old_urls
        self.old_urls.add(new_url)
        return new_url