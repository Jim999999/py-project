# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class DouyuPipeline(object):

    def __init__(self):
        self.f = open('./data.json','w')


    def process_item(self, item, spider):
        #json.dumps()转换python的dict为字符串
        self.f.write(json.dumps(dict(item))+"\n")
        return item #返回item告诉spider engine 已经处理完

    def close_spider(self,spider):
        self.f.close()