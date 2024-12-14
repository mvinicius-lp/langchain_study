import openai
import os

# Definindo a chave da API
api_key = os.getenv('TOKEN_ACCESS_OPENAI')

openai.api_key = api_key

# Definindo a consulta
question = "Whatever you do, take care of your shoes"

# Fazendo a chamada da completions com o modelo especificado
response = openai.Completion.create(
    model="gpt-3.5-turbo",  
    prompt=question,
    max_tokens=50
)

# Imprimindo a resposta
print(response.choices[0].text.strip())
