from src.queue.celery_broker import crawling
import time
#
# result = add.delay(4,4)
# print('Task finished? ', result.ready())
# print('Task result: ', result.result)
# time.sleep(10)
# print('Task finished? ', result.ready())
# print('Task result: ', result.result)

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&oquery=%ED%85%8C%EC%8A%A4%ED%8A%B8&ie=utf8&query=%EB%AC%B8%EC%9E%AC%EC%9D%B8"
res_set = {
    "inp_url": url
}
result = None
with open("../test.yaml", 'r') as stream:
    result = crawling.delay(stream.read(), res_set)

time.sleep(10)
print(result.result)