from lexer.lexer_pug import lexer
from yac_pug import parser

data = open("tests/example0.txt",'r',encoding="utf8").read()

#lexer.input(data)
#while s := lexer.token():
#   print(s)
#print("\n\n\n")

print(parser.parse(data,debug=0))