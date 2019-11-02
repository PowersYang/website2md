import os
import re
import requests
import threading
import html2text as ht

from queue import Queue
from bs4 import BeautifulSoup


def get_urls(base_url):
    """
    获取目录
    :return:
    """
    result = requests.get(base_url)
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        links = soup.find(id="navcolumn").find_all('a')

        global q
        for a in links:
            url = base_url + a.get('href')
            q.put_nowait(url)


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
        # 处理开头ul
        html = re.sub(r'<ul>.*?</ul>\n<div class="section">', '', html, flags=re.DOTALL)
        # 处理图片src
        html = re.sub(r"src=\".*?/", 'src=\"/', html, flags=re.DOTALL)
        html = html.replace(r'<tt>',
                            '').replace(r'</tt>',
                                        '').replace(r'<i>',
                                                    '').replace(r'</i>', '')

        # 图片
        img_urls = []
        imgs = soup.find_all('img')
        if imgs:
            img_urls = [img.get('src') for img in imgs]

        print(url)
        return html, img_urls
    else:
        print('失败状态码：{}，失败链接：{}'.format(result.status_code, url))
        return None, None


def parse(html, text_maker):
    """
    解析
    :param html:
    :return:
    """
    return text_maker.handle(html)


def parse_imgs(url, img_urls, base_url):
    """
    下载图片
    :param url: 页面链接
    :param img_urls: 图片src
    """
    for src in img_urls:
        # src为图片的src属性值
        # if 'hadoop-logo.jpg' not in src and 'asf_logo_wide.png' not in src:
        if 'http' not in src and 'maven' not in src:
            if src.startswith('.'):
                src = src[1:]
            temp_url = url[:url.rfind('/')] + '/' + src
            # dirs = temp_url.replace(base_url, '')
            # index = dirs.rfind('/')
            # dirs = temp_url.replace(base_url, '')[:index]
            res = requests.get(temp_url)

            if res.status_code == 200:
                index = src.rfind('/')
                filename = src[index + 1:]

                dirs = 'images'
                if not os.path.exists(dirs):
                    os.makedirs(dirs)

                img = res.content
                filename = dirs + '/' + filename
                with open(filename, 'wb') as f:
                    f.write(img)
            else:
                print('-------------图片下载失败------------')
                print('失败页面：' + url)
                print('失败链接：' + src)
                print('-----------------------------------')


def write(text, filename):
    """
    写入markdown
    :param text:
    :return:
    """
    with open(filename, 'w', encoding='utf8') as f:
        f.write(text)


def task(q, base_ul):
    # 属性设置
    text_maker = ht.HTML2Text()
    text_maker.ignore_links = False
    text_maker.bypass_tables = False
    text_maker.ignore_images = False
    text_maker.images_as_html = True
    text_maker.ignore_emphasis = True
    text_maker.body_width = 0

    while not q.empty():
        url = q.get_nowait()
        html, img_urls = get_html(url)

        if html:
            # 创建文件夹
            temp_url = url.replace(base_url, '')
            index = temp_url.rfind('/')
            dirs = temp_url[:index]
            try:
                if not os.path.exists(dirs):
                    os.makedirs(dirs)
            except OSError as e:
                e.with_traceback(None)
                print('dirs:' + dirs)

            # 解析html并写入md文件
            text = parse(html, text_maker)
            filename = temp_url[index + 1:].replace('.html', '.md')
            filename = dirs + '/' + filename
            print(filename)
            write(text, filename)

        if img_urls:
            # 下载图片
            parse_imgs(url, img_urls, base_url)


if __name__ == '__main__':
    base_url = 'https://hadoop.apache.org/docs/stable/'

    # 用于存储目录
    q = Queue()
    get_urls(base_url)
    print('Queue: ' + str(q.qsize()))
    if not q.empty():
        threads = []
        for i in range(4):
            t = threading.Thread(target=task, args=(q, base_url))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

