# Importar a biblioteca
from langchain_community.document_loaders.csv_loader import CSVLoader

# Criar um carregador de documentos para o arquivo fifa_countries_audience.csv
loader = CSVLoader('fifa_countries_audience.csv')

# Carregar o documento
data = loader.load()
print(data[0])
