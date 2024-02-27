import pandas as pd

# 1-importando dados
data = pd.read_excel("data/VendaCarros.xlsx")

# 2-selecionando colunas especificas do dataframe
df = data[["Fabricante",  "ValorVenda", "Ano"]]
print(df)

# 3-criando tabela pivô
pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda",
    aggfunc="sum"
)

print(pivot_table)

# 4-exportando tabela pivô em arquivo excel
pivot_table.to_excel("data/pivot_table.xlsx", "Relatório")