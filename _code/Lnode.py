from Anode import *
from typing import TypeVar
E = TypeVar('E')

class LNode(Anode):
    def __init__(self,item:E):
        self.item:E=item

    def getItem(self) -> E:
        return self.item
    
    def getLeft(self) -> Anode:
        return None
    
    def getRight(self) -> Anode:
        return None
    
    
    def isLeaf(self) -> bool:
        return True
