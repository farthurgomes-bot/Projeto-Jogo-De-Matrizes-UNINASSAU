total_partidas = 0
vitorias_x = 0
vitorias_o = 0
empates = 0
seq_atual_x = 0
max_seq_x = 0
seq_atual_o = 0
max_seq_o = 0

opcao = "1"

if opcao == "1":
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
        
        if turno == "X":
            turno = "O"
        else:
            turno = "X"
        
        partida_andamento = False