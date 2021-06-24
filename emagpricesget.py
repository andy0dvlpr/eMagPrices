import requests
from bs4 import BeautifulSoup

print("Insert link to eMag product:")
url = input()

res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
#print(soup.prettify)
text = soup.find_all(class_="product-new-price")
price = text[0].prettify()

import re

def cleanhtml(price):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', price)
    return cleantext

output = cleanhtml(price)
print(output.translate({ord('\n'): None}))