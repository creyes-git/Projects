from bs4 import BeautifulSoup as bs
import requests

    
def scrape_image(product_url):
    
    content = requests.get(product_url).text # get the html content(maketado)
    soup = bs(content, "html.parser") # create a soup object parsing the html
    
    image_tag = soup.find('div', {'id': 'pdImgContainer'}).find('div', {'data-index': '2'}).find('img')
    image_url = image_tag.get("src")
    
    return str(image_url)