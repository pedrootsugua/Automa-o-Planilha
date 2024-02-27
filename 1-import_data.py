import pandas as pd

# importando dados
data = pd.read_excel("data/VendaCarros.xlsx")
print(data)

# lista os primeiros registros
print(data.head())

# lista os ultimos registros
print(data.tail())

# contagem de valores por fabricante
print(data["Fabricante"].value_counts())