from sympy import true
from Astack import * 
from Link import *
import numpy as np

class ArrayStack(Astack):
    DefaultSize:int=10
    def __init__(self):
        self.maxSize=ArrayStack.DefaultSize*2 #더블링
        self.top:int=-1 #시작을 -1로 해야 딱 맞음
        self.listArray=np.zeros(self.maxSize)
        self.size:int=0

    def clear(self):
        self.top=-1 #다시 -1로
        self.size=0
        self.listArray=np.zeros(self.maxSize)
    
    def topValue(self) -> E:
        
        if(self.size==0):
            return "No item"
        return int(self.listArray[self.top])

    def push(self, item: E):
        self.top+=1
        self.listArray[self.top]=item
        self.size+=1

    def length(self) -> int:
        return self.size
    
    def pop(self) -> E:
        if(self.size==0):
            return "No item"
        ret:E=self.listArray[self.top]
        self.top-=1
        self.size-=1
        return int(ret)

    def empty(self) -> bool:
        return self.size==0