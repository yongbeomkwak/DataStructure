from Anode import *
from typing import TypeVar
E = TypeVar('E')

class LNode(Anode):
    def __init__(self,item:E):
        self.item:E=item
        self.left:Anode=None
        self.right:Anode=None

    def getItem(self) -> E:
        return self.item
    
    def getLeft(self) -> Anode:
        return self.left
    
    def getRight(self) -> Anode:
        return self.right
    
    
    def isLeaf(self) -> bool:
        return True

    def setRight(self,n:Anode):
        self.right=n
    
    def setLeft(self,n:Anode):
        self.left=n
    def setItem(self,e):
        self.item=e