import time
from page_parsing import url_list
from page_parsing import item_info
# while True:
#     #print(url_list.find().count())
#     print(item_info.find().count())
#     time.sleep(5)

place_list=[]
for i in item_info.find():
    #print(i['place'][0])
    place_list.append(i['place'][0])
place_index=list(set(place_list))
print(place_index)