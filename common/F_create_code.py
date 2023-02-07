import os.path
import csv
from jinja2 import Environment, FileSystemLoader
from common.util import get_root_path, make_api_name, make_testcase_class_name
from common.F_loader import load_yaml
from common.util import remove_host


class ProductionCode(object):
    def __init__(self, yaml_file=None, py_file=None, case_file=None):
        # TODO 初始化的时候传了yaml地址，但是yaml文件不存在，校验
        # yaml 文件路径
        self.yaml_file = yaml_file
        if py_file:
            # py文件写入路径
            self.py_filedir = py_file
            self.__check_create_file(py_file)
        if case_file:
            # case文件写入路径
            self.case_file = case_file
        # 根目录
        self.root = get_root_path()
        # 模板文件路径
        self.template_pathdir = self.root + r"/data/templates/"
        # api模板文件名
        self.api_template_name = 'template_api.txt'
        # testcase模板文件名
        self.testcase_template_name = 'template_testcase.txt'

    # 通过yaml文件名称生成要创建py文件的类名称
    def __get_file_name(self):
        srt_temp = os.path.basename(self.yaml_file)
        class_name = srt_temp.split(".")[0].capitalize()
        return class_name

    def __read_yaml(self):
        yaml_str = load_yaml(self.yaml_file)
        return yaml_str

    def __arrange_api_data(self):
        """
        整理生成接口代码需要的数据
        :return:     {"data": [{"method_name": "dulumen", "method": "GET", "url": "www.baidu.com", "describe": "测试"},
                         {"method_name": "dulumen", "method": "GET", "url": "www.baidu.com", "describe": "测试"}]}
        """
        yaml_datas = self.__read_yaml()
        template_dict = dict()
        template_list = list()
        for data in yaml_datas[0]['teststeps']:
            content = dict()
            if data['name'] == "":
                content['method_name'] = make_api_name(data['request']['url'])
            else:
                content['method_name'] = data['name']
            content['describe'] = data['describe']
            content['method'] = data['request']['method']
            content['url'] = remove_host(data['request']['url'])
            template_list.append(content)
        template_dict['data'] = template_list
        template_dict['class_title'] = self.__get_file_name()
        return template_dict

    def __generate_api_code(self, template_dict):
        """
        通过模板生成对应的api接口
        :param template_dict:
        :return: 返回字符串用于写入py文件
        """
        loader = FileSystemLoader(self.template_pathdir)
        env = Environment(loader=loader)
        template = env.get_template(self.api_template_name)
        return template.render(template_dict)

    def __generate_testcase_file(self, template_dict):
        """
        通过模板生成对应testcase文件
        :param template_dict:
        :return: 返回字符串用于写入py文件
        """
        if template_dict:
            for template_data in template_dict['data']:
                loader = FileSystemLoader(self.template_pathdir)
                env = Environment(loader=loader)
                template = env.get_template(self.testcase_template_name)
                content = template.render(template_data)
                # 准备测试用例的文件名
                new_case_file = self.case_file + "\\" + template_data['package_name'] + ".py"
                # 如果没有目录创建测试文件目录
                self.__check_create_file(self.case_file)
                with open(new_case_file, "w", encoding="utf-8") as f:
                    f.write(content)

    def __write_in_file(self, file_content):
        with open(self.py_filedir, "w", encoding="utf-8") as f:
            f.write(file_content)

    def __write_add_file(self, file_content):
        with open(self.py_filedir, "a+", encoding="utf-8") as f:
            f.write(file_content)

    # 将路径改变为import调用的点式
    def __file_to_import(self, filepath):
        a = filepath
        c = a.split(self.root)[1].replace(".py", "").split("\\")
        d = [i for i in c if i != ""]
        e = ".".join(d)
        return e

    #  自动化创建代码，创建参数自动化csv
    @staticmethod
    def create_csv(data: dict, csv_name):
        filename = csv_name
        filepath = get_root_path() + "\\data\\csvdata\\" + filename
        with open(filepath, 'w', encoding='utf-8') as f:
            # 创建一个writer对象
            writer = csv.writer(f)
            headers = list(data.keys())
            headers.insert(0, "key")
            # 写入表头
            writer.writerow(headers)
        return filepath

    def generate_test_code(self):
        """
        生成测试模块相关的代码
        """
        # 读取yaml文件
        yaml_datas = self.__read_yaml()
        # 准备装载变量
        template_dict = dict()
        template_list = list()
        # 多个接口组装循环
        for data in yaml_datas[0]['teststeps']:
            # 单个接口对象
            content = dict()
            # 要生成的包名
            content['package_name'] = "test_" + make_api_name(data['request']['url'])
            # 导入的文件路径，这个依赖于创建api文件的路径
            content['file_path'] = self.__file_to_import(self.py_filedir)
            # api类名称，这个是由yaml文件生成
            content['class_title'] = self.__get_file_name()
            # 自动获取的接口校验数据
            content['assert_list'] = data['validate']
            # 获取header信息
            content['headers'] = data.get('request').get('headers')
            # 测试类名称
            content['testcase_class_name'] = "Test" + make_testcase_class_name(data['request']['url'])
            # csv数据驱动文件需要自动创建，创建完成之后返回地址，用于测试代码调用
            # body用于生成csv，用于生成测试用例
            body = data.get('request').get('body')
            if body:
                csv_name = "Test" + make_testcase_class_name(data['request']['url']) + "_data.csv"
                csv_file = self.create_csv(body, csv_name)
                content['csv_file'] = csv_file
                content['case_list'] = list()
                for key in body.keys():
                    case_dict = dict()
                    # 测试用例名称
                    case_dict['case_name'] = "test_" + make_api_name(data['request']['url']) + "_" + key
                    # 测试参数名
                    case_dict['param_name'] = key
                    # api名 用于方法调用
                    case_dict['api_name'] = make_api_name(data['request']['url'])
                    # 请求参数
                    case_dict['params'] = list(body.keys())
                    content['case_list'].append(case_dict)
            template_list.append(content)
        template_dict['data'] = template_list
        return template_dict

    @staticmethod
    def __check_create_file(filepath):
        """
        检查目录是否存在,如果不存在创建目录
        :return: boolean
        """
        dir_temp = os.path.dirname(filepath)
        if not os.path.exists(dir_temp):
            os.makedirs(dir_temp)
            fb = open(dir_temp + r"\__init__.py", "w")
            fb.close()

    # 一次性给文件新增接口内容
    def start(self, yaml_file=None, py_file=None, case_file=None):
        """
        开始一次性生成，api文件
        :param yaml_file:
        :param py_file:
        :return:
        """
        if py_file:
            # 要生成的api文件路径
            self.py_filedir = py_file
            self.__check_create_file(py_file)
        if case_file:
            self.case_file = case_file
            self.__check_create_file(case_file)
        if yaml_file:
            if not os.path.exists(yaml_file):
                return "yaml_file 文件不存在"
            else:
                # yaml文件路径，在实例中共享路径，以便于其他方法读取yaml文件
                self.yaml_file = yaml_file
        # 将yaml中的数据整理成数据字典，用于通过模板生成代码
        data_temp = self.__arrange_api_data()
        # 将生成的api代码放于缓存中
        file_content = self.__generate_api_code(data_temp)
        # 输出代码到py_file文件中
        self.__write_in_file(file_content)
        # 整理生成testcase的数据
        testcase_content = self.generate_test_code()
        # 多接口生成的测试用例不同，这个方法可以生成每个接口的测试文件
        self.__generate_testcase_file(testcase_content)
        return self

    # 给api文件增加接口
    def start_add(self, yaml_file=None, py_file=None):
        if py_file:
            self.__check_create_file(py_file)
        if not os.path.exists(yaml_file):
            return "yaml_file 文件不存在"
        self.api_template_name = "template_api_add.txt"
        self.yaml_file = yaml_file
        self.py_filedir = py_file
        data_temp = self.__arrange_api_data()
        file_content = self.__generate_api_code(data_temp)
        self.__write_add_file(file_content)
        return "ok"


