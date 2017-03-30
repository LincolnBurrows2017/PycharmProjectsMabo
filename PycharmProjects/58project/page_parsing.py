from bs4 import BeautifulSoup
import requests
import time
import pymongo

client=pymongo.MongoClient('localhost', 27017)
ceshi=client['ceshi']
url_list=ceshi['url_list']
item_info=ceshi['item_info']

def get_links_from(chanel,page):
    url='{}pn{}/'.format(chanel,str(page))
    wb_data=requests.get(url)
    time.sleep(1)
    soup=BeautifulSoup(wb_data.text,'lxml')
    myurls=soup.select('#infolist > div > table > tbody > tr > td.t > a')
    if soup.find('td',{'class':'t'}):
        for myurl in myurls:
            link=myurl.get('href')
            url_list.insert_one({'url':link})
            print(link)
    else:
        pass

def get_info(url):
    if 'zhuanzhuan.58.com' in url.split('/'):
        print('正在解析、；',url)
        wb_data=requests.get(url)
        soup=BeautifulSoup(wb_data.text,'lxml')
        # if '404' in soup.find('script',type='text/javascript').get('src').split('/'):
        #     pass
        # else:
        title=soup.find('h1').text
        price=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.price_li > span > i')[0].text
        date=soup.find('li',{'class':'time'}).text
        place=list(soup.find('span',{'class':'c_25d'}).stripped_strings) if soup.find('span',{'class':'c_25d'}) else None
        print({'title':title,'price':price,'date':date,'place':place})
        item_info.insert_one({'title':title,'price':price,'date':date,'place':place})





#save_info('http://bj.58.com/zixingche/17216840220170x.shtml?psid=141693528195082930022038611&entinfo=17216840220170_0&iuType=z_2&PGTID=0d3000f0-0000-14aa-5f7c-caf7da6cb28f&ClickID=1')
get_links_from('http://bj.58.com/zixingche/',1)