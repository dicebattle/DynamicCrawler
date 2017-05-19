from context.TestRuntimeContext import TestRuntimeContext
from task.task import Task
from task.task_builder import parse_object
from newspaper import *
import re
import yaml


ctx = TestRuntimeContext()

class DummyTask(Task):
    def execute(ctx, self, input_value, result_set: dict):
        return input_value

    @classmethod
    def get_task(cls, command: str, option):
        return DummyTask(option)


def test_task():
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&oquery=%ED%85%8C%EC%8A%A4%ED%8A%B8&ie=utf8&query=%EB%AC%B8%EC%9E%AC%EC%9D%B8"
    res_set = {
        "inp_url": url
    }
    context = TestRuntimeContext()
    task_source = None
    with open("../../test.yaml", 'r') as stream:
        try:
            task_source = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    print(task_source)
    task = parse_object(task_source)
    task.execute(context, "", res_set)
    for article in res_set['result']:
        extracted_article = article_extract(article['url'], article['title'])
        article.extracted = extracted_article
    print(res_set)

def article_extract(url, title):
    # url = "http://news.joins.com/article/21587110"
    a = Article(url, language='ko')
    a.download()
    a.parse()
    a.nlp()
    res_set = {
        "input_article_url": url
    }
    res_set.title = title or a.title
    res_set.author = str(a.authors)
    res_set.publish_date = str(a.publish_date)
    res_set.text = a.text
    res_set.keywords = a.title
    res_set.quotes = str(re.findall(u'(?:\u201c(.*?)\u201d)', a.text))
    return res_set

    # print("제목: " + a.title)
    # print("작성자: " + str(a.authors))
    # print("일시: " + str(a.publish_date))
    # print("본문: " + a.text)
    # print("키워드: " + str(a.keywords))
    # print("발언들: " + str(re.findall(u'(?:\u201c(.*?)\u201d)', a.text)))
