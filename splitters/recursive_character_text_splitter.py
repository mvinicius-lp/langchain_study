# Importar o separador recursivo de caracteres
from langchain_text_splitters import RecursiveCharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Criar uma instância da classe de separação
splitter = RecursiveCharacterTextSplitter(
    separators=["\n", " ", ""],  # Separadores utilizados na divisão
    chunk_size=chunk_size,       # Tamanho máximo de cada parte
    chunk_overlap=chunk_overlap  # Sobreposição entre as partes
)

# Dividir o documento e imprimir as partes
docs = splitter.split_text(quote)
print(docs)  # Imprimir as partes resultantes
print([len(doc) for doc in docs])  # Imprimir o tamanho de cada parte
