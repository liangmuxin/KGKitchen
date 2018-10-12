from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
import requests
import recipe.items


class RecipeSpider(CrawlSpider):
    name = 'recipe'
    allowed_domains = ['allrecipes.com']
    start_urls = ['https://www.allrecipes.com/recipes/']

    def parse(self, response):
        # dish type
        items = []
        infos = Selector(response).xpath("//div[@class='col-container']/div[@class='all-categories-col'][3]/section[1]/ul/li")
        for info in infos:
            item = recipe.items.RecipeItem()
            item['type_url'] = info.xpath('a/@href').extract_first()
            item['type_name'] = info.xpath('a/text()').extract_first()
            items.append(item)

        for item in items:
            yield Request(url="".join(item['type_url']), meta={'item': item}, callback=self.parse_list)


    def parse_list(self, response):
        PAGES = 12
        # list
        for page in range(1, PAGES):
            yield Request(url = response.url + '?page=' + str(page), meta={'item':response.meta['item']}, callback=self.parse_item)


    def parse_item(self, response):
        item_1 = response.meta['item']

        items = []
        infos = Selector(response).xpath("//div[@class='fixed-recipe-card__info']/h3/a/@href")
        for info in infos:
            item = recipe.items.RecipeItem()
            item['food_url'] = info.extract()
            item['type_url'] = item_1['type_url']
            item['type_name'] = item_1['type_name']
            items.append(item)

        for item in items:
            yield Request(url=item['food_url'], meta={'item':item}, callback=self.parse_detail)


    def parse_detail(self, response):
        item = response.meta['item']

        selector = Selector(response)
        item['food_name'] = selector.xpath("//h1[@class='recipe-summary__h1']/text()").extract_first()
        item['food_ingredients'] = selector.xpath("//div/ul/li[@class='checkList__line']//span[@class='recipe-ingred_txt added']/text()").extract()

        # print(item)
        yield item









