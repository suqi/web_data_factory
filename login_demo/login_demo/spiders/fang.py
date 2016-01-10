# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class FangSpider(scrapy.Spider):
    name = "fang"
    allowed_domains = ["sz.fang.com"]
    start_urls = (
        'http://www.sz.fang.com/',
    )

    def parse(self, response):

        req_list = []
        for page_num in range(1,4):
            url = "http://esf.sz.fang.com/house-a085-b0326/i3%s/" % page_num
            req = Request(
                url,
                callback = self.parse_page
            )
            req_list.append(req)

        return req_list

    def parse_page(self, response):

        for house in response.css(".houseList").css("dl"):
            price = float(house.css(".price::text").extract()[0])
            link = house.css("p").css(".title").css("a").css("::attr(href)").extract()[0]
            yield Request(
                "http://esf.sz.fang.com" + link,
                callback = self.parse_house
            )

    def parse_house(self, response):
        print response.css("#agantesfxq_B02_08").css("::text").extract()[0]

