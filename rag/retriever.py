# Carregar o PDF usando o PyPDFLoader
loader = PyPDFLoader('rag_vs_fine_tuning.pdf')
data = loader.load()

# Dividir o documento em fragmentos usando RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,        # Tamanho máximo de cada fragmento
    chunk_overlap=50       # Sobreposição entre os fragmentos
)
docs = splitter.split_documents(data) 

# Incorporar os documentos em um banco de vetores persistente usando Chroma
embedding_function = OpenAIEmbeddings(
    api_key='<OPENAI_API_TOKEN>',   # Chave de API do OpenAI
    model='text-embedding-3-small' # Modelo usado para criar embeddings
)
vectorstore = Chroma.from_documents(
    docs,                          # Documentos fragmentados
    embedding=embedding_function,  # Função de embeddings
    persist_directory=os.getcwd()  # Diretório para salvar o banco de dados
)

# Configurar o banco de vetores como um sistema de busca (retriever)
retriever = vectorstore.as_retriever(
    search_type="similaridade",       # Tipo de busca: similaridade
    search_kwargs={"k": 3}            # Retornar os 3 resultados mais similares
)
