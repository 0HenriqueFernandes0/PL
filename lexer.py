import ply.lex as lex

tokens = (
    'IDENTACAO',
    'NEWLINE',
    'TAG',
    'ATRIBUTOS',
    'QUANT'
)

t_IDENTACAO = r'\t'
t_NEWLINE = r'\n'
t_TAG = r'\w+'
t_ATRIBUTOS = r'\(\w+\)'
t_QUANT = r'\d+;'

t_ignore = ' '

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
data = open("example.txt",'r')
lexer.input(data.read())
while s := lexer.token():
   print(s)