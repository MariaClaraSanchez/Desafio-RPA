from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook
from datetime import date

# Cria uma pasta de trabalho para conter a planilha
arquivo_excel = Workbook()

# Ativa a guia que já vem por padrão no Workbook
sheetVagas = arquivo_excel.active

# Pega a data de hoje para nomear a guia da planilha
today = date.today()

# Renomenado o título da guia para a data de hoje
sheetVagas.title = format(today)

# Escrevendo no arquivo o Nome/Local e Descrição da vaga
sheetVagas['A1'] = "Nome"
sheetVagas['B1'] = "Local"
sheetVagas['C1'] = "Descrição"

# Salvando o arquivo
arquivo_excel.save('Vagas do Dia.xlsx')


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--lang=pt-BR')
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)


driver.get('https://cadmus.com.br/vagas-tecnologia/')  # inicia o navegador
driver.maximize_window()  # maximiza o navegador

time.sleep(10)
# busca os titulos das vagas
vagas = driver.find_elements(By.XPATH, '//div[@class="box"]/h3')
time.sleep(2)

for vaga in vagas:
    print(vaga.accessible_name)
time.sleep(5)

locais = driver.find_elements(By.XPATH,)


driver.close()
