import os

import requests
from lxml import etree

url = 'https://www.mzitu.com/xinggan/page/2/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
proxies = {
    "https": "http://218.60.8.99:3129",
    # "http": "125.74.14.38:80"
}

page_text = requests.get(url=url, headers=headers, proxies=proxies).text
tree = etree.HTML(page_text)
img_src_list = tree.xpath("//ul[@id='pins']/li/a/img/@data-original")
print(len(img_src_list))
print(img_src_list)
for img_src in img_src_list:
    print(img_src)
    name = img_src.rsplit('/', 1)[-1]
    file_path = os.path.join('meizitu', name)
    res = requests.get(url=img_src,headers=headers).content
    print(res)
    # https://i.meizitu.net/2018/11/26b02.jpg
    with open(file_path, 'wb')as fp:
        fp.write(res)
        break
print('下载完成')
