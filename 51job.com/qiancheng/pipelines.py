# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime


class QianchengPipeline(object):

    def __init__(self):
        #pass
        self.file_name = open('./jobs.xls','w+')
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        content = '时间:' + time
        self.file_name.write(content + "\n")

    def process_item(self, item, spider):
        contents = item['job_name']+"\t"+item['job_price']+"\t"+item['company_name']+"\t"+item['job_addr']+"\t"+item['job_url']
        self.file_name.write(contents+ "\n")

        #print(item)
        #pass
        return item

    def close_spider(self,spider):
        self.file_name.close()