from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()


template = PromptTemplate(input_variables = ["top_news"],
                          template = """You are a skilled writer assistant tasked with crafting a concise and engaging weekly newsletter summary. 
                                        Please use the provided top news articles to create a summary that is easy to understand and free of jargon. 
                                        When summarizing, aim to preserve the original meaning and tone of the news articles. 
                                        Consider adding only necessary context or transitional phrases to enhance clarity. 
                                        The summary should be approximately 500-1000 words in length. 
                                        Here are the top news articles for this week: {top_news}""")
   
llm = ChatGroq(model = "llama-3.1-70b-versatile",
               temperature = 1,
               max_tokens = 1000,
               timeout = None,
               max_retries = 2,
               stop_sequences = None)


def summarize_news(top_news : str):
    
    if top_news != "No news found":
    
        try:
            chain = template | llm
            response = chain.invoke({"top_news": top_news})
            
            return response.content
        
        except:
            raise Exception("An error occurred while summarizing the news articles. Please try again later.")
    
    else:
        raise Exception("No news found. Please try again later.")