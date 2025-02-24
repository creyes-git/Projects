from settings import *
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_voyageai import VoyageAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import os 


load_dotenv() # Load the .env file


# Initializing the LLM
llm = ChatGroq(model = "llama-3.1-70b-versatile",
               temperature = 1,
               max_tokens = 300,
               max_retries = 2,
               stop_sequences = ["stop", "quit", "exit"])


# Initializing the embeddings
embedding_model = VoyageAIEmbeddings(model="voyage-3", 
                                        truncation= False, 
                                        batch_size= 128)


db_path = r"/workspaces/Projects/Hayek&You/data/chroma-db"

if os.path.exists(db_path): # Check if the database exists and load it
    vector_db = Chroma(persist_directory = db_path,
                       embedding_function = embedding_model,
                       collection_name = "langchain")
else:
    print("Database not found")


# Star creating the chains
context_q_prompt = ChatPromptTemplate.from_messages([MessagesPlaceholder(variable_name="chat_history"),
                                                     ("human",  "{input}"),
                                                     ("system", "Given a chat history and the latest user question"
                                                                "wich might reference context in the chat history, "
                                                                "formulate a standalone question wich can be understood"
                                                                "without the chat history. Do not answer the question"
                                                                "just reformulate it if needed and otherwise return it as is.")])

qa_system_prompt = ("You are Frederich Hayek, expert on Austrian economics, that answers questions about economy and related topics,"
                    "Using the following pieces of retrieved context from Hayek books to answer the question."
                    "If the question is not about economy, just say 'I am not an expert', and then answer the question."
                    "\n\n"
                    "{context}")

qa_prompt = ChatPromptTemplate.from_messages([MessagesPlaceholder(variable_name="chat_history"),
                                                                 ("human", "{input}"),
                                                                 ("system", qa_system_prompt)])



retriever = vector_db.as_retriever(search_type = "similarity", search_kwargs = {'k': 3})


history_awere_retriever = create_history_aware_retriever(llm, retriever, context_q_prompt)
qa_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
rag_chain = create_retrieval_chain(history_awere_retriever, qa_answer_chain)


# This library stores the conversation history in streamlit memory, allowing the agent to mantain context during the conversation
memory = StreamlitChatMessageHistory()
memory.add_message(SystemMessage(content = qa_system_prompt)) # Start the conversation with the system message


def ask_to_hayek(user_input : str):
    """
    Ask a question to the Hayek agent, and print the response as well as storing it in memory.
    
    Args:
        user_input (str): The user's question to the agent
    """
    memory.add_message(HumanMessage(content = user_input))
    
    response = rag_chain.invoke({"input":user_input, "chat_history": memory.messages})
    
    memory.add_message(AIMessage(content = response['answer']))
    
    
    return response["answer"]
    

def clear_memory():
    """
    Clear the conversation history and reset the agent to the initial state by adding the system message again to the memory.
    """
    memory.clear()
    
    memory.add_message(SystemMessage(content = qa_system_prompt))