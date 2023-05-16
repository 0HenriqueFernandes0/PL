import ply.yacc as yac
from lexer.lexer_pug import tokens
from blocks import *

vars = {}

def p_html(p):
    '''html :   linhas
                | 
    '''
    p[0]=''
    if type(p[1]) is list:
        for block in p[1]:
            p[0]+=block.html()
        
def p_linhas(p):
    '''linhas : linhas NEWLINE linha_normal
                | linha_normal
                | linhas NEWLINE linha_codigo
                | linha_codigo
                | linhas NEWLINE linha_var
                | linha_var
                | linhas NEWLINE linha_textplain
    '''
    if len(p)==4:
        next = p[1]
        if type(next) is list and len (next)>0:
            if type(p[3]) == Block or type(p[3]) == Code:
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
            elif type(p[3]) is str:
                next=next[-1]
                while len(next.sub_blocks)>0:
                    next = next.sub_blocks[-1]
                next.texto+=p[3]
                p[0]=p[1]
            else:
                p[0]=p[1]
    elif len(p)==2 and (type(p[1]) == Block or type(p[1]) == Code):
        p[0]=[p[1]]

def p_linha_var(p):
    '''linha_var :  IDENTACAO VAR TEXTO EQUAL TEXTO
                    | VAR TEXTO EQUAL TEXTO
    '''

    if len(p)==6:
        var = p[3]
        value = p[5]
    else:
        var = p[2]
        value = p[4]
    
    if value == 'True':
        vars[var]=True
    elif value == 'False':
        vars[var]=False
    elif value.isnumeric():
        vars[var]=int(value)
    else:
        vars[var]=value  
    p[0]=True

def p_linha_codigo(p):
    '''linha_codigo :   IDENTACAO IF TEXTO
                        | IF TEXTO
                        | IDENTACAO ELSE
                        | ELSE
    '''
    if len(p)>2:
        if p[2] == "if": 
            if p[3] in vars and vars[p[3]]==True:
                p[0]=Code(p[1],True,1,'if')
            else:
                p[0]=Code(p[1],False,1,'if')
        elif p[1] == "if": 
            if p[2] in vars and vars[p[2]]:
                    p[0]=Code(0,True,1,'if')
            else:
                p[0]=Code(0,False,1,'if')
        else:
            p[0]=Code(p[1],None,1,'else')
    else:
        p[0]=Code(0,None,1,'else')

def p_linha_normal(p):
    '''linha_normal :  IDENTACAO corpo COMA
                | IDENTACAO corpo
                | corpo
    '''
    nivel=0
    if(len(p)==4):
        nivel=p[1]
        info=p[2]
    elif len(p)==3:
        nivel=p[1]
        info=p[2]
    else:
        info=p[1]

    p[0]=Block(nivel,info)

def p_linha_textplain(p):
    'linha_textplain : IDENTACAO TEXTPLAIN '
    p[0]= "\n"+ " " * p[1] + p[2]

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