import ply.yacc as yac
from lexer.lexer_pug import tokens
from blocks import *

vars = {}

def p_html(p):
    '''html :   linhas
    '''
    p[0]=p[1].html()
        
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
        next = p[1].sub_blocks
        if (type(p[3]) == tuple and type(p[3][0]) ==Block ) or type(p[3]) == Code:

                if type(p[3]) == Code and type(p[3].bol) == str:
                    if p[3].bol in p[1].vars:
                        p[3].bol=p[1].vars[p[3].bol]
                    else:
                        p[3].bol= False
                elif type(p[3]) == tuple and p[3][1]==0:
                    if p[3][0].texto in p[1].vars:
                        p[3][0].texto = p[1].vars[p[3][0].texto]
                    else:
                        p[3][0].texto = ''
                    p[3]=p[3][0]
                elif type(p[3]) == tuple:
                    p[3]=p[3][0]

                while len(next[-1].sub_blocks)>0 and next[-1].nivel_seguinte!= -1 and next[-1].nivel_seguinte < p[3].nivel_atual:
                    next = next[-1].sub_blocks

                if p[3].nivel_atual > next[0].nivel_atual:
                    cod = next[-1].new_sub_block(p[3])
                    if cod == -1:
                        print('erro na identaçao'+str(next))

                elif next[0].nivel_atual == p[3].nivel_atual:
                    next.append(p[3])

        elif type(p[3]) is str:
            next=next[-1]
            while len(next.sub_blocks)>0:
                next = next.sub_blocks[-1]
            next.texto+=p[3]

        elif type(p[3]) is tuple:
            p[1].vars[p[3][0]]=p[3][1]
            
        p[0]=p[1]
    elif len(p)==2 and type(p[1]) == tuple and type(p[1][0]) == Block:
        p[0]=Blocks()
        p[0].sub_blocks.append(p[1][0])
    elif len(p)==2 and type(p[1]) == Code:
        p[0]=Blocks()
        p[1].bol=False
        p[0].sub_blocks.append(p[1])
    elif len(p)==2 and type(p[1]) == tuple:
        p[0]=Blocks()
        p[0].vars[p[1][0]]=p[1][1]


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
    
    if value == 'true':
        value=True
    elif value == 'false':
        value=False
    elif value.isnumeric():
        value=int(value)

    p[0]=(var,value)

def p_linha_codigo(p):
    '''linha_codigo :   IDENTACAO IF TEXTO
                        | IF TEXTO
                        | IDENTACAO ELSE
                        | ELSE
    '''
    if len(p)==4:
        if p[2] == "if": 
            p[0]=Code(p[1],p[3],'if')
    elif len(p)==3:
        if p[1] == "if": 
            p[0]=Code(0,p[2],'if')
        else:
            p[0]=Code(p[1],None,'else')
    else:
        p[0]=Code(0,None,'else')

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

    p[0]=(Block(nivel,(info[0],info[1])),info[2])

def p_linha_textplain(p):
    'linha_textplain : IDENTACAO TEXTPLAIN '
    p[0]= "\n"+ " " * p[1] + p[2]

def p_corpo(p):
    '''corpo :  tag
                | tag SPACE
                | tag SPACE TEXTO
                | tag EQUAL SPACE TEXTO
    '''
    if (len(p)==2 or len(p)==3):
        p[0]=(p[1],'',1)
    elif(len(p)==4):
        p[0]=(p[1],p[3],1)
    elif(len(p)==5):
        p[0]=(p[1],p[4],0)

def p_tag(p):
    '''tag :  tag TAG atributos_linha
                | tag CLASS atributos_linha
                | tag ID atributos_linha
                |
    '''
    if len(p)==4:
        if '#' in p[2]:
            p[0]=(p[1][0],p[2],p[1][2],p[1][3]+p[3])
        elif '.' in p[2]:
            p[0]=(p[1][0],p[1][1],p[1][2]+(p[2].replace('.',' ')),p[1][3]+p[3])
        else:
            p[0]=(p[2],p[1][1],p[1][2],p[1][3]+p[3])
    else:
        p[0]=('','','',[])

def p_atributos_linha(p):
    '''atributos_linha :  LPAREN atributos RPAREN
                        |
    '''
    if len(p)==4:
        p[0]=p[2]
    else:
        p[0]=[]

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