from __future__ import annotations


class No:
    """
    Nó da Árvore Binária de Busca (BST).

    Campos:
    - valor: valor armazenado no nó
    - esquerda: referência para o filho da esquerda
    - direita: referência para o filho da direita
    """

    def __init__(self, valor: int) -> None:
        self.valor = valor
        self.esquerda: "No | None" = None
        self.direita: "No | None" = None


class ArvoreBST:
    """
    Árvore Binária de Busca (BST - Binary Search Tree).

    Regras da BST:
    - Valores menores que o nó ficam na subárvore esquerda.
    - Valores maiores que o nó ficam na subárvore direita.

    Onde é usada:
    - Em src/experimento.py, durante cada repetição:
      1) cria ArvoreBST()
      2) insere os mesmos valores da lista aleatória
      3) mede o tempo de 'arvore.buscar(alvo)'
    """

    def __init__(self) -> None:
        self.raiz: No | None = None

    def inserir(self, valor: int) -> None:
        # Ponto de entrada da inserção. Chama a função recursiva _inserir()
        # e atualiza a raiz, caso a árvore esteja vazia.
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no: No | None, valor: int) -> No:
        # Inserção recursiva:
        # - Se chegou em um ponto vazio, cria um novo Nó.
        # - Senão, desce para esquerda/direita conforme comparação.
        if no is None:
            return No(valor)

        if valor < no.valor:
            no.esquerda = self._inserir(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._inserir(no.direita, valor)

        return no

    def buscar(self, valor: int) -> bool:
        # Ponto de entrada da busca. Chama a função recursiva _buscar().
        return self._buscar(self.raiz, valor)

    def _buscar(self, no: No | None, valor: int) -> bool:
        # Busca recursiva:
        # - Se chegar em None: não encontrou.
        # - Se for igual: encontrou.
        # - Senão desce para esquerda/direita de acordo com a regra da BST.
        if no is None:
            return False
        if no.valor == valor:
            return True
        if valor < no.valor:
            return self._buscar(no.esquerda, valor)
        return self._buscar(no.direita, valor)
