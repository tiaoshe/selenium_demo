import re

from common.util import get_root_path


def test_howell():
    a = r"D:\workspace\selenium_demo\src\api\shenmeijia\test_api_shengmeijia.py"
    root_path = get_root_path()
    b = a.split(root_path)[1].replace(".py", "")
    c = b.split("\\")
    d = [i for i in c if i != ""]
    e = ".".join(d)
    print(e)


def test_howell_dict():
    a = {'username': 'admin', 'password': '123456'}
    for i in a.keys():
        print(i)



if __name__ == '__main__':
    test_howell()
