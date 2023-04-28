import ply.yacc as yac
from lexer.lexer_pug import tokens
from blocks import Block

def p_html(p):
    '''html :   linhas
                | 
    '''
    p[0]=''
    if type(p[1]) is list:
        for block in p[1]:
            p[0]+=block.html()

def p_linhas(p):
    '''linhas : linhas NEWLINE linha
                | linha
    '''
    if len(p)==4:
        next = p[1]
        if type(next) is list and len (next)>0:
            while len(next[-1].sub_blocks)>0 and next[-1].nivel_seguinte!= -1 and next[-1].nivel_seguinte < p[3].nivel_atual:
                next = next[-1].sub_blocks
            if p[3].nivel_atual > next[0].nivel_atual:
                cod = next[-1].new_sub_block(p[3])
                if cod == -1:
                    print('erro na identaçao'+str(next))
                p[0]=p[1]
            elif next[0].nivel_atual == p[3].nivel_atual:
                next.append(p[3])
                p[0]=p[1]
    elif len(p)==2:
        p[0]=[p[1]]
    
def p_linha(p):
    '''linha :  IDENTACAO tag COMA textplain
                | IDENTACAO corpo
                | corpo
    '''
    nivel=0
    if(len(p)==5):
        nivel=p[1]
        info=(p[2],p[4])
    elif len(p)==3:
        nivel=p[1]
        info=p[2]
    else:
        info=p[1]

    p[0]=Block(nivel,info)

def p_textplain(p):
    '''textplain : NEWLINE IDENTACAO TEXTPLAIN textplain
                  |
    '''
    if len(p)==5:
        p[0]=p[4]+"\n"+p[3]
    else:
        p[0]=""

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
                | CLASS 
                | ID
                | TAG tag
                | CLASS tag
                | ID tag
                | tag LPAREN atributos RPAREN
    '''
    if len(p)==2:
        if '#' in p[1]:
            p[0]=('',p[1],'',[])
        elif '.' in p[1]:
            p[0]=('','',p[1].replace('.',' '),[])
        else:
            p[0]=(p[1],'','',[])
    elif len(p)==3:
        if '#' in p[1]:
            p[0]=(p[2][0],p[1],p[2][2],p[2][3])
        elif '.' in p[1]:
            p[0]=(p[2][0],p[2][1],p[2][2]+(p[1].replace('.',' ')),p[2][3])
        else:
            p[0]=(p[1],p[2][1],p[2][2],p[2][3])
    elif len(p)==5:
        p[0]=(p[1][0],p[1][1],p[1][2],p[3])

def p_atributos(p):
    '''atributos :   ATRIBUT
                    | ATRIBUT atributos
    '''
    if len(p)==2:
        p[0]=[p[1]]
    else:
        p[0]=p[2].append(p[1])

def p_error(p):
    print("erro sintatico: "+str(p))

parser = yac.yacc()