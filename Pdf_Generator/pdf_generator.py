from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from PIL import Image
from io import BytesIO
from datetime import datetime
import requests


def get_url_img(url):
   
   no_img = ImageReader(r"/workspaces/Projects/Pdf_Generator/images/no_picture_url.png")
   
   if not url or url.strip() == "":
      return no_img
    
   try:
      response = requests.get(url, timeout=10)
        
      image = Image.open(BytesIO(response.content))
   
      return ImageReader(image)
      
   except:
      return no_img


def gen_pdf(sku, brand, name, upc = " ", finish = " ", collection = " ",
                 primary_image_url = " ", alt_image1_url = " ", alt_image2_url = " ", alt_image3_url = " ",
                 weight = " ", height = " ", width = "", length = " ", canopy_height = " ", canopy_width = " ",
                 shipping_weight = " ", shipping_height = " ", shipping_width = " ", shipping_length = " ", shipping_via = " ",
                 shade_included = " ", shade_height = " ", shade_width = " ", shade_length = " ",
                 bulb_inlcuded = " ", number_bulbs = " ", bulb_type = " ", bulb_base = " ", max_wattage = " ", CRI = " ", color_temp = " ", lumens = " ",
                 safety_rating = " ", ul_wet_damp_location = " ", voltage = " ",
                 shade = " ", glass = " ", cyrstal = " ",
                 chain_length = " ", extensions_stems = " ", adjustable_stems_rods = " ", adjustable_height = " ", dual_mount_included = " "):  
    
   # CREATING THE CANVAS AND USING THE ACTUAL SKU AS PDF NAME ON THE DIRECTORY ---------------------------------------------
   
   try:
      pdf = canvas.Canvas(fr"/workspaces/Projects/Pdf_Generator/data/saved_pdf/Speec_sheet-{sku}.pdf", pagesize=letter)
   except:
      print(f"Path not found, creating a new one")
   
   # LAYOUT: TOP BRAND LOGO ------------------------------------------------------------------------------------------------
   
   try:
      logo = ImageReader(fr"/workspaces/Projects/Pdf_Generator/images/{brand}.png")
      pdf.drawImage(logo, x = 251, y = 685, width = 110, height = 110, mask='auto') # mask = 'auto' to preserve transparency
   except:
      print(f"No logo for {brand} on the images folder")
   
   # TAKING HEADERS COLOR BY BRAND -----------------------------------------------------------------------------------------
   
   if brand in ["Alora", "Beacon Lighting", "Big Ass Fans", "Corbett Lighting", "CWI Lighting", "Elan", "Gama Sonic", "Golden Lighting", "Sonneman", "Vaxcel", "Lucas McKearn", "Meridian"]:
      color = "gold"
   elif brand in ["Access Lighting", "Acclaim Lighting", "AFX Lighting", "Bulbrite", "EGLO", "Eurofase", "Kichler", "Trade Winds Lighting", "Progress Lighting", "Minka-Aire", "Quoizel", "Maxim Lighting"]:
      color = "blue"
   elif brand in ["ET2 Lighting", "Legrand", "Oxygen Lighting"]:
      color = "red"
   elif brand == "Allegri":
      color = "purple"
   elif brand == "Hunter Fans":
      color = "green"
   else:
      color = "brown"
   
   # LAYOUT: RIGTH SIDE ----------------------------------------------------------------------------------------------------

   pdf.setFont("Helvetica-Bold", 12, leading = 3) # Font for Name
   pdf.setFillColor(color) # Color for Name
   pdf.drawString(x = 45, y = 675 , text = " ".join(str(name).split(' ')[0:3])) # Name
   
   # First pdf block
   pdf.setFont("Helvetica-Bold", 9, leading = 3) # Font for regular text
   pdf.setFillColor("black") # Color for regular text
   pdf.drawString(x = 45, y = 640 , text = f"SKU: {sku}") # Draw the SKU with a different font
   pdf.setFont("Helvetica", 9, leading = 3) # Font for regular text
   pdf.drawString(x = 45, y = 620 , text = f'''Finish: {" ".join(str(finish).split(' ')[0:2])}''')
   pdf.drawString(x = 45, y = 600 , text = f'''Print Date: {datetime.now().strftime("%m/%d/%Y")}''') # right now date
   pdf.drawString(x = 175, y = 620 , text = f'''UPC: {str(upc).split(".")[0]}''')
   pdf.drawString(x = 175, y = 600 , text = f'''Collection: {" ".join(str(collection).split(' ')[0:2])}''')
   
   # Images lines container
   pdf.setLineWidth(1) 
   pdf.line(x1 = 45, y1 = 580, x2 = 290, y2 = 580)
   imagen = get_url_img(primary_image_url)
   pdf.drawImage(imagen, x = 56, y = 356, width = 223, height = 223, mask = 'auto') # Product Primary Image
   pdf.line(x1 = 45, y1 = 355, x2 = 290, y2 = 355)
   alt1 = get_url_img(alt_image1_url) # get the image using my function
   alt2 = get_url_img(alt_image2_url)
   alt3 = get_url_img(alt_image3_url)
   pdf.drawImage(alt1, x = 45, y = 286, width = 67.5, height = 67.5, mask = 'auto') # Alt1
   pdf.drawImage(alt2, x = 134, y = 286, width = 67.5, height = 67.5, mask = 'auto') # Alt2 134 is the median of Alt1 and Alt3
   pdf.drawImage(alt3, x = 223, y = 286, width = 67.5, height = 67.5, mask = 'auto') # Alt3
   pdf.line(x1 = 45, y1 = 285, x2 = 290, y2 = 285)
   
   # Second pdf block
   pdf.setFont("Helvetica-Bold", 9, leading = 3) # Font for headers
   pdf.setFillColor(color) # Color for headers
   pdf.drawString(x = 45, y = 265 , text = "PRODUCT DIMENSIONS")
   pdf.setFont("Helvetica", 9, leading = 3)
   pdf.setFillColor("black") 
   pdf.drawString(x = 45, y = 245 , text = f"Weight: {weight}")
   pdf.drawString(x = 45, y = 230 , text = f"Height (Top to Bottom): {height}")
   pdf.drawString(x = 45, y = 215 , text = f"Width (Side to Side): {width}")
   pdf.drawString(x = 45, y = 200 , text = f"Length (Side to Side): {length}")
   pdf.drawString(x = 45, y = 185 , text = f"Canopy Height (Top to Bottom): {canopy_height}")
   pdf.drawString(x = 45, y = 170 , text = f"Canopy Width (Side to Side): {canopy_width}")
   pdf.line(x1 = 45, y1 = 160, x2 = 290, y2 = 160)
   
   # Second pdf block
   pdf.setFont("Helvetica-Bold", 9, leading = 3)
   pdf.setFillColor(color)
   pdf.drawString(x = 45, y = 140 , text = "SHIPPING DIMENSIONS")
   pdf.setFont("Helvetica", 9, leading = 3)
   pdf.setFillColor("black") 
   pdf.drawString(x = 45, y = 120 , text = f"Weight: {shipping_weight}")
   pdf.drawString(x = 45, y = 105 , text = f"Height (Top to Bottom): {shipping_height}")
   pdf.drawString(x = 45, y = 90 , text = f"Width (Side to Side): {shipping_width}")
   pdf.drawString(x = 45, y = 75 , text = f"Length (Side to Side): {shipping_length}")
   pdf.drawString(x = 45, y = 60 , text = f"Shipped Via: {shipping_via}")
   
   # LAYOUT: LEFT SIDE -----------------------------------------------------------------------------------------------------
   
   # First pdf block
   pdf.setLineWidth(0.5) 
   pdf.setFont("Helvetica-Bold", 9, leading = 3)
   pdf.setFillColor(color)
   pdf.drawString(x = 320, y = 675 , text = "SHADE INFORMATION")
   pdf.line(x1 = 320, y1 = 605, x2 = 567, y2 = 605)
   pdf.setFont("Helvetica", 9, leading = 3)
   pdf.setFillColor("black") 
   pdf.drawString(x = 320, y = 660 , text = f"Shade Included: {shade_included}")
   pdf.drawString(x = 320, y = 645 , text = f"Shade Height (Top to Bottom): {shade_height}")
   pdf.drawString(x = 320, y = 630 , text = f"Shade Width (Side to Side): {shade_width}")
   pdf.drawString(x = 320, y = 615 , text = f"Shade Length (Front to Back): {shade_length}")
   
   # Second pdf block
   pdf.setFont("Helvetica-Bold", 9, leading = 3)
   pdf.setFillColor(color)
   pdf.drawString(x = 320, y = 585 , text = "BULB INFORMATION")
   pdf.setFont("Helvetica", 9, leading = 3)
   pdf.setFillColor("black") 
   pdf.drawString(x = 320, y = 565 , text = f"Bulb Included: {bulb_inlcuded}")
   pdf.drawString(x = 320, y = 550 , text = f"Number of Bulbs: {number_bulbs}")
   pdf.drawString(x = 320, y = 535 , text = f"Bulb Type: {bulb_type}")
   pdf.drawString(x = 320, y = 520 , text = f"Bulb Base: {bulb_base}")
   pdf.drawString(x = 320, y = 505 , text = f"Max. Wattage per Socket: {max_wattage}")
   pdf.drawString(x = 320, y = 490 , text = f"CRI: {CRI}")
   pdf.drawString(x = 320, y = 475 , text = f"Color Temperature: {color_temp}")
   pdf.drawString(x = 320, y = 460 , text = f"LUMENS: {lumens}")
   pdf.line(x1 = 320, y1 = 450, x2 = 567, y2 = 450)
   
   # Thrid pdf block
   pdf.setFont("Helvetica-Bold", 9, leading = 3)
   pdf.setFillColor(color)
   pdf.drawString(x = 320, y = 435 , text = "OTHER INFORMATION")
   pdf.setFont("Helvetica", 9, leading = 3)
   pdf.setFillColor("black") 
   pdf.drawString(x = 320, y = 420 , text = f"Safety Rating: {safety_rating}")
   pdf.drawString(x = 320, y = 405 , text = f"UL Wet/Damp Location: {ul_wet_damp_location}")
   pdf.drawString(x = 320, y = 390 , text = f"Voltage: {voltage}")
   pdf.line(x1 = 320, y1 = 380, x2 = 567, y2 = 380)
   
   # Fourth pdf block
   pdf.setFont("Helvetica-Bold", 9, leading = 3)
   pdf.setFillColor(color)
   pdf.drawString(x = 320, y = 360 , text = "MATERIALS")
   pdf.setFont("Helvetica", 9, leading = 3)
   pdf.setFillColor("black") 
   pdf.drawString(x = 320, y = 345 , text = f"Shade: {shade}")
   pdf.drawString(x = 320, y = 330 , text = f"Glass: {glass}")
   pdf.drawString(x = 320, y = 315 , text = f"Crystal: {cyrstal}")
   pdf.line(x1 = 320, y1 = 305, x2 = 567, y2 = 305)
   
   # Fifth pdf block
   pdf.setFont("Helvetica-Bold", 9, leading = 3)
   pdf.setFillColor(color)
   pdf.drawString(x = 320, y = 285 , text = "HANGING METHOD ")
   pdf.setFont("Helvetica", 9, leading = 3)
   pdf.setFillColor("black") 
   pdf.drawString(x = 320, y = 270 , text = f"Chain Length: {chain_length}")
   pdf.drawString(x = 320, y = 255 , text = f"Extension Stems: {extensions_stems}")
   pdf.drawString(x = 320, y = 240 , text = f"Adjustable Stems/Rods: {adjustable_stems_rods}")
   pdf.drawString(x = 320, y = 225 , text = f"Adjustable Height: {adjustable_height}")
   pdf.drawString(x = 320, y = 210 , text = f"Dual Mount Hang Included: {dual_mount_included}")
   pdf.line(x1 = 320, y1 = 195, x2 = 567, y2 = 195)
   
   # Sixth pdf block
   pdf.setFont("Helvetica-Bold", 9, leading = 3)
   pdf.setFillColor(color)
   pdf.drawString(x = 320, y = 175 , text = "FILLING INFORMATION")
   pdf.setFont("Helvetica", 9, leading = 3)
   pdf.setFillColor("black") 
   pdf.drawString(x = 320, y = 155 , text = "Project Name: ______________________________________")
   pdf.drawString(x = 320, y = 131.25 , text = "Location: __________________________________________")
   pdf.drawString(x = 320, y = 107.5 , text = "Type: _____________________________________________")
   pdf.drawString(x = 320, y = 83.75 , text = "Quantity: __________________________________________")
   pdf.drawString(x = 320, y = 60 , text = "Comments: ________________________________________")
   
   
   pdf.save() # Saving the pdf on the name path