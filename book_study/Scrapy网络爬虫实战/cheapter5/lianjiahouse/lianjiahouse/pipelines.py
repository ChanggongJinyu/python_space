# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy import Request


class LianjiahousePipeline:

    # 设置存储文档目录
    collection_name = 'secondhandhouse'

    def __init__(self, mongo_url, mongo_db):
        self.mongo_uri = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
        #     通过crawler获取setting文件，获取其中mongodb配置信息
            mongo_url=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE','lianjia')
        )

    def open_spider(self,spider):
    #     当爬虫打开时连接mongodb数据库
    # 先连接server，再连接指定数据库
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self,spider):
    #     爬虫结束时关闭数据库连接
        self.client.close()

    def process_item(self, item, spider):
        # 将item插入数据库
        self.db[self.collection_name].insert_one(dict(item))
        return item


class LianjiaImagePipeline:

    def get_midia_requests(self,item,info):
        for image_url in item['image_urls']:
            # 将图片地址传入Request，进行下载，同时将item参数添加到Request中
            yield Request(image_url,meta={'item':item})

    def file_path(self,request, response=None,info = None):
        # 从Request中获取item，以房屋标题做文件夹名称
        item = request.meta['item']
        image_folder = item['house_name']
        # 使用图片url做图片存储名称
        image_guild = request.url.split('/')[-1]
        # 图片保存，文件夹/图片
        image_save = u'{0}/{1}'.format(image_folder, image_guild)
        return image_save
