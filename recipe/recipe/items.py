# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class RecipeItem(Item):
    type_url = Field()
    type_name = Field()
    food_url = Field()
    food_name = Field()
    food_ingredients = Field()

