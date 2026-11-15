# Jogo da Velha com Matriz 3x3

Projeto desenvolvido em Python para a disciplina Coding, da UNINASSAU. O programa permite que duas pessoas joguem Jogo da Velha pelo terminal. O tabuleiro é representado por uma matriz de três linhas e três colunas.

## Objetivo

Praticar os conteúdos estudados na disciplina, principalmente variáveis, operadores, estruturas condicionais, estruturas de repetição e matrizes, por meio de um jogo executado no terminal.

## Requisitos

- Python 3 instalado;
- Terminal ou prompt de comando;
- Não são necessárias bibliotecas externas.

## Como baixar e executar

1. Abra o terminal ou prompt de comando.
2. Clone o repositório:

```bash
git clone https://github.com/farthurgomes-bot/Projeto-Jogo-De-Matrizes-UNINASSAU.git
```

3. Entre na pasta do projeto:

```bash
cd Projeto-Jogo-De-Matrizes-UNINASSAU
```

4. Execute o programa:

```bash
python Projeto-Jogo-De-Matrizes.py
```

No Windows, caso o comando `python` não seja reconhecido, utilize:

```powershell
py Projeto-Jogo-De-Matrizes.py
```

## Como jogar

- O jogo é disputado por duas pessoas no mesmo computador: jogador X e jogador O.
- O jogador X começa, e os turnos são alternados.
- O tabuleiro possui três linhas e três colunas, identificadas pelos índices de 0 a 2.
- Em cada turno, o jogador informa primeiro a linha e depois a coluna da casa desejada.
- Uma casa ocupada não pode ser escolhida novamente.
- Vence quem formar três símbolos iguais em uma linha, coluna ou diagonal.
- Se todas as casas forem preenchidas sem que haja vencedor, a partida termina empatada.

## Opções do menu

1. **Jogar:** inicia uma nova partida.
2. **Ver regras:** apresenta as regras do jogo no terminal.
3. **Sair e ver estatísticas:** encerra a sessão e apresenta os resultados acumulados.

## Conteúdos de programação utilizados

- **Variáveis e tipos de dados:** textos para os símbolos e entradas dos jogadores, números inteiros para contadores e valores booleanos para controlar o andamento do programa.
- **Operadores:** atribuição, comparação, operações aritméticas e operadores lógicos nas condições do menu e nas regras.
- **Estruturas condicionais:** `if`, `elif` e `else` para validar opções e jogadas, alternar os turnos e verificar os resultados.
- **Estruturas de repetição:** `while` para manter o menu e a partida em execução e repetir a solicitação de entradas inválidas; `for` para percorrer as posições da matriz.
- **Matriz e `for` aninhado:** o tabuleiro é representado por uma lista de três listas. Os laços percorrem linhas e colunas para exibir o tabuleiro, reiniciar suas casas e contar as posições vazias.

## Desafio de lógica: estatísticas da sessão

O desafio implementado é o de estatísticas da sessão. Ao encerrar o programa, são apresentados o total de partidas, as vitórias de X e O, os empates, a porcentagem de vitórias de cada jogador e a maior sequência de vitórias consecutivas de cada um.

## Arquivos do repositório

```text
Projeto-Jogo-De-Matrizes-UNINASSAU/
├── Projeto-Jogo-De-Matrizes.py
└── README.md
```

## Autoria e responsabilidades

**Responsável pelo desenvolvimento:** Francisco Arthur Gomes Lima e Silva  
**Curso:** Análise e Desenvolvimento de Sistemas (ADS)  
**Disciplina:** Coding — UNINASSAU

O projeto foi desenvolvido individualmente. As atividades realizadas incluíram a criação da matriz e da representação visual do tabuleiro, elaboração do menu e das regras, validação das entradas e das jogadas, alternância dos jogadores, verificação de vitória e empate, atualização do placar, implementação das estatísticas da sessão e testes do funcionamento.

## Links

- **Repositório GitHub:** https://github.com/farthurgomes-bot/Projeto-Jogo-De-Matrizes-UNINASSAU
- **Vídeo de apresentação:** https://youtu.be/N4ckjuEa8xk
