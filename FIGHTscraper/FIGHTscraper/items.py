# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FightscraperItem(scrapy.Item):
    # define the fields for your item here like:
    fighter1_name = scrapy.Field()
    fighter2_name = scrapy.Field()
    fight_name = scrapy.Field()
    fighter1_outcome = scrapy.Field()
    fighter2_outcome = scrapy.Field()
    weight_bout = scrapy.Field()
    method = scrapy.Field()
    num_rounds = scrapy.Field()
    details = scrapy.Field()
    time = scrapy.Field()
    referee = scrapy.Field()

    kd_1 = scrapy.Field()
    kd_2 = scrapy.Field()
    sig_str_1 = scrapy.Field()
    sig_str_2 = scrapy.Field()
    sig_str_pct_1 = scrapy.Field()
    sig_str_pct_2 = scrapy.Field()
    total_str_1 = scrapy.Field()
    total_str_2 = scrapy.Field()
    td_1 = scrapy.Field()
    td_2 = scrapy.Field()
    td_pct_1 = scrapy.Field()
    td_pct_2 = scrapy.Field()
    sub_att_1 = scrapy.Field()
    sub_att_2 = scrapy.Field()
    pass_1 = scrapy.Field()
    pass_2 = scrapy.Field()

    head_1 = scrapy.Field()
    head_2 = scrapy.Field()
    body_1 = scrapy.Field()
    body_2 = scrapy.Field()
    leg_1 = scrapy.Field()
    leg_2 = scrapy.Field()
    distance_1 = scrapy.Field()
    distance_2 = scrapy.Field()
    clinch_1 = scrapy.Field()
    clinch_2 = scrapy.Field()
    ground_1 = scrapy.Field()
    ground_2 = scrapy.Field()





