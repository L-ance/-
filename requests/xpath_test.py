from lxml import etree
import requests
import os

url = 'http://www.haoduanzi.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
proxies = {
    # "https": "http://218.60.8.99:3129",
    "http": "125.74.14.38:80"
}
page_text = requests.get(url=url, headers=headers, proxies=proxies).text
tree = etree.HTML(page_text)
div_list = tree.xpath('//div[@id="main"]/div')[2:-1]
for div in div_list:
    img_url = div.xpath('./div/img/@src')[0]

    # http://www.haoduanzi.com/uploads/201743/6846134S35108-0.jpg
    filename = img_url.rsplit('/', 1)[-1]
    file_path = os.path.join('haoduanzi', filename)
    res = requests.get(url=img_url, headers=headers, proxies=proxies).content
    with open(file_path, 'wb')as fp:
        fp.write(res)
print('下载成功')
