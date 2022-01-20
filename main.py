from pydoc import describe
from subprocess import list2cmdline
from controllers.site_vagas_cadmus import SiteCadmus


def start():
    site_cadmus = SiteCadmus()
    site_cadmus.acessar_vagas()

    vagas = site_cadmus.pegar_vagas()
    print(vagas)
    locais = site_cadmus.pegar_locais()
    print(locais)
    descricao = site_cadmus.pegar_descricao_vagas(vagas)
    print(descricao)


if __name__ == '__main__':
    start()
