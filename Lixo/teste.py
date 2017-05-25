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

#DICI = {'1':['aBC','b','c','d','e'],
#        '2':['am','bm','cm','dm','em']}
#
#print (DICI['1'][0][:-1])
#d = dict(a=1, b=10, c=30, d=2)
#print (d)
#e = []
#d = dict((k, v) for k, v in DICI.items() if k == '2')
#for y in d.values():
#
#    e.append(y)
#print ('lista de E:', e)
#print (e[0][1])


#DICI_P_LISTA = dict((x,y)for x, y in DICIONARIO_POSICAO_PECAS.items() if x == LIST_DIC:

DESENHOA, DESENHOB, DESENHOC, DESENHOD, DESENHOE, DESENHOF, DESENHOG, DESENHOH, DESENHOI, DESENHOJ, DESENHOK, DESENHOL, DESENHOM, DESENHON, DESENHOO, DESENHOP = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
NUMEROS = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

print(NUMEROS)
DESENHOA.append('A')
DESENHOB.append('B')
DESENHOC.append('C')
DESENHOD.append('D')
DESENHOE.append('E')
DESENHOF.append('F')
DESENHOG.append('G')
DESENHOH.append('H')
DESENHOI.append('I')
DESENHOJ.append('J')
DESENHOK.append('K')
DESENHOL.append('L')
DESENHOM.append('M')
DESENHON.append('N')
DESENHOO.append('O')
DESENHOP.append('P')

DESENHOA.append("  O " * 15)

print (DESENHOA)
DESENHOB.append("  O " * 15)
print (DESENHOB)
DESENHOC.append("  O " * 15)
print (DESENHOC)
DESENHOD.append("  O " * 15)
print (DESENHOD)

DESENHOE.append("  O " * 15)
print (DESENHOE)
DESENHOF.append("  O " * 15)
print (DESENHOF)
DESENHOG.append("  O " * 15)
print (DESENHOG)
DESENHOH.append("  O " * 15)
print (DESENHOH)
DESENHOI.append("  O " * 15)
print (DESENHOI)
DESENHOJ.append("  O " * 15)
print (DESENHOJ)
DESENHOK.append("  O " * 15)
print (DESENHOK)
DESENHOL.append("  O " * 15)
print (DESENHOL)
DESENHOM.append("  O " * 15)
print (DESENHOM)
DESENHON.append("  O " * 15)
print (DESENHON)
DESENHOO.append("  O " * 15)
print (DESENHOO)
DESENHOP.append("  O " * 15)
print (DESENHOP)