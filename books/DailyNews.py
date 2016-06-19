#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re, datetime
import urllib
import json
from bs4 import BeautifulSoup
from lib.urlopener import URLOpener
from base import BaseFeedBook
from config import SHARE_FUCK_GFW_SRV
from config import SHARE_SRV

def getBook():
    return tech

class tech(BaseFeedBook):
    title                 = u'Daily News'
    __author__            = 'calibre'
    description           = u'每日知乎精选，豆瓣一刻，Quora精选，深夜食堂，各种科普。'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_dailynews.gif"
    coverfile             = "cv_dailynews.jpg"
    network_timeout       = 60
    oldest_article        = 7
    max_articles_per_feed = 9
    deliver_days          = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    feeds = [
        (u'瞎扯', 'http://zhihurss.miantiao.me/section/id/2'),
        (u'豆瓣一刻', 'http://yikerss.miantiao.me/rss'),
        (u'知乎日报', 'http://zhihurss.miantiao.me/dailyrss'),
        (u'知乎精选', 'http://www.zhihu.com/rss'),
        (u'深夜食堂', 'http://zhihurss.miantiao.me/section/id/1'),
        ('Quora', 'http://www.quora.com/rss'),
        (u'MIT科技评论', 'http://www.technologyreview.com/topnews.rss'),
    ]

    def url4forwarder(self, url):
        ' 生成经过转发器的URL '
        return SHARE_FUCK_GFW_SRV % urllib.quote(url)

    def url4forwarder_backup(self, url):
        ' 生成经过转发器的URL '
        return SHARE_SRV % urllib.quote(url)

    def fetcharticle(self, url, opener, decoder):
        """链接网页获取一篇文章"""
        if self.fulltext_by_instapaper and not self.fulltext_by_readability:
            url = "http://www.instapaper.com/m?u=%s" % self.url_unescape(url)
        if "daily.zhihu.com" in url:
            url = self.url4forwarder(url)
        if "economist.com" in url:
            url = self.url4forwarder(url)

        return self.fetch(url, opener, decoder)
