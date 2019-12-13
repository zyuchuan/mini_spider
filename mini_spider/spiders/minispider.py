
import scrapy
from ..items import MiniItem


class MiniSpider(scrapy.Spider):

    name = "MiniSpider"

    def start_requests(self):
        yield scrapy.Request(url="https://www.midiworld.com", callback=self.parse)

    def parse(self, response):
        midis_cloud = response.css('.midis-cloud').xpath('./ul/li')
        midi = midis_cloud[0]
        style_page = midi.css('li a::attr(href)').get()
        style = midi.css('::text').get()

        style_page = response.urljoin(style_page)
        style_meta = {'style': style}
        yield scrapy.Request(style_page, callback=self.parse_style_page, meta=style_meta)

    def parse_style_page(self, response):
        item = MiniItem()
        uls = response.css("#page ul")
        midi_li = uls[0].css('li')
        for li in midi_li:
            title_and_author = li.css("::text").get()
            left_parenthesis = title_and_author.find('(')
            right_parenthesis = title_and_author.find(')')
            author = title_and_author[left_parenthesis+1:right_parenthesis]
            title = title_and_author[:left_parenthesis].strip()

            item['author'] = author
            item['title'] = title

            download_link = li.css('a::attr(href)').get()
            item['file_urls'] = [download_link]

            yield item
