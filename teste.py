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

DICI = {'1':['a','b','c','d','e'],
        '2':['am','bm','cm','dm','em']}

#d = dict(a=1, b=10, c=30, d=2)
#print (d)
e = []
d = dict((k, v) for k, v in DICI.items() if k == '2')
for y in d.values():

    e.append(y)
print ('lista de E:', e)
print (e[0][1])


#DICI_P_LISTA = dict((x,y)for x, y in DICIONARIO_POSICAO_PECAS.items() if x == LIST_DIC:

