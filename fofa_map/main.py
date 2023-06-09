# -*- coding: utf-8 -*-
# @Time    : 2023/05/22 21:02
# @Author  : jerem1ah
# @File    : main.py
# @Github  : https://github.com/Lejeremiah

import library.utils.log
import logging

from library.utils.download import Downloader
from library.utils.keywordsHandler import KeywordsHandler
from library.utils.contentsHandler import ContentsHandler
from concurrent.futures import ThreadPoolExecutor

# keyword_handler.handle_by_nologin('''
# protocol=="socks5" &&
# "Version:5" &&
# "Method:No Authentication(0x00)" &&
# country="CN"
# ''',2)
#
# url = keyword_handler.handle_by_nologin('''
#     app="ThinkPHP" &&
#     body="__destruct" &&
#     status_code="200"
#     ''',i)


downloader = Downloader()
keyword_handler = KeywordsHandler()
contents_handler = ContentsHandler()











def handler(i):
    url = keyword_handler.handle_by_nologin('''
            title="chatgpt"
            ''', i)
    content =  downloader(url)
    contents_handler.get_contents_by_cssselect(content)



if __name__ == '__main__':
    pool = ThreadPoolExecutor(max_workers=5)

    for i in range(10):
        pool.submit(handler,i)
    pool.shutdown()

