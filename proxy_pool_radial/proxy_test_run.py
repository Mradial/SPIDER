from  proxy_test_aiohttp import  Test_Proxy
from redis_db import RedisClient


tester=Test_Proxy()


if __name__=="__main__":
    tester.run()