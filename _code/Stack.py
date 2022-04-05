from sympy import true
from Astack import * 
from Link import *

class Stack(Astack):

    def __init__(self):
        self.size:int=0
        self.top:Link=Link(None,None) #Dummy Node

    def length(self) -> int:
        return self.size

    def push(self, item: E):
        new:Link=Link(item,self.top.next) # 새노드의 다음을 다음 걸로 지정 
        self.top.next=new #top의 다음을 new로 지정
        self.size+=1
    
    def pop(self) -> E:

        if(self.size==0): 
            return "No item"

        ret:E=self.top.next.item # 리턴 값

        self.top.next=self.top.next.next #top의 다음 값을 재설정  다다음 것으로
        self.size-=1

        return ret
    
    def topValue(self) -> E:
        
        if(self.size==0):
            return "No item"
        
        return self.top.next.item
    
    def clear(self):
        #초기화 
        self.top.next=None
        self.size=0
    
    def empty(self) -> bool: #비어있는지 확인
        if(self.size==0):
            return True
        return False
