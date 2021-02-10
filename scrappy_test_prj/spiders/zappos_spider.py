import scrapy
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin


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


class ZapposSpider(scrapy.Spider):
    name = "zappos"

    allowed_domains = ['zappos.com']

    start_urls = ['https://www.zappos.com/women-shoes']

    def __init__(self):
        self.driver = configure_driver()
       

    def parse(self, response):
        # Step 1: Go to pluralsight.com, category section with selected search keyword
        url = response.url
        self.driver.get(url)

        #stub = 'https://www.zappos.com'

        #link_list = self.driver.find_element_by_xpath('//article[@class="ow-z dq-z"]//a//@href').extract()[:4]
        #print('url_list', url_list)

        link_tag_list = self.driver.find_elements_by_xpath('//article[@class="ow-z dq-z"]//a')
        url_list = [link.get_attribute("href") for link in link_tag_list[:4]]
        #print('url_list', url_list)

        # url_list = []
        # for link in link_list:
        #     url_list.append(urljoin(stub, link))
        
        for single_url in url_list:
            self.driver.get(single_url)
            time.sleep(1)

            title = self.driver.find_element_by_xpath('//*[@id="overview"]//span[@class="nP-z"]').text
            brand = self.driver.find_element_by_xpath('//span[@class="mP-z"]//a//span').text
            description = self.driver.find_element_by_xpath('//div[@itemprop="description"]//ul//li').text
            price_list = self.driver.find_elements_by_xpath('//*[@id="productRecap"]//aside[@class="dc-z"]//div[@class="GL-z"]//span[@class="JL-z"]')
            price = [price.text for price in price_list]
            image_list = self.driver.find_elements_by_xpath('//div[@class="jQ-z"]//ul//li//a')
            image = [link.get_attribute("href") for link in image_list]
            sku_list = self.driver.find_elements_by_xpath('//*[contains(text(), "SKU")]')
            sku_number = [sku.text for sku in sku_list]
            review_list = self.driver.find_elements_by_xpath('//*[@itemprop="reviewBody"]//div[@class="WP-z XP-z"]')
            review = [review.text for review in review_list]
            rating = self.driver.find_element_by_xpath('//div[@class="Li-z"]//span').get_attribute('data-star-rating')
            rating_count = self.driver.find_element_by_xpath('//*[@id="overview"]//span[@class="zP-z"][1]').text


            print('title', title)
            print('brand', brand)
            print('description', description)
            print('price', price)
            print('sku_number', sku_number)
            print('image', image)
            print('rating', rating)
            print('review', review)
            print('rating_count', rating_count)

    # def parse_detail(self, response):
       
        # title = self.driver.find_element_by_xpath('//*[@id="overview"]//span[@class="nP-z"]')
        # brand = self.driver.find_element_by_xpath('//span[@class="mP-z"]//a//span').extract_first()
        # description = self.driver.find_elements_by_xpath('//div[@itemprop="description"]//ul//li').extract()
        # price = self.driver.find_element_by_xpath('//div[@class="GL-z"]//span[@class="JL-z"]').extract_first()
        # image = self.driver.find_elements_by_xpath('//div[@class="jQ-z"]//ul//li//a//@href').extract()
        # review = self.driver.find_element_by_xpath('//*[@itemprop="reviewBody"]//div[@class="WP-z XP-z"]')
        # rating = self.driver.find_element_by_xpath('//div[@class="Li-z"]//a//@data-star-rating').extract_first()
        # rating_count = self.driver.find_element_by_xpath('//div[@class="Li-z"]//a//span[@class="zP-z"][1]').extract()
        
        # print('title', title.text)
        # print('brand', brand)
        # print('description', description)
        # print('price', price)
        # print('image', image)
        # print('review', review)
        # print('rating', rating)
        # print('rating_count', rating_count)


       

