import ply.lex as lex

states = (
    ('indentacao', 'exclusive'),
    ('atributos', 'exclusive'),
    ('tag', 'exclusive'),
    ('frase', 'exclusive')
)

tokens = (
    'TAB',
    'SPACE',
    'NEWLINE',
    'TAG',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'ATRIBUT',
    'ID',
    'CLASS',
    'TEXTO'
)

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

def t_indentacao_TAB(t):
    r'\t+'
    return t

def t_indentacao_SPACE(t):
    r'(\ )+'
    return t

def t_indentacao_error(t):
    print(f"Carácter ilegal {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)


def t_tag_TAG(t):
    r'\w+'
    return t

def t_tag_LPAREN(t):
    r'\('
    t.lexer.begin('atributos')
    return t

def t_tag_CLASS(t):
    r'\.\w+'
    return t

def t_tag_SPACE(t):
    r'(\ )+'
    t.lexer.begin('frase')
    return t

def t_tag_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('indentacao')
    return t

def t_tag_ID(t):
    r'\#\w+'
    return t

def t_tag_EQUAL(t):
    r'='
    return t

def t_tag_error(t):
    print(f"Carácter ilegal {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)



def t_atributos_RPAREN(t):
    r'\)'
    t.lexer.begin('frase')
    return t

def t_atributos_ATRIBUT(t):
    r'\w+=("[^"]+"|\'[^\']+\')'
    return t

def t_atributos_error(t):
    print(f"Carácter ilegal {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)




def t_frase_TEXTO(t):
    r'[^\n]+'
    return t

def t_frase_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    t.lexer.begin('indentacao')
    return t

def t_frase_error(t):
    t.lexer.skip(1)

def t_INITIAL_TAG(t):
    r'\w+'
    t.lexer.begin('tag')
    return t

def t_INITIAL_SPACE(t):
    r'\ '
    t.lexer.begin('indentacao')
    return t

t_atributos_ignore = ' '

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
