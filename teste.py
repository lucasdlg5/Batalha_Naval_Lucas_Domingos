#TABULEIRO_Y = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
#TESTE = 'A11'
#
#def RANGE_DO_TABULEIRO():
#    # CRIAR CAMPOS DO TABULEIRO #
#    i = 1
#    RANGE_TABULEIRO = []#
#    for x in TABULEIRO_Y:
#        while i < 16:
#            TABULEIRO = x + str(i)
#            RANGE_TABULEIRO.append(TABULEIRO)
#            i += 1
#        i = 1
#    print (RANGE_TABULEIRO)
#    return RANGE_TABULEIRO
#
#print (RANGE_DO_TABULEIRO().index(TESTE))

#def VERIFICACAO_PECA(N):
#    # FAZER VERIFICAÇÃO E EXCECAO DE PEÇAS FORA DO TABULEIRO!!
#    VERIF_PECA_TABUL = ""
#    print (N)
#    for x in N:
#        print ('Peca a ser analisada:', x)
#        for y in RANGE_DO_TABULEIRO():
#            if x == y:
#                VERIF_PECA_TABUL = y
#                break
#        if x != VERIF_PECA_TABUL:
#            print('ERROR_POSITION_NONEXISTENT_VALIDATION:', x,'\n')  # ATENCAO - COLOCAR DENTRO D O ARQUIVO DE SAIDA!!!!!!!!!!!!!!!!!!!!
#            VERIF_PECA_TABUL = False
#
#VERIFICACAO_PECA(['A1','B2','B16','P14','5',5,'NH5'])


def definicao1():
    print('definicao aqui')

def definicao2(n):
    print(n)
    return n

print (definicao2('1-'))