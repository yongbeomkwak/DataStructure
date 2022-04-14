from Node import *
from typing import TypeVar
from Lnode import *
E = TypeVar('E')

class BinaryTree:
    def __init__(self,root:Node):
        self.__root:Node=root
    
    def getRoot(self)->Node:
        return self.__root

    def visit(self,node:Node):
        print(node.getItem(),end=" ")
    
    def preorder(self,node:Anode):
        if(node==None):
            return
        self.visit(node) #자기자신
        self.preorder(node.getLeft()) #왼쪽 
        self.preorder(node.getRight()) #오른쪽
    
    def postorder(self,node:Anode):
        if(node==None):
            return
        self.postorder(node.getLeft()) #왼
        self.postorder(node.getRight()) #오 
        self.visit(node) #자기자신 

    def inorder(self,node:Anode):
        if(node==None):
            return
        self.inorder(node.getLeft()) #왼
        self.visit(node) #자기자신
        self.inorder(node.getRight()) #오    