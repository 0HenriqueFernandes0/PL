

def t_frase_TEXTO(t):
    r'[^\n]+'
    return t

def t_frase_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')
    return t

def t_frase_error(t):
    t.lexer.skip(1)