# coding=utf-8
import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    # 调度程序
    def __init__(self):
        # 获取URL管理器
        self.urls = url_manager.UrlManager()
        # 获取网页下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 获取网页解析器
        self.parser = html_parser.HtmlParser()
        # 获取数据输出器
        self.output = html_outputer.HtmlOutput()

    def craw(self, root_url, max_count):
        count = 1
        # 添加爬虫入口的跟路径
        self.urls.add_new_url(root_url)
        # 创建一个循环,如果URL管理器中还有新的URL就一直循环
        while self.urls.has_new_url():
            try:
                # 从URL管理器中获取新的URL
                new_url = self.urls.get_new_url()
                print 'craw %d : %s ' % (count, new_url)
                # 下载网页
                html_cont = self.downloader.downloader(new_url)
                # 解析网页数据
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                # 添加新的URL
                self.urls.add_new_urls(new_urls)
                # 添加新的数据
                self.output.collect_data(new_data)
                # 满足爬取数量及中断
                if count == max_count:
                    break
                count = count + 1
            except Exception, e:
                print '爬取失败：', e
        # 输出数据
        self.output.output_html()


if __name__ == '__main__':
    # 爬虫的根URL
    root_url = "https://blog.csdn.net/qq_33200967/article/details/70186759"
    # 爬取的数量
    max_count = 10
    obj_spider = SpiderMain()
    # 启动调度器
    obj_spider.craw(root_url, max_count)
