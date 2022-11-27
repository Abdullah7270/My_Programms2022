import scrapy

class richspider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com/']
    base_url = 'https://books.toscrape.com'

    def parse(self,response):
        all_the_books = response.xpath('//article')

        for book in all_the_books:
            book_url = self.start_urls[0] + book.xpath('.//div[@class="image_container"]/a/@href').extract_first()
            yield scrapy.Request(book_url, callback=self.parse_book)

    def parse_book(self,response):
        title = response.xpath('//div/h1/text()').extract_first()
        relative_image = response.xpath('//div[@class="item active"]/img/@src').extract_first()
        final_image = self.base_url + relative_image.replace('../..', '')
        price = response.xpath('//div[contains(@class, product_main)]/p[@class="price_color"]/text()').extract_first()
        rating = response.xpath('//div/p[contains(@class,"star-rating")]/@class').extract_first().replace('star-rating ', '')
        description = response.xpath('//div[@id="product_description"]/following-sibling::p/text()').extract_first()
        upc = response.xpath('//table[@class="table table-striped"]/tr[1]/td/text()').extract_first()
        price_excl_tax = response.xpath('//table[@class="table table-striped"]/tr[3]/td/text()').extract_first()
        price_incl_tax = response.xpath('//table[@class="table table-striped"]/tr[4]/td/text()').extract_first()
        tax = response.xpath('//table[@class="table table-striped"]/tr[5]/td/text()').extract_first()

        yield {
            'Title': title,
            'Image': final_image,
            'Rating': rating,
            'Description': description,
            'Upc': upc,
            'Price with Tax': price_incl_tax,
            'Price excl Tax': price_excl_tax,
            'Tax': tax,


        }



