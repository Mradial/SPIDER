from mitmproxy import http
from urllib import parse
from pymongo import MongoClient

mongo= MongoClient('mongodb://localhost:27017')
db=mongo['python_book_five']
collection=db['cloudmusic']
## 文档实例
# def request(flow: http.HTTPFlow):
#     # redirect to different host
#     if flow.request.pretty_host == "httpbin.org":
#         flow.request.host = "mitmproxy.org"
#     # answer from proxy
#     elif flow.request.path.endswith("/brew"):
#     	flow.response = http.HTTPResponse.make(
#             418, b"I'm a teapot")

## 网易云音乐视频解析
# ur_='http://vodkgeyttp8.vod.126.net/cloudmusic/d2bde7a81f3ac83e7ebf87a6fac18c99.mp4?wsSecret=a7d8e9ace90ab897c36b6da47265627e&wsTime=1534817347'
# url='http%3A%2F%2Fvodkgeyttp8.vod.126.net%2Fcloudmusic%2FsIu4p7yy_1521323706_hd.mp4%3FwsSecret%3D466083a139b312483f6d039c1786c7b3%26wsTime%3D1534817626'
# a={
#     "/":'%2F',
#     ":":"%3A",
#     "?":"%3F",
#     "=":"%3D",
#     "&":"%26"
# }
# 'http://vodkgeyttp8.vod.126.net/cloudmusic/sIu4p7yy_1521323706_hd.mp4?wsSecret=466083a139b312483f6d039c1786c7b3&wsTime=1534817626'
# now=url.replace("%2F","/",5).replace("%3A",":").replace("%3F","?").replace("%3D","=").replace("%26","&")
# orgin_url="http://127.0.0.1:61323/video?id=E1E660DC91DE0CA824CD696FF85AC55E&bitrate=480&length=15538041&type=video&videoUrl=http%3A%2F%2Fvodkgeyttp8.vod.126.net%2Fvodkgeyttp8%2FXwInCNA4_126855167_hd.mp4%3FwsSecret%3Dd2d823abffe1a8c3b9f5883354daa7ef%26wsTime%3D1534851427&preLoadlength=1048576"
# print(len(orgin_url))
def to_url(url):
    result = parse.parse_qs(url)["videoUrl"][0].replace("%2F","/",5).replace("%3A",":").replace("%3F","?").replace("%3D","=").replace("%26","&")
    return  result

## 测试文件
def request(flow:http.HTTPFlow):
    global collection
    url = "http://127.0.0.1"
    if flow.request.url.startswith(url):
        soup=to_url(flow.request.url)
        collection.insert({"url":soup})
