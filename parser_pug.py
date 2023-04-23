from lexer_pug import lexer

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_identacao():
    nivel = 0
    global prox_simb
    while (prox_simb.type=='TAB' or prox_simb.type=='Space'):
        if(prox_simb.type=='TAB'):
            nivel+=4
        elif(prox_simb.type=='SPACE'):
            nivel+=1
        prox_simb = lexer.token()
    return nivel

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)
        prox_simb = ('erro', '', 0, 0)

def rec_Block(nivel_atual):
    global prox_simb
    if prox_simb.type == 'NUM':
        t1 = prox_simb.value
        rec_term('NUM')
        t2 = None
        t3 = None
        rec_term('PF')
    else:
        parserError(prox_simb)
    return None

def rec_pug(nivel_anterior):
    global prox_simb
    nivel_atual=rec_identacao()
    rec_term('WORD')
    return rec_Block(nivel_atual)

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    print(rec_pug(0).html())

    
