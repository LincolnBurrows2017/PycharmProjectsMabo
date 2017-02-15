from bs4 import BeautifulSoup
import requests

def get_url(starturl):
    wb_data=requests.get(starturl)
    soup=BeautifulSoup(wb_data.text,'lxml')
    links=soup.select('#ymenu-side > ul > li > span.dlb > a')
    for link in links:
        if 'href' in link.attrs:
            oriLink='http://bj.58.com'+link.get('href')
            #print(oriLink)
        else:
            pass

get_url('http://bj.58.com/sale.shtml')

chanel_list="""
http://bj.58.com/shouji/
http://bj.58.com/danche/
http://bj.58.com/zixingche/
http://bj.58.com/diannao/
http://bj.58.com/shuma/
http://bj.58.com/jiadian/
http://bj.58.com/ershoujiaju/
http://bj.58.com/bangong/
http://bj.58.com/yingyou/
http://bj.58.com/fushi/
http://bj.58.com/meirong/
http://bj.58.com/yishu/
http://bj.58.com/tushu/
http://bj.58.com/wenti/
http://bj.58.com/chengren/
"""