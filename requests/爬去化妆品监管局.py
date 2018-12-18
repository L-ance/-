import requests

page = input("输入查询的页数")
page_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
detail_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

proxies = {
    "https": "http://218.60.8.99:3129"
}
data = {
    'on': 'true',
    'page': page,
    'pageSize': '15',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': '',
}
res = requests.post(url=page_url, data=data, headers=headers, proxies=proxies)
msg_list = res.json()['list']
for msg in msg_list:
    print(msg['ID'])
    detail_data = {
        'id': msg['ID']
    }
    detail_res = requests.post(url=detail_url, data=detail_data, headers=headers, proxies=proxies)
    print(detail_res.json())
