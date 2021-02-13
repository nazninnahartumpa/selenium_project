import scrapy
from urllib.parse import urljoin
import time


class TESTMacysSpider(scrapy.Spider):
    name = "testmacys"

    start_urls = ['https://www.macys.com/shop/mens-clothing/mens-jackets-coats?id=3763&cm_sp=c2_1111US_catsplash_men-_-row1-_-image_coats-%26-jackets&edge=hybrid']
    

    def parse(self, response):

        stub = 'https://www.macys.com/'

        url_list = []

        proiduct_link_list = response.xpath('//*[@class="productDescription"]//a//@href').extract()

        for link in proiduct_link_list:
            url_list.append(urljoin(stub, link))
        # print('url_list', url_list)

        for url in url_list[:4]:
            yield scrapy.Request(url=url, callback=self.parse_detail)


    def parse_detail(self, response):
        
        # scrape title
        title = response.xpath('//div[@data-auto="product-title"]//h1[@itemprop="name"][1]//text()').extract_first()

        # scrape brand
        brand = response.xpath('//div[@data-auto="product-title"]//h4//a//text()').extract_first()

        # scrape description
        description = response.xpath('//div[@data-el="product-details"]//ul//text()').extract()

        # scrape description
        price = response.xpath('//div[@class="price"]//text()').extract_first()

        # scrape images
        images = response.xpath('//div[@class="scroller-wrp"]//ul//li//picture//img//@src').extract()

        # scrape rating_count
        rating_count = response.xpath('//*[@data-type="reviews"]//text()').extract_first()
        
        print('title', title)
        print('brand', brand)
        print('description', description)
        print('price', price)
        print('images', images)
        print('rating_count', rating_count)




