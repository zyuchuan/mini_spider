# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from urllib.parse import urlparse
from pathlib import Path
from scrapy.pipelines.files import FilesPipeline


class MiniSpiderPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        return Path(urlparse(request.url).path).name
