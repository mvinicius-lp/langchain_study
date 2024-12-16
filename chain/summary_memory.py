api_key = '<SEU_TOKEN_API_AQUI>'
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)

# Define uma memória de resumo que usa um modelo de chat OpenAI
memory = ConversationSummaryMemory(llm=llm)

# Define a cadeia para integrar a memória ao modelo
summary_chain = ConversationChain(llm=llm, memory=memory, verbose=True)

# Invoca a cadeia com as entradas fornecidas
summary_chain.invoke("Describe the relationship of the human mind with the keyboard when taking a great online class.")  
summary_chain.invoke("Use an analogy to describe it.")  
