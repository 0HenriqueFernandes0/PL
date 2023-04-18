import ply.lex as lex

tokens = (
    'IDENTACAO',
    'NEWLINE',
    'WORD',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'ASPAS',
    'ID',
    'CLASS'
)

t_IDENTACAO = r'\t'
t_NEWLINE = r'\n'
t_WORD = r'(\w|\!|\?|\/|\-|\+|\:|;|,)+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'='
t_ASPAS = r'(\"|\')'
t_ID = r'\#'
t_CLASS = r'\.'

t_ignore = ' '

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

data = open("example1.txt",'r')
lexer.input(data.read())
while s := lexer.token():
   print(s)