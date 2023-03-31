from sqlalchemy import create_engine
from locacao.util.util import Utilidades
from locacao.repositorios.repositorio_locadora import RepositorioLocadora
from locacao.repositorios.repositorio_pessoa import RepositorioPessoa
from locacao.repositorios.repositorio_veiculo import RepositorioVeiculo
from locacao.ui.interface_grafica import InterfaceGrafica

def main():

    engine = create_engine(Utilidades.obter_connection_string(), echo=False)

    repo_locadora = RepositorioLocadora(engine)
    repo_pessoa = RepositorioPessoa(engine)
    repo_veiculo = RepositorioVeiculo(engine)

    ui = InterfaceGrafica(repo_locadora, repo_pessoa, repo_veiculo)
    ui.iniciar()

if __name__ == '__main__':
    main()