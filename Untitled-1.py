tab = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
turno = "X"
vencedor = ""
jogadas = 0
partida_andamento = True

while partida_andamento == True:
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

    while jogada_valida == False:
        valida_linha = False
        while valida_linha == False:
            l_str = input("Escolha a linha (0 a 2): ")
            for n in range(3):
                if l_str == str(n):
                    valida_linha = True
                    linha_jog = n
            if valida_linha == False:
                print("Erro: Digite 0, 1 ou 2.")

        valida_coluna = False
        while valida_coluna == False:
            c_str = input("Escolha a coluna (0 a 2): ")
            for n in range(3):
                if c_str == str(n):
                    valida_coluna = True
                    coluna_jog = n
            if valida_coluna == False:
                print("Erro: Digite 0, 1 ou 2.")

        if tab[linha_jog][coluna_jog] == " ":
            jogada_valida = True
        else:
            print("Casa ocupada! Jogue em um espaco livre.")

    tab[linha_jog][coluna_jog] = turno
    jogadas = jogadas + 1

    for i in range(3):
        if tab[i][0] == tab[i][1] and tab[i][1] == tab[i][2] and tab[i][0] != " ":
            vencedor = turno
        if tab[0][i] == tab[1][i] and tab[1][i] == tab[2][i] and tab[0][i] != " ":
            vencedor = turno

    if tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and tab[0][0] != " ":
        vencedor = turno
    if tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] and tab[0][2] != " ":
        vencedor = turno

    if vencedor != "":
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
        print("\nFim de jogo! O jogador", vencedor, "venceu!")
        partida_andamento = False
    elif jogadas == 9:
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
        print("\nFim de jogo! Deu velha!")
        partida_andamento = False
    else:
        if turno == "X":
            turno = "O"
        else:
            turno = "X"