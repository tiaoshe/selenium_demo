import requests, datetime, time
from concurrent import futures


def get_request(url):
    r = requests.get(url)
    print('{}:{}  {}'.format(datetime.datetime.now(), url, r.status_code))


def howell_te():
    while True:
        print(1)
        time.sleep(1)


urls = ['https://www.baidu.com', 'https://www.tmall.com', 'https://www.jd.com']
pool = futures.ThreadPoolExecutor(max_workers=10)
for url in urls:
    task = pool.submit(get_request, url)
pool.submit(howell_te())
print('{}主线程'.format(datetime.datetime.now()))
time.sleep(2)
