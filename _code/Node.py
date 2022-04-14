from Anode import *
from typing import TypeVar
E = TypeVar('E')

class Node(Anode):
    def __init__(self,item:E,left:Anode=None,right:Anode=None):
        self.item:E=item
        self.left:Anode=left
        self.right:Anode=right

    def getItem(self) -> E:
        return self.item
    
    def getLeft(self) -> Anode:
        if(self.left!=None):
            return self.left
        return None
    
    def getRight(self) -> Anode:
        if(self.right!=None):
            return self.right
        return None
    
    
    def isLeaf(self) -> bool:
        if(self.left==None and self.right==None): #자식노드가 모두 없으면 True
            return True
        return False
