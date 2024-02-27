from openpyxl import load_workbook

# 1-ler pasta de trabalho e planilha
wb = load_workbook("data/pivot_table.xlsx")
sheet = wb["Relatório"]

# 2-acessando valor especifico
print(sheet["A3"].value)
print(sheet["B3"].value)

# 3-iterando valores por meio de loop
for i in range(2, 6):
    ano = sheet["A%s" %i].value
    am = sheet["B%s" %i].value
    bt = sheet["C%s" %i].value
    print("Em {0} o Aston Martin vendeu R$ {1} e o Bentley vendeu R$ {2}".format(ano, am, bt))