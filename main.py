from pydoc import describe
from subprocess import list2cmdline
from controllers.site_vagas_cadmus import SiteCadmus
from controllers.relatorio_vagas import Planilha
from controllers.enviaemail import Email


def start():
    site_cadmus = SiteCadmus()
    site_cadmus.acessar_vagas()
    vagas = site_cadmus.pegar_vagas()
    locais = site_cadmus.pegar_locais()
    descricao = site_cadmus.pegar_descricao_vagas(vagas)

    planilha = Planilha()
    planilha.formatar_planilha()
    planilha.escreve_dados(vagas, locais, descricao)
    email = Email('bruno.cabral@cadmus.com.br')
    email.enviar_email()


    


if __name__ == '__main__':
    start()
