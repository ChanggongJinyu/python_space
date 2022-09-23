import scrapy
from downloadimage.items import DownloadimageItem


class GetimageSpider(scrapy.Spider):
    name = 'getimage'
    allowed_domains = ['qidian.com']
    start_urls = ['https://qidian.com/finish/']
    # qidian_headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    #     'cookie': '_yep_uuid=e76682fb-90d0-eec8-0387-2836bdfa45b5; e1=%7B%22pid%22%3A%22qd_P_fin%22%2C%22eid%22%3A%22qd_A18%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A17%22%2C%22l1%22%3A3%7D; _csrfToken=LMI8qLgAwmaSKjpdqBDDDKbfeczqVpF6ybAAFIXm; newstatisticUUID=1651913867_1702172988; fu=1968582928; _yep_uuid=70ba6c20-d3d4-2b1a-2086-29fb0e3181b2; _gid=GA1.2.1732907558.1652010707; _gat_gtag_UA_199934072_2=1; e1=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A17%22%2C%22l1%22%3A3%7D; e2=%7B%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A71%22%2C%22l1%22%3A3%7D; _ga_FZMMH98S83=GS1.1.1652009430.2.1.1652011201.0; _ga_PFYW0QLV3P=GS1.1.1652009430.2.1.1652011201.0; _ga=GA1.2.163360949.1651913863',
    #     'Referer': 'https://www.qidian.com/'
    # }
    #
    # def start_requests(self):
    #     for u in self.start_urls:
    #         yield scrapy.Request(u,
    #                              meta={
    #                                  'dont_redirect' : True,
    #                                  'handle_httpstatus_list': [302,301]
    #                              },
    #                              callback=self.parse,
    #                              headers=self.qidian_headers)

    def parse(self, response):
        for novel in response.css(".all-img-list > li"):
            # > li : 表示选择li子标签
            item = DownloadimageItem()
            # item['title'] = novel.xpath('.//h4/a/text()').extract_first()
            item['title'] = novel.xpath('.//h2/a/text()').extract_first()
            # //*[@id="book-img-text"]/ul/li[1]/div[2]/h2/a
            item['author'] = novel.css('.name::text').extract_first()
            item['type'] = novel.css('em + a::text').extract_first()
            item['image_urls'] = ['https:' + novel.xpath('.//img/@src').extract_first()]
            yield item