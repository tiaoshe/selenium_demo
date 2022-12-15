from hamcrest import *


def check_resout(response, assert_list, params=None, jsondat=None):
    # 常规status_code 参数类型校验
    if len(assert_list) > 0:
        for check_item in assert_list:
            if check_item['check'] == "status_code" and check_item['assert'] == "equals":
                assert_that(response.status_code, equal_to(check_item['expect']), check_item['msg'])
            elif check_item['check'] == "headers.Content-Type" and check_item['assert'] == "equals":
                assert_that(response.headers['Content-Type'], equal_to(check_item['expect']), check_item['msg'])
            else:
                return None
    temp = None
    # params 返回数据校验
    if params:
        temp = eval(response.text)
        for key, value in params.items():
            if key.startswith("ck") and value != "":
                new_key = key.replace("ck-", "")
                assert_that(temp.get(new_key), equal_to(value), "实际结果： %s 和预期结果： %s不符 " % (temp.get(new_key), value))
    elif jsondat:
        temp = response.json()
        for key, value in jsondat.items():
            if key.startswith("ck") and value != "":
                new_key = key.replace("ck-", "")
                # if value.isdigit():
                #     value = int(value)
                assert_that(str(temp.get(new_key)), equal_to(value), "实际结果： %s 和预期结果： %s不符 " % (temp.get(new_key), value))
    time_temp = response.elapsed.microseconds / 1000
    # 接口响应时间校验
    assert_that(time_temp, less_than(900), "接口响应时间要控制在900ms内，再优化下吧")


if __name__ == '__main__':
    pass
