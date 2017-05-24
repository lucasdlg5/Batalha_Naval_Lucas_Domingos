TABULEIRO_X = []
TABULEIRO_Y = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']

ENTRADA = ['A1']

# ADICIONAR O PROGRAMA PRINCIPAL #
i = 1
RANGE_TABULEIRO = []
PECAS_COLOCADAS_JOGADOR = []


# CRIAR CAMPOS DO TABULEIRO #
for x in TABULEIRO_Y:
    while i < 16:
        TABULEIRO = x+str(i)
        RANGE_TABULEIRO.append(TABULEIRO)
        i += 1
    i = 1


# FAZER VERIFICAÇÃO E EXCECAO DE PEÇAS FORA DO TABULEIRO!!
for x in ENTRADA:
    #print ('Peca a ser analisada:', x)
    for y in RANGE_TABULEIRO:
        if x == y:
            VERIF_PECA_TABUL = y
            break
    if x != VERIF_PECA_TABUL:
        print ('ERROR_POSITION_NONEXISTENT_VALIDATION:', x,'\n') # ATENCAO - COLOCAR DENTRO D O ARQUIVO DE SAIDA!!!!!!!!!!!!!!!!!!!!
        VERIF_PECA_TABUL = False






#    for y in RANGE_TABULEIRO:
#        while VERIF_PECA_TABUL == False:
#            if x == y:
#                #print('A PECA COLOCADA ESTA DENTRO DO RANGE!')
#                VERIF_PECA_TABUL = True
#            else:
#                VERIF_PECA_TABUL = False
#                print ('BATEU AQUI')
#