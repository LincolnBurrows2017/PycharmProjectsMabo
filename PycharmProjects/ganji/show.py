from page_parsing import url_list,item_info

print(url_list.find().count())
print([item['price'] for item in item_info.find()])