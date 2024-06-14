from src.dominio.entidade import Livro, Sessao
from src.servico.LivroServico import LivroServico
from src.servico.SessaoServico import SessaoServico


def cria_entidade_sessao(sessao_servico: SessaoServico, sessao: Sessao):
    sessao_servico.salva_sessao(sessao)


def cria_entidade_livro(livro_servico: LivroServico, livro: Livro):
    livro_servico.salva_livro(livro)


def main():
    # inicio os serviços
    livro_servico = LivroServico()
    sessao_servico = SessaoServico()

    # criamos as entidades modelos
    # vamos executar o servico
    sessao = Sessao(codigo=1, nome="Ficcao cientifica", descricao="", localizacao="C10L10P001")
    livro = Livro(codigo=1, titulo="Era os Deuses Astronautas", autor="Erik Von Danniken", codigo_sessao=sessao.codigo)
    cria_entidade_sessao(sessao_servico, sessao)
    cria_entidade_livro(livro_servico, livro)

    sessao = Sessao(codigo=2, nome="Dicionario", descricao="", localizacao="C11L11P001")
    livro = Livro(codigo=2, titulo="Portugues", autor="Aurelio", codigo_sessao=sessao.codigo)
    cria_entidade_sessao(sessao_servico, sessao)
    cria_entidade_livro(livro_servico, livro)

    sessao = Sessao(codigo=3, nome="Dicionario", descricao="", localizacao="C12L12P002")
    livro = Livro(codigo=3, titulo="Ingles", autor="Shakespary", codigo_sessao=sessao.codigo)
    cria_entidade_sessao(sessao_servico, sessao)
    cria_entidade_livro(livro_servico, livro)

    # mostra todos os livros e sessoes
    print(livro_servico.get_livros())
    print(sessao_servico.get_sessoes())


if __name__ == "__main__":
    main()

