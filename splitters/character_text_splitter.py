# Importar o separador de caracteres
from langchain_text_splitters import CharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Criar uma instância da classe de separação
splitter = CharacterTextSplitter(
    separator='\n',  # Usar '\n' como separador
    chunk_size=24,   # Tamanho máximo de cada parte
    chunk_overlap=10 # Sobreposição entre as partes
)

# Dividir a string e imprimir as partes
docs = splitter.split_text(quote)
print(docs)
print([len(doc) for doc in docs])  # Imprimir o tamanho de cada parte
