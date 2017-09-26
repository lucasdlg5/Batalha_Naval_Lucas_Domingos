import re
JOGADOR1 = open('jogador1.txt', 'r')
JOGADOR2 = open('jogador2.txt', 'r')
RESULTADO = open('resultado.txt', 'w')
JOGADOR = 'J1'
DICIONARIO_PECAS, DICIONARIO_POSICAO_PECAS, POSICAO_PECA = {}, {}, []
DICIONARIO_PECAS2 = {}
chave = 1
TABULEIRO_X = []
TABULEIRO_Y = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P']
LEITURA = []
ADC_PECAS_JOG1 = []
ADC_PECAS_TABULEIRO = []
TOTAL_EXT_PECA = []
TORPEDOS_J1, TORPEDOS_J2 = [], []
LEITURA2 = []
DICIONARIO_POSICAO_PECAS2 = {}
POSICAO_PECA2 = []
TOTAL_EXT_PECA2 = []
chave2 = 1
def TORPEDOS_NAVIOS():
    PONTOS_J1, PONTOS_J2 = 0, 0
    ACERTOS_NAVIOS1 = []
    ACERTOS_NAVIOS2 = []
    I = 0
    for y in TOTAL_EXT_PECA2:
        for x in TORPEDOS_J1:
           if x == y:
                PONTOS_J1 += 3
                ACERTOS_NAVIOS1.append(x)
    for A in ACERTOS_NAVIOS1:
        if A == TOTAL_EXT_PECA2[0]:
                I += 1
        if A == TOTAL_EXT_PECA2[1]:
                I += 1
        if A == TOTAL_EXT_PECA2[2]:
                I += 1
        if A == TOTAL_EXT_PECA2[3]:
                I += 1
        if I == 4:
            PONTOS_J1 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS1:
        if A == TOTAL_EXT_PECA2[4]:
            I += 1
        if A == TOTAL_EXT_PECA2[5]:
            I += 1
        if A == TOTAL_EXT_PECA2[6]:
            I += 1
        if A == TOTAL_EXT_PECA2[7]:
            I += 1
        if I == 4:
            PONTOS_J1 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS1:
        if A == TOTAL_EXT_PECA2[8]:
            I += 1
        if A == TOTAL_EXT_PECA2[9]:
            I += 1
        if A == TOTAL_EXT_PECA2[10]:
            I += 1
        if A == TOTAL_EXT_PECA2[11]:
            I += 1
        if A == TOTAL_EXT_PECA2[12]:
            I += 1
        if I == 5:
            PONTOS_J1 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS1:
        if A == TOTAL_EXT_PECA2[13]:
            I += 1
        if A == TOTAL_EXT_PECA2[14]:
            I += 1
        if A == TOTAL_EXT_PECA2[15]:
            I += 1
        if A == TOTAL_EXT_PECA2[16]:
            I += 1
        if A == TOTAL_EXT_PECA2[17]:
            I += 1
        if I == 5:
            PONTOS_J1 += 2
            break
    for A in ACERTOS_NAVIOS1:
        if A == TOTAL_EXT_PECA2[18]:
            PONTOS_J1 += 2
        if A == TOTAL_EXT_PECA2[19]:
            PONTOS_J1 += 2
        if A == TOTAL_EXT_PECA2[20]:
            PONTOS_J1 += 2
        if A == TOTAL_EXT_PECA2[21]:
            PONTOS_J1 += 2
        if A == TOTAL_EXT_PECA2[22]:
            PONTOS_J1 += 2
    I = 0
    for A in ACERTOS_NAVIOS1:
        if A == TOTAL_EXT_PECA2[23]:
            I += 1
        if A == TOTAL_EXT_PECA2[24]:
            I += 1
        if I == 2:
            PONTOS_J1 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS1:
        if A == TOTAL_EXT_PECA2[25]:
            I += 1
        if A == TOTAL_EXT_PECA2[26]:
            I += 1
        if I == 2:
            PONTOS_J1 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS1:
        if A == TOTAL_EXT_PECA2[27]:
            I += 1
        if A == TOTAL_EXT_PECA2[28]:
            I += 1
        if I == 2:
            PONTOS_J1 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS1:
        if A == TOTAL_EXT_PECA2[29]:
            I += 1
        if A == TOTAL_EXT_PECA2[30]:
            I += 1
        if I == 2:
            PONTOS_J1 += 2
            break
    for y in TOTAL_EXT_PECA:
        for x in TORPEDOS_J2:
           if x == y:
                PONTOS_J2 += 3
                ACERTOS_NAVIOS2.append(x)
    for A in ACERTOS_NAVIOS2:
        if A == TOTAL_EXT_PECA[0]:
                I += 1
        if A == TOTAL_EXT_PECA[1]:
                I += 1
        if A == TOTAL_EXT_PECA[2]:
                I += 1
        if A == TOTAL_EXT_PECA[3]:
                I += 1
        if I == 4:
            PONTOS_J2 += 2
            break
    for A in ACERTOS_NAVIOS2:
        if A == TOTAL_EXT_PECA[18]:
            PONTOS_J2 += 2
        if A == TOTAL_EXT_PECA[19]:
            PONTOS_J2 += 2
        if A == TOTAL_EXT_PECA[20]:
            PONTOS_J2 += 2
        if A == TOTAL_EXT_PECA[21]:
            PONTOS_J2 += 2
        if A == TOTAL_EXT_PECA[22]:
            PONTOS_J2 += 2
    I = 0
    for A in ACERTOS_NAVIOS2:
        if A == TOTAL_EXT_PECA[4]:
            I += 1
        if A == TOTAL_EXT_PECA[5]:
            I += 1
        if A == TOTAL_EXT_PECA[6]:
            I += 1
        if A == TOTAL_EXT_PECA[7]:
            I += 1
        if I == 4:
            PONTOS_J2 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS2:
        if A == TOTAL_EXT_PECA[8]:
            I += 1
        if A == TOTAL_EXT_PECA[9]:
            I += 1
        if A == TOTAL_EXT_PECA[10]:
            I += 1
        if A == TOTAL_EXT_PECA[11]:
            I += 1
        if A == TOTAL_EXT_PECA[12]:
            I += 1
        if I == 5:
            PONTOS_J2 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS2:
        if A == TOTAL_EXT_PECA[13]:
            I += 1
        if A == TOTAL_EXT_PECA[14]:
            I += 1
        if A == TOTAL_EXT_PECA[15]:
            I += 1
        if A == TOTAL_EXT_PECA[16]:
            I += 1
        if A == TOTAL_EXT_PECA[17]:
            I += 1
        if I == 5:
            PONTOS_J2 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS2:
        if A == TOTAL_EXT_PECA[23]:
            I += 1
        if A == TOTAL_EXT_PECA[24]:
            I += 1
        if I == 2:
            PONTOS_J2 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS2:
        if A == TOTAL_EXT_PECA[25]:
            I += 1
        if A == TOTAL_EXT_PECA[26]:
            I += 1
        if I == 2:
            PONTOS_J2 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS2:
        if A == TOTAL_EXT_PECA[27]:
            I += 1
        if A == TOTAL_EXT_PECA[28]:
            I += 1
        if I == 2:
            PONTOS_J2 += 2
            break
    I = 0
    for A in ACERTOS_NAVIOS2:
        if A == TOTAL_EXT_PECA[29]:
            I += 1
        if A == TOTAL_EXT_PECA[30]:
            I += 1
        if I == 2:
            PONTOS_J2 += 2
            break
    print('TOTAL PONTOS J1:', PONTOS_J1)
    print('TOTAL PONTOS J2:', PONTOS_J2)
    if PONTOS_J1 == PONTOS_J2:
        print('EMPATE!!')
        RESULTADO.write('J1 '+ str(len(ACERTOS_NAVIOS1)) +'AA '+(str(13-(len(ACERTOS_NAVIOS1))))+'AE '+ str(PONTOS_J1)+'PT'+'\nJ2 '+ str(len(ACERTOS_NAVIOS2)) +'AA ' +(str(13-(len(ACERTOS_NAVIOS2))))+'AE '+ str(PONTOS_J2)+'PT')
    elif PONTOS_J1 > PONTOS_J2:
        print('J1 GANHOU!!')
        RESULTADO.write('J1 ' + str(len(ACERTOS_NAVIOS1)) + 'AA ' + (str(13-(len(ACERTOS_NAVIOS1)))) + 'AE ' + str(PONTOS_J1) + 'PT')
    elif PONTOS_J2 > PONTOS_J1:
        print('J2 GANHOU!!')
        RESULTADO.write('J2 '+ str(len(ACERTOS_NAVIOS2)) +'AA ' +(str(13-(len(ACERTOS_NAVIOS2))))+'AE '+ str(PONTOS_J2)+'PT')
    return
