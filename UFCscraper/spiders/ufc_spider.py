import scrapy
import string
from ..items import UfcscraperItem

class FigherSpider(scrapy.Spider):

    name = 'fighters'

    def start_requests(self):
        start_urls = ['http://www.ufcstats.com/statistics/fighters?char=' + char + '&page=all' for char in string.ascii_lowercase]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # get the fighter links
        links = response.css('tr.b-statistics__table-row td.b-statistics__table-col a::attr(href)').extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_fighter)

    def parse_fighter(self, response):
        items = UfcscraperItem()


        items['name'] = response.xpath('/html/body/section/div/h2/span[1]/text()').get().strip()
        items['nick_name'] = response.css(".b-content__Nickname::text").get().strip()
        items['height'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[1].get().strip()
        items['weight'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[3].extract().strip()
        items['reach'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[5].get().strip()
        items['stance'] = response.css(".b-list__info-box_style_small-width :nth-child(4)::text")[1].get().strip()
        items['date_birth'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[9].get().strip()
        items['record'] = response.css(".b-content__title-record::text").get().strip()
        items['SLpm'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[11].get().strip()
        items['StrAcc'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[13].get().strip()
        items['SApm'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[15].get().strip()
        items['StrDef'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[17].get().strip()
        items['TDavg'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[21].get().strip()
        items['TDacc']= response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[23].get().strip()
        items['TDdef'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[25].get().strip()
        items['SubAvg'] = response.css('li.b-list__box-list-item.b-list__box-list-item_type_block::text')[27].get().strip()



        yield items

