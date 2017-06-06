import time
from celery import Celery

celeryInstance = Celery('tasks',
                        backend='redis://localhost:6379/0',
                        broker='redis://localhost:6379/0')

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&oquery=%ED%85%8C%EC%8A%A4%ED%8A%B8&ie=utf8&query=%EB%AC%B8%EC%9E%AC%EC%9D%B8"
res_set = {
    "inp_url": url
}
result = None
with open("../test.yaml", 'r') as stream:
    result = celeryInstance.send_task('src.queue.celery_worker.crawling',
                                      args=(stream.read(), res_set))

time.sleep(5)
print(result.result)