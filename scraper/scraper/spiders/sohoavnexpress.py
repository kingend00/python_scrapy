# -*- coding: utf8 -*-
import scrapy

class SohoaVnexpressNet(scrapy.Spider):
    name = "sohoa"
    start_urls = [
            'https://sohoa.vnexpress.net/tin-tuc/doi-song-so/tap-chi-co-chu-ky-steve-jobs-duoc-ban-gia-50-000-usd-3662652.html',
        ]


    def parse_artilce(self, response):
        artilce = {}
        artilce['title'] = response.xpath('//*[@id="col_sticky"]/h1/text()').extract_first()
        artilce['description'] = response.xpath('//*[@id="col_sticky"]/h2').extract_first()
        artilce['content'] = response.xpath('//*[@id="col_sticky"]/article').extract_first()
        artilce['author'] = response.xpath('//*[@id="col_sticky"]/article/p[5]/strong/text()').extract_first()
        artilce['publish_date'] = response.xpath('//*[@id="col_sticky"]/header/span/text()').extract_first()
        for key, text in artilce.iteritems():
            yield "{key}: {text}"