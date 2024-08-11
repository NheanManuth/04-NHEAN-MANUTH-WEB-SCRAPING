import scrapy

class DatascrapySpider(scrapy.Spider):
    name = "dataScrapy"
    allowed_domains = ["www.goldonecomputer.com"]
    start_urls = ["https://www.goldonecomputer.com/index.php?route=common/home"]

    def parse(self, response):
        # Extract category names from the dropdown menu
        categories = response.css("ul.dropmenu > li.top_level.dropdown > a::text").getall()
        
        categories = [category.strip() for category in categories if category.strip()]
        print(f"\nCategories: {categories}")
