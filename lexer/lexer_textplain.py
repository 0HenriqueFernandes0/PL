def t_textplain_NEWLINE(t):
    r'[\ |\t]*\n'
    t.lexer.lineno += len(t.value)
    return t

def t_textplain_IDENTACAO(t):
    r'(\t|\ )+'
    nivel = 0
    for char in t.value:
        if char==" ":
            nivel+=1
        elif char=="\t":
            nivel+=4
    t.value = nivel
    if(t.lexer.nivel>=t.value):
        t.lexer.begin('INITIAL')
    return t

def t_textplain_TEXTPLAIN(t):
    r'[^\n]+'
    return t

def t_textplain_error(t):
    print(f"Carácter ilegal {t.value[0]} na linha {t.lineno}")
    t.lexer.skip(1)