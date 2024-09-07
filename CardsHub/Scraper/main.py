from maketado_html import get_html_content
from bs4 import BeautifulSoup as bs
import pandas as pd


# URL of the website to scrape, change every time
url  = "https://www.creditcards.com/chase/"
content = get_html_content(url) # get the HTML content and store it in a html file
soup = bs(content, 'html.parser') # parse the HTML content


card_name, card_image, multipliers, signup_bonus_requirement, signup_bonus, annual_fee, apr_range, recommended_score, why_get, pros, cons, bottom_line, all_benefits = [], [], [], [], [], [], [], [], [], [], [], [], []


div_tags = soup.find_all('div', {'class': 'product-box__inner'}) # getting all cards containers


for i in div_tags:
    
    try:
        
        card = i.find('a', {'class': 'product-box__title-link'}).text.strip()
        card_name.append(card) # name
        
        card_image.append(i.find('img', {'alt': f'{card}'}).get('data-src')) # image
        
        multipliers_tag = i.find('section', {'class': 'product-box__benefits'}).find_all('dd')
    
        s = ""
        for m in multipliers_tag:
            s += m.text.strip() + "..\n"    
        multipliers.append(s) # multipliers
        
        dd_tags = i.find_all('dd', {'class': 'f-title-5 product-box__features-text u-margin-0'})
        signup_bonus.append(dd_tags[0].find('span').text)
        annual_fee.append(dd_tags[1].find('span').text)  
        apr_range.append(dd_tags[2].find('span').text)
        recommended_score.append(dd_tags[3].find('span').text)
          
        signup_bonus_requirement.append(i.find('dd', {'class': 'f-title-5 product-box__features-text u-margin-0'}).find('span', {'class': 'c-tooltip u-margin-top-15 u-remove-child-margin focus-white js-product-box__tooltip-content'}).text)
        
        why_get.append(i.find('div', {'class': 'f-longform-3 u-color-gray-100'}).text)
        
        pros_cons_tag = i.find('div', {'class': 'product-box__pros-cons-inner'}).find_all('ul')
        pros_list = pros_cons_tag[0].find_all('li')
        p = ""
        for pp in pros_list:
            p += str(pp.text.strip()) + "..\n "
        pros.append(p)
        cons_list = pros_cons_tag[1].find_all('li')
        c = ""
        for cc in cons_list:
            c += str(cc.text.strip()) + "..\n "
        cons.append(c)

        bottom_line.append(i.find('div', {'class': 'f-body-4 u-color-gray-100 product-box__bottom-line-content u-remove-child-margin'}).text)

        all_benefits_tag = i.find('div', {'class': 'product-box__highlights-content'}).find_all('li')
        l = ""
        for ll in all_benefits_tag:
            l += str(ll.text.strip()) + "..\n"
        all_benefits.append(l)
    
    
    except(Exception) as e:
        pass
    
    
df = pd.DataFrame({
    'Card Name': card_name[3:],
    'Card Image': card_image[3:],
    'Multipliers': multipliers[3:],
    'Signup Bonus Requirement': signup_bonus_requirement,
    'Signup Bonus': signup_bonus[3:],
    'Annual Fee': annual_fee[3:],
    'APR Range': apr_range[3:],
    'Recommended Score': recommended_score[3:],
    'Why Get': why_get,
    'Pros': pros,
    'Cons': cons,
    'Bottom Line': bottom_line,
    'All Benefits': all_benefits})


df.to_sql('/workspaces/Projects/CardsHub/Scraper/data/Cards_Chase.csv', index = False, encoding = 'utf-8-sig')