def RANGE_DO_TABULEIRO():
    i = 1
    RANGE_TABULEIRO = []
    for x in TABULEIRO_Y:
        while i < 16:
            TABULEIRO = x + str(i)
            RANGE_TABULEIRO.append(TABULEIRO)
            i += 1
        i = 1
    return RANGE_TABULEIRO
def VERIFICACAO_PECA(N,J):
    if N == 'AAA':
        RESULTADO.write(J + ' ERROR_POSITION_NONEXISTENT_VALIDATION')
        print(J + ' ERROR_POSITION_NONEXISTENT_VALIDATION')
        exit()
    VERIF_PECA_TABUL = ""
    for x in N:
        for y in RANGE_DO_TABULEIRO():
            if x == y:
                VERIF_PECA_TABUL = y
                break
        if x != VERIF_PECA_TABUL:
            RESULTADO.write(J+' ERROR_POSITION_NONEXISTENT_VALIDATION')
            print (J+' ERROR_POSITION_NONEXISTENT_VALIDATION')
            exit()
def ADC_PECAS(ADC):
    for x in ADC:
        ADC_PECAS_TABULEIRO.append(x)
def NUMERO_PECAS_INVALIDO(J):
    RESULTADO.write(J +' ERROR_NR_PARTS_VALIDATION')
    print (J,'ERROR_NR_PARTS_VALIDATION')
    exit()
