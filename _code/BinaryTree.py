from Node import *
from typing import TypeVar
E = TypeVar('E')

class BinaryTree:
    def __init__(self,root:Node):
        self.__root:Node=root
    
    def insert_Node(self,parent:Node,node:Node): #부모노드와 자식노드
        if(node.getItem()<parent.getItem()): # 부모보다 작으면 왼쪽
            if(parent.left==None): #비어있으면
                parent.left=node
                return
            else: #있다면 해당 왼쪽을 기준으로 재귀
                self.insert_Node(parent.left,node)
        else:
            if(parent.right==None):#비어있으면
                parent.right=node
                return
            else: #오른쪽으로 재귀
                self.insert_Node(parent.right,node)
    
    def getRoot(self)->Node:
        return self.__root

    def visit(self,node:Node):
        print(node.getItem())
    
    def preorder(self,node:Node):
        if(node==None):
            return
        self.visit(node) #자기자신
        self.preorder(node.left) #왼쪽 
        self.preorder(node.right) #오른쪽
    
    def postorder(self,node:Node):
        if(node==None):
            return
        self.postorder(node.left) #왼
        self.postorder(node.right) #오 
        self.visit(node) #자기자신 

    def inorder(self,node:Node):
        if(node==None):
            return
        self.inorder(node.left) #왼
        self.visit(node) #자기자신
        self.inorder(node.right) #오
    