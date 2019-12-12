"""
@author: Jack Zou
@file: midiworld.py
@time: 2019-12-04 5:17 PM
@file_desc:
"""

import scrapy
from ..items import MidiItem


class MidiWorldSpider(scrapy.Spider):

    name = "www.midiworld.com"

    def start_requests(self):
        yield scrapy.Request(url="https://www.midiworld.com", callback=self.parse)

    def parse(self, response):
        midis_cloud = response.css('.midis-cloud').xpath('./ul/li')
        # for midi in midis_cloud:
        #     style_page = midi.css('li a::attr(href)').get()
        #     style = midi.css('::text').get()
        #
        #     style_page = response.urljoin(style_page)
        #     style_meta = {'style': style}
        #     yield scrapy.Request(style_page, callback=self.parse_style_page, meta=style_meta)

        midi = midis_cloud[0]
        style_page = midi.css('li a::attr(href)').get()
        style = midi.css('::text').get()

        style_page = response.urljoin(style_page)
        style_meta = {'style': style}
        yield scrapy.Request(style_page, callback=self.parse_style_page, meta=style_meta)

    def parse_style_page(self, response):
        item = MidiItem()
        item['style'] = response.meta['style']

        uls = response.css("#page ul")
        midi_li = uls[0].css('li')
        for li in midi_li:
            title_and_author = li.css("::text").get()
            left_parenthesis = title_and_author.find('(')
            right_parenthesis = title_and_author.find(')')
            author = title_and_author[left_parenthesis+1:right_parenthesis]
            if len(author) == 0:
                author = '<Unknown>'

            title = title_and_author[:left_parenthesis].strip()
            if len(title) == 0:
                title = '<Unknown>'

            item['author'] = author
            item['title'] = title

            download_link = li.css('a::attr(href)').get()
            item['file_urls'] = [download_link]
            item['url'] = download_link
            yield item
