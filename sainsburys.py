from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
import os

email_address = os.environ.get('email_address')
email_password = os.environ.get('email_password')
recipients = ['connor@connorcairns.xyz']

cheap = 4
flavours = []
urls = ['https://www.sainsburys.co.uk/shop/gb/groceries/häagen-dazs-vanilla-500ml', 'https://www.sainsburys.co.uk/shop/gb/groceries/haagen-dazs-salted-caramel-500ml', "https://www.sainsburys.co.uk/shop/gb/groceries/häagen-dazs-strawberry-cheesecake-500ml", "https://www.sainsburys.co.uk/shop/gb/groceries/häagen-dazs-cookies---cream-500ml"]

for url in urls:
    r  = requests.get(url.encode("utf-8").decode("latin-1"), allow_redirects=True)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find("p", class_="pricePerUnit").get_text(strip="True")

    if float(price[1:4]) < cheap:
        name = url[59:].replace("-", " ").replace("500ml", "").replace("   ", " ")
        flavours.append(name)

if len(flavours) > 0:
    msg = EmailMessage()
    msg["Subject"] = "Haagen Bargins!"
    msg["From"] = email_address
    msg["To"] = ", ".join(recipients)
    msg.set_content(f"""Haagen Dazs is cheap!

    The following flavours are on sale:
    {flavours}
    """)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)