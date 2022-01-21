from controllers.site_vagas_cadmus import SiteCadmus
from controllers.relatorio_vagas import Planilha
from controllers.email import Email

def start():
    site_cadmus = SiteCadmus()
    site_cadmus.acessar_vagas()
    vagas = site_cadmus.pegar_vagas()

    vagas = site_cadmus.pegar_descricao_vagas(vagas)
    planilha = Planilha()
    planilha.formatar_planilha()
    planilha.escreve_dados(vagas)


if __name__ == '__main__':
    start()
