from bs4 import BeautifulSoup
import requests
cheap = 2.5
urls = ['https://www.sainsburys.co.uk/shop/gb/groceries/häagen-dazs-vanilla-500ml', 'https://www.sainsburys.co.uk/shop/gb/groceries/haagen-dazs-salted-caramel-500ml', 'https://www.sainsburys.co.uk/shop/gb/groceries/häagen-dazs-cookies---cream-500ml']

for url in urls:
    r  = requests.get(url.encode("utf-8").decode("latin-1"), allow_redirects=True)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find("p", class_="pricePerUnit").get_text(strip="True")

    if float(price[1:4]) < cheap:
        print("haha yes")
    else:
        print("no")
