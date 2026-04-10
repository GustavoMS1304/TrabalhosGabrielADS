from __future__ import annotations

from typing import List


def busca_binaria(lista_ordenada: List[int], alvo: int) -> int:
    """
    Busca Binária.

    Pré-requisito:
    - A lista precisa estar ORDENADA (crescente).

    Ideia:
    - Divide o intervalo ao meio, compara com o elemento do meio e descarta
      metade do intervalo a cada passo.

    Retorno:
    - Índice do elemento encontrado
    - -1 se não encontrar.

    Onde é chamada:
    - Em src/experimento.py, dentro de 'executar_experimentos()', a função
      'medir_tempo()' chama 'busca_binaria(lista_ordenada, alvo)' para medir
      o tempo dessa estratégia.
    """
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista_ordenada[meio] == alvo:
            return meio
        if lista_ordenada[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1
