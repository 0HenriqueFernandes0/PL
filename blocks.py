# abin_ast.py
# 2023-03-21 by jcr
# ----------------------
# P1: Block --> tag  
# P2:        | tag atributos texto sub_blocks   
# -------------------------------         
class Block:
    def __init__(self, tag, atributes, sub_blocks):
        self.tag = tag
        self.atributes = atributes
        self.sub_blocks = sub_blocks

    def json(self):
        node = """  <f{self.tag}>
        """
        for b in self.sub_blocks:
            node+= b.json()
        node+= """  </f{self.tag}>
        """   
        return node
    
    def count(self):
        return 1 + self.left.count() + self.right.count()
    
    def sum(self):
        return int(self.num) + self.left.sum() + self.right.sum()

class ABinEmpty:
    def __init__(self, type):
        self.type = type

    def pp(self):
        print('()')

    def inorder(self):
        pass

    def preorder(self):
        pass

    def json(self):
        return "null"
    
    def count(self):
        return 0
    
    def sum(self):
        return 0
        

    
