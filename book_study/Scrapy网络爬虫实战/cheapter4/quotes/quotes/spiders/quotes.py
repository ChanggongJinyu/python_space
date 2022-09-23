import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class Quotes(CrawlSpider):
    name = "quotes" # 爬虫名称
    allow_domain = 'quotes.toscrape.com'
    start_urls = ['http://quotes.toscrape.com/']

    # 定义抽取链接的规则
    rules = (
        # 对于quotes内容页URL，调用parse_quotes处理，并以此规则跟进获取的链接
        # <a href="/page/2/">Next <span aria-hidden="true">→</span></a>
        # "下一页"链接
        # follow = True: 表示跟进Response返回的所有符合规则的链接
        # LinkExtractor: 提取链接
        Rule(LinkExtractor(allow='/page/\d+'),callback='parse_quotes',follow=True),
        # 对于author内容页URL，调用parse_author处理，提取数据
        # <a href="/author/Steve-Martin">(about)</a>
        Rule(LinkExtractor(allow='/author/\w+'),callback='parse_author')
    )

    # 提取内容页数据方法
    def parse_quotes(self,response):
        # response.css(".quote")
        # 返回所有class属性值为'quote'的标签列表
        # 列表元素示例:
        # <Selector xpath="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>
        for quote in response.css(".quote"):
            yield {
                # .text 返回所有class属性值为'text'的标签列表
                # ::text将获取标签的文本
                # quote.css('.text::text')
                # [<Selector xpath="descendant-or-self::*[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“The world as we have created it is a...'>]
                # quote.css('.text::text').extract_first()
                # '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
                # extract_first() 返回第一个值
                # extract() 返回列表
                'content': quote.css('.text::text').extract_first(),
                # 'Albert Einstein'
                'author': quote.css('.author::text').extract_first(),
                # ['change', 'deep-thoughts', 'thinking', 'world']
                'tags': quote.css('.tag::text').extract()
            }

    # 获取作者数据方法
    def parse_author(self,response):
        name = response.css('.author-title::text').extract_first()
        author_born_date = response.css('.author-born-date::text').extract_first()
        author_born_location = response.css('.author-born-location::text').extract_first()
        author_description = response.css('.author-description::text').extract_first()

        return ({
            'name': name,
            'author_born_data': author_born_date,
            'author_born_location': author_born_location,
            'author_born_description': author_description
        })