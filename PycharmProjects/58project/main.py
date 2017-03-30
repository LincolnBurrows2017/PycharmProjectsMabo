#多进程
from multiprocessing import Pool
from chanel_extract import chanel_list
from page_parsing import url_list
from page_parsing import get_info
from page_parsing import get_links_from

def get_all_links_from(chanel):
    for num in range(1,101):
        get_links_from(chanel,num)


#__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
if __name__=='__main__':
    pool=Pool()
    #map函数中第一个函数不用带（）
    #pool.map(get_all_links_from,chanel_list.split())
    #pool.map(get_info,[item['url'] for item in url_list.find()])
