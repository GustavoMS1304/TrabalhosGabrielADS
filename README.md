# TrabalhosGabrielADS

Projetos da disciplina de Estruturas, Pesquisa e Ordenação de Dados — ADS.

---

## Estrutura do Repositório

```
TrabalhosGabrielADS/
├── Trabalho 1/
├── Trabalho 3 Gabriel/
├── projeto2-buscas/
└── .gitignore
```

---

## Trabalho 1 — Árvores de Busca e TSP

Implementação e comparação de três estruturas de árvore, mais a heurística do Vizinho Mais Próximo para o Problema do Caixeiro-Viajante.

### Arquivos

| Arquivo          | Descrição                            |
|------------------|--------------------------------------|
| `bst.py`         | Árvore Binária de Busca              |
| `avl.py`         | Árvore AVL                           |
| `rubro_negra.py` | Árvore Rubro-Negra                   |
| `tsp.py`         | Heurística do Vizinho Mais Próximo   |
| `main.py`        | Ponto de entrada, executa tudo junto |

### Estruturas

- **BST** — inserção, remoção, busca e altura
- **AVL** — mesmas operações com balanceamento automático por altura
- **Rubro-Negra** — balanceamento por cores, inserção, busca e altura

### TSP — Vizinho Mais Próximo

Começa em uma cidade, sempre vai para a mais próxima ainda não visitada, e no final volta para a origem. Não garante a solução ótima, mas é uma boa aproximação.

### Como rodar

```bash
git clone https://github.com/LeoOrnat/TrabalhosGabrielADS.git
cd TrabalhosGabrielADS/Trabalho\ 1
python main.py
```

Saída esperada:
```
BST altura: 5
AVL altura: 3
RB altura: 3

Caminho TSP: [0, 1, 2, 4, 3, 0]
Distância total: 25.35
```

### Análise

- A BST pode se desbalancear dependendo da ordem de inserção, aumentando a altura.
- A AVL mantém balanceamento rígido, garantindo operações em O(log n).
- A Rubro-Negra tem balanceamento mais flexível, com bom desempenho prático.

---

## Trabalho 3 Gabriel — Árvores de Busca e TSP

Mesma proposta do Trabalho 1, desenvolvida de forma independente pelo integrante Gabriel.

### Estruturas

- **BST** — inserção, remoção, busca e altura
- **AVL** — balanceamento automático por altura, inserção, busca e altura
- **Rubro-Negra** — balanceamento por cores, inserção, busca e altura

### TSP — Vizinho Mais Próximo

1. Começar em uma cidade inicial
2. Visitar a cidade mais próxima ainda não visitada
3. Repetir até visitar todas
4. Retornar à cidade inicial

### Como rodar

```bash
git clone https://github.com/LeoOrnat/TrabalhosGabrielADS.git
cd TrabalhosGabrielADS/Trabalho\ 3\ Gabriel
python main.py
```

Saída esperada:
```
BST altura: 5
AVL altura: 3
RB altura: 3

Caminho TSP: [0, 1, 2, 4, 3, 0]
Distância total: 25.35
```

### Análise

- A BST pode se tornar desbalanceada, apresentando altura elevada.
- A AVL mantém balanceamento rígido, garantindo operações em O(log n).
- A Rubro-Negra tem balanceamento mais flexível, com bom desempenho prático.
- O TSP foi resolvido com heurística aproximada, não garantindo solução ótima.

---

## Trabalho 2 — Benchmark: Bubble Sort vs Quick Sort

Comparação empírica entre Bubble Sort e Quick Sort medindo tempo, comparações e trocas em três cenários: melhor caso, caso médio e pior caso.

### Configuração dos testes

- Tamanhos testados: 100, 500, 1.000, 2.000 e 5.000 elementos
- 10 repetições por configuração
- Medição com `time.perf_counter()`

### Casos de teste

| Caso        | Bubble Sort            | Quick Sort                   |
|-------------|------------------------|------------------------------|
| Melhor caso | Array já ordenado      | Divisão equilibrada do array |
| Caso médio  | Array aleatório        | Array aleatório              |
| Pior caso   | Array em ordem inversa | Array já ordenado            |

### Complexidade

| Algoritmo   | Melhor     | Médio      | Pior  |
|-------------|------------|------------|-------|
| Bubble Sort | O(n)       | O(n²)      | O(n²) |
| Quick Sort  | O(n log n) | O(n log n) | O(n²) |

### Como rodar

```bash
git clone https://github.com/LeoOrnat/TrabalhosGabrielADS.git
cd TrabalhosGabrielADS/projeto2-buscas
python benchmark.py
```

O terminal vai mostrar uma tabela com tempo médio, desvio padrão, comparações, trocas e a diferença entre o resultado prático e o teórico.

---

## Referências

- CORMEN et al. *Introdução a Algoritmos*. 3. ed. MIT Press, 2009.
- SEDGEWICK, R.; WAYNE, K. *Algorithms*. 4. ed. Addison-Wesley, 2011.
