# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JrjmarketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    _id = scrapy.Field()
    Comanpy_name = scrapy.Field()
    English_name = scrapy.Field()
    Former_name = scrapy.Field()
    Built_date = scrapy.Field()
    Business_registration = scrapy.Field()
    Registered_capital = scrapy.Field()
    Legal_representative = scrapy.Field()
    Industry_classification_CSRC = scrapy.Field()
    Global_Industry_Classification = scrapy.Field()
    ShenWan_industry_classification = scrapy.Field()
    Employee_Count = scrapy.Field()
    General_Manager = scrapy.Field()
    Board_Secretary = scrapy.Field()
    Securities_representative = scrapy.Field()
    Register_location = scrapy.Field()
    Working_place = scrapy.Field()
    Zip_Code=scrapy.Field()
    Tel=scrapy.Field()
    Fax=scrapy.Field()
    Website = scrapy.Field()
    MailBox = scrapy.Field()
    Accounting_firm = scrapy.Field()
    Law_office = scrapy.Field()
    Compay_detail = scrapy.Field()
    Main_Business = scrapy.Field()
    Assets_evaluation_organization = scrapy.Field()
    Chartered_accountant = scrapy.Field()
    Information_discloser = scrapy.Field()
    Lawer = scrapy.Field()
    Evaluator = scrapy.Field()
