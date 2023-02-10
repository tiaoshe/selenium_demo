# https://open.feishu.cn/open-apis/bot/v2/hook/64a34812-fd9d-4088-95ee-0fcfda5de444
import json

import requests

# 你复制的webhook地址
url = "https://open.feishu.cn/open-apis/bot/v2/hook/64a34812-fd9d-4088-95ee-0fcfda5de444"

payload_message = {
"msg_type": "text",
"content": {
"text": "你要发送的消息 127.0.0.1:5000/index"
}
}
headers = {
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload_message))

print(response.text)