from typing import List, Tuple

from src.dominio.entidade import Livro
from src.infra.repositorio import LivroRepositorio


class LivroServico:
    def __init__(self):
        self._livro_repositorio = LivroRepositorio()

    def salva_livro(self, livro: Livro):
        self._livro_repositorio.salva(livro)

    def get_livros(self) -> List[Tuple]:
        return self._livro_repositorio.get_livros()
