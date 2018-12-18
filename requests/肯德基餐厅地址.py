import requests

page = input('请输入页码')
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
data = {
    'cname': '',
    'pid': '',
    'keyword': '北京',
    'pageIndex': page,
    'pageSize': '10'
}

proxies = {
    "https": "http://218.60.8.99:3129"
}

res = requests.post(url=url, data=data, headers=headers, proxies=proxies)
print(res.json())