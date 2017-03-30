import requests
from bs4 import BeautifulSoup

url='http://bj.ganji.com/wu/'
wb_data=requests.get(url)
soup=BeautifulSoup(wb_data.text,'lxml')
chanels=soup.select('#wrapper > div.layout > div.side-area > div.main > ul > li > div > dl > dt > a')
for chanel in chanels:
    chanel='http://bj.ganji.com'+chanel.get('href')
    #print(chanel)

chanel='''
http://bj.ganji.com/shouji/
http://bj.ganji.com/shoujihaoma/
http://bj.ganji.com/shoujipeijian/
http://bj.ganji.com/bijibendiannao/
http://bj.ganji.com/taishidiannaozhengji/
http://bj.ganji.com/diannaoyingjian/
http://bj.ganji.com/wangluoshebei/
http://bj.ganji.com/shumaxiangji/
http://bj.ganji.com/youxiji/
http://bj.ganji.com/xuniwupin/
http://bj.ganji.com/jiaju/
http://bj.ganji.com/jiadian/
http://bj.ganji.com/zixingchemaimai/
http://bj.ganji.com/rirongbaihuo/
http://bj.ganji.com/yingyouyunfu/
http://bj.ganji.com/fushixiaobaxuemao/
http://bj.ganji.com/meironghuazhuang/
http://bj.ganji.com/yundongqicai/
http://bj.ganji.com/yueqi/
http://bj.ganji.com/tushu/
http://bj.ganji.com/bangongjiaju/
http://bj.ganji.com/wujingongju/
http://bj.ganji.com/nongyongpin/
http://bj.ganji.com/xianzhilipin/
http://bj.ganji.com/shoucangpin/
http://bj.ganji.com/baojianpin/
http://bj.ganji.com/laonianyongpin/
http://bj.ganji.com/gou/
http://bj.ganji.com/qitaxiaochong/
http://bj.ganji.com/xiaofeika/
http://bj.ganji.com/menpiao/
'''
#wrapper > div.layout > div.side-area > div.main > ul > li.icon-jiaju > div > dl:nth-child(2) > dt > a
#wrapper > div.layout > div.side-area > div.main > ul > li.icon-sport > div > dl:nth-child(2) > dt > a
#wrapper > div.layout > div.side-area > div.main > ul > li.icon-live > div > dl:nth-child(5) > dt > a