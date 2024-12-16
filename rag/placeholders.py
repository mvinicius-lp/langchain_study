# Adicionar marcadores de posição (placeholders) à string da mensagem
message = """
Responda à seguinte pergunta usando o contexto fornecido:

Contexto:
{context}

Pergunta:
{question}

Resposta:
"""

# Criar um template de prompt de chat a partir da string da mensagem
prompt_template = ChatPromptTemplate.from_messages([("human", message)])
