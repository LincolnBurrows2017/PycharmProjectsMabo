from bs4 import BeautifulSoup
import requests
import pymongo
import random
import time

#connect to mongodb
client=pymongo.MongoClient('localhost',27017)
ganji=client['ganji']
item_info=ganji['item_info']
url_list=ganji['url_list']
#hide ip
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0','Connection':'keep-alive'}
proxy_ip_list=['http://125.117.115.184','http://117.93.190.225','http://163.125.16.139','http://27.46.37.32','http://163.125.16.139','http://111.40.84.73']
#save url
def get_links_from(url,page,whosales=''):
    ori_link='{}{}o{}'.format(url,whosales,str(page))
    print(ori_link)
    proxy_ip = random.choice(proxy_ip_list)
    proxies = {'http:': proxy_ip}
    print(proxies)
    time.sleep(2)
    try:
        wb_data=requests.get(ori_link,headers=headers,proxies=proxies)
        soup=BeautifulSoup(wb_data.text,'lxml')
        #zhuanzhuan_url
        if soup.select('body > div.h-search > div > div.clearfix > div.logo-box > a'):
            links=soup.select('#infolist > div.infocon > table > tbody > tr > td.t > a')
            for link in links:
                url=link.get('href')
                print(url)
                url_list.insert_one({'url':url})
        else:
            pass
    except Exception:
        print(Exception)
        # infolist > div:nth-child(3) > table > tbody > tr:nth-child(6) > td.t > a
        # infolist > div.infocon > table > tbody > tr > td.t > a

get_links_from('http://bj.ganji.com/diannao/',29)
#save item_info
def get_info(url):
    if 'zhuanzhuan.ganji.com' in url.split('/'):
        proxy_ip=random.choice(proxy_ip_list)
        proxies={'http:':proxy_ip}
        time.sleep(1)
        try:
            wb_data=requests.get(url,headers=headers,proxies=proxies)
            soup=BeautifulSoup(wb_data.text,'lxml')
            title=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > h1')[0].text
            price=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.price_li > span > i')[0].text
            place=soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i')[0].text.split('-') if soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.palce_li > span > i') else None
            date=None
            phone_num=None
            type=None
            data={'title':title,'type':type,'place':place,'phone_num':phone_num,'date':date,'price':price}
            print(data)
            item_info.insert_one(data)
        except Exception:
            print(Exception)
    else:
        proxy_ip = random.choice(proxy_ip_list)
        proxies = {'http:': proxy_ip}
        wb_data = requests.get(url, headers=headers, proxies=proxies)
        soup=BeautifulSoup(wb_data.text,'lxml')
        title=soup.select('#wrapper > div.content.clearfix > div.leftBox > div.col-cont.title-box > h1')[0].text
        date=soup.select('#wrapper > div.content.clearfix > div.leftBox > div.col-cont.title-box > div > ul.title-info-l.clearfix > li > i')[0].text.replace(' ','').replace('\n','').replace('发布','').replace('\xa0','')
        place=list(soup.select('#wrapper > div.content.clearfix > div.leftBox > div:nth-of-type(2) > div > ul > li:nth-of-type(3)')[0].stripped_strings) if soup.select('#wrapper > div.content.clearfix > div.leftBox > div:nth-of-type(2) > div > ul > li:nth-of-type(3)') else None
        #data cleaning of place
        place.pop(0)
        place.remove('-') if '-' in place else None
        place.remove('-') if '-' in place else None
        type=soup.select('#wrapper > div.content.clearfix > div.leftBox > div:nth-of-type(2) > div > ul > li > span > a')[0].text
        #BeautifulSoup 不识别通过 google 开发者工具获取的CSS选择器nth-child(第几个子元素而且是特定元素),可以用nth-of-type(第几个特定元素)替换。
        phone_num=soup.select('#wrapper > div.content.clearfix > div.leftBox > div > div > ul > li > span.phoneNum-style')[0].text.strip()
        price=soup.select('#wrapper > div.content.clearfix > div.leftBox > div:nth-of-type(2) > div > ul > li:nth-of-type(2) > i.f22.fc-orange.f-type')[0].text
        data={'title':title,'type':type,'place':place,'phone_num':phone_num,'date':date,'price':price}
        print(data)
        item_info.insert_one(data)

#get_info('http://zhuanzhuan.ganji.com/detail/835171727663022086z.shtml?from=pc&source=ganji&cate=&cateurl=&gj_other_ifid=from_ganji&gj_other_city_id=12&gj_other_gc_1=wu&gj_other_uuid=&gj_other_ca_s=&gj_other_ca_kw=&gj_other_ca_n=&gj_other_ca_i=&gj_other_sid=')
#get_info('http://bj.ganji.com/jiaju/27876988362541x.htm')
#get_info('http://bj.ganji.com/menpiao/2650417454x.htm')
