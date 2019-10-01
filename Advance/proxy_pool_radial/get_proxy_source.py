
from lxml import etree
import re
# from proxy_pool_redial.redis_db import RedisClient
from  get_html import  get_page


class GetProxy():

    # #返回所有的解析方法
    # def  method(self):
    #     pool=["kuai_proxu()","yun_proxy()","xici_proxy()","ip89_proxy()"]
    #     return  pool

    # 快代理
    # 发布页多，获取30页内容
    def kuai_proxy(self,page=31):
        root_url = "https://www.kuaidaili.com/free/inha/{}/"
        try:
            for i in range(1, page):
                soup = get_page(root_url.format(i))
                html = etree.HTML(soup)
                trs = html.xpath('//tbody/tr')
                for j in trs:
                    ip_proxy = j.xpath("./td[1]/text()")[0] + r":" + j.xpath("./td[2]/text()")[0]
                    yield ip_proxy
        except:
            return "出现错误"

    #云代理
    # 发布页较少，获取5页内容
    def yun_proxy(self,page=6):
        yun_url = "http://www.ip3366.net/?page={}"
        try:
            for i in range(1,page):
                soup = get_page(yun_url.format(i))
                html = etree.HTML(soup)
                trs = html.xpath('//tbody/tr')
                for j in trs:
                    ip_proxy = j.xpath("./td[1]/text()")[0] + r":" + j.xpath("./td[2]/text()")[0]
                    yield ip_proxy
        except:
            return "出现错误"

    # 西刺代理
    ## 发布页多，获取30页内容，友好访问
    def xici_proxy(self,page=31):
        xici_url = "http://www.xicidaili.com/nn/{}"
        try:
            for i in range(1, page):
                soup = get_page(xici_url.format(i))
                html = etree.HTML(soup)
                trs = html.xpath('//tr[@class=""or"odd"]')
                for j in trs:
                    if len(j.xpath("./td[2]/text()")) == 0:
                        pass
                    else:
                        ip_proxy = j.xpath("./td[2]/text()")[0] + r":" + j.xpath("./td[3]/text()")[0]
                yield  ip_proxy
        except:
            return "出现错误"

    # 89ip免费代理
    # 发布页较少，获取5页内容
    def ip89_proxy(self,page=6):
        ip89_url = "http://www.89ip.cn/index_{}.html"
        try:
            find_ip = re.compile('\d+\.\d+\.\d+\.\d+', re.S)
            find_port = re.compile('\d+', re.S)
            for i in range(1, page):
                soup = get_page(ip89_url.format(i))
                html = etree.HTML(soup)
                trs = html.xpath('//tbody/tr')
                for j in trs:
                    ip_proxy = find_ip.findall(j.xpath("./td[1]/text()")[0])[0] + r":" + find_port.findall(j.xpath("./td[2]/text()")[0])[0]
                    yield ip_proxy
        except:
            return "出现错误"

# 简单运行测试
if __name__ == '__main__':
    getter = GetProxy()
    result = getter.yun_proxy()
    for i in  result:
        print(i)