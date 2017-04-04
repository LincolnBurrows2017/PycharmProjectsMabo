import requests,urllib.request
from bs4 import BeautifulSoup
import os
import socket

socket.setdefaulttimeout(6.0)#设置超时时间
header={'header':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0'}
ori_urls=['http://2222av.co/html/tupian/toupai/index_{}.html'.format(str(i)) for i in range(2,257)]
#获取要下载的网页的链接
def get_urls(url):
    urls=[]
    wb_data = requests.get(url, headers=header)
    wb_data.encoding = 'utf-8'  # 完美解决request模块下网页乱码的问题
    soup = BeautifulSoup(wb_data.text, 'lxml')
    myurls=soup.select('#main > div > div.art_box > div > ul > li > a')
    for myurl in myurls:
        urls.append(myurl.get('href'))
    print(urls)
    return urls
#下载网页内部图片
def download_pics(url):
    pic_links=[]
    path='H://download//自拍偷拍//'
    wb_data=requests.get(url,headers=header)
    wb_data.encoding = 'utf-8'#完美解决request模块下网页乱码的问题
    soup=BeautifulSoup(wb_data.text,'lxml')
    pics=soup.select('#main > div > div.art_box > div > p > img')
    title=soup.select('head > title')[0].text
    for pic in pics:
        print(pic.get('src'))
        pic_links.append(pic.get('src'))
    for link in pic_links:
        print('downloading')
        newPath=path+title
        try:
            if not os.path.isdir(newPath):
                os.mkdir(newPath)
                urllib.request.urlretrieve('http:'+link,newPath+'//'+link.split('/')[-1])
            else:
                urllib.request.urlretrieve('http:'+link,newPath+'//'+link.split('/')[-1])
            print('ok')
        except socket.error:#捕获超时异常后执行下一条下载
            continue

#先爬去第一个页面，从第二个页面开始会有规律科找
urls=get_urls('http://2222av.co/html/tupian/toupai/index.html')
for url in urls:
    download_pics('http://2222av.co/'+url)
for ori_url in ori_urls:
    print(ori_url)
    urls=get_urls(ori_url)
    for url in urls:
        download_pics('http://2222av.co/' + url)
