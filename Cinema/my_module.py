import requests
from PIL import Image
import bs4

def icon_calendar():
    # Get the calendar images of the day
    url = "https://www.google.com/calendar/embed?src=primary&ctz=America/New_York&pli=1"
    response = requests.get(url)

    # Parse the response
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    # Get the image
    image_src = soup.find("img", class_="calendar-image")["src"]

    # Download the image
    image = Image.open(requests.get(image_src, stream=True).raw)

    # Save the image
    icon = image.save("calendar_image_of_the_day.png")
    
    return(icon)
    
