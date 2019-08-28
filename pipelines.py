# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import time

class BilibiliPipeline(object):
    def __init__(self):
        self.path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'泉州风景')

        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        title=item['title']
        arcurl=item['arcurl']
        # title_path = os.path.join(self.path, title)
        # if not os.path.exists(title_path):
        #     os.mkdir(title_path)
        print('.*50')
        print('正在下载%s'%title)
        os.system('you-get -o {} {}'.format(self.path,arcurl) )
        print('视频{}下载完成'.format(title))
        # time.sleep(5)
        x=0
        x += 1
        if x ==7:
            time.sleep(360)
            x=0
        return item