if __name__ == '__main__':
    # yaml_filedir = get_root_path() + r"/data/yamlDoc/zendao.yaml"
    # py_filedir = get_root_path() + r"\src\api\shenmeijia\test_api_shengmeijia.py"
    # yaml_filedir = get_root_path() + r"/data/yamlDoc/shengmeijia.yaml"
    # print(ProductionCode().start(yaml_filedir, py_filedir))
    # print(ProductionCode(yaml_filedir, py_filedir).generate_test_code())
    # print(ProductionCode(yaml_filedir, py_filedir).start())
    # print(ProductionCode().start_add(yaml_file, py_filedir))
    # 圣美家生成测试用例
    # py_filedir = get_root_path() + r"\src\api\shenmeijia\test_api_shengmeijia.py"
    # yaml_filedir = get_root_path() + r"\data\yamlDoc\shengmeijia.yaml"
    # case_file = get_root_path() + r"\src\test_case\shengmeijia"

    py_filedir = get_root_path() + r"\src\api\wangxiaobao\test_api_wangxiaobao.py"
    yaml_filedir = get_root_path() + r"\data\yamlDoc\wangxiaobao.yaml"
    case_file = get_root_path() + r"\src\test_case\wangxiaobao"
    product = ProductionCode(yaml_filedir, py_filedir, case_file)
    product.start()

    # Product.generate_testcase_code(content)
