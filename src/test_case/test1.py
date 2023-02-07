import requests
import urllib3

urllib3.disable_warnings()

header = {'Host': 'fandom-video.test.wangxiaobao.com', 'Accept': '*/*', 'Connection': 'keep-alive',
          'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Html5Plus/1.0 (Immersed/44) uni-app',
          'Content-Fft': '46aa178a098aefd28d7b020344d60a41&Q4NxNbRmujQiMiUxIVfG&1675750035385',
          'Accept-Language': 'zh-CN,zh-Hans;q=0.9', 'Accept-Encoding': 'gzip, deflate, br',
          'Cookie': 'sid_fandom-uniapp-gateway=s%3Aac3dGBF8SXuD_ft2MtNNkYrpMH43zpyR.AoU922tjHifn6%2FINWVWP3B5vDCnphyXE4SKaFuz3QX0'}

url="https://fandom-video.test.wangxiaobao.com/app/saler/saler/v1/account"


# HTTPS_PROXY = "https://127.0.0.1:8000"
response = requests.get(url=url, headers=header, params="", verify=False)
print(response.json())
print(response.headers)
print(response.url)
