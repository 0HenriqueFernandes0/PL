
def t_tag_TAG(t):
    r'\w+'
    return t

def t_tag_CLASS(t):
    r'\.\w+'
    return t

def t_tag_ID(t):
    r'\#\w+'
    return t

def t_tag_COMA(t):
    r'\.'
    t.lexer.begin('textplain')
    return t

def t_tag_LPAREN(t):
    r'\('
    t.lexer.begin('atributos')
    return t

def t_tag_SPACE(t):
    r'(\ )+'
    t.lexer.begin('frase')
    return t

def t_tag_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('INITIAL')
    return t

def t_tag_EQUAL(t):
    r'='
    return t

def t_tag_error(t):
    print(f"Carácter ilegal {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)