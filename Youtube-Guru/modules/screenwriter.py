from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv


load_dotenv() # Load the .env file


# Initializing the LLM
llm = ChatGroq(model = "llama-3.3-70b-versatile",
               temperature = 1,
               max_tokens = 10000,
               timeout = None,
               max_retries = 2,
               stop_sequences = None)


system_prompt = ("You are Frederich Hayek, expert on Austrian economics, that answers questions about economy and related topics,"
                 "Using the following pieces of retrieved context from Hayek books to answer the question."
                 "If the question is not about economy, just say 'I am not an expert', and then answer the question."
                 "\n\n"
                 "{context}")

prompt = ChatPromptTemplate.from_messages([MessagesPlaceholder(variable_name = "chat_history"),
                                                              ("human", "{input}"),
                                                              ("system", system_prompt)])


chain = prompt | llm


# This library stores the conversation history in streamlit memory, allowing the agent to mantain context during the conversation
memory = StreamlitChatMessageHistory()
memory.add_message(SystemMessage(content = system_prompt)) # Start the conversation with the system message


def ask_to_hayek(user_input : str):
    """Ask a question to the Hayek agent, and print the response as well as storing it in memory.
    
    Args:
        user_input (str): The user's question to the agent"""
    memory.add_message(HumanMessage(content = user_input))
    
    response = chain.invoke({"input":user_input, "chat_history": memory.messages})
    
    memory.add_message(AIMessage(content = response['answer']))
    
    
    return response["answer"]
    

def clear_memory():
    "Clear the conversation history and reset the agent to the initial state by adding the system message again to the memory."
    memory.clear()
    
    memory.add_message(SystemMessage(content = system_prompt))