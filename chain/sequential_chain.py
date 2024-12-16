# Crie um modelo de prompt que receba uma atividade como entrada
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="Eu quero aprender como {activity}. Você pode sugerir como posso aprender isso passo a passo?"
)

# Crie um modelo de prompt que coloque uma restrição de tempo na resposta
time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="Eu tenho apenas uma semana. Você pode criar um plano para me ajudar a atingir esse objetivo: {learning_plan}."
)

# Invoque o learning_prompt com uma atividade
print(learning_prompt.invoke({"activity": "learning_plan"}))
