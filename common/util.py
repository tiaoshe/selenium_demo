import os, re, time
import subprocess
import faker
import requests
import schedule
import json

from common.control_config import ControlConfig
from faker import Faker

fake = Faker(locale='zh_CN')

from concurrent.futures import ThreadPoolExecutor

worker = ThreadPoolExecutor(max_workers=10)


# 获取根目录路径 ：根据配置文件中所定义的根目录下文件夹，定位根目录
def get_root_path(file_dir=None):
    if file_dir is None:
        file_dir = os.getcwd()
    head, tail = os.path.split(file_dir)
    # 通过读取配置文件定位根目录下的文件
    root_path = ControlConfig().get("base_data", "root_path")
    root_path_list = root_path.split(",")
    if tail not in root_path_list:
        try:
            return get_root_path(head)
        except RecursionError or Exception:
            ControlConfig().write("run_data", "start_num", "1000")
            return "sorry,the filedir not in rootpath"

    else:
        return head


# 将URL域名去掉
def remove_host(url_temp: str):
    print()
    # return re.sub(r"http[s]?://[\w\.]*[:]?[\d]*", "", url_temp)
    temp_a = re.sub(r"^((http://)|(https://))?([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}(/)", "",
                    url_temp)
    temp = re.sub(r".*\?(.*)", "", temp_a)
    return temp


# 判断文件是否存在，装饰器
def check_file(func):
    def check_file_exists(file_path):
        if os.path.exists(file_path):
            return func(file_path)
        else:
            return "文件不存在"

    return check_file_exists


# 自动生成接口名称,用于yaml文件自动生成api文件
def make_api_name(url_temp: str):
    api_str = remove_host(url_temp)
    str_list = api_str.split(r'/')
    new_list = list()
    for time in range(str_list.count("")):
        str_list.remove("")
    for str_temp in str_list:
        new_str = str_temp.replace("-", "_").replace(".html", "").replace("=", "")
        new_list.append(new_str)
    name = "_".join(new_list)
    return name


# 自动生成testcase类名称
def make_testcase_class_name(url_temp: str):
    name = make_api_name(url_temp)
    new_name_list = list()
    for item in name.split("_"):
        new_name_list.append(item.capitalize())
    class_name_t = "".join(new_name_list)
    return class_name_t


# Facker实例化，让测试用例处不用特地实例化
def instantiation_faker():
    return faker.Faker(locale="zh_CN")


# 运行flask程序
def app_run():
    # file_path = os.getcwd() + r"\flask_c"
    # re.sub("","",file_path)
    os.chdir("D:\\workspace\\selenium_demo\\flask_c")
    # print(file_path)
    # os.chdir(file_path)
    # subprocess.run("export FLASK_APP=app.py", shell=True)
    # subprocess.run("export FLASK_ENV=production", shell=True)
    subprocess.run("flask run -p 5555 -h 0.0.0.0", shell=True)


# 运行测试用例
def run_test_case():
    # 执行测试用例路径
    file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + r"/src/test_case/wangxiaobao"
    # 命令行执行命令
    subprocess.run("pytest %s" % file_path, shell=True)
    # subprocess.run("pytest")
    # 发送信息
    time.sleep(5)
    text = ControlConfig().get("run_data", "message")
    send_message_to_feishu("%s" % text)
    send_message_to_feishu("http://192.168.1.3:5555/index")


# 定时任务方法，用于执行定时任务job
def schedule_worker(sched_time):
    schedule.every().day.at(sched_time).do(run_test_case)
    while True:
        schedule.run_pending()
        time.sleep(1)


def schedule_run(sched_time):
    worker.submit(schedule_worker, sched_time)


def flask_run():
    worker.submit(app_run)


# 发送信息给飞书
def send_message_to_feishu(text):
    # 你复制的webhook地址
    url = r"https://open.feishu.cn/open-apis/bot/v2/hook/64a34812-fd9d-4088-95ee-0fcfda5de444"

    payload_message = {
        "msg_type": "text",
        "content": {
            "text": text
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload_message))

    # print(response.text)


if __name__ == '__main__':
    # # print(get_root_path(r"D:\workspace\selenium_demo"))
    # url = "http://192.168.1.3:8088//zentao/user-refreshRandom.html"
    # # make_api_name(url)
    # a = make_testcase_class_name(url)
    # # f = instantiation_faker()
    # # print(f.text(max_nb_chars=20))
    # print(a)
    # run_test_case()
    # send_message_to_feishu("127.0.0.1:5000/index")
    run_test_case()
