from redis_db import RedisClient
from setting import TEST_URL
import requests

class Test_Proxy():
    def __init__(self):
        self.db=RedisClient()

    def proxy_test(self, proxy):
        url = TEST_URL
        proxies={
            "http":proxy,
            "https":proxy
        }
        # print("{}(测试中)".format(proxy))
        try:
            r = requests.get(url, proxies=proxies, timeout=5)
            if r.status_code ==200:
                # print("{}(可用)".format(proxy))
                self.db.max(proxy)
        except requests.exceptions.ConnectionError:
            self.db.decrease(proxy)
            # print("{}(减一)".format(proxy))

