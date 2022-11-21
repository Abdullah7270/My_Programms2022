import  scrapy

class PopulationSpider(scrapy.Spider):
    name = 'population'
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self,response):

        rows= response.xpath('//tr')
        for row in rows:

            #title = response.xpath('//h1/text()').get()
            country = row.xpath('./td/a/text()').get()
            population = row.xpath('./td[3]/text()').get()
            land_area = row.xpath('./td[7]/text()').get()
            yield {
                    #'title': title,
                    'country name': country,
                    'population': population,
                    'Land Area' : land_area,
            }

