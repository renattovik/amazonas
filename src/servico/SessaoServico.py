from typing import List, Tuple

from src.dominio.entidade import Sessao
from src.infra.repositorio import SessaoRepositorio


class SessaoServico:
    def __init__(self):
        self._sessao_repositorio = SessaoRepositorio()

    def salva_sessao(self, sessao: Sessao):
        self._sessao_repositorio.salva(sessao)

    def get_sessoes(self) -> List[Tuple]:
        return self._sessao_repositorio.get_sessoes()

