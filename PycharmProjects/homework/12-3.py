from bs4 import BeautifulSoup
import requests

url='http://bj.xiaozhu.com/fangzi/6470910115.html'
oriUrls=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,50,1)]
print(oriUrls)
myurl=[]
#从列表页中获取行情页的所有链接
def get_urls(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    urls=soup.select('ul > li > a[target="_blank"]')
    for aurl in urls:
        if len(myurl)<=300:
            myurl.append(aurl.get('href'))
        else:
            break




#获取详情页具体信息
def get_rentInfo(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    titles=soup.select('div.pho_info > h4 > em')
    addresses=soup.select('div.pho_info > p > span')
    rentPrices=soup.select('div.day_l > span')
    picLinks=soup.select('#curBigImage')
    lorderlinks=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
    lorderNames=soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    lorderSexs=soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span')

    #print(titles,addresses,rents,piclinks,lorderlinks,lorderNames,lorderSexs)
    for title,address,rentPrice,picLink,lorderLink,lorderName,lorderSex in zip(titles,addresses,rentPrices,picLinks,lorderlinks,lorderNames,lorderSexs):
        data={
            '标题':title.get_text().strip(),
            '地址':address.get_text().strip(),
            '日租金':rentPrice.get_text().strip(),
            '第一张房源图片链接':picLink.get('src').strip(),
            '房东图片链接':lorderLink.get('src').strip(),
            '房东名字':lorderName.get_text().strip(),
            '房东性别':'woman' if len(soup.find_all("span",class_='member_girl_ico'))==1 else 'man'
        }
        print(data)


for oriUrl in oriUrls:
    get_urls(oriUrl)
    if len(myurl)>=300:
        break
for url in myurl:
    get_rentInfo(url)

print('------------')
print(len(myurl))