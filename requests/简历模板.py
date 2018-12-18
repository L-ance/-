from lxml import etree
import requests
import os
import random

url = 'http://sc.chinaz.com/jianli/free_%s.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
proxies = {
    # "https": "http://218.60.8.99:3129",
    "http": "125.74.14.38:80"
}
for i in range(1, 2):
    if i == 1:
        page_text = requests.get(url='http://sc.chinaz.com/jianli/free.html', headers=headers, proxies=proxies)
    else:
        page_url = url % i
        page_text = requests.get(url=page_url, headers=headers, proxies=proxies)
    page_text.encoding = 'utf-8'
    page_text = page_text.text
    tree = etree.HTML(page_text)
    msg_list = tree.xpath('//div[@id="container"]/div/p')
    for msg in msg_list:
        title = msg.xpath('./a/text()')[0]
        detail_url = msg.xpath('./a/@href')[0]
        # print(detail_url)
        page_detail = requests.get(url=detail_url, headers=headers, proxies=proxies).text
        tree = etree.HTML(page_detail)
        down_url_list = tree.xpath('//div[@id="down"]/div/ul/li/a/@href')
        down_url = random.choice(down_url_list)
        # print(down_url)
        res = requests.get(url=down_url, headers=headers, proxies=proxies).content
        file_path = os.path.join('jianli', title)
        with open(file_path+'.rar', 'wb') as fp:
            fp.write(res)
            print(title + '下载完成')

