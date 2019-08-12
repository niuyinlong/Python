from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

# 创建html解析类，实现对html的解析
class HtmlParse(object):

    # 获取解析后的新的URL
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        # links获取所有的词条url，正则表达式查询 /view/123.htm
        links = soup.find_all('a',href=re.compile(r"/item/"))
        for link in links:
            # 获得url
            new_url = link['href']
            # 补全不完整的url
            new_full_url = urljoin(page_url,new_url)
            # 添加上补全后的url
            new_urls.add(new_full_url)
        return new_urls

    # 获取解析后的新的数据
    def _get_new_data(self,page_url,soup):
        # 存放数据
        res_data = {}

        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        # <div class="lemma-summary">
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return None
        
        # 将html_coun添加进soup
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        # 两个解析，调用本地方法
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data