from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()
api = os.getenv("GROQ_API_KEY")

llm = Groq(api_key=api)

def chat_with_Jacinto():
    
    print(" Hello, i'm Jacinto, your personal and free assistant. For quit you can type exit. How can i help you today?: ")
    
    while True:
        promt = input("You: ")
        
        if promt in ["exit", "quit"]:
            break
        
        response = llm.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user",
             "content": promt}
        ],
        temperature=1,
        max_tokens=100,
        stream=False)
        
        print(f"Jacinto: {response.choices[0].message.content}")
        
        
def good_morning():
    
        prompt = '''I'm sending an email report to my boss, i wanto you to create a good morning message with less than 30 characters and being nice fully and respectfully. 
                Give me the final message ready to send, do not add any additional text or comments. '''
        
        response = llm.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user",
             "content": prompt}
        ],
        temperature=1,
        max_tokens=30,
        stream=False)
        
        return str(response.choices[0].message.content)


def joke():
    
        prompt = '''Write a good joke about lamps and lights. Focus on a joke, not a story. Tell a medium length joke, be nice and respectful. '''
        
        response = llm.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user",
             "content": prompt}
        ],
        temperature=1,
        max_tokens=100,
        stream=False)
        
        return str(response.choices[0].message.content)
        
        
def gen_description(title, brand, collection_name):
    
    promt = f'''I want you to create a product description for a Lamp and Lights Store, do not use line breaks and do not add any additional text or comments,
            your answer should be in plain English and should be as detailed as possible, do not use more than 100 characters. 
            Please use the following information to create the description: 
            Product name: {title}, Product brand: {brand}, Collection Name: {collection_name}.'''
               
    response = llm.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user",
             "content": promt}
        ],
        temperature=0.25,
        max_tokens=100,
        stream=False)
    
    print(f"Generated!")
    return str(f"{response.choices[0].message.content}")


def re_write(description):
    
    prompt = f''' I want you to re write this product description for a Lighting store, please do not add any additional text or comments, do not use line breaks.
                Your answer should be in plain English and should be as detailed as possible. Use this text as reference and try to get a similar result as possible: 
                Here is the text: {description}'''
                
    response = llm.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user",
            "content": prompt}
    ],
    temperature=0.55,
    max_tokens=150,
    stream=False)
    
    return str(f"{response.choices[0].message.content}")