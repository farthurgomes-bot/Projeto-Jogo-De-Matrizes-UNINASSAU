total_partidas = 0
vitorias_x = 0
vitorias_o = 0
empates = 0
seq_atual_x = 0
seq_atual_o = 0
max_seq_x = 0
max_seq_o = 0

tab = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
rodando_programa = True

while rodando_programa:
    print("\n" + "=" * 35)
    print("          JOGO DA VELHA")
    print("=" * 35)
    print("1. Jogar")
    print("2. Ver regras")
    print("3. Sair e ver estatisticas")

    opcao_valida = False
    opcao = ""

    while not opcao_valida:
        opcao = input("Escolha uma opcao: ")

        if opcao == "1" or opcao == "2" or opcao == "3":
            opcao_valida = True
        else:
            print("Opcao invalida! Digite 1, 2 ou 3.")

    if opcao == "2":
        print("\n" + "-" * 35)
        print("REGRAS DO JOGO DA VELHA:")
        print("- O tabuleiro e uma matriz 3x3, com linhas e colunas de 0 a 2.")
        print("- O jogador X comeca e alterna os turnos com o jogador O.")
        print("- Vence quem alinhar 3 simbolos na linha, coluna ou diagonal.")
        print("- Se o tabuleiro ficar cheio sem um vencedor, a partida termina empatada.")
        print("-" * 35)
        input("Pressione ENTER para voltar ao menu...")

    elif opcao == "1":
        for i in range(3):
            for j in range(3):
                tab[i][j] = " "

        turno = "X"
        vencedor = ""
        partida_andamento = True

        while partida_andamento:
            print("\n  0 1 2")

            for i in range(3):
                linha_visual = str(i) + " "

                for j in range(3):
                    linha_visual = linha_visual + tab[i][j]

                    if j < 2:
                        linha_visual = linha_visual + "|"

                print(linha_visual)

                if i < 2:
                    print("  -+-+-")

            print("\nVez do jogador", turno)

            jogada_valida = False
            linha_jog = -1
            coluna_jog = -1

            while not jogada_valida:
                valida_linha = False

                while not valida_linha:
                    l_str = input("Escolha a linha (0 a 2): ")

                    for n in range(3):
                        if l_str == str(n):
                            valida_linha = True
                            linha_jog = n

                    if not valida_linha:
                        print("Erro: digite 0, 1 ou 2.")

                valida_coluna = False

                while not valida_coluna:
                    c_str = input("Escolha a coluna (0 a 2): ")

                    for n in range(3):
                        if c_str == str(n):
                            valida_coluna = True
                            coluna_jog = n
