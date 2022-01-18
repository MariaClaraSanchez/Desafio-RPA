from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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
driver.close()
