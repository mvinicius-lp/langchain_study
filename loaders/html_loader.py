from langchain_community.document_loaders import UnstructuredHTMLLoader

# Criar um carregador de documentos para HTML não estruturado
loader = UnstructuredHTMLLoader('white_house_executive_order_nov_2023.html')

# Carregar o documento
data = loader.load()

# Imprimir o primeiro documento
print(data[0])

# Imprimir os metadados do primeiro documento
print(data[0].metadata)
