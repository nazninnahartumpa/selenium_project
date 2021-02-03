from logging import log
import scrapy

class EcabSpider(scrapy.Spider):
    name = 'ecab'
    start_urls = ['http://e-cab.net/e-cab-members/']

    def parse(self, response):
        self.log(f"response data url {response.url}")

        # link_list = response.xpath('//article//h1//a')
        link_list = response.xpath('//article//h1//a//@href').extract()

        self.log(f"responselink_list {link_list}")

        for link in link_list:
            yield scrapy.Request(link, callback=self.parse_details)

    def parse_details(self, response):
        item = {}
        self.log(f"parse_details(): response data url {response.url}")
        info = []
        # scrape title
        title = response.xpath('//*[@class="page-_comment-title"]//@title').extract_first()
        self.log(f"parse_details(): title {title}")

        phone = response.xpath('//*[@class="info-box"]//div[contains(text(), "Phone")]/span/text()').extract_first()
        email = response.xpath('//*[@class="info-box"]//div[contains(text(), "Email")]/span/text()').extract_first()
        url = response.xpath('//*[@class="info-box"]//div[contains(text(), "URL")]//span//a//text()').extract_first()
        owner_name = response.xpath('//*[@class="info-box"]//div[contains(text(), "Owner Name")]/span/text()').extract_first()
        owner_designation = response.xpath('//*[@class="info-box"]//div[contains(text(), "Owner Designation")]/span/text()').extract_first()
        address = response.xpath('//*[@class="info-box"]//div[contains(text(), "Address")]/span/text()').extract_first()

        # scrape info
        data_list = response.xpath('//*[@class="info-box"]//div//text()').extract()
        self.log(f"parse_details(): data {data_list}")

        key_list = []
        value_list = []
        for count, i in enumerate(data_list):
            self.log(f"data count {count}")
            if count % 2 == 0:
                # key = data_list[count]
                # value = data_list[count + 1]
                # item.add(key, value)
                # self.log(f"item key {item[data_list[count]]}")
                key_list.append(data_list[count])
            else:
                value_list.append(data_list[count])
            
        
        self.log(f"key list {key_list}")
        self.log(f"value list {value_list}")
        self.log(f"value item {item}")

        information = dict(zip(key_list, value_list))

        self.log(f"data informnation {information}")
        # dic_data = dict(information)
        # item.update(dic_data)
        # self.log(f"value item update {item}")

        item = {
            "title": title,
            "phone": phone,
            "email": email,
            "url": url,
            "owner_name": owner_name,
            "owner_designation": owner_designation,
            "address": address
        }
        yield item
