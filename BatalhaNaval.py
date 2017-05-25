import re

# VARIAVEIS DE ARQUIVOS - LEITURA E ESCRITA #
JOGADOR1 = open('jogador1.txt', 'r')
JOGADOR2 = open('jogador2.txt', 'r')
RESULTADO = open('resultado.txt', 'w')
JOGADOR = 'J1'

# VARIAVEIS PARA FILTRO ORIENTACAO E PECA TABULEIRO #
DICIONARIO_PECAS, DICIONARIO_POSICAO_PECAS, POSICAO_PECA = {}, {}, []
chave = 1

# VARIAVEIS DO ALGORITMO #
TABULEIRO_X = []
TABULEIRO_Y = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']

# VARIAVEIS DE AUXILIO E INDICES GERAIS #
LEITURA = []


ADC_PECAS_JOG1 = []
ADC_PECAS_TABULEIRO = []

TOTAL_EXT_PECA = []

#PEC_1 = 0

#######################################################
# DEFINICOES DE CODIGOS PARA UTILIZAR #

def RANGE_DO_TABULEIRO():
    # CRIAR CAMPOS DO TABULEIRO #
    i = 1
    RANGE_TABULEIRO = []
    for x in TABULEIRO_Y:
        while i < 16:
            TABULEIRO = x + str(i)
            RANGE_TABULEIRO.append(TABULEIRO)
            i += 1
        i = 1

    return RANGE_TABULEIRO

def VERIFICACAO_PECA(N):

    VERIF_PECA_TABUL = ""
    #ESTADO_PECA_TABUL = False
    #print (N)
    for x in N:
        #print ('Peca a ser analisada:', x)
        for y in RANGE_DO_TABULEIRO():
            if x == y:
                VERIF_PECA_TABUL = y
                break
        if x != VERIF_PECA_TABUL:
            RESULTADO.write('ERROR_POSITION_NONEXISTENT_VALIDATION')
            print ('ERROR_POSITION_NONEXISTENT_VALIDATION')
            exit()
            #print('ERROR_POSITION_NONEXISTENT_VALIDATION:', x,'\n')
            #ESTADO_PECA_TABUL = True

# PARA TIRAR TODOS OS VETORES DE TODAS PECAS E VERIFICAR SE JA FOI COLOCADO A PECA NO TABULEIRO
def ADC_PECAS(ADC):
    for x in ADC:
        ADC_PECAS_TABULEIRO.append(x)


def NUMERO_PECAS_INVALIDO():
    RESULTADO.write('ERROR_NR_PARTS_VALIDATION')
    print ('ERROR_NR_PARTS_VALIDATION')
    exit()


# VERIFICACAO DE PECAS REPETIDAS NO TABULEIRO APOS A LEITURA DE TODAS AS PECAS DO TABULEIRO
def VERIF_PECAS_JOGADORES(VERF):
    for x in VERF:
        if TOTAL_EXT_PECA.count(x) > 1:
            RESULTADO.write('ERROR_OVERWRITE_PIECES_VALIDATION')
            print ('ERROR_OVERWRITE_PIECES_VALIDATION')
            print (TOTAL_EXT_PECA)
            exit()
#######################################################

# CRIAR O EIXO __X__ DO TABULEIRO - VERIFICAR A REMOCAO DESTE BLOCO#
#for CONT in range(1,16):
#    TABULEIRO_X.append(CONT)
#print(TABULEIRO_X)

### INCLUSÃO DAS PEÇAS DO TABULEIROS ###
## Leitura das posicoes das pecas ##
for linha in JOGADOR1.readlines():
    aux = (re.split(r'[;|\n|]+', linha))
    for numero in aux:
        LEITURA.append(numero)
#print(LEITURA)

print('Range do Tabuleiro: ',RANGE_DO_TABULEIRO())

DICIONARIO_PECAS[1] = LEITURA[LEITURA.index('1')+1:LEITURA.index('2')-1]
#DICIONARIO_PECAS[1] = LEITURA[1:3]
DICIONARIO_PECAS[2] = LEITURA[LEITURA.index('2')+1:LEITURA.index('3')-1]
#DICIONARIO_PECAS[2] = LEITURA[5:7]
DICIONARIO_PECAS[3] = LEITURA[LEITURA.index('3')+1:LEITURA.index('4')-1]
#DICIONARIO_PECAS[3] = LEITURA[9:14]
DICIONARIO_PECAS[4] = LEITURA[LEITURA.index('4')+1:len(LEITURA)]
#DICIONARIO_PECAS[4] = LEITURA[16:20]


