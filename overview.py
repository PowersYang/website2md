# -*- coding: utf-8 -*-


import requests
import html2text as ht

from bs4 import BeautifulSoup


def write(text, filename):
    """
    写入markdown
    :param text:
    :return:
    """
    with open(filename, 'w', encoding='utf8') as f:
        f.write(text)


def parse(html, text_maker):
    """
    解析
    :param html:
    :return:
    """
    return text_maker.handle(html)


def get_html(base_url):
    """
    文档首页
    :return:
    """
    result = requests.get(base_url)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        html = str(soup.find(id="contentBox"))
        return html


if __name__ == '__main__':
    text_maker = ht.HTML2Text()
    text_maker.ignore_links = False
    text_maker.bypass_tables = False
    text_maker.ignore_images = False
    text_maker.images_as_html = True
    text_maker.ignore_emphasis = True
    text_maker.body_width = 0

    base_url = 'https://hadoop.apache.org/docs/stable/'

    html = get_html(base_url)
    text = parse(html, text_maker)
    write(text, 'overview.md')
