import os
import re

import requests
from bs4 import BeautifulSoup

import html2text as ht

# 属性设置
text_maker = ht.HTML2Text()
text_maker.ignore_links = False
text_maker.bypass_tables = False
text_maker.ignore_images = False
text_maker.images_as_html = True
text_maker.ignore_emphasis = True
text_maker.body_width = 0


def get_urls(base_url):
    """
    获取目录
    :return:
    """
    result = requests.get(base_url)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        links = soup.find(id="navcolumn").find_all('a')

        return [base_url + a.get('href') for a in links]
    else:
        print(result.status_code)
        return None


def get_html(url):
    """
    获取详情页源代码
    :param url:
    :return:
    """
    result = requests.get(url)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        html = str(soup.find(id="contentBox"))
        html = re.sub(r'<ul>.*?</ul>\n<div class="section">', '', html, flags=re.DOTALL)
        html = html.replace(r'<tt>', '').replace(r'</tt>', '').replace(r'<i>', '').replace(r'</i>', '')
        print(url)
        return html
    else:
        print('失败状态码：{}，失败链接：{}'.format(result.status_code, url))
        return None


def parse(html):
    """
    解析
    :param html:
    :return:
    """
    global text_maker
    return text_maker.handle(html)


def write(text, filename):
    """
    写入markdown
    :param text:
    :return:
    """
    file = open(filename, 'w', encoding='utf8')
    file.write(text)
    file.close()


if __name__ == '__main__':
    base_url = 'https://hadoop.apache.org/docs/stable/'
    urls = get_urls(base_url)
    if urls:
        for url in urls:
            # 创建文件夹
            temp_url = url.replace(base_url, '')
            index = temp_url.rfind('/')
            dirs = temp_url[:index].replace('/', '\\')
            if not os.path.exists(dirs):
                os.makedirs(dirs)

            html = get_html(url)
            text = parse(html)

            filename = temp_url[index + 1:].replace('.html', '.md')
            filename = dirs + '\\' + filename
            print(filename)
            write(text, filename)
