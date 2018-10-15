# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
#导入setting.py文件的常量
from scrapy.utils.project import get_project_settings

class ImagePipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        #注意此次 yield
       yield  scrapy.Request(item['link'])



    def item_completed(self, results, item, info):
        '''results的数据格式：
        [(True, {'checksum': '1e2cc73f256eff17f2d6a69388421f97', 'path': 'full/d8de0a55eb41d9a4ac4a39a0d1fc008f360d8b98.jpg', 'url': 'h
ttps://rpic.douyucdn.cn/appCovers/2017/09/24/630154_20170924201445_small.jpg'})]
        '''
        # 获取setting.py文件的所有常量
        settings = get_project_settings()
        # 获取 IMAGES_STORE 的值
        images_folder = settings['IMAGES_STORE']
        data = [x['path'] for ok,x in results if ok]
        #替换 图片名 ,data 数据格式:
        #['full/b008d9e23bdb013f672ca7527d704e049bf0c87c.jpg']
        image_ext = data[0].split('.')[-1]
        os.rename(images_folder+data[0],images_folder+item['nickname']+'.'+image_ext)
        # print(images_folder+data[0])
        # print('#'*20)
        # print(images_folder+item['nickname']+'.'+image_ext)
        #这里用return 返回，而不能用yield，否则修改不了图片名
        return  item
