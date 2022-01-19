from openpyxl import Workbook
from datetime import date

# Cria uma pasta de trabalho para conter a planilha
arquivo_excel = Workbook()

# # Ativa a guia que já vem por padrão no Workbook
sheetVagas = arquivo_excel.active

# # Pega a data de hoje para nomear a guia da planilha
today = date.today()

# # Renomenado o título da guia para a data de hoje
sheetVagas.title = format(today)

# # Escrevendo no arquivo o Nome/Local e Descrição da vaga
sheetVagas['A1'] = "Nome"
sheetVagas['B1'] = "Local"
sheetVagas['C1'] = "Descrição"


# Salvando o arquivo
arquivo_excel.save('Vagas do Dia.xlsx')
