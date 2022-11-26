import scrapy

class richspider(scrapy.Spider):
    name = 'richmen'
    start_urls = ['https://books.toscrape.com/']

    def parse(self,response):
        all_the_books = response.xpath('//article')

        for book in all_the_books:
            title = book.xpath('.//h3/a/@title').extract_first()
            price = book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').extract_first()
            image_url = self.start_urls[0] + book.xpath('//a/img/@src').extract_first()
            book_url = self.start_urls[0] + book.xpath('//div[@class="image_container"]/a/@href').extract_first()

            yield {
                'Title': title,
                'Price' : price,
                'Image' : image_url,
                'Book Link': book_url
            }







