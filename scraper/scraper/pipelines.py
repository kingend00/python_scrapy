# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#import mysql.connector

class ScraperPipeline(object):

    def process_item(self,item,spider):
        print('Pipeline: '+ item['title'][0])
        return item
    # def __init__(self):
    #     self.create_connection()
    #     self.create_table()
    
    # def create_connection(self):
    #     self.conn = mysql.connector.connect(
    #         host = 'localhost',
    #         user = 'hoangx',
    #         passwd = 'Hoang_01',
    #         database = 'python_scrapy'
    #     )
    #     self.curr = self.conn.cursor()
    
    # def create_table(self):
    #     self.curr.execute(""" DROP TABLE IF EXISTS jokes """)
    #     self.curr.execute(""" create table jokes(
    #                     question text,
    #                     answer text
    #                     ) """)

    # def process_item(self,item,spider):
    #     self.store_db(item)
    #     return item

    # def store_db(self,item):
    #     self.curr.execute(""" insert into jokes values (%s,%s) """,(
    #         item['question'][0],
    #         item['answer'][1],
    #     ))
    #     self.conn.commit() 

