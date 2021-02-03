import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def configure_driver():
    # Add additional Options to the webdriver
    chrome_options = Options()
    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)
    # For windows
    # path=r"F:\\Coding\scrapy\scraping_selenium\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=r"E:\\test_scrapy\scrappy_test_prj\scrappy_test_prj\\chromedriver.exe", options = chrome_options)
    return driver


class DarazSpider(scrapy.Spider):
    name = 'daraz'
    # name = "product_spider"
    allowed_domains = ['daraz.com.bd']
    # start_urls = ['https://www.pluralsight.com/search?q=web_scraping&categories=course']
    start_urls = ['https://www.daraz.com.bd/products/fresh-hand-towel-tissue-paper-250-pcs-x-1-ply-i25766-s225742.html?search=store?spm=a2a0e.8553159.0.0.f0573569h9wMMB&search=store&mp=3']

    def __init__(self):
        self.driver = configure_driver()

    def parse(self, response):
        # Step 1: Go to pluralsight.com, category section with selected search keyword
        self.driver.get("https://www.daraz.com.bd/products/fresh-hand-towel-tissue-paper-250-pcs-x-1-ply-i25766-s225742.html?search=store?spm=a2a0e.8553159.0.0.f0573569h9wMMB&search=store&mp=3")
        
        title = self.driver.find_element_by_class_name("pdp-mod-product-badge-title")
        price = self.driver.find_element_by_class_name("pdp-price")
        rating = self.driver.find_element_by_class_name("score-average")
        count = self.driver.find_element_by_xpath("//div[@class='count']")

        print("title data", title.text)
        print("price data", price.text)
        print("rating data", rating.text)
        print("rating data", count.text)