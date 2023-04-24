import ply.yacc as yac
from lexer_pug import tokens

def p_linhas(p):
    '''linhas : linha
                | linha linhas
                | 
    '''
    
def p_linha(p):
    '''linha :  IDENTACAO corpo NEWLINE
                | corpo NEWLINE
    '''
    
    nivel=0
    if len(p)==4:
        for tok in p[1]:
            if tok == ' ':
                nivel+=1
            if tok == '\t':
                nivel+=4
    print(str(nivel)+" "+str(p[2]))

def p_corpo(p):
    '''corpo :  tag
                | tag SPACE TEXTO
                | tag EQUAL SPACE TEXTO
    '''
    if (len(p)==2):
        p[0]=(p[1],'')
    elif(len(p)==4):
        p[0]=(p[1],p[3])
    elif(len(p)==5):
        p[0]=(p[1],'')

def p_tag(p):
    '''tag :    TAG
                | TAG tag
                | ID
                | ID tag
                | CLASS
                | CLASS tag
                | tag LPAREN atributos RPAREN
    '''
    if len(p)==2:
        if '#' in p[1]:
            p[0]=('',p[1],'',[])
        elif '.' in p[1]:
            p[0]=('','',p[1],[])
        else:
            p[0]=(p[1],'','',[])
    elif len(p)==3:
        if '#' in p[1]:
            p[0]=(p[2][0],p[1],p[2][2],p[2][3])
        elif '.' in p[1]:
            p[0]=(p[2][0],p[2][1],p[2][2].join(p[1]),p[2][3])
        else:
            p[0]=(p[1],p[2][1],p[2][2],p[2][3])
    elif len(p)==5:
        p[0]=(p[1][0],p[1][1],p[1][2],p[3])

def p_atributos(p):
    '''atributos :   ATRIBUT atributos
                    |
    '''
    if len(p)<2:
        p[0]=[]
    else:
        p[0]=[p[1]]


def p_error(p):
    print("erro sintatico: "+str(p))

parser = yac.yacc()