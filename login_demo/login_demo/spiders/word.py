# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest


class WordSpider(scrapy.Spider):
    name = "word"
    allowed_domains = ["www.baicizhan.com"]
    start_urls = (
        'http://www.baicizhan.com/login/',
    )

    def parse(self, response):
        return FormRequest(
            "http://www.baicizhan.com/login/",
            formdata={
                "email": "matt.su@foxmail.com",
                "raw_pwd": "scrapy"
            },
            callback= self.after_login_parse
        )

    def after_login_parse(self, response):
        return Request(
            "http://www.baicizhan.com/user/words/list",
            callback = self.parse_word_list
        )

    def parse_word_list(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        rows=response.css("#all-passed-word-list").css(".list-page-1")

        # for row in rows:

        word=rows.css(".list-word-title").css("::text").extract()
        mean=rows.css(".list-word-mean").css("::text").extract()

        print zip(word, mean)

        return Request(
            "http://www.baicizhan.com/user/words/list",
            callback = self.another_parse
        )
        # print u"单词名称:%s;单词意思:%s" %(word,mean)

    def another_parse(self, response):
        # do
        pass





