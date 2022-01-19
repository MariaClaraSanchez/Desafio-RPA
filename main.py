from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
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

# Começando a parte de pegar os dados do site
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--lang=pt-BR')
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(
    options=chrome_options)

# inicia o navegador no site da cadmus
driver.get('https://cadmus.com.br/vagas-tecnologia/')


time.sleep(5)

# busca todas as vagas

vagas = driver.find_elements(By.XPATH, '//div[@class="box"]')
time.sleep(2)


# descrição
dados_vagas = []

# Contador para controlar o número de linhas da planilha
i = 0

# coleta as vagas e os locais das vagas
driver.execute_script("window.scrollTo(0,1000);")
time.sleep(2)
for vaga in vagas:

    titulo_el = vaga.find_element(By.TAG_NAME, 'h3')
    local_el = vaga.find_element(By.CLASS_NAME, 'local')
    titulo = titulo_el.text
    local = local_el.text
    print(f'Vaga: {titulo}')
    print(f'Local: {local}')

    # Titulo é chave

    dados_vagas.append({titulo: {
        'local': local,
        'descricao': None
    }})

    # Inserindo título e local da linha 2 em diante e coluna A1 e B1 respectivamente
    sheetVagas.cell(row=i+2, column=1).value = titulo
    sheetVagas.cell(row=i+2, column=2).value = local
    i += 1

time.sleep(5)


for vaga in dados_vagas:
    driver.execute_script("window.scrollTo(0,1000);")
    time.sleep(1)
    btn_descricao = '//div[@class="box"]/h3[contains(text(), "{}")]/../p/a'.format(
        list(vaga.keys())[0])
    link = driver.find_element(
        By.XPATH, btn_descricao)
    link.send_keys(Keys.RETURN)
    descricao = driver.find_element(
        By.XPATH, '//div[@class="box z-depth-1"]/p')
    print(descricao.text)
    driver.back()

# Contador para controlar o número de linhas da planilha
i = 0

# for vaga in vagas:
#     print(vaga.accessible_name)
#     # Insere o nome da vaga na coluna 1
#     sheetVagas.cell(row=i+2, column=1).value = vaga.accessible_name
#     i += 1

# # Fazer esse jeito para inserir a descrição na planilha
# textTest = dados_vagas[0]['Analista de Sistemas Sênior']['descricao'] = "Teste"
# sheetVagas.cell(row=2, column=3).value = textTest

# time.sleep(5)

print(dados_vagas)
# time.sleep(5)
driver.close()

# # Salvando o arquivo
arquivo_excel.save('Vagas do Dia.xlsx')
