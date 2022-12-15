import os, re
from common.control_config import ControlConfig
import faker


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
    return re.sub(r"http[s]?://[\w\.]*[:]?[\d]*", "", url_temp)


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


if __name__ == '__main__':
    # print(get_root_path(r"D:\workspace\selenium_demo"))
    url = "http://192.168.1.3:8088//zentao/user-refreshRandom.html"
    # make_api_name(url)
    a = make_testcase_class_name(url)
    # f = instantiation_faker()
    # print(f.text(max_nb_chars=20))
    print(a)
