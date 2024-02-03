import scrapy

class PexelsSpider(scrapy.Spider):
    name = "pexels"
    start_urls = [
        'https://unsplash.com/s/photos/knife'
    ]

    def parse(self, response):
        for index in range(1, 11):
            xpath = f'/html/body/div/div/div[1]/div/div[2]/div[4]/div/div[1]/div[2]/div/div/div[1]/div/div/div[{index}]/figure[2]/div/div[1]/div/div/a/div/div[2]/img'
            image_url = response.xpath(xpath + '/@src').get()
            yield {
                'image_urls': [image_url]
            }