import requests 
from bs4 import BeautifulSoup
#lecture des donnees HTML
f = open ("recette.html", 'r')
html_content = f.read()
f.close

soup = BeautifulSoup(html_content, "html.parser" )
titre_h1 = soup.find("h1")
description = soup.find("p",class_="description")
image = soup.find("div",class_="info")
image_src= image.find("img")
print("titre de la page HTML :", titre_h1.text)
print("description de la page HTML :", description.text)
print("le src de l'image est :", image_src['src'])
