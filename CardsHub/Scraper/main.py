from maketado_html import get_html_content
from scrape import scrape_image
from bs4 import BeautifulSoup as bs
import pandas as pd


# URL of the website to scrape, change every time
url  = "https://www.lampsplus.com/products/chandeliers/"

content = get_html_content(url) # get the HTML content and store it in a html file

soup = bs(content, 'html.parser') # parse the HTML content

sku_list, titles_list, category_list, price_list, images_list = [], [], [], [], []


# get al the "div" tags with some specific attributes
div_tags = soup.find_all('div', {'class': 'jsResultContainer sortResultContainer',
                                    'data-sku-input-type': "1"})

for i in div_tags:
    
    try:
        sku = i.get('data-sku')
        
        product_tag = i.find('a', {'class': 'sortResultLink'})
        
        product_link = product_tag.get('href')
        image = scrape_image(f"https://www.lampsplus.com{product_link}")
        
        sku_list.append(sku)
        images_list.append(image)
        
        print(":)")
    
    except(Exception) as e:
        pass
        print(e)
    
df = pd.DataFrame({'sku': sku_list, 'image_url': images_list}) # creating a dataframe with the scraped data
df.to_csv('scraped_data.csv', index=False)
   
   
   
"""data_tag = product_tag.find('div', {'class': 'sortResultImgContainer'}).find('img')
sku_list.append(str(data_tag.get('data-sku'))) # catching all "sku" values and saving them in a empty list
titles_list.append(str(data_tag.get('title'))) # titles
category_list.append(str(data_tag.get('data-primary-category'))) # category
price_list.append(str(data_tag.get('data-price'))) # price"""