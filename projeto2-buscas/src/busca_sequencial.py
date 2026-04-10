from __future__ import annotations

from typing import List


def busca_sequencial(lista: List[int], alvo: int) -> int:
    """
    Busca Sequencial (ou Linear Search).

    O que faz:
    - Percorre a lista do início ao fim.
    - Compara cada elemento com o 'alvo'.

    Retorno:
    - Índice do elemento encontrado (0..n-1)
    - -1 se não encontrar.

    Onde é chamada:
    - Em src/experimento.py, dentro de 'executar_experimentos()', a função
      'medir_tempo()' chama 'busca_sequencial(lista_desordenada, alvo)' para
      medir o tempo dessa estratégia.
    """
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1

