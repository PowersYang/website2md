# -*- coding: utf-8 -*-


import requests
import html2text as ht

from bs4 import BeautifulSoup


def get_uls(base_url):
    """
    文档首页
    :return:
    """
    result = requests.get(base_url)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        uls = soup.find(id="navcolumn").find_all('ul')
        return uls


def gen_nav(uls):
    for ul in uls:
        ass = ul.find_all('a')
        for a in ass:
            name = a.text
            link = '/docs/' + a.get('href')
            print('[\'{}\', \'{}\'],'.format(link, name))


if __name__ == '__main__':
    text_maker = ht.HTML2Text()
    text_maker.ignore_links = False
    text_maker.bypass_tables = False
    text_maker.ignore_images = False
    text_maker.images_as_html = True
    text_maker.ignore_emphasis = True
    text_maker.body_width = 0

    base_url = 'https://hadoop.apache.org/docs/stable/'

    uls = get_uls(base_url)
    gen_nav(uls)
