# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest

class TrainSpider(scrapy.Spider):
    name = "train"
    allowed_domains = ["12306.cn"]
    start_urls = (
        'http://www.12306.cn/',
    )

    def parse(self, response):
        return Request(
            "https://kyfw.12306.cn/otn/index/initMy12306",
            cookies={
                "BIGipServerotn": "668401930.50210.0000",
                "JSESSIONID": "0A01D727C4D1FD6A5E18D071C4ECAF8918948E41F7",
                "BIGipServerportal":"3134456074.17695.0000",
                "current_captcha_type":"Z"
            },
            callback=self.parse_name
        )

    def parse_name(self, response):
        # name = response.css("#my12306page").extract()
        # print repr(name).decode("unicode-escape")

        return Request(
                "https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date=2016-01-20&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=BJP&purpose_codes=ADULT",
                callback=self.parse_ticket
        )

    def parse_ticket(self, response):
        import json
        ticket_data = json.loads(response.body)
        for train in ticket_data['data']:
            print train["queryLeftNewDTO"]["station_train_code"], ":  ",  train["queryLeftNewDTO"]["swz_num"]
