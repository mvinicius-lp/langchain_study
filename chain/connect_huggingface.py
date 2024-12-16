from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()

# Definir o token da API do Hugging Face
huggingfacehub_api_token = os.getenv('TOKEN_ACCESS_HUGGINGFACE')

# Definir o modelo LLM
llm = HuggingFaceEndpoint(
    repo_id='tiiuae/falcon-7b-instruct', 
    huggingfacehub_api_token=huggingfacehub_api_token
)

# Prever as palavras que seguem o texto da questão
question = 'Whatever you do, take care of your shoes'
output = llm.invoke(question)

print(output)
