import lxml.html as html
import requests
import json


class HabrScrapper:

    def __init__(self, page_list_url, filename='data.json'):
        self.page_list_url = page_list_url
        self.filename = filename

    def start(self):
        try:
            articles = self.recieve_article_list()
            for article in articles:
                self.save_to_file(self.recieve_article_content(article))
        except BaseException as err:
            print(err)
        print('Done!')

    def recieve_article_list(self):
        response = requests.get(self.page_list_url)
        page = html.fromstring(response.content)
        return page.xpath('//li/article[contains(@class, "post_preview")]/h2/a/@href')

    def recieve_article_content(self, url):
        response = requests.get(url)
        article = html.fromstring(response.content)
        article_images = article.xpath('//article//div/img/@src')
        article_body = article.xpath('//article//div[contains(@class, "post__body")]/div/text()')
        author = article.xpath(
            '//header[contains(@class, "post__meta")]//span[contains(@class, "user-info__nickname")]/text()'
        )
        title = article.xpath('//span[contains(@class, "post__title-text")]/text()')

        data = {}
        data['author'] = author
        data['title'] = title
        data['body'] = article_body
        data['images'] = article_images

        return data

    def save_to_file(self, data):
        with open(self.filename, 'a', encoding="utf-8") as outfile:
            json.dump(data, outfile, ensure_ascii=False)
