from bs4 import BeautifulSoup as bs
import sqlite3 as sql
import pandas as pd
import requests


for issuer in ["american-express", "bank-of-america", "capital-one", "chase", "citi", "discover"]: # list of issuers

    url  = f"https://www.creditcards.com/{issuer}/" # URL of the website to scrape, change every time
    content = requests.get(url).text # get the HTML content and store it in a html file
    soup = bs(content, 'html.parser') # parse the HTML content


    card_name, card_image, multipliers, signup_bonus_requirement, signup_bonus, annual_fee, apr_range, recommended_score, why_get, pros, cons, bottom_line, all_benefits = [], [], [], [], [], [], [], [], [], [], [], [], []


    div_tags = soup.find_all('div', {'class': 'product-box__inner'}) # getting all cards containers


    for i in div_tags:
            
            try:
                card = i.find('a', {'class': 'product-box__title-link'}).text.strip()
                card_name.append(card) # name
                card_image.append(i.find('img', {'alt': f'{card}'}).get('data-src')) # image
            except:
                card_name.append("") # name
                card_image.append("") # image
            
            
            try:
                multipliers_tag = i.find('section', {'class': 'product-box__benefits'}).find_all('dd')
                s = ""
                for m in multipliers_tag:
                    s += m.text.strip() + "..\n"    
                multipliers.append(s) # multipliers
            except:
                multipliers.append("")
            
            
            try:
                dd_tags = i.find_all('dd', {'class': 'f-title-5 product-box__features-text u-margin-0'})
                signup_bonus.append(dd_tags[0].find('span').text) # signup bonus
                annual_fee.append(dd_tags[1].find('span').text)  # annual fee
                apr_range.append(dd_tags[2].find('span').text) # apr range
                recommended_score.append(dd_tags[3].find('span').text) # recommended score
            except:
                signup_bonus.append("") # signup bonus
                annual_fee.append("") # annual fee
                apr_range.append("") # apr range
                recommended_score.append("") # recommended score
                
            
            try:  
                signup_bonus_requirement.append(i.find('dd', {'class': 'f-title-5 product-box__features-text u-margin-0'}).find('span', {'class': 'c-tooltip u-margin-top-15 u-remove-child-margin focus-white js-product-box__tooltip-content'}).text)
            except:
                signup_bonus_requirement.append("") # signup bonus: requirement to get it
            
            try:
                why_get.append(i.find('div', {'class': 'f-longform-3 u-color-gray-100'}).text)
            except:
                why_get.append("") # review, why get the card
            
            
            pros_cons_tag = i.find('div', {'class': 'product-box__pros-cons-inner'}).find_all('ul') # pros and cons html tag
            try:
                pros_list = pros_cons_tag[0].find_all('li')
                p = ""
                for pp in pros_list:
                    p += str(pp.text.strip()) + "..\n "
                pros.append(p) 
            except:
                pros.append("") # pros
            try:
                cons_list = pros_cons_tag[1].find_all('li')
                c = ""
                for cc in cons_list:
                    c += str(cc.text.strip()) + "..\n "
                cons.append(c) 
            except:
                cons.append("") # cons


            try:
                bottom_line.append(i.find('div', {'class': 'f-body-4 u-color-gray-100 product-box__bottom-line-content u-remove-child-margin'}).text)
            except:
                bottom_line.append("") # bottom line description
            
            try :
                all_benefits_tag = i.find('div', {'class': 'product-box__highlights-content'}).find_all('li')
                l = ""
                for ll in all_benefits_tag:
                    l += str(ll.text.strip()) + "..\n"
                all_benefits.append(l) # all benefits
            except:
                all_benefits.append("") # all benefits
        

    df_new = pd.DataFrame({
            'Card_Name': card_name,
            'Card_Image': card_image,
            'Multipliers': multipliers,
            'Signup_Bonus_Requirement': signup_bonus_requirement,
            'Signup_Bonus': signup_bonus,
            'Annual_Fee': annual_fee,
            'APR_Range': apr_range,
            'Recommended_Score': recommended_score,
            'Why_Get': why_get,
            'Pros': pros,
            'Cons': cons,
            'Bottom_Line': bottom_line,
            'All_Benefits': all_benefits})

    try:
        df.describe() # check if dataframe exists
    except:
        df = pd.DataFrame(columns=df_new.columns) #if not create a empty dataframe with column names
        
    df = pd.concat([df, df_new], axis = 0)
    print(f"{issuer.upper()} credit cards scraped successfully!")


# Final Dataframe cleaning to transform to Database:
df = df.drop_duplicates(subset=['Card_Name'])

df['APR_Range'] = df['APR_Range'].str.replace("variable", "").str.replace("APR on purchases and balance transfers", "")

df["Recommended_Score"] = df["Recommended_Score"].apply(lambda row: row.split("(")[0])

df.loc[df['Recommended_Score'].str.lower() == " ".lower(), 'Recommended_Score'] = "No Credit Nedded"


conn = sql.connect('/workspaces/Projects/CardsHub/data/Cards.db') # create a connection to the sqlitedatabase using sqlite3

column_definitions = ', '.join([f'{col} TEXT' for col in df.columns]) # create a string of column definitions

conn.execute(f'''CREATE TABLE IF NOT EXISTS cards_table ({column_definitions})''') # create a table in the database

df.to_sql('cards_table', conn, if_exists='replace', index=False) # write the dataframe to the database

conn.close() # close the connection