from lexer_pug import lexer

prox_simb = ('Erro', '', 0, 0)

def parserError(simb):
    print("Erro sintático, token inesperado: ", simb)

def rec_term(simb):
    global prox_simb
    if prox_simb.type == simb:
        prox_simb = lexer.token()
    else:
        parserError(prox_simb)
        prox_simb = ('erro', '', 0, 0)

def rec_ABin2():
    global prox_simb
    if prox_simb.type == '\t' or prox_simb.type == ' ':
        rec_term('PF')
    elif prox_simb.type == 'NUM':
        t1 = prox_simb.value
        rec_term('NUM')
        t2 = None
        t3 = None
        rec_term('PF')
    else:
        parserError(prox_simb)
    return None

def rec_ABin():
    global prox_simb
    rec_term('PA')
    return rec_ABin2()

def rec_Parser(data):
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token()
    return rec_ABin()
    
