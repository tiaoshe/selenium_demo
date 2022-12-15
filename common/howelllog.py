import logging
import shutil
import time

from common import util
import datetime, os
from inspect import currentframe, stack, getmodule

logfile = util.get_root_path() + r'\logs\running.log'
# 获取日志记录
logging.basicConfig(  # 针对 basicConfig 进行配置(basicConfig 其实就是对 logging 模块进行动态的调整，之后可以直接使用)
    level=logging.INFO,  # INFO 等级以下的日志不会被记录
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  # 日志输出格式
    filename=logfile,  # 日志存放路径(存放在当前相对路径)
    filemode='a',  # 输入模式；如果当前我们文件已经存在，可以使用 'a' 模式替代 'w' 模式
    # 与文件写入的模式相似，'w' 模式为没有文件时创建文件；'a' 模式为追加内容写入日志文件
    encoding='utf-8',
)
logger = logging.getLogger()


class WriteLog(object):
    def __init__(self, name):
        self.filemode = 'a'
        self.encoding = 'utf-8'
        self.name = os.path.split(name)[-1]
        # self.logfile = util.get_root_path() + r'\logs\running.log'
        # 由于报错使用绝对路径
        self.logfile = r'D:\workspace\selenium_demo\logs\running.log'
        # 判断文件是否存在，如果存在进行下一步判断，如果不存在则创建新文件
        if os.path.isfile(self.logfile):
            fsize = os.path.getsize(self.logfile)
            fsize = fsize / float(1024 * 1024)
            # 判断文件是否大于2.3MB 如果大于 则将文件重新命名移动到history文件夹中
            if fsize >= 2.3:
                filepath_new_name = os.path.dirname(self.logfile) + r"\old" + str(int(time.time())) + ".log"
                os.rename(self.logfile, filepath_new_name)
                oldpos = filepath_new_name
                newpos = os.path.dirname(self.logfile) + r"\history"
                shutil.move(oldpos, newpos)
                file = open(self.logfile, 'w', encoding=self.encoding)
                file.close()
                self.filepath = self.logfile
        else:
            file = open(self.logfile, 'w', encoding=self.encoding)
            file.close()
            self.filepath = self.logfile

    def write(self, content):
        # 获取当前时间
        d_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 获取调用函数的行号
        f_current_line = str(currentframe().f_back.f_lineno)
        # mod = getmodule(stack()[1][0])  # 调用函数的信息
        # module_name = mod.__name__  # 函数名
        module_info = self.name + "[line %s]" % f_current_line
        content_list = [d_time, module_info, content, '\n']
        content_str = " ".join(content_list)
        with open(self.logfile, self.filemode, encoding=self.encoding) as f:
            f.write(content_str)
