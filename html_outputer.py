#-*- coding: UTF-8 -*-
import urllib.parse
# 将数据以html格式输出
class HtmlOutputer(object):
    # 在构造函数中进行初始化
    def __init__(self):
        self.datas = []
    # 该方法用于收集数据
    def collect_data(self,new_data):
        if new_data is None:
            return
        self.datas.append(new_data)
    # 将收集好的数据写出到html文件中
    def output_html(self):
        # 创建一个文件的输出对象
        fout = open('output.html','w',encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        # 将数据输出为表格的格式
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            # urllib.parse.unquote可以将编码转化为中文
            fout.write("<td>%s</td>" % urllib.parse.unquote(data['url']))
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()