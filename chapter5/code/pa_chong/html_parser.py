# coding=utf-8
import re
from bs4 import BeautifulSoup


class HtmlParser(object):
    def parser(self, page_url, html_cont):
        """
        # html解析器
        :param page_url: 网页的URL
        :param html_cont: 网页的字符串数据
        :return: 网页包含相关的URL和文章的内容
        """
        # 判断网页URL和网页内容是否为空
        if page_url is None or html_cont is None:
            return
        # 获取解析器
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        # 获取解析到的URL
        new_urls = self._get_new_urls(soup)
        # 获取解析到的文章数据
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 解析相关文章的URL
    def _get_new_urls(self, soup):
        new_urls = set()
        # 获取相关的文章URL,格式如下:
        # <a href="https://blog.csdn.net/qq_18601953/article/details/78395878"
        # target="_blank" strategy="BlogCommendFromBaidu_7">
        links = soup.find_all('a', strategy=re.compile(r"BlogCommendFromBaidu_\d+"))
        # 提取所有相关的URL
        for link in links:
            new_url = link['href']
            new_urls.add(new_url)
        return new_urls

    # 解析数据
    def _get_new_data(self, page_url, soup):
        res_data = {}
        # 获取URLurl
        res_data['url'] = page_url

        # 获取标题<h1 class="csdn_top">把项目上传到码云</h1>
        essay_title = soup.find('h1', class_="csdn_top")
        res_data['title'] = essay_title.get_text()

        # 内容标签的格式如下:
        # <div id="article_content" class="article_content csdn-tracking-statistics tracking-click"
        # data-mod="popu_519" data-dsm="post">
        essay_content = soup.find('div', class_="article_content csdn-tracking-statistics tracking-click")
        res_data['content'] = essay_content.get_text()
        return res_data
