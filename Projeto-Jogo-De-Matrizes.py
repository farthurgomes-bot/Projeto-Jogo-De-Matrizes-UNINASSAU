total_partidas = 0
vitorias_x = 0
vitorias_o = 0
empates = 0
seq_atual_x = 0
seq_atual_o = 0
max_seq_x = 0
max_seq_o = 0

rodando_programa = True

while rodando_programa == True:
    print("\n" + "="*30)
    print("      JOGO DA VELHA")
    print("="*30)
    print("1. Jogar")
    print("2. Ver regras")
    print("3. Sair e ver estatisticas")
    
    opcao_valida = False
    opcao = ""
    while opcao_valida == False:
        opcao = input("Escolha uma opcao: ")
        if opcao == "1" or opcao == "2" or opcao == "3":
            opcao_valida = True
        else:
            print("Opcao invalida! Digite 1, 2 ou 3.")
            
    if opcao == "2":
        print("\nREGRAS: O tabuleiro tem 3x3. Os jogadores escolhem linha e coluna de 0 a 2.")
        print("Vence quem completar linha, coluna ou diagonal primeiro.")
        
    elif opcao == "1":
        tab = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        turno = "X"
        vencedor = ""
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
            
            for i in range(3):
                if tab[i][0] == turno and tab[i][1] == turno and tab[i][2] == turno:
                    vencedor = turno
                if tab[0][i] == turno and tab[1][i] == turno and tab[2][i] == turno:
                    vencedor = turno
            
            if tab[0][0] == turno and tab[1][1] == turno and tab[2][2] == turno:
                vencedor = turno
            if tab[0][2] == turno and tab[1][1] == turno and tab[2][0] == turno:
                vencedor = turno
                
            casas_vazias = 0
            for i in range(3):
                for j in range(3):
                    if tab[i][j] == " ":
                        casas_vazias = casas_vazias + 1
                        
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
                        
                print("\n>>> JOGADOR", vencedor, "VENCEU! <<<")
                total_partidas = total_partidas + 1
                
                if vencedor == "X":
                    vitorias_x = vitorias_x + 1
                    seq_atual_x = seq_atual_x + 1
                    seq_atual_o = 0
                    if seq_atual_x > max_seq_x:
                        max_seq_x = seq_atual_x
                else:
                    vitorias_o = vitorias_o + 1
                    seq_atual_o = seq_atual_o + 1
                    seq_atual_x = 0
                    if seq_atual_o > max_seq_o:
                        max_seq_o = seq_atual_o
                        
                partida_andamento = False
                
            elif casas_vazias == 0:
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
                        
                print("\n>>> DEU EMPATE! <<<")
                total_partidas = total_partidas + 1
                empates = empates + 1
                seq_atual_x = 0
                seq_atual_o = 0
                partida_andamento = False
            else:
                if turno == "X":
                    turno = "O"
                else:
                    turno = "X"

    elif opcao == "3":
        print("\n" + "="*30)
        print("   ESTATISTICAS DA SESSAO")
        print("="*30)
        print("Total de partidas:", total_partidas)
        print("Vitorias X:", vitorias_x)
        print("Vitorias O:", vitorias_o)
        print("Empates:", empates)
        
        if total_partidas > 0:
            perc_x = (vitorias_x / total_partidas) * 100
            perc_o = (vitorias_o / total_partidas) * 100
            print("Aproveitamento X:", round(perc_x, 1), "%")
            print("Aproveitamento O:", round(perc_o, 1), "%")
            
        print("Maior sequencia X:", max_seq_x)
        print("Maior sequencia O:", max_seq_o)
        print("\nEncerrando programa...")
        rodando_programa = False
