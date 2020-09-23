# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class UfcscraperPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect("../ufcfights.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS fighters_tb""")
        self.curr.execute("""CREATE TABLE fighters_tb(
                         name text,
                         nick_name text,
                         height text,
                         weight text,
                         reach text,
                         stance text,
                         date_birth text,
                         record text,
                         SLpm text,
                         StrAcc text,
                         SApm text,
                         StrDef text,
                         TDavg text,
                         TDacc text,
                         TDdef text,
                         SubAvg text
                         )
                            """)
    def store_db(self,item):

        self.curr.execute("""INSERT INTO fighters_tb VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
            item['name'], item['nick_name'], item['height'], item['weight'], item['reach'],
            item['stance'],item['date_birth'],item['record'], item['SLpm'], item['StrAcc'],
            item['SApm'], item['StrDef'], item['TDavg'], item['TDacc'], item['TDdef'], item['SubAvg']))

        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)

        return item

