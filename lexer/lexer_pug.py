import ply.lex as lex
from lexer.lexer_indentacao import*
from lexer.lexer_tag import*
from lexer.lexer_atributos import*
from lexer.lexer_frase import*

states = (
    ('indentacao', 'exclusive'),
    ('atributos', 'exclusive'),
    ('tag', 'exclusive'),
    ('frase', 'exclusive')
)

tokens = (
    'IDENTACAO',
    'SPACE',
    'NEWLINE',
    'TAG',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'ATRIBUT',
    'ID',
    'CLASS',
    'TEXTO',
    'TEXTPLAIN'
)


def t_INITIAL_TAG(t):
    r'\w+'
    t.lexer.begin('tag')
    return t

def t_INITIAL_CLASS(t):
    r'\.\w+'
    t.lexer.begin('tag')
    return t

def t_INITIAL_ID(t):
    r'\#\w+'
    t.lexer.begin('tag')
    return t

def t_INITIAL_IDENTACAO(t):
    r'(\t|\ )+'
    return t


t_atributos_ignore = ' '

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
