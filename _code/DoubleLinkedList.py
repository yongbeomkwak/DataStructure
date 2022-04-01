# -*- coding: utf-8 -*-
from typing import TypeVar
from Dlink import *
from ListIterator import *
from Dlist import Dlist

E = TypeVar('E')

class DoubleLinkedList(Dlist):
    def __init__(self) -> None:
        self.head:Dlink=Dlink(None,None,None) # 별도의 head .next를 tail
        self.tail:Dlink=Dlink(None,self.head,None) # 별도의 tail .prev를 head
        self.head.next=self.tail
        self.size=0

    def length(self) -> int:
        return self.size
    
    def append_front(self, item: E):
        new:Dlink=Dlink(item,self.head,self.head.next) #새로운 노드 생성(이전을 head,다음을 head.next) 
        self.head.next.prev=new #해당 노드의 이전노드를 새노드 넣어주고 
        self.head.next=new # head의 다음을 새 노드로 
        self.size+=1
        
    
    def append_back(self, item: E):
        new:Dlink=Dlink(item,self.tail.prev,self.tail) # 이전을 tail의 prev ,다음을 tail
        self.tail.prev.next=new # tail.prev의 다음을 new
        self.tail.prev=new #tail이전을 new
        self.size+=1
    
    def insert(self, pos: int, item: E):
        
        if(pos>=self.size):
            print("Out of Bound")
            return

        curr:Dlink=self.head.next #head의 다음부터 시작
        

        for _ in range(pos):
            curr=curr.next
        
        new:Dlink=Dlink(item,curr.prev,curr) # curr을 뒤로 밀어낸다.
        curr.prev.next=new  #이전의 다음을 new로
        curr.prev=new #이전을 new로 
        self.size+=1
    
    def remove(self, pos: int) -> E:
        
        if(pos>=self.size):
            print("Out of Bound")
            return

        curr:Dlink=self.head.next #head의 다음부터 시작
        

        for _ in range(pos):
            curr=curr.next
        
        curr.next.prev=curr.prev  #다음노드의  이전 노드를  변경
        curr.prev.next=curr.next #이전노드의 다음 노드를 변경
        self.size-=1

        return curr.item
        

    def pop_front(self)->E:
        if(self.size==0):
            return "No Item"
        else:
            ret:E=self.head.next.item
            curr:Dlink=self.head.next
            self.head.next=curr.next # head 다음을 변경
            curr.next.prev=self.head # 다음 것의 이전을 헤드로 연결
            self.size-=1
            return ret
    
    def pop_back(self) -> E:
        if(self.size==0):
            return "No Item"
        else:
            ret:E=self.tail.prev.item 
            curr:Dlink=self.tail.prev #가장 마지막 원소
            self.tail.prev=curr.prev #tail의 이전원소 변경
            curr.prev.next=self.tail #이전 원소의 다음을 tail로 변경
            self.size-=1
            return ret
        
    
    def update(self, pos: int, item: E):

        if(self.size<=pos):
            print("Out of Bound")
            return
        
        if(pos<=self.size//2): # 중간지점 보다 작으면 head부터 
            curr:Dlink=self.head.next #
            for _ in range(pos):
                curr=curr.next
            
            curr.item=item
        
        else: #tail부터 
            curr:Dlink=self.tail.prev
            reverse_pos:int=self.size-1-pos
            for _ in range(reverse_pos):
                curr=curr.prev
            curr.item=item
    
    def getValue(self, pos: int)->E:
        if(self.size<=pos):
            print("Out of Bound")
            return
        
        if(pos<=self.size//2): # 중간지점 보다 작으면 head부터 
            curr:Dlink=self.head.next #
            for _ in range(pos):
                curr=curr.next
            
            return curr.item
            
            
        
        else: #tail부터 
            curr:Dlink=self.tail.prev
            reverse_pos:int=self.size-1-pos
            for _ in range(reverse_pos):
                curr=curr.prev
            
            return curr.item
        
    def clear(self):
        #초기화
        self.head:Dlink=Dlink(None,None,None) # 별도의 head .next를 tail
        self.tail:Dlink=Dlink(None,self.head,None) # 별도의 tail .prev를 head
        self.head.next=self.tail
        self.size=0
 
    
    def listIterator(self) -> ListIterator:
        return self.DoubleLinkedListIterator(self)

    
    class DoubleLinkedListIterator(ListIterator):
        
        def __init__(self,outer):
            self.outer:DoubleLinkedList=outer
            self.curr:Dlink=self.outer.head  # head부터
            self.rev_curr:Dlink=self.outer.tail # tail 부터
        
        def hasNext(self) -> bool:
            return self.curr!=self.outer.tail.prev #tail 이전노드면 더 이상 다음은 없음
        
        def next(self) -> E:
            self.curr=self.curr.next
            return self.curr.item
        
        def previous(self) -> E:
            self.rev_curr=self.rev_curr.prev
            return self.rev_curr.item
        
        def hasPrevious(self) -> bool:
            return self.rev_curr!=self.outer.head.next # head 다음 노드가 아니면 previous를 갖고있다
        
        
        

