import re

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from icibaSpider.items import IcibaspiderItem


class CibaSpider(Spider):
    name = 'ICiba'
    allowed_domains = ["iciba.com"]

    # IELTS class course 228 which is the last course, scrape reversely 
    start_urls = ["http://word.iciba.com/?action=words&class=15&course=228"]


    course = 228
    def parse(self, response):

        sel = Selector(response)
        items = []

        # Init the wordList for a centain page
        wordList = []

        for i in \
            sel.xpath("//span[not(contains(@title, '.'))]/text()").extract():
                temp = i.strip('\r\n\t')
                if re.match('[a-zA-Z]', temp):
                    wordList.append(temp)

        # Init the phonetic symbol list
        phoneticList = []

        for i in \
            sel.xpath("//strong[@lang = 'EN-US']/text()").extract():
                temp = i.strip().strip('\r\n\t')
                phoneticList.append(temp)

        # Init the Chinese paraphrase list for a centain page
        paraphraseList = []

        for i in \
            sel.xpath("//span[contains(@title, '.')]/text()").extract():
                temp = i.strip('\r\n\t')
                paraphraseList.append(temp)



        # Init the url-list of the pronunciation clip to centain word
        mp3ClipURLList = []

        for i in \
            sel.xpath("//a/@id").extract():
                if (i.find('.mp3') != -1):
                    mp3ClipURLList.append(i)


        for i in zip(wordList, phoneticList, paraphraseList, mp3ClipURLList):
            item = IcibaspiderItem()
            item['word'] = i[0]
            item['phonetic_symbol'] = i[1]
            item['paraphrase'] = i[2]
            item['pronunciation'] = i[3]

            yield item

            items.append(item)

        #yield items
        print items

        CibaSpider.course -= 1
        url = 'http://word.iciba.com/?action=words&class=15&course=' + str(CibaSpider.course)

        if CibaSpider.course >= 1:
            yield Request(url, callback = self.parse)

