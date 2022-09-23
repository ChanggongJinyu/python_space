import scrapy


class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['163.com']
    start_urls = ['https://hr.163.com/job-list.html']

    def parse(self, response):
        print(response.text)
        node_list = response.xpath("//div[@class='content-base']")
        print(len(node_list))
        print(node_list)
