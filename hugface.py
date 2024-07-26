from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAI
import google.generativeai as genai

from dotenv import load_dotenv

# Load environment variables
load_dotenv()



# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
llm = ChatGoogleGenerativeAI(model="Final Course List (July - Dec 2023)")


# Load environment variables from .env file
load_dotenv()
sec_key = os.getenv('HF_TOKEN')

print("Hugging Face Token:", sec_key)
# Use the token key in your LangChain setup or API calls

#os.environ["HUGGINGFACEHUB_TOKEN"] = sec_key

#  print("Hugging Face Token:", HF_TOKEN)

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id,max_length=128,temperature=0.7,token=sec_key)
result = llm.invoke("who is mahendra singh dhoni")

print(result)