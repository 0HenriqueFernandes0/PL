import ply.yacc as yac
from lexer_pug import tokens

def p_linha(p):
    'linha :  identacao corpo NEWLINE'
    print(p[1])
    pass

def p_identacao(p):
    '''identacao :  TAB identacao
                    | SPACE identacao
                    | 
    '''
    nivel=0
    if len(p)>1:
        nivel+=len(p[1])

    p[0]=str(nivel)
    pass

def p_corpo(p):
    '''corpo :  tag
                | tag SPACE TEXTO
                | tag EQUAL SPACE TEXTO
    '''
    pass

def p_tag(p):
    '''tag :    TAG
                | ID
                | ID tag
                | CLASS
                | CLASS tag
                | tag LPAREN atributos RPAREN
    '''
    pass

def p_atributos(p):
    '''atributos :  ATRIBUT
                    | ATRIBUT atributos
    '''
    pass


def p_error(p):
    print(p)

parser = yac.yacc()