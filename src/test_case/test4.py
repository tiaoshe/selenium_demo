# -*- coding:utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor

worker = ThreadPoolExecutor(max_workers=10)


def run_proc():
    """子进程要执行的代码"""
    while True:
        print("----2----")
        time.sleep(1)


def run_procc():
    """子进程要执行的代码"""
    while True:
        print("----1----")
        time.sleep(1)


def howell1():
    worker.submit(run_proc)


def howell2():
    worker.submit(run_procc)


if __name__ == '__main__':
    pass
