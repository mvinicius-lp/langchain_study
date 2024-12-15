llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key='<OPENAI_API_TOKEN>')

# Crie o histórico da conversa e adicione a primeira mensagem da IA
history = ChatMessageHistory()
history.add_ai_message("Hello! Ask me anything about Python programming!")  # "Olá! Pergunte-me qualquer coisa sobre programação em Python!"

# Adicione a mensagem do usuário ao histórico
history.add_user_message("What is a list comprehension?")  # "O que é uma list comprehension?"

# Adicione outra mensagem do usuário e chame o modelo
history.add_user_message("Describe the same in fewer words")  # "Descreva o mesmo em menos palavras"
response = llm.invoke(history.messages)
print(response.content)  # Imprime o conteúdo da resposta gerada pelo modelo
