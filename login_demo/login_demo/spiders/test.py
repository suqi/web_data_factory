# -*- coding: utf-8 -*-
import scrapy

def test(name):
    print "hello ", name


class TestSpider(object):
    def parse(self):
        self.x

spider1 = TestSpider()
spider1.x = "111111"
spider1.parse()

spider2 = TestSpider()
spider2.x = "222222"
spider2.parse()
