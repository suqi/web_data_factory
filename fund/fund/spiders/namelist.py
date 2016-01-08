# -*- coding: utf-8 -*-
import scrapy

from fund.items import FundItem


class NamelistSpider(scrapy.Spider):
    name = "namelist"
    allowed_domains = ["fund.ccb.com"]
    start_urls = (
        'http://fund.ccb.com/Channel/3218673',
    )

    def parse(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        rows = response.css("#allshow").css("table").css("tbody").css("tr")
        
        
        fund_list = []

        for row in rows:
            f = FundItem()
            f["name"] = row.css("td").css(".data4_c1h").css("::text")[0].extract()
            f['code'] = row.css(".data4_c1g").css("::text")[0].extract()

            fund_list.append(f)

        return fund_list

            # import mysql sqlite3

        # return response.css("a::text").extract()
        # response

