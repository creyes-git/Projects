from pdf_generator import gen_pdf
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import shutil
import time
import json
import os


# Page configuration
st.set_page_config(page_title = "Pocket PDF", page_icon = "🖨", layout = "centered", initial_sidebar_state = "expanded")
# Page Welcome Message
st.title(":orange[Welcome to PDF Generator APP]")


# App functions
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

        
with st.sidebar: # Sidebar
    
    st_lottie(load_lottiefile("my_lottie.json"), height = 150, quality = "high")

    st.write(":orange[Check template and import a valid file:]")
    
    template_button = st.download_button(label = "Download Template", 
                                         data = open(r"data/import_template.csv", "r").read(), 
                                         use_container_width = True,
                                         file_name = "import_template.csv",
                                         help = "See the template file to import your data",
                                         type = "primary")
    
    uploaded_file = st.file_uploader("", type = ["csv", "xlsx"] , key="unique_key", accept_multiple_files = False)
    
    placeholder = st.empty() # Empty placeholder to be a enable or disable button depending on the uploaded status
    if uploaded_file is not None:
        preview_button = placeholder.button("Preview Data", type = "secondary", use_container_width = True)
    else:
        preview_button = placeholder.button("Preview Data", type = "secondary", use_container_width = True, disabled = True)
    
    st.write(":orange[**Upload Your Data to Generate:**]")
    
    placeholder2 = st.empty()
    if uploaded_file is not None:
        generate_pdf = placeholder2.button("Generate PDF", type="primary", use_container_width=True)
    else:
        generate_pdf = placeholder2.button("Generate PDF", type="primary", use_container_width=True, disabled=True)
    
    st.write(":orange[Generate PDF and then dowload it:]")
    
    placeholder3 = st.empty()
    if uploaded_file is not None:
        dowload_zip = placeholder3.download_button(label = "Download PDF", 
                                                   data = open(r"data/Your_Pdfs.zip", "rb"), 
                                                   use_container_width = True,
                                                   type = "secondary",
                                                   mime="application/zip")
    else:
        dowload_zip = placeholder3.download_button(label = "Download PDF", 
                                                   data = open(r"data/Your_Pdfs.zip", "rb"),
                                                   use_container_width = True,
                                                   type = "secondary",
                                                   disabled = True)
        

if uploaded_file is not None:
    try:
        if "csv" in uploaded_file.type:
            df = pd.read_csv(uploaded_file, engine = "pyarrow") # Read the CSV file
            df = df.astype(str)
            
        elif "xml" in uploaded_file.type:
            df = pd.read_excel(uploaded_file) # Read the Excel file
            df = df.astype(str)
        
    except Exception as e:
        st.error(e)
          
                    
if preview_button:
    st.dataframe(df.head(100),hide_index = True, use_container_width = True,) # Display the data in a table
        
        
if generate_pdf:
    
    #for i in df.columns: # Not nedded if the data came directly from the database
    #    if df[i].dtype == "object":
    #       df[i] = df[i].str.replace("__EMPTY__VALUE__", "")
         
        
    my_bar = st.progress(0, text = "Generating your PDFs. Please wait...")
       
    for index, row in df.iterrows(): # Using iterrows() instead of df.apply() because the function gen_pdf() dont return anything
        
        time.sleep(0.01)
        my_bar.progress(index + 1, text="Generating your PDFs. Please wait...")
        
        try:    
            gen_pdf(sku=row["sku"], 
                        brand=row["brand"], 
                        name=row["name"], 
                        upc=row["upc"], 
                        finish=row["finish"], 
                        collection=row["collection_name"],
                        primary_image_url=row["Image"],
                        alt_image1_url=row["Alt Image 1"],
                        alt_image2_url=row["Alt Image 2"],
                        alt_image3_url=row["Alt Image 3"],
                        weight=row["weight"], 
                        height=row["height"], 
                        width=row["width"], 
                        length=row["length"],
                        bulb_inlcuded=row["bulb_included"], 
                        number_bulbs=row["number_of_bulbs"], 
                        bulb_type=row["type_of_bulbs"], 
                        bulb_base=row["type_of_bulbs"], 
                        max_wattage=row["max_wattage"], 
                        CRI=row["cri"], 
                        color_temp=row["color_temp"], 
                        lumens=row["lumens"],
                        safety_rating=row["safety_rating"],
                        voltage=row["voltage"],
                        shipping_via = row["Shipped Via"])
        
        except Exception as e:
            st.error(str(e))
    
    st.balloons()
    st.success("Your PDFs have been generated, now download them, thanks for use Pocket PDF!")
    
    time.sleep(1)
    my_bar.empty()
    
    if os.path.exists("data/Your_Pdfs.zip"):
        os.remove("data/Your_Pdfs.zip")
    
    # Zip the PDF's to a single file ready to dowload by the user
    file_path = 'data/saved_pdf'
    output_path = 'data/Your_Pdfs'
    shutil.make_archive(output_path, 'zip', file_path)
