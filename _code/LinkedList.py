# -*- coding: utf-8 -*-


from List import *
from Link import *
from ListIterator import *
class LinkedList(List):

    def __init__(self):
        self.head:Link=Link(None,None)
        self.tail=self.head #초기화 이므로 같은 head와 tail 같게
        self.size:int=0

        
    
    def clear(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def insert(self, pos: int, item: E):
        curr:Link=self.head
        for i in range(0,pos):
            curr=curr.next
        

        # 1(새 노드)        
        # 0(현재노드) -> 2(햔재노드 다음)

        #new_node:Link=Link(item=item,next=curr.next)      1 -> 2
        #curr.next=new_node  0->1
        # 0->1->2

        #새 노드의 다음 노드를 현재노드의 다음으로 지정
        new_node:Link=Link(item=item,next=curr.next)
        #햔재노드의 다음을 새노드로 지정 
        curr.next=new_node

        if(curr==self.tail): #만약 현재 노드가 tail이면 
            self.tail=curr.next #tail 수정 
        self.size+=1

    def append(self,item:E):
        new_node:Link=Link(item=item,next=None)
        self.tail.next=new_node
        self.tail=new_node
        self.size+=1

    def update(self, pos: int, item: E):
        curr:Link=self.head

        for i in range(0,pos): # 탐색
            curr=curr.next
        
        curr.next.item=item # 업데이트 
    
    def getValue(self, pos: int)-> E:
        curr:Link=self.head

        for i in range(0,pos): # 탐색
            curr=curr.next

        return curr.next.item

    def length(self) -> int:
        return self.size
    
    def remove(self, pos: int) -> E:
        curr:Link=self.head

        for i in range(0,pos): # 탐색
            curr=curr.next
        
        #curr.next가 삭제해야할 노드 
        ret:E=curr.next.item

        if(curr.next==self.tail): #만약 삭제해야할 노드가 tail이면
            self.tail=curr  # tail 옮김 

        curr.next=curr.next.next # 다다음 것으로 옮긴다.
        
        self.size-=1


        return ret

    
    def toString(self) -> str:
        ret:str=""
        curr:Link=self.head

        for i in range(0,self.size):
            ret+= str(curr.next.item) + ","
            curr=curr.next

        
        return ret
    
    def listIterator(self) -> ListIterator:
        return self.LinkedListIterator(self)
    
    class LinkedListIterator(ListIterator):
        
        def __init__(self,outer):
            self.outer:LinkedList=outer #바깥 LinkedList를 가르킴 
            self.curr:Link=self.outer.head # 현재 위치를 head로 
        
        def hasNext(self) -> bool:
            return self.curr!= self.outer.tail #현재 위치가 tail이 아니면 다음 요소가 있음 
        
        def next(self) -> E: #다음 원소를 리턴 
            self.curr=self.curr.next
            return self.curr.item
        
        def hasPrevious(self) -> bool: #현재가 head가 아니면 이전 값이 있음 
            return self.curr!=self.outer.head
        
        def previous(self) -> E: 
            prev:Link =self.outer.head


            #head 부터 현재 이전까지 이동 
            while(prev.next != self.curr):
                prev=prev.next
            
            self.curr=prev # 현재를 이전으로 이동

            #노드와 노드 사이를 가르키고 있다고 생각하면 된다.

            # head -> 1-> 2 -> 3(prev) ->curr-> 4
            # head -> 1-> 2 -> curr -> 3 ->4
            # curr.next=3 
            return self.curr.next.item

            

    