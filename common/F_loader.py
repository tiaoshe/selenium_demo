import json
from common.util import check_file
import yaml
import codecs
import csv


# 将字典列表转为字典
def make_dictlist_to_dict(dict_list):
    """
    :param dict_list:[{"name":"a","value":"b"}]
    :return: {"a":"b"}
    """
    if dict_list:
        dict_temp = dict()
        for item in dict_list:
            dict_temp[item['name']] = item['value']
        return dict_temp
    else:
        return None


def make_validate(status, header):
    dict_list = list()
    dict_temp = dict()
    dict_temp_h = dict()
    if status:
        dict_temp['check'] = "status_code"
        dict_temp['assert'] = "equals"
        dict_temp['expect'] = status
        dict_temp['msg'] = "assert response status code"
        dict_list.append(dict_temp)
    if header:
        headers = make_dictlist_to_dict(header)
        if headers:
            if headers.get('Content-Type'):
                dict_temp_h['check'] = "headers.Content-Type"
                dict_temp_h['assert'] = "equals"
                dict_temp_h['expect'] = headers.get('Content-Type')
                dict_temp_h['msg'] = "assert response header Content-Type"
                dict_list.append(dict_temp_h)
    return dict_list


@check_file
def load_yaml(file_dir):
    fo = open(file_dir, 'r', encoding='utf-8')
    res = yaml.load_all(fo, Loader=yaml.FullLoader)
    resList = []
    for one in res:
        resList.append(one)
    fo.close()
    return resList


@check_file
# 读取CSV文件 返回数据字典列表
def load_csv(file_path):
    dict_list = list()
    with codecs.open(file_path, encoding='utf-8-sig') as f:
        for row in csv.DictReader(f, skipinitialspace=True):
            if row:
                dict_list.append(row)
    return dict_list


@check_file
# 读取CSV文件 返回数据字典列表
def load_csv_to_key(file_path):
    # 返回的真正的字典
    dict_back = dict()
    with codecs.open(file_path, encoding='utf-8-sig') as f:
        for row in csv.DictReader(f, skipinitialspace=True):
            if row:
                key_temp = row['key']
                if key_temp not in dict_back:
                    dict_back[key_temp] = list()
                    dict_back[key_temp].append(row)
                else:
                    dict_back[key_temp].append(row)
    return dict_back


# 将har文件转成类json数据字典
@check_file
def har2json(file_path):
    # codecs 打开文件返回unicode
    with codecs.open(file_path, mode='r', encoding='utf-8-sig') as f:
        data_har = json.load(f)
    entries = data_har['log']['entries']
    data_dict = dict()
    teststeps = list()
    for item in entries:
        api_dict = dict()
        request = dict()
        request['method'] = item.get('request').get('method')
        request['url'] = item.get('request').get('url')
        # 处理headers
        headers = make_dictlist_to_dict(item.get('request').get('headers'))
        if headers and ('Cookie' in headers):
            headers.pop('Cookie')
        request['headers'] = headers
        # 处理Cookies
        Cookies = make_dictlist_to_dict(item.get('request').get('cookies'))
        if Cookies:
            request['cookies'] = Cookies
        # 处理body
        body = make_dictlist_to_dict(item.get('request').get('postData').get('params'))
        if body:
            request['body'] = body
        else:
            text = item.get('request').get('postData').get('text')
            if text:
                request['body'] = eval(item.get('request').get('postData').get('text'))
            else:
                request['body'] = ""
        api_dict['name'] = ""
        api_dict['describe'] = ""
        api_dict['request'] = request
        api_dict['validate'] = make_validate(item.get('response').get('status'), item.get('response').get('headers'))
        teststeps.append(api_dict)
    data_dict['config'] = {"name": "testcase description"}
    data_dict['teststeps'] = teststeps
    print(data_dict)
    return data_dict


def har2yaml(file_path_har, file_path_yaml):
    data_dict = har2json(file_path_har)
    with open(file_path_yaml, "w", encoding="utf-8") as f:
        yaml.safe_dump(data_dict, f, sort_keys=False)


if __name__ == '__main__':
    # filepath = "D:/workspace/selenium_demo/data/yamlDoc/howell_api.yml"
    # filepath = "D:/workspace/selenium_demo/data/csvdata/user.csv"
    file_path_har = "D:/workspace/selenium_demo/data/hardata/1111.har"
    file_path_yaml = "D:/workspace/selenium_demo/data/yamlDoc/1111.yaml"
    har2yaml(file_path_har, file_path_yaml)
