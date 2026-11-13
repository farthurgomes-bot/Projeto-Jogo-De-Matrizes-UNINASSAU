tab = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
turno = "X"
jogadas = 0
partida_andamento = True
    
while partida_andamento:
    print("\n  0 1 2")
    for i in range(3):
        linha = f"{i} " + "|".join(tab[i])
        print(linha)
        if i < 2:
            print("  -+-+-")
    
    print(f"\nVez do jogador {turno}")
    
    jogada_valida = False
    while not jogada_valida:
        l_str = input("Escolha a linha (0, 1 ou 2): ")
        c_str = input("Escolha a coluna (0, 1 ou 2): ")
        
        opcoes_validas = ["0", "1", "2"]
        
        if l_str in opcoes_validas and c_str in opcoes_validas:
            linha_jog = int(l_str)
            coluna_jog = int(c_str)
            
            if tab[linha_jog][coluna_jog] == " ":
                jogada_valida = True
            else:
                print("Erro: Posição já ocupada! Escolha outro lugar.\n")
        else:
            print("Erro: Digite apenas 0, 1 ou 2.\n")
    
    tab[linha_jog][coluna_jog] = turno
    jogadas += 1
    
    ganhou = False
    
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] != " ":
            ganhou = True
        if tab[0][i] == tab[1][i] == tab[2][i] != " ":
            ganhou = True
            
    if tab[0][0] == tab[1][1] == tab[2][2] != " ":
        ganhou = True
    if tab[0][2] == tab[1][1] == tab[2][0] != " ":
        ganhou = True
        
    if ganhou:
        print(f"\nFIM DE JOGO! O jogador {turno} VENCEU!")
        partida_andamento = False
    elif jogadas == 9:
        print("\nFIM DE JOGO! Deu velha (Empate)!")
        partida_andamento = False
    else:
        turno = "O" if turno == "X" else "X"