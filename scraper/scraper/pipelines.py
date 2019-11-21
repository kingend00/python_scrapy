# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#import mysql.connector

import mysql.connector

class ScraperPipeline(object):

    # def process_item(self,item,spider):
    #     print('Pipeline: '+ item['title'][0])
    #     return item
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'root',
            database = 'python_scrapy'
        )
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS myquotes """)
        self.curr.execute(""" create table myquotes(
                        title text,
                        author text,
                        tag text
                        ) """)

    def process_item(self,item,spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr.execute(""" insert into myquotes values (%s,%s,%s) """,(
            item['title'][0],
            item['author'][0],
            item['tag'][0],
        ))
        self.conn.commit() 

