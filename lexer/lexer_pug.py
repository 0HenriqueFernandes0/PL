import ply.lex as lex
from lexer.lexer_tag import*
from lexer.lexer_atributos import*
from lexer.lexer_frase import*
from lexer.lexer_textplain import*
from lexer.lexer_variaveis import*

states = (
    ('atributos', 'exclusive'),
    ('tag', 'exclusive'),
    ('frase', 'exclusive'),
    ('textplain', 'exclusive'),
    ('variaveis', 'exclusive')
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
    'TEXTPLAIN',
    'COMA',
    'IF',
    'ELSE',
    'VAR'
)
def t_INITIAL_VAR(t):
    r'\-\ var'
    t.lexer.begin('variaveis')
    return t

def t_INITIAL_IF(t):
    r'if(\ )+'
    t.value="if"
    t.lexer.begin('frase')
    return t

def t_INITIAL_ELSE(t):
    r'else'
    t.lexer.begin('frase')
    return t

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
    nivel = 0
    for char in t.value:
        if char==" ":
            nivel+=1
        elif char=="\t":
            nivel+=4
    t.value = nivel
    t.lexer.nivel = nivel
    return t


t_atributos_ignore = ' '

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.nivel=0
