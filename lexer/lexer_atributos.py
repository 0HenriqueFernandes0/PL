
def t_atributos_RPAREN(t):
    r'\)'
    t.lexer.begin('tag')
    return t

def t_atributos_ATRIBUT(t):
    r'\w+=("[^"]+"|\'[^\']+\')'
    return t

def t_atributos_error(t):
    print(f"Carácter ilegal {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)

def t_atributos_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')
    return t