def LISTA_DICIONARIO_ELEMENTOS(LIST_DIC,NUM_PECA):
    VERF = []
    #TOTAL_EXT_PECA = []
    #print ('Qual sera a lista de dicionario utilizado:',LIST_DIC)

    #print ('Numero de pecas a serem colocados a mais em cada posicao:',NUM_PECA)

    DICI_P_LISTA = dict((x, y) for x, y in DICIONARIO_POSICAO_PECAS.items() if x == LIST_DIC)
    for y in DICI_P_LISTA.values():
        VERF.append(y)

    for z in VERF[0]:


        #print('Tamanho', len(y))
        #print('Encontrar a posicao do elemetno:',z)
        POSICAO = RANGE_DO_TABULEIRO().index(z)
        #print ('Teste um:',RANGE_DO_TABULEIRO()[POSICAO])
        #print ('Teste dois:',DICIONARIO_PECAS[LIST_DIC][POSICAO][-1:])


        ##ARRUMAR AQUI
        #print ('Valor:',DICIONARIO_PECAS[LIST_DIC][0][:-1])
        #ORIENTACAO = (DICIONARIO_PECAS[LIST_DIC][0][-1:])
        #print (ORIENTACAO)


        #print ('Verificacao1:',RANGE_DO_TABULEIRO()[POSICAO])
        #print ('Verificacao2:',DICIONARIO_PECAS[LIST_DIC][0][:-1] in VERF[0])
        #print ('Verificacao3:',DICIONARIO_PECAS[LIST_DIC][0])
        #print ('Verificacao3:',DICIONARIO_PECAS[LIST_DIC][0][-1:])
        ENTRADA = str(z)  # usar a variavel z
        index = VERF[0].index(ENTRADA)  # usar a variavel POSICAO
        if RANGE_DO_TABULEIRO()[POSICAO] == z and z in VERF[0] and DICIONARIO_PECAS[LIST_DIC][index][-1:] == 'V':
            #print ('Teste index',index)
            #print ('Termina com V!! Peca:',ENTRADA)
            ind = POSICAO
            ind_desc = NUM_PECA
            while ind_desc >= 0:
                # print (ind)
                ind_desc -= 1
                TOTAL_EXT_PECA.append(RANGE_DO_TABULEIRO()[ind])
                ind += 15

        elif RANGE_DO_TABULEIRO()[POSICAO] == z:
            #print('Termina com H!! Peca:', ENTRADA)
            # print ('Ele se encontra na posicao:',POSICAO)
            #print(RANGE_DO_TABULEIRO()[POSICAO])
            ind = POSICAO
            ind_desc = NUM_PECA
            while ind_desc >= 0:
                #print (ind)
                ind_desc -= 1
                TOTAL_EXT_PECA.append(RANGE_DO_TABULEIRO()[ind])
                ind += 1
            #ind_desc = NUM_PECA
        else:
            print('saiu!')
    #print('Resposta Extensao Pecas', TOTAL_EXT_PECA)

    return TOTAL_EXT_PECA



def EXTENCAO_PECA(EXT):
    #print(RANGE_DO_TABULEIRO())
    PEC_1 = 0
    #DICI_N_PECAS = 0 #NUMERO DE PECAS A SEREM ADICIONADAS DE ACORDO COM O NUMERO DA LISTA - DELETAR DEPOIS
    if EXT == 1:
        #print ('Dicionario Numero 1!!')
        #print('Lista inicial', DICIONARIO_POSICAO_PECAS[EXT])
        N_PECA = 3
        PEC_1 += 1
        #cOLAR DAQUI PARA BAIXO NO RESTANTE
        LISTA_DICIONARIO_ELEMENTOS(EXT,N_PECA)

    if EXT == 3:
        #print ('Dicionario Numero 1!!')
        #print('Lista inicial', DICIONARIO_POSICAO_PECAS[EXT])
        N_PECA = 0

        #cOLAR DAQUI PARA BAIXO NO RESTANTE
        LISTA_DICIONARIO_ELEMENTOS(EXT,N_PECA)

    if EXT == 2:
       # print('\nDicionario Numero 2!!')
       # print('Lista inicial', DICIONARIO_POSICAO_PECAS[EXT])
        N_PECA = 4
        LISTA_DICIONARIO_ELEMENTOS(EXT, N_PECA)

    elif EXT == 4:
       # print('\nDicionario Numero 4!!')
       # print('Lista inicial', DICIONARIO_POSICAO_PECAS[EXT])
        N_PECA = 1
        LISTA_DICIONARIO_ELEMENTOS(EXT, N_PECA)
    else:
        return

    #print('Range do tabuleiro:', RANGE_DO_TABULEIRO())
    #print('Range do tabuleiro em A1:', RANGE_DO_TABULEIRO().index('A2'))
    #print('Range do tabuleiro em B1:', RANGE_DO_TABULEIRO().index('B2'))
    #print ('Diferenca de range:',RANGE_DO_TABULEIRO().index('B2') - RANGE_DO_TABULEIRO().index('A2'))

    #cont_list = -1
    #for x in RANGE_DO_TABULEIRO():
    #    cont_list += 1
    #    if EXTENCAO[cont] == x:
    #        while cont







