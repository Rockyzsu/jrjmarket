# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
from scrapy import cmdline
import tushare as ts
import redis
from jrjmarket.settings import REDIS_HOST
def fetch_stock():
    sb_df = ts.get_stock_basics()
    code_list = list(sb_df.index)
    r = redis.StrictRedis(REDIS_HOST,db=0)
    r.flushdb()
    for code in code_list:
        r.lpush('code',code)


fetch_stock()
name = 'jrj'
cmd = 'scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())
print 'done'
