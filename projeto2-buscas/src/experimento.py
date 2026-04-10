from __future__ import annotations

"""
Arquivo principal do experimento (Projeto 2).

Aqui é onde tudo "se conecta":
- importa os 3 métodos de busca:
  - busca_sequencial()  -> src/busca_sequencial.py
  - busca_binaria()     -> src/busca_binaria.py
  - ArvoreBST.buscar()  -> src/arvore_bst.py

Fluxo geral (por tamanho n):
1) Gera lista aleatória
2) Ordena a lista (para busca binária)
3) Insere os mesmos valores na BST
4) Escolhe um alvo existente
5) Mede o tempo de cada método
6) Repete 30 vezes
7) Calcula média e desvio padrão
8) Imprime os resultados na tela
"""

import argparse
import random
import statistics
import time
from dataclasses import dataclass
from typing import List, Optional

from busca_binaria import busca_binaria
from busca_sequencial import busca_sequencial
from arvore_bst import ArvoreBST


@dataclass
class ResultadoPorTamanho:
    # Estrutura para guardar os resultados finais de um tamanho "n".
    # Esses valores são calculados em executar_experimentos() e depois
    # impressos no terminal em imprimir_resultados().
    tamanho: int
    media_sequencial: float
    desvio_sequencial: float
    media_binaria: float
    desvio_binaria: float
    media_bst: float
    desvio_bst: float


def medir_tempo(funcao, *args) -> float:
    # Mede o tempo (em segundos) da execução de uma função.
    # Onde é usada:
    # - executar_experimentos() chama medir_tempo() para cronometrar cada método.
    inicio = time.perf_counter()
    funcao(*args)
    fim = time.perf_counter()
    return fim - inicio


def executar_experimentos(
    tamanhos: List[int],
    repeticoes: int,
    semente: Optional[int],
) -> List[ResultadoPorTamanho]:
    # Núcleo do experimento:
    # - Para cada tamanho "n":
    #   - repete 'repeticoes' vezes:
    #       - gera dados aleatórios
    #       - escolhe o alvo
    #       - mede tempo de busca sequencial, binária e BST
    #   - calcula média e desvio padrão
    # - Retorna uma lista de ResultadoPorTamanho.
    rng = random.Random(semente)
    resultados: List[ResultadoPorTamanho] = []

    for tamanho in tamanhos:
        tempos_sequencial: List[float] = []
        tempos_binaria: List[float] = []
        tempos_bst: List[float] = []

        for _ in range(repeticoes):
            # 1) gerar lista aleatória
            dados = rng.sample(range(tamanho * 10), tamanho)
            # 4) escolher o alvo a ser buscado (pegamos um valor que existe em 'dados')
            alvo = rng.choice(dados)

            # 2) lista desordenada para busca sequencial
            lista_desordenada = dados[:]
            # 2) lista ordenada para busca binária
            lista_ordenada = sorted(dados)

            # 3) inserir os mesmos valores na BST
            arvore = ArvoreBST()
            for valor in dados:
                arvore.inserir(valor)

            # 5) medir o tempo de cada método
            #    (essas chamadas vão para os arquivos abaixo)
            #    - busca_sequencial -> src/busca_sequencial.py
            #    - busca_binaria    -> src/busca_binaria.py
            #    - arvore.buscar    -> src/arvore_bst.py
            tempos_sequencial.append(medir_tempo(busca_sequencial, lista_desordenada, alvo))
            tempos_binaria.append(medir_tempo(busca_binaria, lista_ordenada, alvo))
            tempos_bst.append(medir_tempo(arvore.buscar, alvo))

        # 7) calcular média e desvio padrão (desvio padrão amostral)
        resultados.append(
            ResultadoPorTamanho(
                tamanho=tamanho,
                media_sequencial=statistics.mean(tempos_sequencial),
                desvio_sequencial=statistics.stdev(tempos_sequencial) if len(tempos_sequencial) > 1 else 0.0,
                media_binaria=statistics.mean(tempos_binaria),
                desvio_binaria=statistics.stdev(tempos_binaria) if len(tempos_binaria) > 1 else 0.0,
                media_bst=statistics.mean(tempos_bst),
                desvio_bst=statistics.stdev(tempos_bst) if len(tempos_bst) > 1 else 0.0,
            )
        )

    return resultados


def imprimir_resultados(resultados: List[ResultadoPorTamanho]) -> None:
    # Imprime os resultados no terminal para facilitar a apresentação.
    print("Experimentos concluídos com sucesso!")
    for r in resultados:
        print(f"\nTamanho: {r.tamanho}")
        print(f"Busca Sequencial -> média: {r.media_sequencial:.10f} | desvio: {r.desvio_sequencial:.10f}")
        print(f"Busca Binária    -> média: {r.media_binaria:.10f} | desvio: {r.desvio_binaria:.10f}")
        print(f"Busca BST        -> média: {r.media_bst:.10f} | desvio: {r.desvio_bst:.10f}")


def _parse_lista_int(texto: str) -> List[int]:
    # Converte "100,500,1000" -> [100, 500, 1000]
    return [int(x.strip()) for x in texto.split(",") if x.strip()]


def main() -> None:
    # Entrada do programa:
    # - Lê parâmetros da linha de comando
    # - Executa os experimentos
    # - Imprime o resultado na tela
    parser = argparse.ArgumentParser(
        prog="experimento",
        description="Executa o benchmark de buscas: sequencial, binária e BST.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=(
            "Exemplos:\n"
            "  py -3.10 src/experimento.py -h\n"
            "  py -3.10 src/experimento.py --tamanhos 100,500,1000 --repeticoes 30 --semente 0\n"
        ),
    )
    parser.add_argument(
        "--tamanhos",
        type=str,
        default="1000,10000,100000",
        help="Lista separada por vírgula. Ex: 1000,5000,10000",
    )
    parser.add_argument("--repeticoes", type=int, default=30, help="Quantidade de execuções por tamanho.")
    parser.add_argument("--semente", type=int, default=0, help="Semente do gerador aleatório (reprodutibilidade).")
    args = parser.parse_args()

    tamanhos = _parse_lista_int(args.tamanhos)
    resultados = executar_experimentos(tamanhos=tamanhos, repeticoes=args.repeticoes, semente=args.semente)
    imprimir_resultados(resultados)


if __name__ == "__main__":
    main()

