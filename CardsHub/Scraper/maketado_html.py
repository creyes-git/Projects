import requests
import os


def get_html_content(url):
    
    try:
        
        if not os.path.exists(r"C:\Users\creyes\Desktop\Python_files\My_Projects\LampPlus Scraper\data\maketado.html"):
            # Send a GET request to the website
            response = requests.get(url)
            
            with open(r'C:\Users\creyes\Desktop\Python_files\My_Projects\LampPlus Scraper\data\maketado.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
                
        else:
            pass
        
         
        with open(r'C:\Users\creyes\Desktop\Python_files\My_Projects\LampPlus Scraper\data\maketado.html', 'r', encoding='utf-8') as f:
            content = f.read()
            
            
    except Exception as e:
        print(e)
        
        
    return content
