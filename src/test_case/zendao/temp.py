import requests
import re
import hashlib
from requests_toolbelt import MultipartEncoder
s = requests.session()
user = 'anjing_test'
password = 'test_anjing'
url = 'http://127.0.0.1/pro/user-login.html'
r = s.get(url)
# print(r.content.decode('utf-8'))
verify = re.findall(r"name='verifyRand' id='verifyRand' value='(.*?)'  />", r.content.decode('utf-8'))[0]
# 第一次加密密码
pwd1md5 = hashlib.md5()
pwd1md5.update(password.encode('utf-8'))
pwd1_result = pwd1md5.hexdigest()
# 第2次加密
pwd2md5 = hashlib.md5()
pwd2md5.update((pwd1_result+verify).encode('utf-8'))
pwd2_result = pwd2md5.hexdigest()
body = {
                "account": user,
               "password": pwd2_result,
               "passwordStrength": 1,
               "referer": "/pro/",
               "verifyRand": verify,
               "keepLogin": 0,
               }
r = s.post('http://127.0.0.1/pro/user-login.html', data=body)
# 访问测试页面
test = s.get("http://127.0.0.1/pro/qa/")
if "测试主页" in test.text:
    print('登录成功！！')
else:
    print('登录失败！！')
# 提交bug接口
url2 = 'http://127.0.0.1/pro/bug-create-1-0-moduleID=0.html'
body2 = MultipartEncoder(
    fields=[
        ('product', "1"),
        ('module', '0'),
        ('project', ' '),
        ('openedBuild[]', 'trunk'),
        ('assignedTo', 'admin'),
        ('deadline', ''),
        ('type', 'codeerror'),
        ('os', ''),
        ('browser', ''),
        ('title', '正确的账号密码登录失败'),  # bug 名称
        ('color', ''),
        ('severity', '3'),
        ('pri', '3'),
        ('steps', '<p>[步骤]</p>\n<p>输入正确的账号名密码进行完成登录</p>\n<br />\n<p>[结果]</p>\n登录失败<br />\n<p>[期望]</p>\n登录成功<br />'),
        ('story', '0'),
        ('task','0'),
        ('oldTaskID', '0'),
        ('mailto[]', ''),
        ('contactListMenu', ''),
        ('keywords', ''),
        ('status', 'active'),
        ('labels[]', ''),
        ('files[]', ''),
        ('uid', '602f5eb06ddc9'),
        ('case', '0'),
        ('caseVersion', '0'),
        ('caseVersion', '0'),
        ('result', '0'),
        ('testtask', '0'),
            ],
    )
# 请求提交bug接口
r2 = s.post(url2, headers={'Content-Type': body2.content_type}, data=body2)
if '保存成功' in r2.text:
    print('bug提交成功！')
else:
    print('bug提交失败')