from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from dados import user, password
import time


navegador = Chrome()
navegador.get('http://projectpro.com.br/eproject.aspx')
time.sleep(5)

usuario = navegador.find_element_by_id('txtUsuario')
usuario.send_keys(user)
senha = navegador.find_element_by_id('txtsenha')
senha.send_keys(password)
entrar = navegador.find_element_by_id('btnLogin')
entrar.send_keys(Keys.RETURN)

time.sleep(5)

navegador.get(
    'http://projectpro.com.br/Modulos/Lancamentos/AutoLancamento.aspx')

time.sleep(10)
navegador.close()
