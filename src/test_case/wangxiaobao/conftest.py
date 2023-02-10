import time
from datetime import datetime
from py.xml import html
import pytest
from common.control_config import ControlConfig

config_worker = ControlConfig()


# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th('Description'))
#     cells.insert(1, html.th('Time', class_='sortable time', col='time'))
#     cells.pop()  #删除最后links列的内容
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description.encode('utf-8').decode('gbk')))
#     cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
#     cells.pop()  #删除最后links列的内容


# 也可以用@pytest.hookimpl(hookwrapper=True) 两者作用相同
@pytest.mark.hookwrapper
# 此钩子函数在setup(初始化的操作)，call（测试用例执行时），teardown（测试用例执行完毕后的处理）都会执行一次
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

    # print("----------------------")
    # # 获取常规的钩子方法的调用结果，返回一个result对象
    # out = yield
    # print(dir(out))
    # print('用例的执行结果', out)
    # # 获取调用结果的测试报告，返回一个report对象，report对象的属性包括以下
    # # 包括when（setup、call、teardown三个值）、nodeid（测试用例的名字）、
    # # outcome(用例执行的结果。passed、failed)
    # report = out.get_result()
    # print('测试报告：%s' % report)
    # print('步骤：%s' % report.when)
    # print("nodeid:%s" % report.nodeid)
    # print("description%s" % str(item.function.__doc__))
    # print("运行结果：%s" % report.outcome)
    # print("exception异常%s" % call.excinfo)
    # print("这是错误日志：%s" % report.longrepr)
    # print("duration用例耗时：%s" % report.duration)
    # # print(report.__dict__)
    # # print(dir(report))


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    收集测试结果
    print("*#"*100)
    print(terminalreporter.stats)
    """
    total = terminalreporter._numcollected
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    error = len(terminalreporter.stats.get('error', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    success_lv = len(terminalreporter.stats.get('passed', [])) / terminalreporter._numcollected * 100
    content = "总共执行：%s ,测试通过：%s ,测试失败：%s ,错误：%s ,跳过测试用例：%s ,成功率：%s " % (total, passed, failed, error, skipped, success_lv)
    config_worker.write("run_data", "message", content)
