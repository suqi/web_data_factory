# -*- coding:utf-8 -*-
'''
从建行基金网站获取基金数据
http://fund.ccb.com/Channel/3218673#falg_link
'''

# 首先获取所有基金的列表
import requests
response = requests.get("http://fund.ccb.com/Channel/3218673#falg_link")

# 现在开始使用BeautifulSoup来进行解析
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, "lxml")  ## html文档树

fund_table = soup.find("table", class_="data4")
fund_list = fund_table.tbody.find_all("tr")

for fund_tr in fund_list:
    print fund_tr.find("td", class_="data4_c1b").string, \
    fund_tr.find("td", class_="data4_c1g").string, \
    fund_tr.find("td", class_="data4_c1j").string

