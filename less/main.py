from bs4 import BeautifulSoup

with open("./sayt.html") as file:
    html = file.read()

# print(html)
htmldom = BeautifulSoup(html, "lxml")
# print(htmldom.title.text)
# print(htmldom.title.string)

# el = htmldom.find("figcaption")
# print(el.text.strip())

# print(htmldom.find("li"))
# print(htmldom.findAll("li"))
# li_list = htmldom.findAll("li")
# for li in li_list:
#     print(li.text)

# print(htmldom.find("span", class_="product__price"))
# print(htmldom.find("span", class_="product__discount"))

# our_span = htmldom.find("ul").find("li", class_="li2").find(class_="span1")
# print(our_span.text)

# our_span = htmldom.find("ul").find("li", {"title": "Muhum qator", "class": "li2"}).find(class_="span1")
# print(our_span.text)

data = htmldom.find("ul").find_all("span")
# print(data)
# result = []
# for el in data:
#     result.append(el.text)
# print(result)

# result = []
# for index, el in enumerate(data):
#     if index % 2 != 0:
#         result.append(el.text)
# print(result)

# share_btns = htmldom.find(class_="share-block").find_all("a", class_="share-btn")
# share_link = []
# for a in share_btns:
#     share_link.append(a.get("href"))
# print(share_link)

# share_link = [a["href"] for a in share_btns]

# print(share_link)

# print(htmldom.find("img", {"alt": "kross"}).get("src"))

# print(htmldom.find(class_="span1").find_parent())
# print(htmldom.find(class_="span1").find_parent(class_="details__items"))
# print(htmldom.find(class_="span1").find_parents())
# print(htmldom.find(class_="span1").find_parents("div"))

# print(htmldom.find(class_="details__items").find_next("span"))
# print(htmldom.find(class_="details__items").find_previous())
# print(htmldom.find(class_="details__items").find_previous("span"))

# print(htmldom.find(class_="li2").find_next_sibling())
# print(htmldom.find(class_="li2").find_previous_sibling())

# print(htmldom.find(class_="li2").find_previous_siblings())
# print(htmldom.find(class_="li2").find_next_siblings())

# print(htmldom.find(class_="li2").find_previous_siblings("filter"))
# print(htmldom.find(class_="li2").find_next_siblings("filter"))

# print(htmldom.find("span", text="Yetkazib berish xizmati:").find_next_sibling().text.strip())

# import re
# print(htmldom.find("span", text=re.compile("Kafolat")))
# print(htmldom.findAll("span", text=re.compile("Kafolat")))

# print(htmldom.findAll("span", text=re.compile("([Kk]afolat)")))

# import requests

# site = requests.get("https://mproweb.uz/")
# # print(site.text)
# htmldom = BeautifulSoup(site.text, "lxml")
# # print(htmldom.title.text)

# menu_items = htmldom.find("ul", id="qmenu").find_all("a")

# # print(menu_items)
# menu_items_btns = []
# for item in menu_items:
#     menu_items_btns.append({
#         "url": f"{site.url}{item['href']}",
#         "name": item.find("span", class_="txt").text.strip()
#     })
# print(menu_items_btns)

# import json
# with open("mproweb_menu_item.json", "w") as file:
#     json.dump(menu_items_btns, file, indent=4)
#     print("[INFO]: File saqlandi bro !")



import requests

site = requests.get("https://www.worldometers.info/geography/how-many-countries-are-there-in-the-world/")
# print(site.text)
htmldom = BeautifulSoup(site.text, "lxml")
# print(htmldom.title.text)

table_data = htmldom.find("table", id="example2").find("tbody")
# print(table_data)
table_data_lines = table_data.find_all("tr")
# print(len(table_data_lines))

all_countres = []
for index, tr in enumerate(table_data_lines):
    # if index >= 3:
    #     break
    td_list = tr.findAll("td")
    # print(td_list[1].text)
    all_countres.append({
        "name": td_list[1].text.strip(),
        "population": int(td_list[2].text.strip().replace(",", "")),
        "persent": float(td_list[3].text.strip().replace("%", "")),
        "area_km": int(td_list[4].text.strip().replace(",", "")),
    })
# print(all_countres)

import json
with open("all_countres.json", "w") as file:
    json.dump(all_countres, file, indent=4)
    print("[INFO]: all_countres File saqlandi bro !")
