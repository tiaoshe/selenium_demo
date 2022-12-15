import pytest
from requests_toolbelt import MultipartEncoder, MultipartDecoder
from common.util import *

f = instantiation_faker()


@pytest.mark.parametrize("text", [f.text(max_nb_chars=20) for i in range(10)])
def test_make_bug_demo1(login, text):
    """
    借鉴以下网址代码
    https://www.cnblogs.com/qican/p/15775090.html
    这个网址有比较全的禅道操作
    https://www.cnblogs.com/111testing/p/15176813.html
    :param login: 登录操作，登录成功之后，登录接口返回API操作worker，测试对象可以就可以使用已经登录的对象
    :return:
    """
    worker = login
    body2 = MultipartEncoder(
        fields=[
            ('product', "1"),
            ('module', '1'),
            ('project', '0'),
            ('execution', '0'),
            ('openedBuild[]', 'trunk'),
            ('openedBuild[]', ' '),
            ('assignedTo', 'howell'),
            ('deadline', '2022-12-13'),
            ('type', 'codeerror'),
            ('os', 'windows'),
            ('browser', 'chrome'),
            ('title', text),  # bug 名称
            ('color', ''),
            ('severity', '3'),
            ('pri', '3'),
            ('steps', '<p>[步骤]</p>\n<p>输入正确的账号名密码进行完成登录</p>\n<br />\n<p>[结果]</p>\n登录失败<br />\n<p>[期望]</p>\n登录成功<br />'),
            ('story', '0'),
            ('task', '0'),
            ('oldTaskID', '0'),
            ('mailto[]', ''),
            ('keywords', ''),
            ('status', 'active'),
            ('labels[]', ''),
            ('files[]', ''),
            ('uid', '6398430640917'),
            ('case', '0'),
            ('caseVersion', '0'),
            ('result', '0'),
            ('testtask', '0'),
        ],
    )
    headers = dict()
    headers['Content-Type'] = body2.content_type
    kwargs = dict()
    kwargs['headers'] = headers
    kwargs['data'] = body2
    worker.zentao_bug_create_1_0_moduleID(**kwargs)
