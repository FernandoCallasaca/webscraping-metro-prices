# steps
# 1. install scrapy
# 2. scrapy version
# 3. scrapy startproject tutorial
# 4. go to spiders folder and create this file

# import scrapy
import scrapy

# create a class
# this class inherits from scrapy.Spider
class QuotesSpider(scrapy.Spider):

   # atributes
   name = 'quotes'

   """
      This name is to execute our scrapy project like this
      -- scrapy crawl quotes --
   """

   # Put all the url directions that we want to go
   start_urls = [
      'http://quotes.toscrape.com/'
   ]

   # methods

   # this method define the principal logic
   def parse(self, response):
      with open('resultados.html', 'w', encoding='utf-8') as f:
         f.write(response.text)

