import scrapy
from scraper.items import ScraperItem
from scrapy.loader import ItemLoader

class JokesSpider(scrapy.Spider):
    name="jokes"
    start_urls=['http://www.laughfactory.com/jokes/family-jokes']

    def parse(self,response):
        for joke in response.xpath("//div[@class='jokes']"):
            l=ItemLoader(item=ScraperItem(),selector=joke)
            l.add_xpath('joke_text',".//div[@class='joke-text']/p")
            # yield {
            #     'joke_text': joke.xpath(".//div[@class='joke-text']/p").extract_first()
            # }
            yield l.load_item()
        
        next_page=response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page_link=response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link,callback=self.parse)

        #check username git 