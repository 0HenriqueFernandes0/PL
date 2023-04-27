
def t_indentacao_TAG(t):
    r'\w+'
    t.lexer.begin('tag')
    return t

def t_indentacao_CLASS(t):
    r'\.\w+'
    t.lexer.begin('tag')
    return t

def t_indentacao_ID(t):
    r'\#\w+'
    t.lexer.begin('tag')
    return t

def t_indentacao_error(t):
    print(f"Carácter ilegal {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)