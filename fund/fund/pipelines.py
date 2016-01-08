# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NamelistPipeline(object):
    def process_item(self, item, spider):
        import sys
        reload(sys)
        sys.setdefaultencoding('utf-8')

        f = open("data.txt", 'a')

        import sqlite3
        conn = sqlite3.connect("test.db")
        
        line = u"基金名称:%s ; 基金编码：%s" % (item["name"], item["code"])
        # print line

        f.write(line)
        f.write("\n")
        f.close()

        conn.execute(u"insert into fund values ('%s', '%s')" % (item["name"] ,item["code"]))
        conn.commit()
        conn.close()

        return item
