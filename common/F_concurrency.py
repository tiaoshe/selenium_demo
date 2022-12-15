from concurrent import futures

pool = futures.ThreadPoolExecutor(max_workers=2)


class PerformanceRun(object):
    def __init__(self, concurrent_num=1, run_time=1, thread_num=1):
        # 并发数量
        self.concurrent_num = concurrent_num
        # 线程数量
        self.thread_num = thread_num
        # 运行次数
        self.run_time = run_time
        # 线程池
        self.pool = futures.ThreadPoolExecutor(max_workers=1024)

    def concurrent_gevent(self):
        """
        协程并发
        :return:
        """
        pass

    def concurrent_thread(self, func, *args, **kwargs):
        """
        线程并行
        :return:
        """
        for i in range(self.run_time * self.thread_num):
            task = self.pool.submit(func, *args, **kwargs)
