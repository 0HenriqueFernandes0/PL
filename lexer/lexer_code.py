

def t_code_TEXTO(t):
    r'[^\n]+'
    return t

def t_code_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')
    return t

def t_code_error(t):
    t.lexer.skip(1)