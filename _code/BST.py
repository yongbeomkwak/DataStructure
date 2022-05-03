from re import S
from Dictionary import *
from Node import *
from typing import TypeVar
from LNode import *
E = TypeVar('E')
K = TypeVar('K')

class BST(Dictionary):
    
    def __init__(self):
        self.root:Node=None
        self.__size:int=0



    def size(self) -> int:
        return self.__size
    
    def clear(self):
        self.root=None
        self.__size=0

    
    def insert(self, key: K, e: E):
        if(self.root==None): # 최상위가 비어있으면 설정
            self.root=Node(self.Entry(key,e),None,None)
        else:
            self.insert_helper(key,e,self.root)
        
        self.__size+=1
        
    
    def insert_helper(self,key:K,e:E,rt:Node)->LNode:
        
        if(rt==None):
            return Node(self.Entry(key,e)) # 모든 삽입 은 Node로 
        elif(rt.getItem().key==key):
            self.rt.getItem().element=e
        elif(rt.getItem().key<key): #목표키가 현재키보다 크면 오른쪽으로
            rt.setRight(self.insert_helper(key,e,rt.getRight()))
        else: 
            rt.setLeft(self.insert_helper(key,e,rt.getLeft()))

        return rt
        
    
    def remove(self, key: K) -> E:
        ret:E=self.find_helper(key,self.root)
        if(ret!=None):
            self.root=self.remove_helper(key,self.root)
            self.__size-=1
        
        return ret
    
    def remove_helper(self,key:K,rt:Anode)->Anode: # 삭제하고 바뀐트리의 루트를 리턴해준다. ,왜? 해당트리의 루트를 상위 노드의 오른쪽 또는 왼쪽에 연결하면 끊김이 없음
        if(rt.getItem().key>key): #만약 목표 key가 현재보다 작으면 왼쪽으로
            self.remove_helper(key,rt.getLeft())
        elif(rt.getItem().key<key): #만약 목표 key가 현재보다 크다면 오른쪽
            self.remove_helper(key,rt.getRight())
        else: # 찾았으면 
    
            if(rt.getLeft()==None): #만약 왼쪽만 없을 경우 
                return rt.getRight() # 삭제 후 서브트리의 루트를 오른쪽노드로 설정
            elif(rt.getRight()==None): #만약 오른쪽만 없을 경우
                return rt.getLeft() #삭제 후 서브트리의 루트를 왼쪽노드로 설정
            else: #만약 왼쪽 오른쪽 둘다 있을 경우 , 오른쪽에서 가장 작은 노드를 서브트리의 루트로
                lastmost=self.getLeftMost(rt.getRight())  #찾기 
                rt.setItem(lastmost) #찾은 값으로 변경
                rt.setRight(self.removeLeftMost(rt.getRight())) #삭제후 완성된 서브트리를 오른쪽에 설정
        
        if(rt.isLeaf()): #만약 자식이 없다면 
            tmp_e=rt.getItem().element
            tmp_k=rt.getItem().key
            rt=LNode(tmp_k,tmp_e) #LNode로 대체
        return rt #삭제 후에도 여전히 루트는 rt이므로
    
    def getLeftMost(self,rt:Anode): #키값이 가장 작은 노드의 값을 찾는 함수
        cur:Anode=rt
        while(cur.getLeft()!=None): #왼쪽으로 계속 들어감
            cur=cur.getLeft()
        
        return cur.getItem()
    
    def removeLeftMost(self,rt:Anode): #값을 대체한 후 삭제하는 함수 , 삭제한 후 서브트리의 루트를 리턴
        if(rt.getLeft()==None): #더 이상 왼쪽이 없다면 내가 제일 작은 값, 즉 대체되었으므로 삭제되어야하는 값
            return rt.getRight() # 현재 노드가 삭제되므로 오른쪽 값으로 대체된다.
        else: #만약 왼쪽 값이 더 남아있다면 
            rt.setLeft(self.removeLeftMost(rt.getLeft())) #왼쪽으로 들어간다.
            
            return rt 

            '''
            만약 현재 삭제되어야할 노드가 15일 때 
                        10                              10                                                  10                     
                    9         15                   9          18 (오른쪽의 있는 값 중 가장 작은값으로 바꿔놓고)    9             18               
                5          13      18   =>      5         13       20                          =>   5            13         20(18에 딸려옴)  
                        11    14                      11      14                                             11      14  
                            12                            12                                                    12
                            (11을 삭제 후 11의 오른쪽 12를 13의 왼쪽으로 설정)

            '''           
        
            
        
    
    def removeAny(self): #가장 오른쪽 노드 중 , 자식이 존재하지 않으면 삭제 해당 노드 없을 시 무시
        curr:Node=self.root
        while(curr.getRight()!=None):
            prev=curr
            curr=curr.getRight()
            if(curr.getLeft()==None and curr.getRight()==None):
                prev.setRight(None)
        
        
    
    def find(self, key: K) -> E:

        return self.find_helper(key,self.root)
        
    
    def find_helper(self,k:K,rt:Node) -> E:
        
        if(rt==None): #못 찾았을 때
            return None
        
        if(rt.getItem().key==k):
            return (rt.getItem().element)
        
        elif(rt.getItem().key<k): #목표키값이 현재키값보다 크면 오른쪽
            return self.find_helper(k,rt.getRight())

        else: #작으면 왼쪽
            return self.find_helper(k,rt.getLeft())

    def visit(self,node:Anode):
        print(node.getItem().key,end=' ')
    
    def inorder(self,node:Anode):
        if(node==None):
            return
        self.inorder(node.getLeft()) #왼
        self.visit(node) #자기자신
        self.inorder(node.getRight()) #오
    
    def preorder(self,node:Anode):
        if(node==None):
            return
        self.visit(node) #자기자신
        self.preorder(node.getLeft()) #왼쪽 
        self.preorder(node.getRight()) #오른쪽

        

    class Entry:
        
        def __init__(self,key:K,e:E):
            self.key:K=key
            self.element:E=e
        
            