#print ('print dicionario pecas 1', DICIONARIO_PECAS[1])
#print ('print dicionario pecas 2', DICIONARIO_PECAS[2])
#print ('print dicionario pecas 3', DICIONARIO_PECAS[3])
#print ('print dicionario pecas 4', DICIONARIO_PECAS[4], '\n')

while chave < 5:
# Tirar os vetores de vetores das posicoes de pecas do tabuleiro #
    for x in DICIONARIO_PECAS[chave]:
        if x[-1:] == 'V' or (x[-1:] == 'H'):
            POSICAO_PECA.append(x[:-1])
        else: #Para pegar as posicoes sem orientacao vertical ou  horizontal
            POSICAO_PECA.append(x)
    ##Aplica as posicoes corertas das pecas na sua lista definitiva
    DICIONARIO_POSICAO_PECAS[chave] = POSICAO_PECA.copy()
    POSICAO_PECA.clear()

    chave += 1 # CONTADOR PARA SAIR DO LOOP WHILE #

#print('print do dicionario de posicao das pecas:', DICIONARIO_POSICAO_PECAS, '\n')
o = 1






#def ADC_PECAS(ADC): #PARA TIRAR TODOS OS VETORES DE TODAS PECAS E VERIFICAR SE JA FOI COLOCADO A PECA NO TABULEIRO
#    for x in ADC:
#        ADC_PECAS_TABULEIRO.append(x)

for x, y in DICIONARIO_POSICAO_PECAS.items():
    #LISTA_DICIONARIO_ELEMENTOS(y)
    if x == 1:
        #print ('Chave do Dicionario numero 1!!')
        #print('Chave:',x, y)
        if len(y)>2:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 1!!!') #Colocar a chamada pradefinicao de exceção
            NUMERO_PECAS_INVALIDO()

        # Colocar a extencao total da peca andes de mandar para a DEF VERIFICACAO_PECA!!
        VERIFICACAO_PECA(y)
        ADC_PECAS(y)
        EXTENCAO_PECA(x)
        #AQUI
    if x == 2:
        if len(y)>2:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 2!!!') #Colocar a chamada pradefinicao de exceção
            NUMERO_PECAS_INVALIDO()
        #print ('\nChave do Dicionario numero 2!!')
        #print('Chave:', x, y)
        #print ('Valor de X:',x)
        EXTENCAO_PECA(x)
        # Colocar a extencao total da peca andes de mandar para a DEF VERIFICACAO_PECA!!
        VERIFICACAO_PECA(y)
        ADC_PECAS(y)
    elif x == 3:
        if len(y)>5:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 3!!!') #Colocar a chamada pradefinicao de exceção
            NUMERO_PECAS_INVALIDO()
        #print ('\nChave do Dicionario numero 3!!')
        #print('Chave:', x, y)
        #VERIFICACAO_PECA(y)
        EXTENCAO_PECA(x)
        ADC_PECAS(y)
    elif x == 4:
        if len(y)>4:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 4!!!') #Colocar a chamada pradefinicao de exceção
            NUMERO_PECAS_INVALIDO()
        #print ('\nChave do Dicionario numero 4!!')
        #print('Chave:', x, y)
        #Colocar a extencao total da peca andes de mandar para a DEF VERIFICACAO_PECA!!
        EXTENCAO_PECA(x)
        VERIFICACAO_PECA(y)
        ADC_PECAS(y)




# FAZER A ADICAO DAS PECAS DO SEGUNDO JOGADOR UTILIZANDO O ADC_PECAS(Y) TAMBEM

#ADC_PECAS_JOG1 = ADC_PECAS_TABULEIRO
ADC_PECAS_JOG1 = TOTAL_EXT_PECA
#print ('\n',ADC_PECAS_JOG1)
#print ('\nPecas colocadas no tabuleiro\n',ADC_PECAS_TABULEIRO)

ADC_PECAS_JOG2 = ['A2','C76', 'A5'] # AQUI DEVERA SER UTILIZADO OS VALORES DE ENTRADA DO ARQUIVO JOGARDOR_2!!

VERIF_PECAS_JOGADORES(ADC_PECAS_JOG1)


print ('Pecas adicionadas ao tabuleiro com extencao',TOTAL_EXT_PECA)



#######################################################
JOGADOR1.close()
JOGADOR2.close()
RESULTADO.close()