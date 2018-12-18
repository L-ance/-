import re
from lxml import etree
import requests
from requests.exceptions import RequestException


def get_one_page(url, headers):
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(page_text):
    tree = etree.HTML(page_text)
    dd_movie_list = tree.xpath("/html/body/div[@id='app']/div[@class='content']/div[@class='wrapper']/div/dl/dd")
    movie_list = []
    # print(dd_movie_list)
    for movie in dd_movie_list:
        title = movie.xpath("./a/@title")[0]
        # print(title)
        img_src = movie.xpath("./a/img[2]/@data-src")[0]
        actor = movie.xpath("./div//p[2]/text()")[0].strip()
        time = movie.xpath("./div//p[3]/text()")[0]
        # print(time)
        integer = movie.xpath("./div//i[@class='integer']")[0]
        fraction = movie.xpath("./div//i[@class='fraction']")[0]
        # print(integer)
        # print(fraction)
        one_list = [title, img_src, actor, time]
        movie_list.append(one_list)
    print(movie_list)

def main():
    url = 'https://maoyan.com/board/4?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    proxies = {
        "https": "http://218.60.8.99:3129",
        # "http": "125.74.14.38:80"
    }
    page_text = get_one_page(url, headers)
    # print(html)
    parse_one_page(page_text)


if __name__ == '__main__':
    main()
