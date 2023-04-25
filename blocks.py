# abin_ast.py
# 2023-03-21 by jcr
# ----------------------
# P1: Block --> tag  
# P2:        | tag atributos texto List_blocks   
# -------------------------------         
class Block:
    def __init__(self,nivel_atual,info):
        self.nivel_atual = nivel_atual
        self.nivel_seguinte = -1

        if(info[0][0]==''):
            self.tag = 'div'
        else:
            self.tag = info[0][0]

        self.atributos=''
        if(info[0][1]!=''):
            self.atributos += ' id="'+info[0][1][1:]+'"'
        if(info[0][2]!=''):
            self.atributos += ' class="'+info[0][2][1:]+'"'
        for atri in info[0][3]:
            self.atributos += (' ' +atri)
        
        self.texto = info[1]
        self.sub_blocks = []

    def new_sub_block(self,block):
        if(self.nivel_seguinte==-1):
            self.nivel_seguinte=block.nivel_atual
            self.sub_blocks.append(block)
        elif(self.nivel_seguinte==block.nivel_atual):
            self.sub_blocks.append(block)
        else:
            return -1
        
        return 1
            

    def html(self):
        node = ' '*self.nivel_atual
        if(self.atributos!= ''):
            node += f"<{self.tag} {self.atributos}>"
        else:
            node += f"<{self.tag}>"

        if(self.texto!=''):
            node+=self.texto

        for b in self.sub_blocks:
            node+= b.html()

        node+= '\n'+' '*self.nivel_atual + f"</{self.tag}>"
        return node
    

    
