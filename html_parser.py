import re
import urllib.request
from urllib import parse

from bs4 import BeautifulSoup

class html_parser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # links = soup.find_all('a', href=re.compile(r'/view/\d+\.html'))
        # links = soup.find_all('a',href=re.compile(r"/item/"))
        links = soup.find_all('a', href=re.compile(r"/param.shtml"))
        #<a href="/cell_phone_index/subcate57_list_s6193_1.html">128GB</a>
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        title_node = soup.find('div', class_="product-model page-title clearfix").find('h1')
        res_data['title'] = title_node.get_text()

        # summary_node = soup.find_all('td', class_='hover-edit-param')[11].find('a')
        # # newPmVal_12
        # res_data['summary'] = summary_node.get_text()

        summary_node = soup.find('span', id='newPmVal_12')
        res_data['summary'] = summary_node.get_text()

        return res_data