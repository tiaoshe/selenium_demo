from common.F_request import RequestHttp


class Shengmeijia(object):
    def __init__(self):
        self.worker = RequestHttp()

    # 
    def v1_account_login(self, **kwargs):
        kwargs['method'] = "POST"
        kwargs['url'] = r"/v1/account/login"
        response = self.worker.request_http(**kwargs)
        return response
