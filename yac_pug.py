import ply.yacc as yac
from lexer_pug import tokens

def p_linhas(p):
    '''linhas : linha
                | linha linhas
                | 
    '''
def p_linha(p):
    '''linha :  identacao corpo NEWLINE
                | corpo NEWLINE
    '''
    print(str(p[1])+" "+str(p[2]))

def p_identacao(p):
    '''identacao :  TAB identacao
                    | SPACE identacao
                    | 
    '''
    nivel=0
    if len(p)>1:
        nivel+=len(p[1])

    p[0]=str(nivel)

def p_corpo(p):
    '''corpo :  tag
                | tag SPACE TEXTO
                | tag EQUAL SPACE TEXTO
    '''
    if (len(p)==2):
        p[0]=(p[1],'')
    elif(len(p)==4):
        p[0]=(p[1],p[3])
    elif(len(p)==4):
        p[0]=(p[1],'')

def p_tag(p):
    '''tag :    TAG
                | ID
                | ID tag
                | CLASS
                | CLASS tag
                | tag LPAREN atributos RPAREN
    '''
    p[0]=p[1]

def p_atributos(p):
    '''atributos :  ATRIBUT
                    | ATRIBUT atributos
    '''
    p[0]=p[1]


def p_error(p):
    print("erro sintatico: "+str(p))

parser = yac.yacc()