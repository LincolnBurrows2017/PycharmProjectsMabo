from bs4 import BeautifulSoup
import requests
import time

myurl='https://knewone.com/discover?page='

def get_info(url):
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    pics=soup.select('header > a > img')
    titles=soup.select('section > h4 > a')
    links=soup.select('section > h4 > a')

    for pic,title,link in zip(pics,titles,links):
        data={
            'pic':pic.get('src'),
            'title':title.get('title'),
            'link':'https://knewone.com'+link.get('href')
        }
        print(data)
    print('------------------------------------------------')


for i in range(1,9):
    get_info(myurl+str(i))
    time.sleep(2)