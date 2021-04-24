from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
def index_view(request):
    final_list_of_products = []

    if request.method == "POST":
        url = f"https://coldstorage.com.sg/search?q={request.POST['search']}"

        page = requests.get(url)
        parsed_html = BeautifulSoup(page.content, "html.parser")

        list_of_products = parsed_html.find_all("div", class_="product_box")
    
        for product in list_of_products:
            name = product.find('div', class_="product_name").text
            category = product.find('div', class_="category-name").text
            price = product.find('div', class_="price_now").text
            link = "https://coldstorage.com.sg" + product.find('a').get('href')

            final_list_of_products.append({"name":name, "category":category, "price":price, "link": link})

        

    return render(request, "coldstorage/index.html",{"products":final_list_of_products})

# def show_view(request, name):
#     return render(request, "coldstorage/show.html", {"from_url":name})

