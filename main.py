from lexer_pug import lexer
from parser_pug import rec_Parser

data = open("example.txt",'r',encoding="utf8").read()

lexer.input(data)
while s := lexer.token():
   print(s)

rec_Parser(data)