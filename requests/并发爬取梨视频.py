import requests
from lxml import etree
import os
import re
import time
from multiprocessing.dummy import Pool
from uuid import uuid4


def download_video(data):
    name = str(uuid4())
    file_path = os.path.join('livideo', name)
    with open(file_path + '.mp4', 'wb') as fp:
        fp.write(data)
        print(name + '下载完成')


pool = Pool(processes=5)

start = time.time()
url = 'https://www.pearvideo.com/category_10'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
proxies = {
    # "https": "http://218.60.8.99:3129",
    "http": "125.74.14.38:80"
}
page_text = requests.get(url=url, headers=headers, proxies=proxies).text
# page.encoding = 'utf-8'
tree = etree.HTML(page_text)
li_tag_list = tree.xpath("//div[@id='listvideoList']/ul/li")
detail_url_list = []
for li_tag in li_tag_list:
    video_url = "https://www.pearvideo.com/" + li_tag.xpath('./div/a/@href')[0]
    video_title = li_tag.xpath('./div/a/div/text()')[-1]
    video_detail_text = requests.get(url=video_url, headers=headers, proxies=proxies).text
    exp = 'srcUrl="(.*?)"'
    detail_url = re.findall(exp, video_detail_text, re.S)[0]
    print(detail_url)
    detail_url_list.append(detail_url)
    # print(detail_url)
    """
    var contId="1489850",liveStatusUrl="liveStatus.jsp",liveSta="",playSta="1",autoPlay=!1,
    isLiving=!1,isVrVideo=!1,hdflvUrl="",sdflvUrl="",hdUrl="",sdUrl="",ldUrl="",
    srcUrl="https://video.pearvideo.com/mp4/adshort/20181211/cont-1489850-13348219_adpkg-ad_hd.mp4",
    vdoUrl=srcUrl,skinRes="//www.pearvideo.com/domain/skin",videoCDN="//video.pearvideo.com";
    """
video_data_list = pool.map(lambda link: requests.get(url=link, headers=headers, proxies=proxies).content,
                           detail_url_list)
# video_data = requests.get(url=detail_url, headers=headers, proxies=proxies).content
print(video_data_list)
pool.map(download_video, video_data_list)
pool.close()
pool.join()
end = time.time()
print(time.localtime(end - start))
