#  Projeto – Estruturas de Dados e TSP

Este projeto foi desenvolvido para a disciplina de Estruturas, Pesquisa e Ordenação de Dados.

O objetivo é implementar e comparar diferentes estruturas de dados e resolver o Problema do Caixeiro-Viajante utilizando heurística.

---

##  Tecnologias utilizadas

* Python 3
* VS Code

---

##  Estruturas implementadas
###  Árvore Binária de Busca (BST)

* Inserção
* Remoção
* Busca
* Cálculo de altura

###  Árvore AVL

* Balanceamento automático por altura
* Inserção
* Busca
* Cálculo de altura

###  Árvore Rubro-Negra

* Balanceamento por cores
* Inserção
* Busca
* Cálculo de altura

---

##  Problema do Caixeiro-Viajante (TSP)

Foi implementada a heurística do **Vizinho Mais Próximo**, que consiste em:

1. Começar em uma cidade inicial
2. Visitar a cidade mais próxima ainda não visitada
3. Repetir até visitar todas
4. Retornar à cidade inicial

---

## Como executar o projeto

1. Instale o Python 3
2. Clone ou baixe o projeto
3. Abra a pasta no VS Code
4. Execute no terminal:

```bash
python main.py
```

---

##  Exemplo de saída

```bash
BST altura: 5
AVL altura: 3
RB altura: 3

Caminho TSP: [0, 1, 2, 4, 3, 0]
Distância total: 25.35
```

---

##  Análise

* A BST pode se tornar desbalanceada, apresentando altura elevada.
* A AVL mantém balanceamento rígido, garantindo operações em O(log n).
* A Árvore Rubro-Negra mantém balanceamento mais flexível, com bom desempenho prático.
* O TSP foi resolvido com heurística aproximada, não garantindo solução ótima.

---

##  Observações

Este projeto tem fins acadêmicos e foi desenvolvido para prática de estruturas de dados e análise de algoritmos.
