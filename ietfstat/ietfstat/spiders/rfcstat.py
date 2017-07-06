# -*- coding: utf-8 -*-
import scrapy
import re

class RfcstatSpider(scrapy.Spider):
    name = 'rfcstat'
    allowed_domains = ['https://tools.ietf.org/rfc/index']
    start_urls = ['http://https://tools.ietf.org/rfc/index/']

	#def start_requests(self):
		#urls= re.findall(scrapy.Request( url=start_urls[0])
	
    def parse(self, response):
        pass
