import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["www.cnblogs.com"]
    start_urls = ["https://www.cnblogs.com/cate/java/"]

    def parse(self, response):
        print("---------------------")
        for post in response.css('article a.post-item-title'):
            link = post.css('::attr(href)').get()
            title = post.css('::text').get()
            yield {'link': link, 'title': title}
        print("---------------------")
