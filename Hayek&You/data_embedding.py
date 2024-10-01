from settings import *
from langchain_chroma import Chroma
from langchain_voyageai import VoyageAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from dotenv import load_dotenv
import os 

load_dotenv()

# Get a list of all files in the folder
books_folder = r"/workspaces/Projects/Hayek&You/data"
files_names = os.listdir(books_folder)

for file in files_names[:3]:
    
    if ".pdf" in file: # If the file is .pdf then use PyPDFLoader and TextLoader for txt files 
        document = PyPDFLoader(fr"{books_folder}/{file}").load()
    else:
        document = TextLoader(fr"{books_folder}/{file}").load()
        
        
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splitted_documents = text_splitter.split_documents(document)
    print(f"Chunks created for {file}: {len(splitted_documents)}") # Print the number of chunks for each file
    
    
    embeddings = VoyageAIEmbeddings(model="voyage-3", batch_size= 128) # Embedding model from VoyageAI
    
    
    if not os.path.exists("Hayek&You/chroma-db"): # Check if the database exists
        chroma_db = Chroma.from_documents(documents = splitted_documents, embedding = embeddings, persist_directory = "Hayek&You/chroma-db")
    else:
        chroma_db = Chroma(persist_directory = "Hayek&You/chroma-db")
        chroma_db.add_documents(documents = splitted_documents, embedding_function = embeddings)
    