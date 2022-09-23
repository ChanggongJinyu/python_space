import scrapy
from jingdong.items import JingdongItem


class JdComputerSpider(scrapy.Spider):
    name = 'jd_computer'
    allowed_domains = ['jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=670%2C671%2C672&page=1&s=1&click=0']

    def parse(self, response):
        for node in response.xpath('//*[@id="J_goodsList"]/ul/li'):
            item = JingdongItem()
            item['price'] = node.xpath('./div/div[2]/strong/i/text()').extract()
            item['name'] = node.xpath('./div/div[3]/a/em/text()').extract()
            item['shop'] = node.xpath('./div/div[5]/span/a/text()').extract()
            item['icons'] = node.xpath('./div/div[6]/i/text()').extract()
            item['link'] = "https:" + node.xpath('./div/div[1]/a/@href').extract()[0]
            # print(item)
            yield scrapy.Request(item['link'], callback=self.parse_pro_detail)

    def parse_pro_detail(self,response):
        item = JingdongItem()
        item['has_pro'] = response.xpath('//*[@id="store-prompt"]/strong/text()').extract()
        item['weight'] = response.xpath('//*[@id="summary-weight"]/div[2]/text()').extract()
        item['brand'] = response.xpath('//*[@id="parameter-brand"]/li/a/text()').extract()
        item['ram'] = response.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[4]/text()').extract()
        item['series'] = response.xpath('//*[@id="detail"]/div[2]/div[2]/div[1]/div[1]/dl/dl[2]/dd/text()').extract()
        item['disk'] = response.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[9]/text()').extract()
        item['cpu'] = response.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[12]/text()').extract()
        item['category'] = response.xpath('//*[@id="detail"]/div[2]/div[1]/div[1]/ul[2]/li[15]/text()').extract()
        print(item)

#         //*[@id="store-prompt"]/strong

