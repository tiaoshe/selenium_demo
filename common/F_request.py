import time

import requests
from common.control_config import ControlConfig
from common.howelllog import WriteLog,logger

logger = WriteLog(__file__)


class RequestHttp(object):
    def __init__(self):
        self.host = ControlConfig().get("run_data", "host_b")
        # header统一管理
        self.headers = dict()

    def request_http(self, **kwargs):
        logger.write(str(kwargs))
        kwargs['url'] = self.host + kwargs['url']
        print(kwargs['url'])
        for item, value in kwargs['headers'].items():
            self.headers[item] = value
        kwargs['headers'] = self.headers
        kwargs['verify'] = False
        response = requests.Session().request(**kwargs)
        logger.write(response.text)
        logger.write("接口响应时间是：%s" % str(response.elapsed.microseconds / 1000))
        return response


if __name__ == '__main__':
    print(RequestHttp().request_http().text)
