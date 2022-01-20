from subprocess import list2cmdline
from controllers.site_vagas_cadmus import SiteCadmus

def start() :
    site_cadmus = SiteCadmus()
    site_cadmus.acessar_vagas()

    list = site_cadmus.pegar_vagas()
    list2 = site_cadmus.pegar_descricao_vagas(list)
    
    print(list2)


if __name__ == '__main__':
    start()