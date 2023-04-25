import ply.yacc as yac
from lexer_pug import tokens
from blocks import Block

def p_html(p):
    '''html :   linhas
                | 
    '''
    p[0]=''
    for block in p[1]:
        p[0]+=block.html()
    #print(p[0])

def p_linhas(p):
    '''linhas : linha
                | linha linhas
    '''
    
    if len(p)==3:
        if p[2][0] and p[2][0].nivel_atual > p[1].nivel_atual:
            for b in p[2]:
                cod = p[1].new_sub_block(b)
                if cod == -1:
                    print('erro na ideentaçao'+str(p[1]))
            p[0]=[p[1]]
        elif p[2][0] and p[2][0].nivel_atual == p[1].nivel_atual:
            p[0]=p[2].append(p[1])
    elif len(p)==2:
        p[0]=[p[1]]

    print(p[0])
    print("oi")
    
def p_linha(p):
    '''linha :  IDENTACAO corpo NEWLINE
                | corpo NEWLINE
    '''

    nivel=0
    if len(p)==4:
        info=p[2]
        for tok in p[1]:
            if tok == ' ':
                nivel+=1
            if tok == '\t':
                nivel+=4
    else:
        info=p[1]

    p[0]=Block(nivel,info)

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
            p[0]=(p[2][0],p[2][1],p[2][2].join(p[1].replace('.',' ')),p[2][3])
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