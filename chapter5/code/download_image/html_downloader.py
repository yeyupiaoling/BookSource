# coding=utf-8
import urllib2


class HtmlDownloader(object):
    # html下载器
    def downloader(self, url):
        # 如果路径为空就返回空
        if url is None:
            return None
        # 打开网页数据
        response = urllib2.urlopen(url)
        # 判断是否访问成功，如果不成功就返回空
        if response.getcode() != 200:
            return None
        # 返回网页数据
        return response.read()
