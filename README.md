Overview
===========

Thanks for Scrapy, this is a simple spider to scrape IELTS Vocabulary from iciba.com

This is my first Scrapy based project which is only for tutorial propose.

Requirements
============

* Python 2.7
* Works on Linux
* Make sure you have Scrapy installed

Items
=====

The items scraped by this project are IELTS Vocabulary from iciba.com, and details are defined in the class::

    icibaSpider.items.IcibaspiderItem
    
Spider
======

This project contains only one spider called ``CibaSpider``. When this spider running, the English Words and its'

corresponding phonetic symbol, Chinese parahrase, pronunciation clip's `url` will be scraped. See the source code for

more details

Make it works
=============

All items scraped will be stored into a `json` formatted file named json.data Using::

    scrapy runspider CibaSpider.py -o json.data -t json
      
