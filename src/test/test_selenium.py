from selenium import webdriver
from collections import OrderedDict
from bs4 import BeautifulSoup
import timeit
import sys, os

# chromeOptions = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chromeOptions.add_experimental_option("prefs",prefs)
# chromeOptions.add_argument("--headless")
# chromeOptions.add_argument("--disable-gpu")
# driver = webdriver.Chrome(os.getcwd() + '/../lib/chromedriver',
#                           chrome_options=chromeOptions)


def setup_phantom_driver():
    driver = webdriver.PhantomJS()
    return driver


def setup_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(os.getcwd() + '/../lib/chromedriver',
                              chrome_options=chrome_options)
    return driver


def test_crawl(driver):
    driver.get('http://www.chosun.com')
    raw_html = driver.page_source
    soup = BeautifulSoup(raw_html, "lxml")
    headlines = soup.select(".rel a , #second_news a , .art_list_item dt a , h2 a")
    # headlines = driver.find_elements_by_css_selector\
    #     (".rel a , #second_news a , .art_list_item dt a , h2 a")
    articleDict = OrderedDict()
    for headline in headlines:
        if headline.get_text():
            print(headline.get_text(), headline.get('href', None))
            articleDict[headline.get_text()] = headline.get('href', None)

    count = 0
    for title, href in articleDict.items():
        if count == 10:
            break
        driver.get(href)
        rawHtml = driver.page_source
        soup = BeautifulSoup(rawHtml, "lxml")

        contents = ''.join([s.extract().text for s in soup.select(".par")])
        writer = ''.join([s.extract().text for s in soup.select("#j1")])
        createdAt = ''.join([s.extract().text for s in soup.select("#date_text")])
        subtitle = ''.join([s.extract().text for s in soup.select(".news_subtitle")])

        print(title + "\n" +
              "부제: " + subtitle.strip().partition("\n")[1] + "\n" +
              "작성자: " + writer + "\n" +
              "작성일시: " + createdAt[5:] + "\n" +
              "본문: " + contents.partition("\n")[0] + "\n\n")
        count += 1

    driver.quit()



