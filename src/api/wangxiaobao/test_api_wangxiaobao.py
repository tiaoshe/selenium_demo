from common.F_request import RequestHttp


class Wangxiaobao(object):
    def __init__(self):
        self.worker = RequestHttp()

    # 
    def app_transcribe_msg_v1_badge_tree(self, **kwargs):
        kwargs['method'] = "GET"
        kwargs['url'] = r"app/transcribe/msg/v1/badge-tree"
        response = self.worker.request_http(**kwargs)
        return response

    # 
    def app_saler_saler_v1_account(self, **kwargs):
        kwargs['method'] = "GET"
        kwargs['url'] = r"app/saler/saler/v1/account"
        response = self.worker.request_http(**kwargs)
        return response


    # 
    def app_transcribe_cus_v1_wx_card_212379205181112320(self, **kwargs):
        kwargs['method'] = "GET"
        kwargs['url'] = r"app/transcribe/cus/v1/wx-card/212379205181112320"
        response = self.worker.request_http(**kwargs)
        return response

    # 
    def app_saler_saler_v1_info(self, **kwargs):
        kwargs['method'] = "GET"
        kwargs['url'] = r"app/saler/saler/v1/info"
        response = self.worker.request_http(**kwargs)
        return response
