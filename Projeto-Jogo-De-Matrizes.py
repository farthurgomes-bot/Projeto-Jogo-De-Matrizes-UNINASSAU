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