def VERIF_PECAS_JOGADORES(VERF):
    for x in VERF:
        if TOTAL_EXT_PECA.count(x) > 1:
            RESULTADO.write('J1 ERROR_OVERWRITE_PIECES_VALIDATION')
            print ('J1 ERROR_OVERWRITE_PIECES_VALIDATION')
            print ('peca:',x)
            print (TOTAL_EXT_PECA)
            exit()
def VERIF_PECAS_JOGADORES2(VERF):
    for x in VERF:
        if TOTAL_EXT_PECA2.count(x) > 1:
            RESULTADO.write('J2 ERROR_OVERWRITE_PIECES_VALIDATION')
            print('J2 ERROR_OVERWRITE_PIECES_VALIDATION')
            print('peca:', x)
            print (TOTAL_EXT_PECA2)
            exit()
for linha in JOGADOR1.readlines():
    aux = (re.split(r'[;|\n|]+', linha))
    for numero in aux:
        LEITURA.append(numero.upper())
for linha in JOGADOR2.readlines():
    aux = (re.split(r'[;|\n|]+', linha))
    for numero in aux:
        LEITURA2.append(numero.upper())
DICIONARIO_PECAS[1] = LEITURA[LEITURA.index('1')+1:LEITURA.index('2')-1]
DICIONARIO_PECAS[2] = LEITURA[LEITURA.index('2')+1:LEITURA.index('3')-1]
DICIONARIO_PECAS[3] = LEITURA[LEITURA.index('3')+1:LEITURA.index('4')-1]
DICIONARIO_PECAS[4] = LEITURA[LEITURA.index('4')+1:LEITURA.index("#JOGADA")-1]
TORPEDOS_J1 = LEITURA[LEITURA.index('#JOGADA')+3:len(LEITURA)]
DICIONARIO_PECAS2[1] = LEITURA2[LEITURA2.index('1')+1:LEITURA2.index('2')-1]
DICIONARIO_PECAS2[2] = LEITURA2[LEITURA2.index('2')+1:LEITURA2.index('3')-1]
DICIONARIO_PECAS2[3] = LEITURA2[LEITURA2.index('3')+1:LEITURA2.index('4')-1]
DICIONARIO_PECAS2[4] = LEITURA2[LEITURA2.index('4')+1:LEITURA2.index("#JOGADA")-1]
TORPEDOS_J2 = LEITURA2[LEITURA2.index('#JOGADA')+3:len(LEITURA2)]
def LISTA_DICIONARIO_ELEMENTOS(LIST_DIC,NUM_PECA):
    VERF = []
    DICI_P_LISTA = dict((x, y) for x, y in DICIONARIO_POSICAO_PECAS.items() if x == LIST_DIC)
    for y in DICI_P_LISTA.values():
        VERF.append(y)
    for z in VERF[0]:
        if z not in RANGE_DO_TABULEIRO():
            VERIFICACAO_PECA('AAA','J1')
        else:
            POSICAO = RANGE_DO_TABULEIRO().index(z)
        ENTRADA = str(z)
        index = VERF[0].index(ENTRADA)
        if RANGE_DO_TABULEIRO()[POSICAO] == z and z in VERF[0] and DICIONARIO_PECAS[LIST_DIC][index][-1:] == 'V':
            ind = POSICAO
            ind_desc = NUM_PECA
            while ind_desc >= 0:
                ind_desc -= 1
                TOTAL_EXT_PECA.append(RANGE_DO_TABULEIRO()[ind])
                ind += 15
        elif RANGE_DO_TABULEIRO()[POSICAO] == z:
            ind = POSICAO
            ind_desc = NUM_PECA
            while ind_desc >= 0:
                ind_desc -= 1
                TOTAL_EXT_PECA.append(RANGE_DO_TABULEIRO()[ind])
                ind += 1
        else:
            print('saiu!')
    return TOTAL_EXT_PECA
