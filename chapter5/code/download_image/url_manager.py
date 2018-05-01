# coding=utf-8


class UrlManager(object):
    # url管理器
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 向管理器中添加一个新的url
    def add_new_url(self, url):
        if url is None:
            return
        # 判断要添加的URL是否已存在新列表或者旧列表中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器中添加批量url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            # 添加新的URL
            self.add_new_url(url)

    # 判断管理器中是否有新的待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 从url中获取一个新的待爬取的url
    def get_new_url(self):
        # 获取并移除最先添加的URL
        new_url = self.new_urls.pop()
        # 把这个路径添加到已爬取的列表中
        self.old_urls.add(new_url)
        return new_url
