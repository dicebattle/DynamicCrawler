from newspaper import *
import re
def article_extract():
    # url = "http://www.hankyung.com/news/app/newsview.php?aid=2017051936061"
    url = "http://news.joins.com/article/21587110"
    a = Article(url, language='ko')
    print(a)
    a.download()
    print(a)
    a.parse()
    print(a)
    a.nlp()
    print(a)
    res_set = {
        "input_article_url": url
    }
    # res_set.title = a.title
    # res_set.author = str(a.authors)
    # res_set.publish_date = str(a.publish_date)
    # res_set.text = a.text
    # res_set.keywords = a.title
    # res_set.quotes = str(re.findall(u'(?:\u201c(.*?)\u201d)', a.text))
    # return res_set

    print(a)
    print("제목: " + a.title)
    print("작성자: " + str(a.authors))
    print("일시: " + str(a.publish_date))
    print("본문: " + a.text)
    print("키워드: " + str(a.keywords))
    print("발언들: " + str(re.findall(u'(?:\u201c(.*?)\u201d)', a.text)))