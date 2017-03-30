import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
from chanel_extract import chanel
from page_parsing import get_info
from page_parsing import get_links_from
from page_parsing import url_list


def get_all_links_from(chanel):
    for page_num in range(1,201):
        get_links_from(chanel,page_num)


if __name__=='__main__':
    pool=Pool()
    #pool.map(get_all_links_from,chanel.split())
    pool.map(get_info,[item['url'] for item in url_list.find()])