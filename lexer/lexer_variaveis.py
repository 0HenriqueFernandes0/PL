def t_variaveis_EQUAL(t):
    r'='
    return t

def t_variaveis_TEXTO(t):
    r'[^\s]+'
    return t

def t_variaveis_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')
    return t

def t_variaveis_error(t):
    t.lexer.skip(1)
