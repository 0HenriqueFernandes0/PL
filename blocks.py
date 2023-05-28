class Blocks:
    def __init__(self):
        self.sub_blocks = []
        self.vars = {}

    def html(self):
        html=''
        for b in self.sub_blocks:
            html+=b.html()
        return html

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
        if len(self.sub_blocks)>0:
            code_ty_ant = None
            code_bol_ant = None
            for b in self.sub_blocks:
                if type(b) is Block:
                    node+="\n"+ b.html()
                elif type(b) is Code:
                    if b.bol==None:
                        if code_ty_ant == 'if':
                            b.bol= not code_bol_ant
                        else:
                            print("error else without if\n")
                    code_ty_ant = b.type
                    code_bol_ant = b.bol
                    node+=b.html()
            node+= '\n'+' '*self.nivel_atual + f"</{self.tag}>"
        else:
            node+= f"</{self.tag}>"

        return node
    
class Code:
    def __init__(self,nivel_atual,bol,type):
        self.nivel_atual = nivel_atual
        self.nivel_seguinte = -1
        self.bol=bol
        self.type=type
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
        node = ''
        if self.bol:
                if len(self.sub_blocks)>0:
                    for b in self.sub_blocks:
                        node+="\n"+ b.html()
        return node
