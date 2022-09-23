# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() #工作名称
    link = scrapy.Field() #链接
    job_label = scrapy.Field()  # 岗位类别，全职
    address = scrapy.Field()  # 工作地址
    depart = scrapy.Field() #所属部门
    category = scrapy.Field() #职位分类
    num = scrapy.Field() #招聘人数
    school = scrapy.Field() #学历
    date = scrapy.Field() #招聘日期
    experience = scrapy.Field() #工作年限