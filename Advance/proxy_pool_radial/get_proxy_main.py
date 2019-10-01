import sys
from  get_proxy_source import  GetProxy
from redis_db import RedisClient
from setting import  *

class Getter():
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = GetProxy()

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            # for callback_label in range(self.crawler.__CrawlFuncCount__):
            #             #     callback = self.crawler.__CrawlFunc__[callback_label]
                # 获取代理
            # proxies = self.crawler.yun_proxy()
            # 强制刷新缓冲区
            sys.stdout.flush()
            for proxy in self.crawler.yun_proxy():
                self.redis.add(proxy)
            sys.stdout.flush()
            for proxy in self.crawler.xici_proxy():
                self.redis.add(proxy)
            sys.stdout.flush()
            for proxy in self.crawler.kuai_proxy():
                self.redis.add(proxy)
            sys.stdout.flush()
            for proxy in self.crawler.ip89_proxy():
                self.redis.add(proxy)
            sys.stdout.flush()