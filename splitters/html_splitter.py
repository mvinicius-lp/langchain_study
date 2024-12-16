# Carregar o documento HTML na memória
loader = UnstructuredHTMLLoader('white_house_executive_order_nov_2023.html')
data = loader.load()

# Definir variáveis
chunk_size = 300  # Tamanho máximo de cada fragmento
chunk_overlap = 100  # Sobreposição entre os fragmentos

# Dividir o HTML em fragmentos
splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,         # Definir tamanho do fragmento
    chunk_overlap=chunk_overlap,   # Definir sobreposição
    separators="."                 # Separadores usados para a divisão
)

docs = splitter.split_documents(data)
print(docs)  # Imprimir os fragmentos resultantes
