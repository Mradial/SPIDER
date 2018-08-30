# requests同步加载的方式简直是伤透了我的心啊，千里挑一，简直是千里雪飘啊！
import redis
from multiprocessing import freeze_support,Pool
import requests
import sys
sys.path.append("D:\RADIAL\STUDY\Python\Proxy_\proxy_pool_radial\setting.py")
from setting import REDIS_HOST,REDIS_PORT,REDIS_PASSWORD, MIN_SCORE, MAX_SCORE,REDIS_KEY

pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=13, password=REDIS_PASSWORD)
db = redis.Redis(connection_pool=pool, decode_responses=True)

def proxy_test(proxy):
    global  db
    url="http://httpbin.org/get"
    proxies={
        "http": proxy,
        "https": proxy
    }
    try:
        r = requests.get(url, proxies=proxies,timeout=20)
        if r.status_code==200:
            print("{}(可用)".format(proxy))
            db.zadd("proxy",proxy,100)
    except requests.exceptions.ConnectionError:
        print("{}(移除 )".format(proxy))
        db.zrem("proxy",proxy)
if __name__=="__main__":
    # i=0
    # for proxy in db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE):
    #     i+=1
    #     proxy_=proxy.decode()
    #     print(proxy_)
    #     print(REDIS_KEY)
    #     print(db.zcard(REDIS_KEY))
    #     db.zrem(REDIS_KEY, proxy_)
    #     print(db.zcard(REDIS_KEY))
    #     if i==10:
    #         break
    freeze_support()
    p=Pool(30)
    for proxy in db.zrangebyscore(REDIS_KEY, MIN_SCORE, MAX_SCORE):
        proxy=proxy.decode()
        p.apply_async(proxy_test,args=(proxy,))
    p.close()
    p.join()




