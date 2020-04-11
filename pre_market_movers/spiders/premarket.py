# -*- coding: utf-8 -*-
import scrapy


class PremarketSpider(scrapy.Spider):
    name = 'premarket'
    allowed_domains = ['money.cnn.com']
    start_urls = ['http://money.cnn.com/data/premarket/']

    def parse(self, response):
        for row in response.css('div.wsod_marketMovers table tr')[1:]:
            yield self.row_to_dict(row)

    def row_to_dict(self, row):
        return {
            'symbol': row.css('a.wsod_symbol::text').get(),
            'company': row.css('td.wsod_firstCol span::text').get(),
            'price': row.css('td::text')[0].get(),
            'change': row.css('td')[2].css('span::text').get(),
            'volumne': row.css('td::text')[1].get(),
        }
