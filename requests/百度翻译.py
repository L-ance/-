# 百度翻译爬取
import requests

words = input('请输入你要翻译的内容:')
data = {
    'from': 'zh',
    'to': 'en',
    'query': words,
    'transtype': 'translang',
    'simple_means_flag': '3'
}
# 由于百度的限制,需要加一个头部信息,来伪装成用浏览器访问的
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"
}

url = 'https://fanyi.baidu.com/basetrans'

# 将网址,请求包,以及头部信息传入requests模块,并以post请求方式发送请求.
result = requests.post(url, data=data, headers=headers)
# 粗暴的打印全部结果
print(result.text)
print(result.json()['trans'][0]['dst'])
