# Trabalho Prático 5 - Coloração de Grafos (DSatur)

Este projeto implementa o algoritmo **DSatur** (Degree Saturation) para resolver o problema de coloração de vértices aplicado ao mapa político do Brasil. O objetivo é atribuir uma cor a cada estado de modo que estados vizinhos não compartilhem a mesma cor, respeitando as restrições de um grafo planar e buscando o número cromático mínimo através de uma heurística.

# Resolução de Problemas com Grafos
Orientador: Prof. Me. [Nome do Professor]

Alunos: [Seu Nome Completo]

Link do vídeo: [Apresentação do DSatur no Youtube](link_aqui)

---

## Descrição da Modelagem e Algoritmo

Para colorir o mapa do Brasil, transformamos cada unidade federativa em um vértice e cada fronteira terrestre em uma aresta. O resultado é um grafo com **27 vértices** e **51 arestas**.

### O Algoritmo DSatur
Diferente de uma coloração gulosa simples, o DSatur utiliza o conceito de **Grau de Saturação**. 

1.  **Grau de Saturação ($DS(v)$):** Definido como o número de cores distintas já presentes na vizinhança de um vértice $v$.
2.  **Estratégia de Escolha:** O algoritmo sempre seleciona o vértice não colorido com maior $DS(v)$. Em caso de empate, o critério de desempate é o **grau estático** do vértice (número total de vizinhos).
3.  **Garantia Teórica:** Como o mapa do Brasil é um grafo planar, o **Teorema das Quatro Cores** garante que é possível colori-lo com no máximo 4 cores. O DSatur, sendo uma heurística eficiente, alcançou esse resultado ($k=4$).

### Validação da Solução
O programa percorre todas as 51 arestas após a execução, verificando se para cada aresta $\{u, v\}$, a cor de $u$ é diferente da cor de $v$. A coloração apresentada foi validada com sucesso.

---

## Estrutura do Projeto

* `dados/`: Contém a base de dados do grafo.
    * `brasil.txt`: Arquivo no padrão `algs4` contendo o número de vértices, arestas e a lista de adjacência das fronteiras.
* `src/`:
    * `main.py`: Ponto de entrada que lê o arquivo, executa o algoritmo e exibe os resultados formatados.
    * `dsatur.py`: Implementação da classe `DSatur` com a lógica de saturação e validação.
    * `graph.py`: Classe para representação do grafo por lista de adjacência.
    * `bag.py`: Implementação da estrutura de dados Bag utilizada na lista de adjacência.

---

## Como Executar

O projeto foi desenvolvido em Python e não requer bibliotecas externas.

1.  Abra o terminal na pasta raiz do projeto (`T5/`).
2.  Certifique-se de que o arquivo de dados está na pasta `dados/`.
3.  Execute o seguinte comando:

```bash
python src/main.py dados/brasil.txt