def LISTA_DICIONARIO_ELEMENTOS2(LIST_DIC,NUM_PECA):
    VERF = []
    DICI_P_LISTA = dict((x, y) for x, y in DICIONARIO_POSICAO_PECAS2.items() if x == LIST_DIC)
    for y in DICI_P_LISTA.values():
        VERF.append(y)
    for z in VERF[0]:
        if z not in RANGE_DO_TABULEIRO():
            VERIFICACAO_PECA('AAA','J2')
        else:
            POSICAO = RANGE_DO_TABULEIRO().index(z)
        ENTRADA = str(z)
        index = VERF[0].index(ENTRADA)
        if RANGE_DO_TABULEIRO()[POSICAO] == z and z in VERF[0] and DICIONARIO_PECAS2[LIST_DIC][index][-1:] == 'V':
            ind = POSICAO
            ind_desc = NUM_PECA
            while ind_desc >= 0:
                ind_desc -= 1
                TOTAL_EXT_PECA2.append(RANGE_DO_TABULEIRO()[ind])
                ind += 15
        elif RANGE_DO_TABULEIRO()[POSICAO] == z:
            ind = POSICAO
            ind_desc = NUM_PECA
            while ind_desc >= 0:
                ind_desc -= 1
                TOTAL_EXT_PECA2.append(RANGE_DO_TABULEIRO()[ind])
                ind += 1
        else:
            print('saiu!')
    return TOTAL_EXT_PECA2
def EXTENCAO_PECA(EXT, J):
    PEC_1 = 0
    if EXT == 1:
        N_PECA = 3
        PEC_1 += 1
        if J == ('J1'):
            LISTA_DICIONARIO_ELEMENTOS(EXT,N_PECA)
        elif J == ('J2'):
            LISTA_DICIONARIO_ELEMENTOS2(EXT, N_PECA)
    if EXT == 3:
        N_PECA = 0
        if J == ('J1'):
            LISTA_DICIONARIO_ELEMENTOS(EXT,N_PECA)
        elif J == ('J2'):
            LISTA_DICIONARIO_ELEMENTOS2(EXT, N_PECA)
    if EXT == 2:
        N_PECA = 4
        if J == ('J1'):
            LISTA_DICIONARIO_ELEMENTOS(EXT,N_PECA)
        elif J == ('J2'):
            LISTA_DICIONARIO_ELEMENTOS2(EXT, N_PECA)
    elif EXT == 4:
        N_PECA = 1
        if J == ('J1'):
            LISTA_DICIONARIO_ELEMENTOS(EXT,N_PECA)
        elif J == ('J2'):
            LISTA_DICIONARIO_ELEMENTOS2(EXT, N_PECA)
    else:
        return
