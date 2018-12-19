import os

import requests
from lxml import etree
from requests.exceptions import RequestException


def get_index(url, headers, proxies):
    """
    拿到响应对象
    :param url:
    :return: response.text  字符串类型
    """
    try:
        response = requests.get(url=url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return None


def get_img_src(page_text):
    """
    拿到图片的二进制数据
    :param page_text:
    :return:
    """
    tree = etree.HTML(page_text)
    img_src_list = tree.xpath("//ul[@id='pins']/li/a/img/@data-original")
    return img_src_list


def download_img(img_src_list, headers, proxies):
    """
    循环图片的列表,进行下载
    :param img_src_list:
    :param headers:
    :param proxies:
    :return:
    """
    headers[
        'referer'] = 'https://www.baidu.com/link?url=G3Kkwio1GSRjfgMGhZpDQZN8BC6B6q0Q8ig5yusim7GaqNOV80aVVK6oO_dD38BV&wd=&eqid=c42f8c880003d591000000035c199170'

    for img_src in img_src_list:
        name = img_src.rsplit('/', 1)[-1]
        file_path = os.path.join('meizitu', name)
        res = requests.get(url=img_src, headers=headers, proxies=proxies).content
        with open(file_path, 'wb')as fp:
            fp.write(res)
        # break


def main():
    url = 'https://www.mzitu.com/xinggan/page/3/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    proxies = {
        "https": "123.58.10.126:8080",
        # "http": "125.74.14.38:80"
    }
    page_text = get_index(url, headers, proxies)
    img_src_list = get_img_src(page_text)
    download_img(img_src_list, headers, proxies)


if __name__ == '__main__':
    main()
    print('爬虫结束')
