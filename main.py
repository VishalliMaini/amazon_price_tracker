from bs4 import BeautifulSoup
import requests
header = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"your user-agent"}

response=requests.get("https://www.amazon.in/Noise-Bluetooth-Calling-Tracking-Detection/dp/B0B5LW5DFQ/ref=sr_1_2_sspa?crid=36O9JAHPOMPHH&keywords=smartwatch+for+women&qid=1677676905&sprefix=smartwatch%2Caps%2C275&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",headers=header)
product=response.text
soup=BeautifulSoup(product,"html.parser")
#print(soup.text)
price=soup.find(name="span", class_="a-offscreen").getText()
currency = "₹"
price_without_currency = price.split(currency)[1]
price_as_float = float(price_without_currency.replace(",",""))
product_name=soup.find(name="span", id="productTitle").getText().split(",")[0]
#print(product_name)