while chave < 5:
    for x in DICIONARIO_PECAS[chave]:
        if x[-1:] == 'V' or (x[-1:] == 'H'):
            POSICAO_PECA.append(x[:-1])
        else:
            POSICAO_PECA.append(x)
    DICIONARIO_POSICAO_PECAS[chave] = POSICAO_PECA.copy()
    POSICAO_PECA.clear()
    chave += 1
while chave2 < 5:
    for y in DICIONARIO_PECAS2[chave2]:
        if y[-1:] == 'V' or (y[-1:] == 'H'):
            POSICAO_PECA2.append(y[:-1])
        else:
            POSICAO_PECA2.append(y)
    DICIONARIO_POSICAO_PECAS2[chave2] = POSICAO_PECA2.copy()
    POSICAO_PECA2.clear()
    chave2 += 1
for x, y in DICIONARIO_POSICAO_PECAS.items():
    if x == 1:
        if len(y)>2:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 1!!!')
            NUMERO_PECAS_INVALIDO('J1')
        VERIFICACAO_PECA(y,'J1')
        ADC_PECAS(y)
        EXTENCAO_PECA(x,'J1')
    if x == 2:
        if len(y)>2:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 2!!!')
            NUMERO_PECAS_INVALIDO('J1')
        EXTENCAO_PECA(x,'J1')
        VERIFICACAO_PECA(y,'J1')
        ADC_PECAS(y)
    elif x == 3:
        if len(y)>5:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 3!!!')
            NUMERO_PECAS_INVALIDO('J1')
        EXTENCAO_PECA(x,'J1')
        ADC_PECAS(y)
    elif x == 4:
        if len(y)>4:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 4!!!')
            NUMERO_PECAS_INVALIDO('J1')
        EXTENCAO_PECA(x,'J1')
        VERIFICACAO_PECA(y,'J1')
        ADC_PECAS(y)
for z, a in DICIONARIO_POSICAO_PECAS2.items():
    if z == 1:
        if len(a) > 2:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 1!!!')
            print ('Lista',DICIONARIO_POSICAO_PECAS2)
            NUMERO_PECAS_INVALIDO('J2')
        VERIFICACAO_PECA(a,'J2')
        ADC_PECAS(a)
        EXTENCAO_PECA(z,'J2')
    if z == 2:
        if len(a) > 2:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 2!!!')
            print('Lista', DICIONARIO_POSICAO_PECAS2)
            NUMERO_PECAS_INVALIDO('J2')
        EXTENCAO_PECA(z,'J2')
        VERIFICACAO_PECA(a,'J2')
        ADC_PECAS(a)
    elif z == 3:
        if len(a) > 5:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 3!!!')
            print('Lista', DICIONARIO_POSICAO_PECAS2)
            NUMERO_PECAS_INVALIDO('J2')
        EXTENCAO_PECA(z,'J2')
        ADC_PECAS(a)
    elif z == 4:
        if len(a) > 4:
            print('EXCEÇÃO AQUII RAPAZ - PECA NUMERO 4!!!')
            print('Lista', DICIONARIO_POSICAO_PECAS2)
            NUMERO_PECAS_INVALIDO('J2')
        EXTENCAO_PECA(z,'J2')
        VERIFICACAO_PECA(a,'J2')
        ADC_PECAS(a)
ADC_PECAS_JOG1 = TOTAL_EXT_PECA
VERIF_PECAS_JOGADORES(ADC_PECAS_JOG1)
ADC_PECAS_JOG2 = TOTAL_EXT_PECA2
VERIF_PECAS_JOGADORES2(ADC_PECAS_JOG2)
for x in TORPEDOS_J1 :
    if x not in RANGE_DO_TABULEIRO():
        VERIFICACAO_PECA('AAA', 'J1')
for z in TORPEDOS_J2 :
    if z not in RANGE_DO_TABULEIRO():
        VERIFICACAO_PECA('AAA', 'J2')
if len(TORPEDOS_J1) > 20:
    NUMERO_PECAS_INVALIDO('J1')
elif len(TORPEDOS_J2) > 20:
    NUMERO_PECAS_INVALIDO('J2')
else:
    TORPEDOS_NAVIOS()
JOGADOR1.close()
JOGADOR2.close()
RESULTADO.close()