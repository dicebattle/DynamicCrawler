from newspaper import *
import re
def test():
    url = "http://news.joins.com/article/21587110"
    a = Article(url, language='ko')
    a.download()
    a.parse()
    a.nlp()
    print("제목: " + a.title)
    print("작성자: " + str(a.authors))
    print("일시: " + str(a.publish_date))
    print("본문: " + a.text)
    print("키워드: " + str(a.keywords))
    print("발언들: " + str(re.findall(u'(?:\u201c(.*?)\u201d)', a.text)))