# -*- coding: utf-8 -*-
import scrapy
from jrjmarket.items import JrjmarketItem
import redis
from jrjmarket.settings import REDIS_HOST


class JrjSpider(scrapy.Spider):
    name = 'jrj'
    allowed_domains = ['jrj.com.cn']


    def __init__(self):
        self.r = redis.StrictRedis(REDIS_HOST, db=0,decode_responses=True)
        self.link = 'http://stock.jrj.com.cn/share,{},gsgk.shtml'

    def start_requests(self):

        for _ in range(self.r.llen('code')):
            code = self.r.lpop('code')
            yield scrapy.Request(url=self.link.format(code), meta={'code': code})

    def parse(self, response):
        details = response.xpath('//table[@class="tab2"]/tbody/tr')
        item = JrjmarketItem()

        columns = [
            # '_id',
            'Company_name',
            'English_name',
            'Former_name',
            'Built_date',
            'Business_registration',
            'Registered_capital',
            'Legal_representative',
            'Industry_classification_CSRC',
            'Global_Industry_Classification',
            'ShenWan_industry_classification',
            'Employee_Count',
            'General_Manager',
            'Board_Secretary',
            'Securities_representative',
            'Register_location',
            'Working_place',
            'Zip_Code',
            'Tel',
            'Fax',
            'Website',
            'MailBox',
            'Information_discloser',
            'Chartered_accountant',
            'Lawer',
            'Evaluator',
            'Accounting_firm',
            'Law_office',
            'Assets_evaluation_organization',
            'Compay_detail',
            'Main_Business',
        ]

        item['_id'] = response.meta['code']
        # item['Comanpy_name'] = Comanpy_name
        # item['English_name'] = English_name
        # item['Built_date'] = Built_date
        # item['Registered_capital'] = Registered_capital
        # item['Legal_representative'] = Legal_representative
        # item['Industry_classification_CSRC'] = Industry_classification_CSRC
        # item['Global_Industry_Classification'] = Global_Industry_Classification
        # item['ShenWan_industry_classification'] = ShenWan_industry_classification
        # item['Employee_Count'] = Employee_Count
        # item['General_Manager'] = General_Manager
        # item['Board_Secretary'] = Board_Secretary
        # item['securities_representative'] = securities_representative
        # item['Register_location'] = Register_location
        # item['Working_place'] = Working_place
        # item['Website'] = Website
        # item['Accounting_firm'] = Accounting_firm
        # item['Law_office'] = Law_office
        # item['Compay_detail'] = Compay_detail
        # item['Main_Operation'] = Main_Operation
        # item['Business_registration'] = Business_registration

        for index, detail in enumerate(details):
            item[columns[index]] = detail.xpath('.//td/text()').extract()[0].strip()

        yield item
