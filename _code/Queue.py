# -*- coding: utf-8 -*-
from typing import TypeVar

from pytest import Item
from Dlink import *
from Aqueue import *
E = TypeVar('E')

class Queue(Aqueue):
    def __init__(self) -> None:
        self.head:Dlink=Dlink(None,None,None) 
        self.tail:Dlink=Dlink(None,self.head,None)
        self.head.next=self.tail
        self.size:int=0
        ## 서로 연결  head와 tail
    
    def push(self, item: E):
        new:Dlink=Dlink(item,self.head,self.head.next)
        # prev :head next: head.next
        self.head.next.prev=new  # 이전노드 new
        self.head.next=new #다음노드 new
        self.size+=1
    
    def pop(self) -> E:
        if(self.size==0):
            return "No item"
        
        ret:E=self.tail.prev.item  #리턴 값 
        self.tail.prev.prev.next=self.tail #2번째 전 다음 노드 tail
        self.tail.prev=self.tail.prev.prev #tail의 이전노드 2번째 전

        self.size-=1
        return ret
    
    def front(self) -> E:
        if(self.size==0):
            return "No item"
        
        return self.head.next.item #front
    
    def rear(self) -> E:
        if(self.size==0):
            return "No item"
        
        return self.tail.prev.item #back

    def clear(self):
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0
        #재 설정
    
    def empty(self) -> bool:
        if(self.size==0):
            return True
        return False