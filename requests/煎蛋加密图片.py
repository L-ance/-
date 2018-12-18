from lxml import etree
import requests
import base64

url = 'http://jandan.net/ooxx/page-%s#comments'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
proxies = {
    # "https": "http://218.60.8.99:3129",
    "http": "125.74.14.38:80"
}
page = input("Please enter page number")
page_url = url % page
print(page_url)
page_text = requests.get(url=page_url, headers=headers, proxies=proxies).text
tree = etree.HTML(page_text)
img_code_lst = tree.xpath('//span[@class="img-hash"]/text()')
for img_code in img_code_lst:
    image_url = "http://" + base64.b64decode(img_code).decode()
    print(image_url)
