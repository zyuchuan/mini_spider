# mini_spider

This is a simple spider to reproduce [Issue #4228](https://github.com/scrapy/scrapy/issues/4228)

Use this command to run it:
```python
scrapy crawl MiniSpider
```

Then check the log, you'll find something as shown below:

```
2019-12-13 10:13:53 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.midiworld.com/search/?q=classic>
{'author': 'Debussy',
 'file_urls': ['https://www.midiworld.com/download/4248'],
 'files': [{'checksum': 'ed17d002003c3d0de0b068cf1e6dce4b',
            'path': '4246',
            'url': 'https://www.midiworld.com/download/4246'}],
 'title': 'Project'}
2019-12-13 10:13:53 [scrapy.core.scraper] DEBUG: Scraped from <200 https://www.midiworld.com/search/?q=classic>
{'author': 'Debussy',
 'file_urls': ['https://www.midiworld.com/download/4248'],
 'files': [{'checksum': 'ed17d002003c3d0de0b068cf1e6dce4b',
            'path': '4247',
            'url': 'https://www.midiworld.com/download/4247'}],
 'title': 'Project'}
```

Note the `file_urls` and `files::url` are not identical, which is not correct.
