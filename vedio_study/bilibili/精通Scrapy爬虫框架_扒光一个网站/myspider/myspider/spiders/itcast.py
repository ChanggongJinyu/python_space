import scrapy
from myspider.items import  MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    # 其实url
    start_urls = ['https://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):

        # with open('itcast.html','wb') as f:
        #     f.write(response.body)
        # print(response.text)
        item = MyspiderItem()
        node_list = response.xpath("//div[@class='li_txt']")
        print(len(node_list))
        print(node_list[0])

        for node in node_list:
            temp = {}
            # xpath方法返回选择器对象列表
            # extract():从选择器对象中提取所有数据
            # extract_first():从选择器对象中提取第一个数据
            item['name'] = node.xpath('./h3/text()')[0].extract()
            # temp['name'] = node.xpath('./h3/text()').extract_first()
            item['title'] = node.xpath('./h4/text()')[0].extract()
            item['desc'] = node.xpath('./p/text()')[0].extract()
            yield temp

