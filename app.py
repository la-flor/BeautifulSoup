from bs4 import BeautifulSoup
import re
import requests


URL = "https://www.backcountry.com/Store/catalog/search.jsp?s=u&q=chalk"
page = requests.get(URL).content

soup = BeautifulSoup(page, 'html.parser')

products = soup.find_all('div', class_='product')

count = 0
for product in products:
    
    if product.find('span', class_='ui-pl-pricing-low-price'):
        price = product.find('span', class_='ui-pl-pricing-low-price').text
    else:
        price = product.find('span', class_='ui-pl-pricing-high-price').text
    brand = product.find('span', class_='ui-pl-name-brand').text
    model = product.find('span', class_='ui-pl-name-title').text
    clean_price = re.search("[0-9]+\.[0-9][0-9]", price).group(0)
    count += 1
    print({ "price": clean_price, "brand": brand, "model": model, "count": count })


