import scrapy
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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


class NikeSpider(scrapy.Spider):
    name = "nike"

    allowed_domains = ['nike.com']

    start_urls = ['https://www.nike.com/w?q=women%20shoe&vst=women%20shoe']

    def __init__(self):
        self.driver = configure_driver()
       

    def parse(self, response):
        # Step 1: Go to pluralsight.com, category section with selected search keyword
        url = response.url
        self.driver.get(url)

        product_link_list = self.driver.find_elements_by_xpath('//figure//a[1]')
        url_list = [link.get_attribute("href") for link in product_link_list[:4]]
        # print('url_list', url_list)
        
        for single_url in url_list:
            self.driver.get(single_url)
            time.sleep(1)

            # scrape title
            title = self.driver.find_element_by_xpath('//*[@id="pdp_product_title"][1]').text

            # scrape description
            try:
                element = self.driver.find_element_by_xpath('//*[contains(@class, "description-preview")]/following-sibling::button//span')
                self.driver.execute_script("arguments[0].click();", element)
                time.sleep(1)
                description = self.driver.find_element_by_xpath('//*[@id="product-detail-modal"]//div[@class="pi-pdpmainbody"]').text
            except NoSuchElementException:
                pass

            # scrape price
            price = self.driver.find_element_by_xpath('//*[@class="product-price__wrapper"]//div').text

            # scrape image
            image_list = self.driver.find_elements_by_xpath('//*[@id="ColorwayDiv"]//img')
            image = [link.get_attribute("src") for link in image_list]

            # scrape rating count
            # rating_count_list = self.driver.find_elements_by_xpath('//*[@id="RightRail"]//button').get_attribute('aria-controls')
            # rating_count = [rating_count.text for rating_count in rating_count_list]

            # scrape review
            try:
                element = self.driver.find_element_by_xpath('//*[@id="RightRail"]//button[@aria-controls="accordion-panel-3"]//div//h3')
                self.driver.execute_script("arguments[0].click();", element)
                time.sleep(1)
                review_list = self.driver.find_elements_by_xpath('//*[@id="accordion-panel-3"]//div//div')
                review = [review.text for review in review_list]
                # print(rating)
            except NoSuchElementException:
                pass

            # ratings = self.driver.find_elements_by_xpath('//div[@id="accordion-panel-3"]//div[@class="product-review mb10-sm"]//p[@class="d-sm-ib pl4-sm"]')[0]
            # ratings = [rating.text for rating in rating_list]

            # sku_list = self.driver.find_elements_by_xpath('//*[contains(text(), "SKU")]')
            # sku_number = [sku.text for sku in sku_list]
            # review_list = self.driver.find_elements_by_xpath('//*[@itemprop="reviewBody"]//div[@class="WP-z XP-z"]')
            # review = [review.text for review in review_list]
            
            # rating_count = self.driver.find_element_by_xpath('//*[@id="overview"]//span[@class="zP-z"][1]').text


            print('title', title)
            # print('brand', brand)
            print('description', description)
            print('price', price)
            # print('sku_number', sku_number)
            print('image', image)
            print('review', review)
            print('rating_count', rating_count)


       
# class NikeSpider(scrapy.Spider):
#     name = "nike"

#     start_urls = ['https://www.nike.com/w?q=women%20shoe&vst=women%20shoe']

#     def parse(self, response):
#         url_list = response.xpath('//div[@class="product-card__body"]//figure/a//@href').extract()

#         for url in url_list:
#             # print('product_url', url)
#             yield scrapy.Request(url=url, callback=self.parse_detail)

#     def parse_detail(self, response):
#         title = response.xpath('//div[@class="pr2-sm css-1ou6bb2"]//h1[@id="pdp_product_title"]//text()').extract_first()

        

