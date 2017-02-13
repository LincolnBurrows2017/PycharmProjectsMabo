#获取58上面的某些信息

import requests
from bs4 import BeautifulSoup

header={'header':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
def get_links():
    links=[]
    wb_data=requests.get('http://bj.58.com/pbdn/',headers=header)
    soup=BeautifulSoup(wb_data.text,'lxml')
    mylinks=soup.select('#infolist > div > table > tbody > tr > td.t > a')
    for mylink in mylinks:
        if  'onclick' in mylink.attrs:
            links.append(mylink.get('href'))
    return links

def get_info(link):
    wb_data=requests.get(link,headers=header)
    soup=BeautifulSoup(wb_data.text,'lxml')
    title=soup.find_all('h1')[0].text
    cate=soup.select('#nav > div > span > a')[0].text
    address=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i')[0].text
    price=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.price_li > span > i')[0].text
    liull=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > p > span.look_time')[0].text

    info={
        'title':title,
        'cate':cate,
        'address':address,
        'price':price,
        'liull':liull
    }
    print(info)

theLink=get_links()
for link in theLink:
    get_info(link)


