llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key='<OPENAI_API_TOKEN>')

# Define uma memória de buffer
memory = ConversationBufferMemory(size=4)

# Define a cadeia para integrar a memória ao modelo
buffer_chain = ConversationChain(llm=llm, memory=memory)

# Invoca a cadeia com as entradas fornecidas
buffer_chain.invoke("Write Python code to draw a scatter plot.")  
buffer_chain.invoke("Use the Seaborn library.")  
