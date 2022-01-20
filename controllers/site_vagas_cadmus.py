from dataclasses import replace
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re


class SiteCadmus:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--lang=pt-BR')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--log-level=3')

        self.driver = webdriver.Chrome(options=chrome_options)

    def acessar_vagas(self) -> None:
        self.driver.get('https://cadmus.com.br/vagas-tecnologia/')
        time.sleep(5)

    def pegar_vagas(self) -> list:
        vagas = self.driver.find_elements(By.XPATH, '//div[@class="box"]')
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,1000);")
        time.sleep(2)

        lista_vagas = []

        for vaga in vagas:

            titulo_el = vaga.find_element(By.TAG_NAME, 'h3')
            titulo = titulo_el.text

            lista_vagas.append(titulo)

        return lista_vagas

    def pegar_locais(self) -> list:
        vagas = self.driver.find_elements(By.XPATH, '//div[@class="box"]')
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,1000);")
        time.sleep(2)

        lista_locais = []

        for vaga in vagas:

            local_el = vaga.find_element(By.CLASS_NAME, 'local')
            local = local_el.text

            lista_locais.append(local)

        return lista_locais

    def pegar_descricao_vagas(self, lista_vagas: list) -> list:
        lista_descricao = []
        for vaga in lista_vagas:
            self.driver.execute_script("window.scrollTo(0,1000);")
            time.sleep(1)
            btn_descricao = '//div[@class="box"]/h3[contains(text(), "{}")]/../p/a'.format(
                vaga)
            link = self.driver.find_element(
                By.XPATH, btn_descricao)
            link.send_keys(Keys.RETURN)
            descricao = self.driver.find_element(
                By.XPATH, '//div[@class="box z-depth-1"]/p')

            descricao2 = re.sub('\n', ' ', descricao.text)

            print(descricao2)
            lista_descricao.append(
                descricao2
            )
            self.driver.back()

        return lista_descricao
