# coding=utf-8

class HtmlOutput(object):
    #html输出器
    def __init__(self):
        self.datas = []

    #收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    #将收集好的数据写出到html文件中
    def output_html(self):
        fout = open('output.html','w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        if len(self.datas) == 0:
            print "数据为空！"
        #ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['content'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()