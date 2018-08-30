# from multiprocessing import freeze_support,Pool
from pymongo import MongoClient
from redis_db import RedisClient

mongo = MongoClient('mongodb://localhost:27017')
db = mongo['python_book_five']
collection = db['spider_proxy']
# redis数据库对象实例化
client=RedisClient()
# 遍历mongo数据库，提取并保存到redis数据库
for i in collection.find():
    class_ip_port="{}:{}".format(i["ip"],i["port"])
    client.add(class_ip_port)

