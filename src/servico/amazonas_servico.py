from typing import List, Tuple

from src.dominio.entidade.livro import Livro
from src.dominio.entidade.sessao import Sessao
from src.infra.repositorio import LivroRepositorio, SessaoRepositorio


class AmazonasServico:
    def __init__(self):
        self._livro_repositorio = LivroRepositorio()
        self._sessao_repositorio = SessaoRepositorio()

    def salva_livro(self, livro: Livro):
        self._livro_repositorio.salva(livro)

    def salva_sessao(self, sessao: Sessao):
        self._sessao_repositorio.salva(sessao)

    def get_livros(self) -> List[Tuple]:
        return self._livro_repositorio.get_livros()

    def get_sessoes(self) -> List[Tuple]:
        return self._sessao_repositorio.get_sessoes()

