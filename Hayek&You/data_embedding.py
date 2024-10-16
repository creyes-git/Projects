from settings import *
from langchain_chroma import Chroma
from langchain_voyageai import VoyageAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os 

load_dotenv()

# Get a list of all files in the folder
books_folder = r"data"
files_names = os.listdir(books_folder)

all_documents = []

for file in files_names:
    
    if file.endswith(".pdf"): # If the file is .pdf then use PyPDFLoader and TextLoader for txt files 
        document = PyPDFLoader(fr"{books_folder}/{file}").load()
    else:
        pass
        
        
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splitted_documents = text_splitter.split_documents(document)
    all_documents.extend(splitted_documents)
    print(f"{len(splitted_documents)} Chunks created for the file: {file}") # Print the number of chunks for each file
    
    
embeddings = VoyageAIEmbeddings(model="voyage-3", batch_size= 128) # Embedding model from VoyageAI
    
    
db_path = r"data/chroma-db"
    
if not os.path.exists(db_path): # Check if the database exists
    chroma_db = Chroma.from_documents(documents = all_documents, embedding = embeddings, persist_directory = db_path)
    print("Database created successfully")
else:
    print("Database already exists")
