import scrapy
from ..items import FightscraperItem

class FightsSpider(scrapy.Spider):
    name = 'fights'

    def start_requests(self):
        start_urls = ['http://www.ufcstats.com/statistics/events/completed?page=all']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        links = response.css('tr.b-statistics__table-row td.b-statistics__table-col a::attr(href)').extract()
        for link in links:
            yield scrapy.Request(url=link,callback = self.parse_fights)

    def parse_fights(self,response):

        links = response.css("tr::attr(data-link)").extract()
        for link in links:
            yield scrapy.Request(url=link,callback=self.parse_match)

    def parse_match(self,response):
        items = FightscraperItem()

        fighter1data = response.css(".b-fight-details__person")[0]
        fighter2data = response.css(".b-fight-details__person")[1]

        items['fight_name'] = response.css("h2.b-content__title a::text").get().strip()

        items['fighter1_name'] = fighter1data.css("a::text").get().strip()
        items['fighter2_name'] = fighter2data.css("a::text").get().strip()

        items['fighter1_outcome'] = fighter1data.css("i::text").get().strip()
        items['fighter2_outcome'] = fighter2data.css("i::text").get().strip()

        items['weight_bout'] = response.css(".b-fight-details__fight-title ::text")[0].extract().strip()
        items['method'] = response.css(".b-fight-details__text-item_first i:nth-child(2)::text").get().strip()
        items['num_rounds'] = response.css(".b-fight-details__text-item:nth-child(2)::text")[1].extract().strip()
        items['details'] = response.css(".b-fight-details__text:nth-child(2)::text")[1].extract().strip()
        items['time'] = response.css(".b-fight-details__text-item:nth-child(3)::text")[1].extract().strip()
        items['referee'] = response.css(".b-fight-details__text-item:nth-child(5) span ::text").get().strip()

        #TOTALS
        items['kd_1'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[2]/p[1]/text()').get().strip()
        items['kd_2'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[2]/p[2]/text()').get().strip()
        items['sig_str_1'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[3]/p[1]/text()').get().strip()
        items['sig_str_2'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[3]/p[2]/text()').get().strip()
        items['sig_str_pct_1'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[4]/p[1]/text()').get().strip()
        items['sig_str_pct_2'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[4]/p[2]/text()').get().strip()
        items['total_str_1'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[1]/text()').get().strip()
        items['total_str_2'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[5]/p[2]/text()').get().strip()
        items['td_1'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[1]/text()').get().strip()
        items['td_2'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[6]/p[2]/text()').get().strip()
        items['td_pct_1'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[7]/p[1]/text()').get().strip()
        items['td_pct_2'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[7]/p[2]/text()').get().strip()
        items['sub_att_1'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[1]/text()').get().strip()
        items['sub_att_2'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[8]/p[2]/text()').get().strip()
        items['pass_1'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[9]/p[1]/text()').get().strip()
        items['pass_2'] = response.xpath(
            '//html/body/section/div/div/section[2]/table/tbody/tr/td[9]/p[2]/text()').get().strip()

        #SIGNIFICANT STRIKES
        items['head_1'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[4]/p[1]/text()').get().strip()
        items['head_2'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[4]/p[2]/text()').get().strip()
        items['body_1'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[5]/p[1]/text()').get().strip()
        items['body_2'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[5]/p[2]/text()').get().strip()
        items['leg_1'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[6]/p[1]/text()').get().strip()
        items['leg_2'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[6]/p[2]/text()').get().strip()
        items['distance_1'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[7]/p[1]/text()').get().strip()
        items['distance_2'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[7]/p[2]/text()').get().strip()
        items['clinch_1'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[8]/p[1]/text()').get().strip()
        items['clinch_2'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[8]/p[2]/text()').get().strip()
        items['ground_1'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[9]/p[1]/text()').get().strip()
        items['ground_2'] = response.xpath(
            '//html/body/section/div/div/table/tbody/tr/td[9]/p[2]/text()').get().strip()

        yield items







