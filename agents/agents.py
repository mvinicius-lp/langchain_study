# Defina as ferramentas
tools = load_tools(["wikipedia"])

# Defina o agente
agent = create_react_agent(llm, tools)

# Invoque o agente
response = agent.invoke({"messages": [("human", "Quantas pessoas vivem na cidade de Nova York?")]})
print(response)
