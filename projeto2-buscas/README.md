# Projeto 2 — Sistemas de Busca (Sequencial, Binária e BST)

Estrutura do projeto:

```
projeto2-buscas/
│── src/
│   ├── busca_sequencial.py
│   ├── busca_binaria.py
│   ├── arvore_bst.py
│   └── experimento.py
│── README.md
│── requirements.txt
```

## Descritivo

Neste projeto foram implementados três métodos de busca:
- Busca sequencial (lista desordenada)
- Busca binária (lista ordenada)
- Busca em Árvore Binária de Busca (BST)

Em seguida são executados experimentos com diferentes volumes de dados, repetindo 30 vezes cada tamanho, medindo tempo de execução e calculando média e desvio padrão. Ao final o programa imprime os resultados no terminal.

## Fluxo do experimento (como pedido)

Para cada tamanho `n`:
1. Gerar lista aleatória (`random.sample`)
2. Ordenar a lista para busca binária
3. Inserir os mesmos valores na BST
4. Escolher o elemento a ser buscado (alvo)
5. Medir o tempo de cada método (sequencial, binária, BST)
6. Repetir 30 vezes
7. Calcular média e desvio padrão

## Requisitos

- Python 3.10+

Não há dependências externas.

## Como executar

Opção A (recomendado): entre na pasta `projeto2-buscas` e execute:

```bash
py -3.10 src/experimento.py
```

Ajuda (mostra os parâmetros e o padrão, por exemplo semente = 0):

```bash
py -3.10 src/experimento.py -h
```

Opção B: se você já estiver dentro da pasta `projeto2-buscas/src`, execute sem repetir `src/` no caminho:

```bash
py -3.10 experimento.py
```

Parâmetros principais:
- `--tamanhos` (lista separada por vírgula) padrão: `1000,10000,100000`
- `--repeticoes` padrão: `30`
- `--semente` padrão: `0`

Exemplo rápido (para testar mais rápido):

```bash
py -3.10 src/experimento.py --tamanhos 100,500,1000 --repeticoes 30 --semente 0
```

## Complexidade (Big-O)

- Busca sequencial: `O(n)`
- Busca binária: `O(log n)` (lista precisa estar ordenada)
- Busca em BST: `O(h)` onde `h` é a altura (médio esperado ~ `O(log n)` com inserção aleatória, pior caso `O(n)`)

