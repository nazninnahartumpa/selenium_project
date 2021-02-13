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


class MacysSpider(scrapy.Spider):
    name = "macys"

    allowed_domains = ['macys.com']

    start_urls = ['https://www.macys.com/shop/mens-clothing/mens-jackets-coats?id=3763&cm_sp=c2_1111US_catsplash_men-_-row1-_-image_coats-%26-jackets&edge=hybrid']

    def __init__(self):
        self.driver = configure_driver()
       

    def parse(self, response):
        # Step 1: Go to pluralsight.com, category section with selected search keyword
        url = response.url
        self.driver.get(url)

        link_tag_list = self.driver.find_elements_by_xpath('//*[@class="productDescription"]//a')
        print('link_tag_list', link_tag_list)
        url_list = [link.get_attribute("href") for link in link_tag_list[:4]]
        print('url_list', url_list)

        
        # for single_url in url_list:
        #     self.driver.get(single_url)
        #     time.sleep(1)
        #     print('single_url', single_url)

        #     # scrape title 
        #     title = self.driver.find_element_by_xpath('//div[@data-auto="product-title"]//h1[@itemprop="name"][1]').text

        #     # scrape brand 
        #     brand = self.driver.find_element_by_xpath('//div[@data-auto="product-title"]//h4//a').text

        #     # scrape descriptions
        #     descriptions = self.driver.find_element_by_xpath('//div[@data-el="product-details"]//ul').text

        #     # scrape price 
        #     price = self.driver.find_element_by_xpath('//div[@class="price"]').text

        #     # scrape image
        #     image_list = self.driver.find_elements_by_xpath('//div[@class="scroller-wrp"]//ul//li//picture//img')
        #     image = [link.get_attribute("src") for link in image_list]

        #     # scrape rating_count
        #     rating_count = self.driver.find_element_by_xpath('//*[@data-type="reviews"]').text

            # # scrape review
            # review_list = self.driver.find_elements_by_xpath('//*[@itemprop="reviewBody"]//div')
            # review = [review.text for review in review_list]

            # scrape review
            # try:
            #     element = self.driver.find_element_by_xpath('//div[@data-test-id="reviewContainer"]//div[9]//a//span')
            #     self.driver.execute_script("arguments[0].click();", element)
            #     time.sleep(1)
            #     review_list = self.driver.find_elements_by_xpath('//*[@itemprop="reviewBody"]//div')
            #     review = [review.text for review in review_list]
            # except:
            #     pass


            # print('title', title)
            # print('brand', brand)
            # print('descriptions', descriptions)
            # print('price', price)
            # print('store_product_id', store_product_id)
            # print('image', image)
            # print('rating', rating)
            # print('review', review)
            # print('rating_count', rating_count)

  
    


       

