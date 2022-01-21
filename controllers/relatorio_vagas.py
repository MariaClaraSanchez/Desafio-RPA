from openpyxl import Workbook
from openpyxl.styles import Font, Alignment
from datetime import date
import re

class Planilha:
    def __init__(self) -> None:
        # Cria uma pasta de trabalho para conter a planilha
        self.arquivo_excel = Workbook()
        # # Ativa a guia que já vem por padrão no Workbook
        self.sheetVagas = self.arquivo_excel.active
       

    def formatar_planilha(self) -> None:

        # Renomenado o título da guia para a data de hoje
        self.sheetVagas.title = format(date.today())

        # # Escrevendo no arquivo o Nome/Local e Descrição da vaga
        self.sheetVagas['A1'] = "Nome"
        self.sheetVagas['B1'] = "Local"
        self.sheetVagas['C1'] = "Descrição"

        self.sheetVagas['A1'].font = Font(
            size=18, bold=True)  # Fonte em Negrito
        self.sheetVagas['B1'].font = Font(
            size=18, bold=True)  # Fonte em Negrito
        self.sheetVagas['C1'].font = Font(
            size=18, bold=True)  # Fonte em Negrito

        self.sheetVagas['A1'].alignment = Alignment(
            horizontal='center', vertical='center')
        self.sheetVagas['B1'].alignment = Alignment(
            horizontal='center', vertical='center')
        self.sheetVagas['C1'].alignment = Alignment(
            horizontal='center', vertical='center')

        # Dimensão da coluna A
        self.sheetVagas.column_dimensions['A'].width = 50

        # Dimensão da coluna B
        self.sheetVagas.column_dimensions['B'].width = 20

        # Dimensão da coluna C
        self.sheetVagas.column_dimensions['C'].width = 70

        self.arquivo_excel.save('vagas.xlsx')

    def escreve_dados(self,dados_vagas: dict) -> None:
        i = 0
        for vaga in  dados_vagas:
            self.sheetVagas.cell(row=i+2, column=1).value = vaga
            self.sheetVagas.cell(row=i+2, column=2).value = dados_vagas[vaga]['local']
            descricao = re.sub('\n', ' ',dados_vagas[vaga]['descricao'])
            self.sheetVagas.cell(row=i+2, column=3).value = descricao
            self.sheetVagas[f'A{i+2}'].alignment = Alignment(vertical='center')
            self.sheetVagas[f'B{i+2}'].alignment = Alignment(vertical='center')
            self.sheetVagas[f'C{i+2}'].alignment = Alignment(wrap_text=True)
            i += 1
        self.arquivo_excel.save('vagas.xlsx')
