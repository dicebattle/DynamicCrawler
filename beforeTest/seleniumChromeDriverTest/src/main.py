from selenium import webdriver
from collections import OrderedDict
import sys, os

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(os.getcwd() + '/../lib/chromedriver',
                          chrome_options=chromeOptions)

driver.get('http://www.chosun.com')
headlines = driver.find_elements_by_css_selector\
    (".rel a , #second_news a , .art_list_item dt a , h2 a")
articleDict = OrderedDict()
for headline in headlines:
    if headline.text:
        print(headline.text, headline.get_attribute('href'))
        articleDict[headline.text] = headline.get_attribute('href')


count = 0
for title, href in articleDict.items():
    if count == 10:
        break
    driver.get(href)

    contents = driver.find_element_by_css_selector(".par")
    writer = driver.find_element_by_css_selector("#j1")
    createdAt = driver.find_element_by_css_selector("#date_text")
    subtitle = driver.find_element_by_css_selector(".news_subtitle")
    #title = driver.find_element_by_css_selector("#news_title_text_id")

    print(title + "\n" +
          "부제: " + subtitle.text[:30] + "\n" +
          "작성자: " + writer.text + "\n" +
          "작성일시: " + createdAt.text[5:] + "\n" +
          "본문: " + contents.text[:100])
    count += 1




