# abin_ast.py
# 2023-03-21 by jcr
# ----------------------
# P1: Block --> tag  
# P2:        | tag atributos texto List_blocks   
# -------------------------------         
class Block:
    def __init__(self, tag, atributes,texto, sub_blocks):
        self.tag = tag
        self.atributes = atributes
        self.texto = texto
        self.sub_blocks = sub_blocks

    def html(self):
        node = "<f{self.tag}>\n"
        for b in self.sub_blocks:
            node+= "\t"+b.html()

        node+= "\n</f{self.tag}>"
        return node
    

    
