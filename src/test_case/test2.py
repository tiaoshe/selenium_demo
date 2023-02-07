import requests

header = {'Accept': '*/*', 'Connection': 'keep-alive',
          'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/44) uni-app',
          'Accept-Language': 'zh-CN,zh-Hans;q=0.9', 'Accept-Encoding': 'gzip, deflate, br',}

url = "https://baidu.com"
# HTTPS_PROXY = "https://127.0.0.1:8000"
response = requests.get(url=url, headers=header,verify=False)
print(response)
