from src.dominio.entidade import Livro, Sessao
from src.servico.amazonas_servico import AmazonasServico


def cria_entidade_sessao_livro(amazonas_servico: AmazonasServico, sessao: Sessao, livro: Livro):
    amazonas_servico.salva_sessao(sessao)
    amazonas_servico.salva_livro(livro)


def main():
    # inicio o serviço
    amazonas_servico = AmazonasServico()

    # criamos as entidades modelos
    # vamos executar o servico
    sessao = Sessao(codigo=1, nome="Ficcao cientifica", descricao="", localizacao="C10L10P001")
    livro = Livro(codigo=1, titulo="Era os Deuses Astronautas", autor="Erik Von Danniken", codigo_sessao=sessao.codigo)
    cria_entidade_sessao_livro(amazonas_servico, sessao, livro)

    sessao = Sessao(codigo=2, nome="Dicionario", descricao="", localizacao="C11L11P001")
    livro = Livro(codigo=2, titulo="Portugues", autor="Aurelio", codigo_sessao=sessao.codigo)
    cria_entidade_sessao_livro(amazonas_servico, sessao, livro)

    sessao = Sessao(codigo=3, nome="Dicionario", descricao="", localizacao="C12L12P002")
    livro = Livro(codigo=3, titulo="Ingles", autor="Shakespary", codigo_sessao=sessao.codigo)
    cria_entidade_sessao_livro(amazonas_servico, sessao, livro)

    # mostra todos os livros e sessoes
    print(amazonas_servico.get_livros())
    print(amazonas_servico.get_sessoes())


if __name__ == "__main__":
    main()

