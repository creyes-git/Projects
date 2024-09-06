from maketado_html import get_html_content
from scrape import scrape_image
from bs4 import BeautifulSoup as bs
import pandas as pd


# URL of the website to scrape, change every time
url  = "https://www.creditcards.com/american-express/"

content = get_html_content(url) # get the HTML content and store it in a html file

soup = bs(content, 'html.parser') # parse the HTML content

card_name, card_image, multipliers, signup_bonus, signup_bonus_requirement, annual_fee = [], [], [], [], [], []

div_tags = soup.find_all('div', {'class': 'product-box__inner'}) # getting all cards containers

for i in div_tags:
    
    try:
        
        card = i.find('a', {'class': 'product-box__title-link'}).text.strip()
        card_name.append(card) # name
        
        card_image.append(i.find('img', {'alt': f'{card}'}).get('data-src')) # image
        
        multipliers_tag = i.find('section', {'class': 'product-box__benefits'}).find_all('dd')
        
        s = ""
        for m in multipliers_tag:
            s += m.text.strip() + ".. "
        
        multipliers.append(s) # multipliers
        
        dd_tags = i.find_all('dd', {'class': 'f-title-5 product-box__features-text u-margin-0'})
        signup_bonus = dd_tags[0].find('span').text
        annual_fee = dd_tags[1].find('span').text
        pepe = dd_tags[3].find('span').text
        juan = dd_tags[4].find('span').text
        
        
        
        signup_bonus_requirement.append(i.find('dd', {'class': 'f-title-5 product-box__features-text u-margin-0'}).find('span', {'class': 'c-tooltip u-margin-top-15 u-remove-child-margin focus-white js-product-box__tooltip-content'}).text)
            
        
        
        print(f"{pepe} \n")
    
    except(Exception) as e:
        pass
        print(e)
