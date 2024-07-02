import bs4
import scrapy
from ..items import DoubanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    # statrt_urls = ['https://book.douban.com/top250?start=0']
    start_urls = []
    for x in range(3):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)

    def parse(self, response,*args,**kwargs):
        bs = bs4.BeautifulSoup(response.text, 'html.parser')
        datas = bs.find_all('tr', class_='item')
        for data in datas:
            title = data.find_all('a')[1]['title']
            publish = data.find('p', class_='pl').text
            score = data.find('span', class_='rating_nums').text
            print(title, publish, score)
        # print(response.text)
