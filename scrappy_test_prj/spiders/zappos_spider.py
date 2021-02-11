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

        link_tag_list = self.driver.find_elements_by_xpath('//article//a')
        url_list = [link.get_attribute("href") for link in link_tag_list[:4]]
        print('url_list', url_list)

        # url_list = []
        # for link in link_list:
        #     url_list.append(urljoin(stub, link))
        
        for single_url in url_list:
            self.driver.get(single_url)
            time.sleep(1)
            print('single_url', single_url)

            # scrape title 
            title = self.driver.find_element_by_xpath('//*[@id="overview"]//h1//div//span[2]').text

            # scrape brand 
            brand = self.driver.find_element_by_xpath('//*[@id="overview"]//*[@itemprop="brand"]//span').text

            # scrape descriptions
            descriptions = self.driver.find_element_by_xpath('//div[@itemprop="description"]//ul').text

            # scrape price 
            price = self.driver.find_element_by_xpath('//aside//div//div//div//span').text

            # scrape image
            image_list = self.driver.find_elements_by_xpath('//*[@data-track-label="PrImage"]')
            image = [link.get_attribute("src") for link in image_list]

            # scrape store_product_id
            store_product_id = self.driver.find_element_by_xpath('//*[contains(text(), "SKU")]').text

            # scrape rating
            rating = self.driver.find_element_by_xpath('//*[@id="overview"]//span//div[2]//a//span').get_attribute('data-star-rating')

            # scrape rating_count
            rating_count = self.driver.find_element_by_xpath('//*[@itemprop="reviewCount ratingCount"]').get_attribute('content')

            # scrape review
            review_list = self.driver.find_elements_by_xpath('//*[@itemprop="reviewBody"]//div')
            review = [review.text for review in review_list]

            # scrape review
            # try:
            #     element = self.driver.find_element_by_xpath('//div[@data-test-id="reviewContainer"]//div[9]//a//span')
            #     self.driver.execute_script("arguments[0].click();", element)
            #     time.sleep(1)
            #     review_list = self.driver.find_elements_by_xpath('//*[@itemprop="reviewBody"]//div')
            #     review = [review.text for review in review_list]
            # except:
            #     pass


            print('title', title)
            print('brand', brand)
            print('descriptions', descriptions)
            print('price', price)
            print('store_product_id', store_product_id)
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


       

