import os

from selenium import webdriver

from driver.abstract_driver import AbstractDriver


class ChromeDriver(AbstractDriver):

    def load_webpage(self, url):
        self.driver.get(url)
        raw_html = self.driver.page_source

    def __del__(self):
        super().__del__()
        self.driver.quit()

    def __init__(self):
        super().__init__()
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(os.getcwd() + '/../lib/chromedriver',
                                  chrome_options=chrome_options)