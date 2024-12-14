# Define an OpenAI chat model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key='<OPENAI_API_TOKEN>')		

# Create a chat prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "Respond to question: {question}")
    ]
)

# Chain the prompt template and model, and invoke the chain
llm_chain = prompt_template | llm
response = llm_chain.invoke({"question": "How can I retain learning?"})
print(response.content)