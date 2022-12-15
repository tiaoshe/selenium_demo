from common.F_request import RequestHttp


class ZendaoApi(object):
    def __init__(self):
        self.worker = RequestHttp()

    #
    def zentao_user_refreshRandom(self, **kwargs):
        kwargs['method'] = "GET"
        kwargs['url'] = r"/zentao/user-refreshRandom.html"
        response = self.worker.request_http(**kwargs)
        return response

    #
    def zentao_user_login(self, **kwargs):
        kwargs['method'] = "POST"
        kwargs['url'] = r"/zentao/user-login.html"
        response = self.worker.request_http(**kwargs)
        return response

    #
    def zentao(self, **kwargs):
        kwargs['method'] = "GET"
        kwargs['url'] = r"/zentao/"
        response = self.worker.request_http(**kwargs)
        return response

    #
    def zentao_my(self, **kwargs):
        kwargs['method'] = "GET"
        kwargs['url'] = r"/zentao/my/"
        response = self.worker.request_http(**kwargs)
        return response

    #
    def zentao_misc_getRemind(self, **kwargs):
        kwargs['method'] = "GET"
        kwargs['url'] = r"/zentao/misc-getRemind.html"
        response = self.worker.request_http(**kwargs)
        return response

    #
    def zentao_bug_create_1_0_moduleID(self, **kwargs):
        kwargs['method'] = "POST"
        kwargs['url'] = r"/zentao/bug-create-1-0-moduleID=1.html"
        response = self.worker.request_http(**kwargs)
        return response
