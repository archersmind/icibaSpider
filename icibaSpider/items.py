# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class IcibaspiderItem(Item):
    # define the fields for your item here like:
    # name = Field()
    word = Field()
    phonetic_symbol = Field()
    paraphrase = Field()
    pronunciation = Field()
