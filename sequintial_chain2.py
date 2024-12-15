learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="Eu quero aprender como {activity}. Você pode sugerir como posso aprender isso passo a passo?"
)

time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="Eu tenho apenas uma semana. Você pode criar um plano para me ajudar a atingir esse objetivo: {learning_plan}."
)

# Complete a cadeia sequencial com LCEL (não está claro o significado exato de "LCEL" no contexto, 
# pode ser um erro ou algo relacionado ao seu projeto)
seq_chain = ({"learning_plan": learning_prompt | llm | StrOutputParser()}
    | time_prompt
    | llm
    | StrOutputParser())

# Execute a cadeia
print(seq_chain.invoke({"activity": "learning_plan"}))
