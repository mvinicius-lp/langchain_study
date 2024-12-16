# Importar a biblioteca
from langchain_community.document_loaders import PyPDFLoader

# Criar um carregador de documentos para o arquivo rag_vs_fine_tuning.pdf
loader = PyPDFLoader('rag_vs_fine_tuning.pdf')

# Carregar o documento
data = loader.load()
print(data[0])
