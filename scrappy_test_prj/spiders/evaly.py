import scrapy
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


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


class EvalySpider(scrapy.Spider):
    name = 'evaly'
    # name = "product_spider"
    allowed_domains = ['evaly.com.bd']
    # start_urls = ['https://www.pluralsight.com/search?q=web_scraping&categories=course']
    start_urls = ['https://evaly.com.bd/shops']

    def __init__(self):
        self.driver = configure_driver()

    def parse(self, response):
        # Step 1: Go to pluralsight.com, category section with selected search keyword
        url = response.url
        self.driver.get(url)
        # time.sleep(2)

        # link_tag_list = self.driver.find_elements_by_xpath('//div[@class="shops__Grid-sc-1q87oqt-0 dDPvYk my-4"]//a')
        # link_list = [link.get_attribute("href") for link in link_tag_list]

        # view_more = self.driver.find_element_by_xpath("//span[@class='whitespace-no-wrap']").click()
        # link_tag_list = self.driver.find_elements_by_xpath('//div[@class="shops__Grid-sc-1q87oqt-0 dDPvYk my-4"]//a')
        # link_list = [link.get_attribute("href") for link in link_tag_list]
        # print('link_list', link_list)

        try:
            element = WebDriverWait(self.driver, 2).untill(
                EC.presence_of_all_elements_located(By.xpath, "//span[@class='whitespace-no-wrap']").click()
            )
            print('element', element)
        except:
            pass

        # while True:
        # try:
        #     view_more = self.driver.find_element_by_xpath("//span[@class='whitespace-no-wrap']")
        #     print('view_more', view_more)
        #     view_more.click()
            
            # link_tag_list = self.driver.find_elements_by_xpath('//div[@class="shops__Grid-sc-1q87oqt-0 dDPvYk my-4"]//a')
            # link_list = [link.get_attribute("href") for link in link_tag_list]
            # print('link_list', link_list)
        # except NoSuchElementException:
        #     pass
        

        # for link in link_list:
        #     yield scrapy.Request(link, callback = self.parse_details)

    # def parse_details(self, response):
    #     item = {}
        # shop_name = response.xpath('//div[@class="p-3"]//h2[@class="mb-0 mr-4 font-bold"]//text()').extract_first()
        # shop_address = response.xpath('//p[@class="Details___StyledP-sc-10bhd3a-1 gQdCpE text-gray-700"]//text()').extract_first()
       
        # item = {
        #     'shop_name' :shop_name,
        #     'shop_address': shop_address
        # }

        # self.log(item)

        # yield item



