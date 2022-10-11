import os


# 获取根目录路径
def get_root_path():
    return os.path.abspath(os.path.join(os.getcwd(), "../.."))


