import sqlite3
from langchain_chroma import Chroma
from langchain_voyageai import VoyageAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from dotenv import load_dotenv

import os 

load_dotenv()


# Specify the path to the folder
folder_path = r"/workspaces/Projects/Hayek&You/data"

# Get a list of all files in the folder
files_name = os.listdir(folder_path)

# Print the names of all files
for file in files_name:
    print(file)