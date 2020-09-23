# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class FightscraperPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect("../ufcfights.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS fight_tb""")
        self.curr.execute("""DROP TABLE IF EXISTS fight_stats_tb""")
        self.curr.execute("""CREATE TABLE fight_tb(
                        fight_name,
                        fighter1_name,
                        fighter2_name,
                        fighter1_outcome,
                        fighter2_outcome,
                        weight_bout,
                        method,
                        num_rounds,
                        details,
                        time,
                        referee
                         )
                            """)
        self.curr.execute("""CREATE TABLE fight_stats_tb(
                        fight_name,
                        fighter1_name,
                        fighter2_name,
                        kd_1,
                        kd_2,
                        sig_str_1,
                        sig_str_2,
                        sig_str_pct_1,
                        sig_str_pct_2,
                        total_str_1,
                        total_str_2,
                        td_1,
                        td_2,
                        td_pct_1,
                        td_pct_2,
                        sub_att_1,
                        sub_att_2,
                        pass_1,
                        pass_2,
                        head_1, 
                        head_2, 
                        body_1, 
                        body_2, 
                        leg_1,
                        leg_2,
                        distance_1,
                        distance_2, 
                        clinch_1, 
                        clinch_2, 
                        ground_1, 
                        ground_2                           
                        )
                        """)

    def store_db(self,item):

        self.curr.execute("""INSERT INTO fight_tb VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (
            item['fight_name'],
            item['fighter1_name'],
            item['fighter2_name'],
            item['fighter1_outcome'],
            item['fighter2_outcome'],
            item['weight_bout'],
            item['method'],
            item['num_rounds'],
            item['details'],
            item['time'],
            item['referee'])
                          )
        self.curr.execute("""INSERT INTO fight_stats_tb VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                                ?,?,?,?,?,?,?,?,?,?,?,?)""",(
                          item['fight_name'],
                          item['fighter1_name'],
                          item['fighter2_name'],
                          item['kd_1'],
                          item['kd_2'],
                          item['sig_str_1'],
                          item['sig_str_2'],
                          item['sig_str_pct_1'],
                          item['sig_str_pct_2'],
                          item['total_str_1'],
                          item['total_str_2'],
                          item['td_1'],
                          item['td_2'],
                          item['td_pct_1'],
                          item['td_pct_2'],
                          item['sub_att_1'],
                          item['sub_att_2'],
                          item['pass_1'],
                          item['pass_2'],
                          item['head_1'],
                          item['head_2'],
                          item['body_1'],
                          item['body_2'],
                          item['leg_1'],
                          item['leg_2'],
                          item['distance_1'],
                          item['distance_2'],
                          item['clinch_1'],
                          item['clinch_2'],
                          item['ground_1'],
                          item['ground_2']

                          ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)

        return item

