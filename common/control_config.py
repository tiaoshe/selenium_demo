import os
import configparser


class ControlConfig(object):
    """
    获取配置文件路径
    """

    def __init__(self, filepath=None):
        if filepath is None:
            root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            filepath = root_path + "/config/config.ini"
        self.confiscate = filepath
        self.cf = configparser.ConfigParser()
        self.cf.read(self.confiscate, encoding="utf-8")

    def get(self, *args):
        """
        :param args: args[0]==section args[1]==option
        :return: key for value
        """
        return self.cf.get(args[0], args[1])

    def write(self, section, option, value):
        """
        :param section: 分类
        :param option: 对应的键
        :param value: 值
        :return: 返回添加成功的结果
        """
        if not self.cf.has_section(section):
            self.cf.add_section(section)
        self.cf.set(section, option, value)
        with open(self.confiscate, 'r+', encoding='utf-8') as f:
            self.cf.write(f)
        return "ok"


if __name__ == '__main__':
    ControlConfig().write("run_data1", "1start_num1", "10231")
