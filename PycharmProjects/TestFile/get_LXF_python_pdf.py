from bs4 import BeautifulSoup
import requests
import re
import pdfkit

htmls=[]
#获取所有的html链接
def get_html_url(url):
    myurls=[]
    wb_data=requests.get(url)
    soup=BeautifulSoup(wb_data.text,'lxml')
    urs=soup.find_all('a',{'href':re.compile("\/wiki\/.*\/.*")})
    for ur in urs[0:len(urs)//2]:#使用地板除
        print(ur.get_text())
        myurls.append('http://www.liaoxuefeng.com'+ur.get('href'))
    print(len(myurls))
    return myurls

def save_html(urls):
    for url in urls:
        wb_data=requests.get(url)
        soup=BeautifulSoup(wb_data.text,'lxml')
        title=soup.select('#main > div.uk-container.x-container > div > div > div.x-center > div.x-content > h4')[0].text
        content=soup.select('#main > div.uk-container.x-container > div > div > div.x-center > div.x-content > div.x-wiki-content')[0]
        #content=str(content)
        pics=soup.find_all('img',{'src':re.compile('\/files\/attachments\/.*\/.*')})
        for pic in pics:
            print(title)
            picurl=pic.get('src')
            print(isinstance(picurl,str))
            print(picurl)
            # 修改图片属性为绝对路径
            #soup.find_all('img',{'src':picurl})
            print(pic)

            if soup.img['src']==picurl:
                soup.img['src'] = 'http://www.liaoxuefeng.com' + picurl
                soup.img.next_sibling
            #soup.img.next
            print(soup.img)

        print('----------------')
        with open('F:\\mabo\\{}.html'.format(title.replace('/','-')),'wb') as f:
            f.write(content.encode(encoding='utf-8'))
            print(f.__getattribute__('name'))
            htmls.append(str(f.__getattribute__('name')).replace("\\","\\\\"))
            print(htmls)
            return htmls
#/files/attachments/00138729035993893cc9f9690e042848b0f7e1816815a36000/0
def save_pdf(htmls):
    options = {'page-size': 'Letter', 'encoding': "UTF-8", 'custom-header': [('Accept-Encoding', 'gzip')]}
    pdfkit.from_file(htmls,'F:\\',options=options)

#save_html(save_html(get_html_url('http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000')))
#print(get_html_url('http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'))

save_html(get_html_url('http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'))
pdfkit.from_file('F:\mabo\Python代码运行助手.html','F:\\1.pdf')