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
driver = webdriver.Chrome(
    options=chrome_options)

# inicia o navegador no site da cadmus
driver.get('https://cadmus.com.br/vagas-tecnologia/%27')


time.sleep(10)
# busca todas as vagas
vagas = driver.find_elements(By.XPATH, '//div[@class="box"]')
time.sleep(2)


# descrição
dados_vagas = []

# coleta as vagas e os locais das vagas
for vaga in vagas:
    titulo_el = vaga.find_element(By.TAG_NAME, "h3")
    local_el = vaga.find_element(By.XPATH, '//p[@class="local"]')
    titulo = titulo_el.accessible_name
    local = local_el.get_attribute('innerHTML').replace(
        '<i class="fas fa-map-marker-alt"></i>', '')
    print(f'Vaga: {titulo}')
    print(f'Local: {local}')
    dados_vagas.append({titulo: {
        'local': local,
        'descricao': None
    }})

time.sleep(5)

print(dados_vagas[1])
driver.close()
