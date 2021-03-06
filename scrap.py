import requests
from bs4 import BeautifulSoup


url = "https://coldstorage.com.sg/search?q=peanuts"

page = requests.get(url)
parsed_html = BeautifulSoup(page.content, "html.parser")

list_of_products = parsed_html.find_all("div", class_="product_box")

final_list_of_products = []

for product in list_of_products:
    name = product.find('div', class_="product_name").text
    category = product.find('div', class_="category-name").text
    price = product.find('div', class_="price_now").text
    link = "https://coldstorage.com.sg" + product.find('a').get('href')

    final_list_of_products.append({"name":name, "category":category, "price":price, "link": link})

print(final_list_of_products)
