import requests
from bs4 import BeautifulSoup
import json
import csv

# url = "https://health-diet.ru/table_calorie/"

headers = {
"Accept":"*/*",
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
# req = requests.get(url,headers=headers)

# src = req.text
# print(src)

# with open("index.html", "w") as file:
#     file.write(src)


# with open("index.html") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")

# all_products_hrefs= soup.find_all(class_="mzr-tc-group-item-href")

# all_categories_dict = {}

# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get('href')

#     all_categories_dict[item_text] = item_href

# with open('all_categories_dict.json','w') as file:
#     json.dump(all_categories_dict,file, indent=4,ensure_ascii=False)

with open('all_categories_dict.json') as file:
    all_chategories = json.load(file)


count = 0
for chategory_name , chategory_href in all_chategories.items():

    if count == 0:
        rep = [","," ","-","'"]
        for item in rep:
            if item in chategory_name:
                chategory_name = chategory_name.replace(item, "_")
    # print(chategory_name)

        reg = requests.get(url=chategory_href, headers = headers)
        src = reg.text

        with open(f"data/{count}_{chategory_name}.html", 'w') as file:
            file.write(src)

        with open(f"data/{count}_{chategory_name}.html",) as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')


        # собираем заголовки таблицы 
        table_head = soup.find(class_='mzr-tc-group-table').find("tr").find_all("th")
        # product1= table_head[0].text
        # product2=table_head[1].text
        # product3=table_head[2].text
        # product4=table_head[3].text
        print(table_head)
       

        # with open(f"data/{count}_{chategory_name}.csv",'w',encoding="utf-8") as file:
        #     writer = csv.writer(file)
        #     writer.writerow(
        #         (
        #             product1,
        #             product2,
        #             product3,
        #             product4
        #         )
        #     )
# # закоменченный код
#     products_data = soup.find(class_='mzr-tc-group-table').find('tbody').find_all("tr")
#     for item in products_data:
#         products_tds = item.find_all("td")

#         title = products_tds[0].find("a").text
#         product2 = products_tds[1].text
#         product3 = products_tds[2].text
#         fats = products_tds[3].text
#         product4=products_tds[4].text
         
    

        # with open(f"data/{count}_{chategory_name}.csv",'a', encoding="utf-8") as file:

        #     writer = csv.writer(file)
        #     writer.writerow(
        #         (
        #             title,
        #             product2,
        #             product3,
        #             product4
        #         )
        #     )
        # count += 1

        


